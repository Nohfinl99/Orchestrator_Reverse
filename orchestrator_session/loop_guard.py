"""Opt-in local lineage ledger. Candidates never grant execution authority."""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime
import os
from pathlib import Path
import re
import uuid

from . import core as c


def _hash(value):
    c.require(type(value) is str and re.fullmatch('[0-9a-f]{64}', value),
              'INVALID_SCHEMA', 'Expected SHA256')
    return value


def _ref(ref, current=True):
    c._shape(ref, 'path sha256 bytes')
    c._text(ref['path'])
    _hash(ref['sha256'])
    c.require(type(ref['bytes']) is int and 0 <= ref['bytes'] <= c.MAX_FILE,
              'INVALID_SCHEMA', 'Invalid evidence byte count')
    if current:
        c._revalidate(ref)
    return ref


def _refs(rows, current=True):
    c._rows(rows)
    for ref in rows:
        _ref(ref, current)
    c.require(len({c.sha(c.packed(r)) for r in rows}) == len(rows),
              'INVALID_SCHEMA', 'Duplicate evidence refs')
    return rows


def _policy(policy):
    c._shape(policy, 'schema lineage_id goal caller max_attempts history_complete history_note')
    c.require(policy['schema'] == 'orchestrator.loop-policy.v1', 'INVALID_SCHEMA', 'Policy schema')
    c._identifier(policy['lineage_id'])
    for key in ('goal', 'caller', 'history_note'):
        c._text(policy[key])
    c.require(type(policy['max_attempts']) is int and 1 <= policy['max_attempts'] <= 100,
              'INVALID_SCHEMA', 'Explicit lineage attempt cap required')
    c.require(type(policy['history_complete']) is bool, 'INVALID_SCHEMA', 'History completeness boolean')
    return policy


def _source(path):
    raw = c._read(path, c.MAX_JSON)
    return c.decode(raw), raw


@contextmanager
def _locked(ledger):
    root = c._external(ledger)
    c.require(root.is_dir(), 'LEDGER_MISSING', 'Explicit existing ledger required')
    lock = c._safe(root / '.lock')
    try:
        stream = lock.open('xb')
    except FileExistsError as exc:
        raise c.SessionError('LEDGER_LOCKED', 'Ledger has an active or stale lock; no automatic recovery') from exc
    try:
        with stream:
            stream.write(b'cooperative-single-writer\n')
            stream.flush()
            os.fsync(stream.fileno())
        yield root
    finally:
        lock.unlink()


def _load(ledger, expected_head, locked=False):
    root = c._external(ledger)
    c.require(root.is_dir(), 'LEDGER_MISSING', 'Explicit existing ledger required')
    _hash(expected_head)
    names = sorted(p.name for p in root.iterdir())
    if '.lock' in names:
        c.require(locked, 'LEDGER_LOCKED', 'Ledger is locked')
        names.remove('.lock')
    c.require(names and names == [f'{i:08d}' for i in range(1, len(names) + 1)],
              'LEDGER_INVALID', 'Ledger missing genesis, malformed entries, or sequence gaps')
    events, head = [], None
    for seq, name in enumerate(names, 1):
        directory = c._safe(root / name)
        manifest = c.decode(c._read(directory / 'manifest.json', c.MAX_JSON))
        c._shape(manifest, 'schema files')
        c.require(type(manifest['files']) is dict and set(manifest['files']) in (
            {'event.json', 'source.bin'}, {'event.json', 'source.bin', 'failure.bin'}),
            'LEDGER_INVALID', 'Unexpected manifest file names')
        files, digest = c._bundle(directory, set(manifest['files']))
        c.require(set(p.name for p in directory.iterdir()) == set(files) | {'manifest.json'},
                  'LEDGER_INVALID', 'Unexpected event files')
        c.require('event.json' in files, 'LEDGER_INVALID', 'Missing event')
        event = c.decode(files['event.json'])
        c._shape(event, 'schema seq previous_sha256 kind payload')
        c.require(event['schema'] == 'orchestrator.loop-event.v1' and type(event['seq']) is int
                  and event['seq'] == seq and event['previous_sha256'] == head,
                  'LEDGER_INVALID', 'Hash chain or sequence mismatch')
        c.require(event['kind'] in ('POLICY', 'OBSERVATION', 'REVIEW', 'RESERVATION'),
                  'LEDGER_INVALID', 'Unknown event kind')
        c.require((seq == 1) == (event['kind'] == 'POLICY'), 'LEDGER_INVALID', 'Policy must be genesis only')
        if seq == 1:
            _policy(event['payload'])
        event = {**event, '_sha256': digest, '_files': files}
        try:
            _snapshot(event, events)
        except (KeyError, TypeError, AttributeError, IndexError) as exc:
            raise c.SessionError('LEDGER_INVALID', 'Malformed historical payload') from exc
        events.append(event)
        head = digest
    c.require(head == expected_head, 'HEAD_MISMATCH', 'Selected expected head differs from verified ledger')
    return root, events, events[0]['payload'], head


