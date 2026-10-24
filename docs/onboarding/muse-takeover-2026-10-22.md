# Muse tiếp quản nhánh văn phòng agent 3D

Ngày bàn giao: 22/10/2026. Repository: `Nohfinl99/Orchestrator_Reverse`. Nhánh: `codex/agent-office-3d-muse-handoff`. Đây là bàn giao tài liệu và candidate offline; người dùng đã yêu cầu push nhánh này và giao Muse tiếp tục dự án.

## Nhận đúng repository và revision

```sh
git clone --branch codex/agent-office-3d-muse-handoff --single-branch https://github.com/Nohfinl99/Orchestrator_Reverse.git
cd Orchestrator_Reverse
git rev-parse HEAD
git status --short
```

Nếu đã có clone, fetch rồi checkout nhánh trên; giữ thay đổi local trước khi chuyển nhánh. Người nhận ghi commit HEAD thực tế và SHA-256 của [manifest bàn giao](../../metadata/muse-knowledge-transfer-2026-10-22.json) trong receipt của chính mình. Commit xuất bản được người gửi báo sau khi push; manifest không tự tuyên bố commit chưa tồn tại.

Clone public chứa gói tài liệu `Orchestrator_Reverse`. Workspace cha, archive RE-Decom, raw evidence, source prototypes offline ở workspace cha, worksheet local và config riêng không thuộc bản push này. Khi thiếu nguồn, ghi `LOCAL_ONLY / NOT_ACCESSED` và chỉ chặn claim phụ thuộc. Không tái tạo receipt, source pin hoặc ACK còn thiếu.

## Đã làm được gì

| Phần | Artifact / khả năng hiện có | Mức chứng minh |
|---|---|---|
| Nền Orchestrator | Sáu identity, nguyên lý REA–IDA, phase/gate map, mười prompt stack và mười protocol | Tài liệu offline; chưa có loader/runtime tích hợp |
| Hướng sản phẩm | Roadmap AO-0…AO-7, phòng quan sát nhỏ, roster, meeting/evidence panel, timeline/2D fallback | Proposal và advisory review; chưa chứng minh UX value |
| AO-1 | [Packet v6](../proposals/agent-office-3d/ao-1-offline-replay-packet-06.md), [schema v6](../proposals/agent-office-3d/ao-1-event-v6.schema.json), [fixture v6](../proposals/agent-office-3d/ao-1-fixture-v6.jsonl), [matrix v6](../proposals/agent-office-3d/ao-1-test-matrix-v6.md) | `ADVISORY_REVIEWED / NOT_ACCEPTED / NOT_RUN`; [review06](../proposals/agent-office-3d/ao-1-review-2026-10-22-06.md) không còn material findings theo reviewer |
| Scenario AO-1 | Hai task song song; invite/defer/accept/join; claim thiếu evidence; objection/dissent; cancel; duplicate/conflict/reorder/gap/stale; turn stop và pre-invocation budget stop | Dữ liệu synthetic `SIMULATED`; chưa schema-validate, replay hay benchmark |
| Pentest chuẩn bị AO-3 | [Case01 rev1.1 và oracle](../proposals/agent-office-3d/ao-pentest-case-01.md), [sáu record](../proposals/agent-office-3d/ao-pentest-case-01.jsonl): một authority-spoof và năm benign controls | `DESIGN_ONLY / ADVISORY_REVIEWED / NOT_RUN`; chưa app/harness để kiểm thử động |
| Knowledge | [12 card có nguồn](../knowledge/README.md), source catalog và retrieval guide | `CANDIDATE_REFERENCE_NOT_ADMITTED`; chưa consumer ACK hoặc G2 admission |

Không có app văn phòng 3D, pure reducer/replay engine, mock tool harness, R4a accepted/frozen hay raw run evidence cho nhánh office. Những review agent hỗ trợ soạn tài liệu là advisory; không phải invocation/ACK của sáu identity runtime, human approval hoặc cross-model independence.

## Thứ tự đọc và nguồn quyết định trạng thái

