"""Evidence-bound trace observations, never automatic root-cause attribution."""
import re

from .core import _shape, _rows, _identifier, _text, _revalidate, require


def _ref(ref):
    _shape(ref, 'path bytes sha256')
    _text(ref['path'])
    require(type(ref['bytes']) is int and ref['bytes'] >= 0
            and type(ref['sha256']) is str
            and re.fullmatch('[0-9a-f]{64}', ref['sha256']),
            'INVALID_SCHEMA', 'Evidence pin types/digest')
    _revalidate(ref)


def inspect_trace(trace):
    """Inspect caller-declared topological order; all facts remain local claims.

    An observation requires byte-current evidence. A first failing observation is
    reported only when every transitive predecessor has evidenced SATISFIED
    criteria and its dependencies precede it. Unlisted intermediate steps remain
    outside the scope; trace completeness is not authenticated.
    """
    _shape(trace, 'schema steps hypotheses')
    require(trace['schema'] == 'orchestrator.loop-trace.v1', 'INVALID_SCHEMA', 'Trace schema')
    steps = _rows(trace['steps'])
    seen = set()
    observations = []
    first = []
    satisfied_ancestry = {}
    for step in steps:
        _shape(step, 'id depends_on kind criterion status inputs outputs evidence')
        _identifier(step['id'])
        require(step['id'] not in seen, 'INVALID_SCHEMA', 'Duplicate trace step')
        dependencies = _rows(step['depends_on'])
        require(all(type(d) is str and d in seen for d in dependencies)
                and len(set(dependencies)) == len(dependencies),
                'INVALID_SCHEMA', 'Trace must be topologically ordered with known dependencies')
        require(step['kind'] in ('ENVIRONMENT', 'TOOL', 'SEMANTIC'), 'INVALID_SCHEMA', 'Step kind')
        require(step['status'] in ('SATISFIED', 'VIOLATED', 'UNKNOWN'), 'INVALID_SCHEMA', 'Step status')
        _text(step['criterion'])
        for field in ('inputs', 'outputs', 'evidence'):
            for ref in _rows(step[field]):
                _ref(ref)
        evidenced = bool(step['evidence'])
        predecessors_known = all(satisfied_ancestry[d] for d in dependencies)
        if step['status'] == 'VIOLATED' and evidenced:
            observations.append({'step': step['id'], 'kind': step['kind'],
                                 'criterion': step['criterion'], 'evidence': step['evidence']})
            if predecessors_known:
                first.append(step['id'])
        satisfied_ancestry[step['id']] = (predecessors_known and evidenced
                                         and step['status'] == 'SATISFIED')
        seen.add(step['id'])
    hypotheses = _rows(trace['hypotheses'])
    for hypothesis in hypotheses:
        _shape(hypothesis, 'claim supporting_steps counterevidence uncertainty')
        for field in ('claim', 'uncertainty'):
            _text(hypothesis[field])
        require(all(type(s) is str and s in seen for s in _rows(hypothesis['supporting_steps'])),
                'INVALID_SCHEMA', 'Unknown hypothesis step')
        for ref in _rows(hypothesis['counterevidence']):
            _ref(ref)
    return {'schema': 'orchestrator.loop-trace-report.v1',
            'status': 'FIRST_OBSERVED_VIOLATION' if first else 'UNRESOLVED',
            'first_observed_violation': first[0] if len(first) == 1 else None,
            'first_observed_violations': sorted(first), 'observations': observations,
            'attribution_hypotheses': hypotheses, 'confirmed_root_cause': None,
            'missing_observation': None if first else 'Provide evidenced ordered intermediates before attributing the failure.',
            'scope': 'CALLER_DECLARED_TRACE_ONLY', 'authenticated_acceptance': False}