def _append(root, events, kind, payload, files=None):
    event = {'schema': 'orchestrator.loop-event.v1', 'seq': len(events) + 1,
             'previous_sha256': events[-1]['_sha256'] if events else None,
             'kind': kind, 'payload': payload}
    directory = c._mkdir(root / f'{len(events) + 1:08d}')
    return c._commit(directory, {'event.json': c.packed(event), **(files or {})})


def _report(status, head, policy, used, **extra):
    return {'status': status, 'head': head, 'lineage_id': policy['lineage_id'],
            'used_attempts': used, 'max_attempts': policy['max_attempts'],
            'budget_scope': 'CALLER_DECLARED_LINEAGE_IN_SELECTED_LEDGER',
            'authority_granted': False, 'dispatch': False, 'authenticated_review': False,
            'full_completion': False, 'review_origin': 'UNVERIFIED_CALLER_RECORD',
            'history_origin': 'UNVERIFIED_CALLER_ASSERTION',
            'limitations': ['Opt-in only; v1 and outside callers can bypass this guard',
                            'Hash chains and selected heads are consistency checks, not authentication',
                            'No global tool/time/cost control or semantic relevance verification'], **extra}


def init(ledger, policy_file):
    policy, raw = _source(policy_file)
    _policy(policy)
    root = c._external(ledger)
    c.require(root.parent.is_dir(), 'INPUT_UNAVAILABLE', 'Ledger parent must already exist')
    c._mkdir(root)
    with _locked(root):
        head = _append(root, [], 'POLICY', policy, {'source.bin': raw})
    return _report('LEDGER_CREATED', head, policy, 0)


def _binding(task, task_hash):
    binding = c._binding(task, task_hash, 'unused')
    binding.pop('attempt_id')
    return binding


def _common(record, policy):
    c.require(record['lineage_id'] == policy['lineage_id'] and record['caller'] == policy['caller'],
              'BINDING_MISMATCH', 'Caller/lineage differs from selected policy')
    for key in ('goal_revision', 'operation', 'caller', 'resource', 'failure_family'):
        c._text(record[key])
    c._identifier(record['attempt_id'])
    c._identifier(record['criterion_id'])
    c._text(record['task_dir'])


def _prerequisites(rows, current=True):
    c._rows(rows)
    seen = set()
    for row in rows:
        c._shape(row, 'id state evidence')
        c._identifier(row['id'])
        c.require(row['id'] not in seen and row['state'] in ('READY', 'BLOCKED', 'UNKNOWN'),
                  'INVALID_SCHEMA', 'Prerequisite IDs/state')
        seen.add(row['id'])
        _refs(row['evidence'], current)
    return [r['id'] for r in rows if r['state'] != 'READY']


def _branch(record):
    return tuple(record[k] for k in ('caller', 'operation', 'criterion_id', 'resource'))


def _attempt_key(binding):
    return binding['task_sha256'], binding['attempt_id']


def _used(events):
    return sum(e['kind'] == 'RESERVATION' or
               (e['kind'] == 'OBSERVATION' and e['payload']['imported']) for e in events)


def _observations(events, record):
    return [e for e in events if e['kind'] == 'OBSERVATION' and
            _branch(e['payload']['record']) == _branch(record)]