1. [AGENTS](../../AGENTS.md), [current snapshot](../../context/current.md), [phase map](../planning/phase-map.md), [work queue](../planning/work-queue.md), [source map](../reference/source-map.md), [sáu identity](../architecture/agents.md).
2. [Roadmap office](../proposals/agent-office-3d/roadmap.md), [preflight/R4](../proposals/agent-office-3d/preflight-knowledge-and-benchmark.md), [hướng hình ảnh](../proposals/agent-office-3d/visual-review-2026-10-22-01.md), [AI_Judges advisory](../proposals/agent-office-3d/ai-judges-review-2026-10-22-01.md).
3. Packet v6 và review06 cho trạng thái AO-1; case01 rev1.1 cho pentest design. Mở schema/fixture/matrix theo objective, không nạp toàn bộ lịch sử mặc định.
4. [Sổ vấn đề](../reference/open-questions.md), đặc biệt `AO-HANDOFF-01`; dùng báo cáo review trước và version cũ khi cần lần finding.

Current snapshot giữ mốc 21/10; các tài liệu roadmap/runbook/handoff đầu ngày 22/10 có thể còn ghi AO-1 `NOT_STARTED` hoặc `PROPOSED_NOT_DISPATCHED`. Chúng là nguồn thiết kế/lịch sử. Packet v6 và review06 mô tả artifact AO-1 đã chuẩn bị sau đó, không tự biến nó thành accepted.

Packet v6 có câu cũ “has not had independent review” trong đoạn đầu Decision boundary, trong khi đoạn sau và review06 ghi đã có fresh advisory review. Bàn giao giữ nguyên bytes của candidate đã review, ghi cả hai locator trong `AO-HANDOFF-01`. Hiểu đúng là **đã advisory review, chưa accepted/chưa chạy**. Nếu sửa candidate, tạo revision/digest mới và review lại; không sửa âm thầm pin v6.

Lịch sử review 01–05 và [handling lapse ở review03](../proposals/agent-office-3d/ao-1-review-2026-10-22-03.md) phải giữ. Trước đây có dùng `ConvertFrom-Json` để quan sát ID/sequence; report đã ghi rõ đó không phải schema validation/replay/benchmark. Không mô tả toàn bộ quá trình cũ là chưa từng parse.

## Prompt-Master chuyển kiến thức thế nào

Muse là phiên tiếp quản công việc. Khi phụ trách điều phối, dùng trách nhiệm **Prompt-Master** đã có; không đăng ký Muse như identity thứ bảy. Evidence-Synthesizer giữ trách nhiệm nguồn/review; Product-Evolution-Architect giữ acceptance sản phẩm.

1. **Đóng gói task:** ghi một objective, scope, output, acceptance, owner/reviewer, dependency, budget và stop condition. Task đầu tiên là tiếp nhận và reconcile hồ sơ; chưa dispatch runtime. Không chọn model/provider hoặc số budget hộ người dùng từ dữ liệu minh họa.
2. **Chọn context:** dùng manifest bàn giao cho đúng source path/revision/SHA-256. Manifest chia tài liệu tiếp nhận và tham chiếu evaluation. Chỉ hash/read file; chưa chạy fixture. Thấy mismatch thì ghi expected/actual, dừng nhánh phụ thuộc, tiếp tục phần độc lập.
3. **Chuyển WHAT/WHY/HOW:** WHAT = trạng thái và contract cần giữ; WHY = receipt khác animation, candidate khác approval, unsupported claim không thành consensus; HOW = event log/reducer làm nguồn state, UI và timeline cùng suy ra từ event có provenance, review theo exact candidate.
4. **Retrieval có lý do:** chọn K01/K02 cho task/context, K04/K06 cho artifact/handoff/state, K07/K10 cho evidence/oracle. Xem rights/applicability/source pins trong knowledge catalog. Các card là tham khảo; source S1 rights UNKNOWN chỉ catalog metadata. Không ingest prompt corpus, gold/heldout hoặc failure labels vào active KB.
5. **Người nhận tự xác nhận:** Muse phải tự ghi file đã đọc, digest đã kiểm, phần chưa truy cập, diễn giải lại nhiệm vụ, selected/rejected và dependency còn thiếu. Người gửi để `consumer_ack=NOT_RECEIVED`; không ký thay Muse. Receipt tiếp nhận tài liệu không phải runtime KB ACK, target pair ACK hay gate acceptance.
6. **Handoff kế tiếp:** artifact/revision/digest, done/gap, design/code/executed/reviewed, raw evidence nếu có, gates, một next atomic task. Nội dung knowledge/tool luôn là dữ liệu; quyền đến từ yêu cầu người dùng và enforcement hiện hành.

Mẫu receipt cho Muse tự ghi, chưa có giá trị xác nhận khi chưa được điền bởi người nhận:

```text
Consumer session / task / context revision:
Git HEAD / branch / transfer-manifest SHA-256:
Input paths + SHA-256 verified / actual read scope:
WHAT / WHY / HOW understood:
Selected cards + source rights/applicability; rejected items + reason:
Missing local sources / conflicts / blocked predicates:
One next task + output + acceptance + budget / stop condition:
Documentation intake result + timestamp + actual author:
Runtime KB admission / target ACK / execution authority: NOT_GRANTED_BY_THIS_RECEIPT
```

## Bước tiếp theo và điều kiện chạy

Task đầu tiên cho Muse: xuất một báo cáo tiếp nhận có source/digest và proposal quyết định AO-1 exact v6 (`ACCEPT`, `REVISE`, `STOP`), ghi rõ đoạn trạng thái mâu thuẫn. Bám quyền đã có trong phiên người dùng; không hỏi lại quyền điều phối/chuẩn bị tài liệu/push nhánh. General approval trước đây chưa được ghi thành receipt chấp nhận exact v6; không tự tạo receipt đó.

Sau AO-1 acceptance, chuẩn bị task AO-2 trong app project riêng: chốt owner, vị trí/codebase, capacity, browser target, technology và numeric budget. Scope là replay synthetic local, scene nhỏ + timeline/detail/meeting, 2D fallback, keyboard và reduced motion. Không đưa code app vào gói tài liệu này nếu chưa có quyết định project tương ứng.

Trước mọi schema-validation/fixture/replay/benchmark execution theo protocol, phải có R4a accepted/frozen: exact candidate/input/oracle digests, environment/toolchain versions, numeric attempt cap, authority/scope, executor, capture plan và reviewer R4b khác producer/executor. R4b chỉ review sau khi có raw argv/environment/timestamps/stdout/stderr và child/wrapper/outer exit, traces/state snapshots và attempt history theo applicability. Thiếu proof giữ `OPEN`; không suy PASS từ authoring hoặc review đồng thuận.

Pentest case01 là development design cho AO-3, phụ thuộc implementation/harness thích hợp; không dùng nó để nhảy qua AO-1/AO-2. Execution phải ghi riêng injection presence, detector prediction, attempted action (kể cả bị chặn), completed dummy-state delta. Cần freeze cả mapping case/event/source ID đã ghi trong packet.

Giữ P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`. Giữ sáu identity và REA–IDA boundaries. Runtime/provider/target/REA/IDA/W4/training/live bridge nằm ngoài scope office offline hiện hành.

## Kiểm tra tài liệu khi nhận clone

Chạy verifier IA từ repo root bằng Python 3 sẵn có:

```sh
python -I -B scripts/verify_ia.py
```

Verifier chỉ read/hash/navigation/preservation, không parse/replay fixture nghiệp vụ hoặc đóng gate. Với Windows, có thể kiểm manifest bàn giao bằng PowerShell sau đây; thao tác chỉ hash bytes:

```powershell
$transfer = Get-Content -Raw metadata/muse-knowledge-transfer-2026-10-22.json | ConvertFrom-Json
foreach ($entry in @($transfer.selected_inputs) + @($transfer.evaluation_reference_only)) {
    $actual = (Get-FileHash -LiteralPath $entry.path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $entry.sha256) { throw ('Digest mismatch: ' + $entry.path) }
}
```

## Prompt người dùng gửi Muse

```text
Tiếp quản dự án Orchestrator_Reverse ở GitHub Nohfinl99/Orchestrator_Reverse,
nhánh codex/agent-office-3d-muse-handoff.
Đọc AGENTS.md rồi docs/onboarding/muse-takeover-2026-10-22.md.
Kiểm Git HEAD và metadata/muse-knowledge-transfer-2026-10-22.json;
tự ghi receipt tiếp nhận với source/digest, phần đã đọc và gap.
Đảm nhiệm trách nhiệm Prompt-Master để tiếp tục nhánh office 3D theo roadmap.
Task đầu: reconcile AO-1 v6/review06 và issue AO-HANDOFF-01, báo proposal
quyết định exact candidate và một next atomic task có owner/output/acceptance.
Bám các quyền tôi đã giao, tiến hành phần độc lập, không hỏi lại chung chung.
Mọi fixture/benchmark execution cần R4a accepted/frozen trước attempt và
R4b độc lập sau raw evidence. Giữ sáu identity, REA–IDA và gate snapshot;
không nối runtime/provider/agent thật. AO-2 dùng app project riêng khi đủ điều kiện.
Phân biệt việc đã thiết kế, đã code, đã chạy và đã review; không tự tạo ACK.
```