def _progress(value, current=True):
    if value is None:
        return
    c._shape(value, 'kind note evidence')
    c.require(value['kind'] in ('SOURCE_CHANGE', 'HYPOTHESIS_REFUTED', 'PREREQUISITE_PROVEN', 'CRITERION_IMPROVED'),
              'INVALID_SCHEMA', 'Progress kind')
    c._text(value['note'])
    _refs(value['evidence'], current)
    c.require(value['evidence'], 'INVALID_EVIDENCE', 'Progress needs pinned evidence')


def _candidate(candidate_file, policy):
    record, raw = _source(candidate_file)
    c._shape(record, 'schema lineage_id goal_revision task_dir attempt_id operation caller criterion_id resource failure_family previous_observation prerequisites progress')
    c.require(record['schema'] == 'orchestrator.loop-candidate.v1', 'INVALID_SCHEMA', 'Candidate schema')
    _common(record, policy)
    if record['previous_observation'] is not None:
        _hash(record['previous_observation'])
    blocked = _prerequisites(record['prerequisites'])
    _progress(record['progress'])
    _, task, task_hash = c._task(record['task_dir'])
    blocked += ['dependency:' + row['id'] for row in task['request']['dependencies']
                if row['required'] and row['status'] == 'BLOCKED']
    c.require(record['criterion_id'] in {r['id'] for r in task['request']['acceptance']},
              'BINDING_MISMATCH', 'Criterion not in v1 task')
    binding = _binding(task, task_hash)
    digest = c.sha(c.packed({'candidate': record, 'binding': binding}))
    return record, raw, binding, digest, blocked


def _normalize(record, raw):
    rules = c._rows(record['noise'])
    seen = set()
    for rule in rules:
        c._shape(rule, 'kind value')
        c._text(rule['value'])
        value, kind = rule['value'], rule['kind']
        c.require(kind in ('TIMESTAMP', 'UUID', 'TEMP_PREFIX'), 'INVALID_SCHEMA', 'Noise kind')
        c.require(value not in seen, 'INVALID_SCHEMA', 'Duplicate noise value')
        seen.add(value)
        try:
            if kind == 'UUID':
                c.require(str(uuid.UUID(value)) == value.lower(), 'INVALID_SCHEMA', 'Canonical UUID required')
            elif kind == 'TIMESTAMP':
                c.require('T' in value, 'INVALID_SCHEMA', 'ISO timestamp required')
                datetime.fromisoformat(value.replace('Z', '+00:00'))
            else:
                c.require(value.endswith(('/', '\\')) and value != record['resource'],
                          'INVALID_SCHEMA', 'Explicit temporary directory prefix required')
        except (ValueError, AttributeError) as exc:
            raise c.SessionError('INVALID_SCHEMA', 'Malformed declared noise') from exc
        c.require(not any(value in record[k] or record[k] in value for k in ('operation', 'caller', 'criterion_id', 'resource', 'failure_family')),
                  'INVALID_SCHEMA', 'Noise would erase a distinguishing field')
    try:
        text = raw.decode('utf-8')
    except UnicodeError:
        return {'version': 'literal-noise-v1', 'raw_sha256': c.sha(raw), 'rules': rules,
                'text': None, 'sha256': None, 'status': 'UNKNOWN_NON_TEXT'}
    for rule in sorted(rules, key=lambda r: (-len(r['value']), r['kind'], r['value'])):
        text = text.replace(rule['value'], '<' + rule['kind'] + '>')
    return {'version': 'literal-noise-v1', 'raw_sha256': c.sha(raw), 'rules': rules,
            'text': text, 'sha256': c.sha(text.encode('utf-8')), 'status': 'NORMALIZED'}


def observe(ledger, expected_head, observation_file):
    record, raw = _source(observation_file)
    c._shape(record, 'schema lineage_id goal_revision task_dir attempt_id operation caller criterion_id resource failure_family raw_failure noise prerequisites steps')
    c.require(record['schema'] == 'orchestrator.loop-observation.v1', 'INVALID_SCHEMA', 'Observation schema')
    with _locked(ledger) as root:
        _, events, policy, head = _load(root, expected_head, True)
        _common(record, policy)
        _prerequisites(record['prerequisites'])
        # M4-D is separately inspected through trace_review; no second DAG interpretation.
        c.require(record['steps'] == [], 'INVALID_SCHEMA', 'Use trace-check for ordered trace; steps must be empty')
        _ref(record['raw_failure'])
        failure = c._read(record['raw_failure']['path'])
        c.require(c.sha(failure) == record['raw_failure']['sha256'], 'STALE_SOURCE', 'Failure changed while reading')
        _, task, packet = c._attempt(record['task_dir'], record['attempt_id'])
        c.check(record['task_dir'], record['attempt_id'])
        c.require(record['criterion_id'] in {r['id'] for r in task['request']['acceptance']},
                  'BINDING_MISMATCH', 'Unknown criterion')
        binding = packet['binding']
        prior_observations = [e for e in events if e['kind'] == 'OBSERVATION']
        c.require(not any(_attempt_key(e['payload']['binding']) == _attempt_key(binding) for e in prior_observations),
                  'DUPLICATE_ATTEMPT', 'Attempt already observed')
        reservations = [e for e in events if e['kind'] == 'RESERVATION' and
                        _attempt_key(e['payload']['binding']) == _attempt_key(binding)]
        imported = not reservations
        if reservations:
            planned = reservations[0]['payload']['candidate']
            c.require(all(record[k] == planned[k] for k in ('goal_revision', 'operation', 'caller', 'criterion_id', 'resource', 'failure_family')),
                      'BINDING_MISMATCH', 'Observation differs from reservation')
        c.require(not imported or _used(events) < policy['max_attempts'], 'ATTEMPT_BUDGET', 'Imported attempt exceeds cap')
        normal = _normalize(record, failure)
        failure_key = {k: record[k] for k in ('caller', 'operation', 'criterion_id', 'resource', 'failure_family')}
        failure_key['normalized_sha256'] = normal['sha256']
        fingerprint = {**failure_key, 'lineage_id': record['lineage_id'], 'goal_revision': record['goal_revision'],
                       'inputs_sha256': binding['inputs_sha256'], 'context_sha256': binding['context_sha256'],
                       'prerequisites': record['prerequisites']}
        payload = {'record': record, 'binding': binding, 'imported': imported, 'normalization': normal,
                   'failure_key': failure_key, 'fingerprint_sha256': c.sha(c.packed(fingerprint)),
                   'first_observed_violation': None, 'attribution': 'UNRESOLVED'}
        head = _append(root, events, 'OBSERVATION', payload, {'source.bin': raw, 'failure.bin': failure})
        return _report('OBSERVATION_RECORDED', head, policy, _used(events) + int(imported),
                       normalization=normal, imported=imported, failure_key=failure_key)


def _validate_review(record, expected_head, policy, current=True):
    c._shape(record, 'schema lineage_id prior_head candidate_sha256 previous_observation reviewer producer provenance verdict evidence rationale')
    c.require(record['schema'] == 'orchestrator.loop-review.v1' and record['lineage_id'] == policy['lineage_id'],
              'INVALID_SCHEMA', 'Review schema/lineage')
    c.require(record['prior_head'] == expected_head, 'HEAD_MISMATCH', 'Review prior head')
    _hash(record['candidate_sha256'])
    _hash(record['previous_observation'])
    for key in ('reviewer', 'producer', 'provenance', 'rationale'):
        c._text(record[key])
    c.require(record['reviewer'] != record['producer'], 'INVALID_SCHEMA', 'Same producer/reviewer label')
    c.require(record['verdict'] in ('RELEVANT_PROGRESS', 'NO_PROGRESS', 'UNKNOWN'), 'INVALID_SCHEMA', 'Review verdict')
    _refs(record['evidence'], current)
    c.require(record['evidence'], 'INVALID_EVIDENCE', 'Review needs pinned evidence')


def _snapshot(event, previous):
    """Validate immutable historical payloads without consulting old live sources."""
    kind, payload, files = event['kind'], event['payload'], event['_files']
    c.require(set(files) == ({'event.json', 'source.bin', 'failure.bin'} if kind == 'OBSERVATION'
                            else {'event.json', 'source.bin'}), 'LEDGER_INVALID', 'Event file set')
    source = c.decode(files['source.bin'])
    if kind == 'POLICY':
        c.require(source == payload, 'BINDING_MISMATCH', 'Policy snapshot differs')
        return
    policy = previous[0]['payload']
    if kind == 'REVIEW':
        c.require(source == payload, 'BINDING_MISMATCH', 'Review snapshot differs')
        _validate_review(payload, event['previous_sha256'], policy, False)
        c.require(any(e['kind'] == 'OBSERVATION' and e['_sha256'] == payload['previous_observation'] for e in previous),
                  'BINDING_MISMATCH', 'Historical review references missing observation')
        return
    if kind == 'OBSERVATION':
        c._shape(payload, 'record binding imported normalization failure_key fingerprint_sha256 first_observed_violation attribution')
        record = payload['record']
        c._shape(record, 'schema lineage_id goal_revision task_dir attempt_id operation caller criterion_id resource failure_family raw_failure noise prerequisites steps')
        c.require(record['schema'] == 'orchestrator.loop-observation.v1' and source == record,
                  'BINDING_MISMATCH', 'Observation snapshot differs')
        c.require(type(payload['imported']) is bool and record['steps'] == [], 'INVALID_SCHEMA', 'Observation flags/steps')
        _ref(record['raw_failure'], False)
        c.require(record['raw_failure']['sha256'] == c.sha(files['failure.bin']) and
                  record['raw_failure']['bytes'] == len(files['failure.bin']), 'INTEGRITY_MISMATCH', 'Raw failure snapshot differs')
        normal = _normalize(record, files['failure.bin'])
        c.require(normal == payload['normalization'], 'INTEGRITY_MISMATCH', 'Normalization differs from raw')
        failure_key = {k: record[k] for k in ('caller', 'operation', 'criterion_id', 'resource', 'failure_family')}
        failure_key['normalized_sha256'] = normal['sha256']
        fingerprint = {**failure_key, 'lineage_id': record['lineage_id'], 'goal_revision': record['goal_revision'],
                       'inputs_sha256': payload['binding']['inputs_sha256'],
                       'context_sha256': payload['binding']['context_sha256'], 'prerequisites': record['prerequisites']}
        c.require(payload['failure_key'] == failure_key and payload['fingerprint_sha256'] == c.sha(c.packed(fingerprint))
                  and payload['first_observed_violation'] is None and payload['attribution'] == 'UNRESOLVED',
                  'INTEGRITY_MISMATCH', 'Historical observation derivation differs')
    else:
        c._shape(payload, 'candidate candidate_sha256 binding selected_review decision budget_before budget_after')
        record = payload['candidate']
        c._shape(record, 'schema lineage_id goal_revision task_dir attempt_id operation caller criterion_id resource failure_family previous_observation prerequisites progress')
        c.require(record['schema'] == 'orchestrator.loop-candidate.v1' and source == record,
                  'BINDING_MISMATCH', 'Candidate snapshot differs')
        c.require(type(payload['budget_before']) is int and type(payload['budget_after']) is int and
                  payload['budget_before'] == _used(previous) and payload['budget_after'] == _used(previous) + 1,
                  'LEDGER_INVALID', 'Reservation budget derivation differs')
        binding = dict(payload['binding'])
        binding.pop('attempt_id', None)
        c.require(payload['candidate_sha256'] == c.sha(c.packed({'candidate': record, 'binding': binding})),
                  'BINDING_MISMATCH', 'Historical candidate digest differs')
        c.require(payload['decision'] in ('INITIAL_ATTEMPT_CANDIDATE', 'BOUNDED_RETRY_CANDIDATE'),
                  'LEDGER_INVALID', 'Reservation decision')
        _progress(record['progress'], False)
        c.require(policy['history_complete'] and not _prerequisites(record['prerequisites'], False),
                  'LEDGER_INVALID', 'Reservation had incomplete history or blocked declared prerequisites')
        observations = _observations(previous, record)
        latest = observations[-1]['_sha256'] if observations else None
        c.require(record['previous_observation'] == latest, 'BINDING_MISMATCH', 'Historical candidate prior observation differs')
        pending = [e for e in previous if e['kind'] == 'RESERVATION' and
                   _branch(e['payload']['candidate']) == _branch(record) and not any(
                       _attempt_key(o['payload']['binding']) == _attempt_key(e['payload']['binding'])
                       for o in observations)]
        c.require(not pending, 'LEDGER_INVALID', 'Reservation repeated an unobserved branch attempt')
        if payload['selected_review'] is not None:
            c.require(previous[-1]['kind'] == 'REVIEW' and previous[-1]['_sha256'] == payload['selected_review'],
                      'BINDING_MISMATCH', 'Reservation review not preceding head')
            selected = previous[-1]['payload']
            c.require(selected['candidate_sha256'] == payload['candidate_sha256'] and
                      selected['previous_observation'] == record['previous_observation'] and record['progress'] is not None and
                      sorted(c.packed(r) for r in selected['evidence']) == sorted(c.packed(r) for r in record['progress']['evidence']) and
                      selected['verdict'] == 'RELEVANT_PROGRESS' and payload['decision'] == 'BOUNDED_RETRY_CANDIDATE',
                      'BINDING_MISMATCH', 'Reservation review binding/verdict differs')
        else:
            c.require(payload['decision'] == 'INITIAL_ATTEMPT_CANDIDATE' and _used(previous) == 0 and latest is None,
                      'LEDGER_INVALID', 'Initial reservation had prior attempts or retry has no selected review')
    _common(record, policy)
    _prerequisites(record['prerequisites'], False)
    binding = payload['binding']
    keys = 'task_id attempt_id task_sha256 original_sha256 inputs_sha256 context_sha256'
    c._shape(binding, keys + (' packet_sha256' if kind == 'OBSERVATION' else ''))
    c._identifier(binding['task_id'])
    c.require(binding['attempt_id'] == record['attempt_id'], 'BINDING_MISMATCH', 'Attempt binding differs')
    for key in set(binding) - {'task_id', 'attempt_id'}:
        _hash(binding[key])
    matches = [e for e in previous if e['kind'] in ('OBSERVATION', 'RESERVATION') and
               _attempt_key(e['payload']['binding']) == _attempt_key(binding)]
    if kind == 'RESERVATION':
        c.require(not matches, 'DUPLICATE_ATTEMPT', 'Duplicate historical reservation')
    else:
        c.require(not any(e['kind'] == 'OBSERVATION' for e in matches), 'DUPLICATE_ATTEMPT', 'Duplicate historical observation')
        reserved = [e for e in matches if e['kind'] == 'RESERVATION']
        c.require(payload['imported'] == (not reserved), 'LEDGER_INVALID', 'Historical import flag differs')
        if reserved:
            planned = reserved[0]['payload']
            c.require(all(binding[k] == v for k, v in planned['binding'].items()) and
                      all(record[k] == planned['candidate'][k] for k in ('goal_revision', 'operation', 'caller', 'criterion_id', 'resource', 'failure_family')),
                      'BINDING_MISMATCH', 'Historical reservation/observation differs')
    c.require(_used(previous) + int(kind == 'RESERVATION' or payload.get('imported', False)) <= policy['max_attempts'],
              'LEDGER_INVALID', 'Historical budget exceeded')


def review(ledger, expected_head, review_file):
    record, raw = _source(review_file)
    with _locked(ledger) as root:
        _, events, policy, head = _load(root, expected_head, True)
        _validate_review(record, head, policy)
        c.require(any(e['_sha256'] == record['previous_observation'] and e['kind'] == 'OBSERVATION' for e in events),
                  'BINDING_MISMATCH', 'Review references missing observation')
        head = _append(root, events, 'REVIEW', record, {'source.bin': raw})
        return _report('REVIEW_RECORDED_UNVERIFIED', head, policy, _used(events))


def _decision(events, policy, head, candidate_file, root_review):
    record, raw, binding, digest, blocked = _candidate(candidate_file, policy)
    used = _used(events)
    extra = {'candidate_sha256': digest, 'candidate_binding': binding,
             'selected_review': root_review, 'reopen_condition': 'Provide relevant current evidence and explicit root-selected bound review within remaining cap'}
    observations = _observations(events, record)
    latest = observations[-1]['_sha256'] if observations else None
    c.require(record['previous_observation'] == latest, 'BINDING_MISMATCH', 'Candidate must bind latest branch observation')
    planned_binding = {**binding, 'attempt_id': record['attempt_id']}
    existing = [e for e in events if e['kind'] in ('OBSERVATION', 'RESERVATION') and
                _attempt_key(e['payload']['binding']) == _attempt_key(planned_binding)]
    c.require(not existing and not os.path.lexists(Path(record['task_dir']) / 'attempts' / record['attempt_id']),
              'DUPLICATE_ATTEMPT', 'Candidate attempt already exists or reserved')
    pending = [e for e in events if e['kind'] == 'RESERVATION' and
               _branch(e['payload']['candidate']) == _branch(record) and not any(
                   _attempt_key(o['payload']['binding']) == _attempt_key(e['payload']['binding'])
                   for o in observations)]
    if used >= policy['max_attempts']:
        status = 'STOP_BUDGET'
    elif not policy['history_complete'] or blocked or pending:
        status = 'WAIT_EVIDENCE'
        extra['gaps'] = (['history_incomplete'] if not policy['history_complete'] else []) + blocked + (['unobserved_reserved_attempt'] if pending else [])
    elif latest is None:
        status = 'INITIAL_ATTEMPT_CANDIDATE' if used == 0 else 'WAIT_PROGRESS_REVIEW'
        if used:
            extra['gaps'] = ['new_branch_independence_not_established']
    elif root_review is None:
        same = (observations[-1]['payload']['record']['failure_family'] == record['failure_family'] and
                observations[-1]['payload']['normalization']['status'] == 'NORMALIZED')
        status = 'STOP_NO_PROGRESS' if record['progress'] is None and same else 'WAIT_PROGRESS_REVIEW'
    else:
        _hash(root_review)
        c.require(root_review == head and events[-1]['kind'] == 'REVIEW',
                  'BINDING_MISMATCH', 'Selected review must be current ledger head')
        selected = events[-1]['payload']
        c.require(record['progress'] is not None and selected['candidate_sha256'] == digest
                  and selected['previous_observation'] == latest
                  and sorted(c.packed(r) for r in selected['evidence']) == sorted(c.packed(r) for r in record['progress']['evidence']),
                  'BINDING_MISMATCH', 'Review candidate/observation/evidence binding')
        _refs(selected['evidence'])
        status = {'RELEVANT_PROGRESS': 'BOUNDED_RETRY_CANDIDATE', 'NO_PROGRESS': 'STOP_NO_PROGRESS',
                  'UNKNOWN': 'WAIT_PROGRESS_REVIEW'}[selected['verdict']]
    return _report(status, head, policy, used, **extra), record, raw, planned_binding


def check(ledger, expected_head, candidate_file, root_review=None):
    _, events, policy, head = _load(ledger, expected_head)
    return _decision(events, policy, head, candidate_file, root_review)[0]


def prepare(ledger, expected_head, candidate_file, root_review=None, executor='UNKNOWN', parent_attempt=None):
    with _locked(ledger) as root:
        _, events, policy, head = _load(root, expected_head, True)
        result, candidate, raw, binding = _decision(events, policy, head, candidate_file, root_review)
        c.require(result['status'] in ('INITIAL_ATTEMPT_CANDIDATE', 'BOUNDED_RETRY_CANDIDATE'),
                  'GUARD_STOP', result['status'])
        payload = {'candidate': candidate, 'candidate_sha256': result['candidate_sha256'],
                   'binding': binding, 'selected_review': root_review, 'decision': result['status'],
                   'budget_before': result['used_attempts'], 'budget_after': result['used_attempts'] + 1}
        head = _append(root, events, 'RESERVATION', payload, {'source.bin': raw})
        try:
            work = c.prepare_work(candidate['task_dir'], candidate['attempt_id'],
                                  parent_attempt=parent_attempt, executor=executor)
        except (c.SessionError, OSError, ValueError, TypeError) as exc:
            return _report('PREPARE_FAILED_RESERVED', head, policy, result['used_attempts'] + 1,
                           error=str(exc), error_code=getattr(exc, 'code', type(exc).__name__), reservation_consumed=True)
        return _report('WORK_PREPARED_GUARDED', head, policy, result['used_attempts'] + 1,
                       decision=result['status'], work=work, reservation_consumed=True)
