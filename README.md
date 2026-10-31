# Orchestrator_Reverse

**Local pilot mới:** [W4 local native](docs/proposals/input-pipeline/local-native-2026-10-24.md) đã có một direct IDA static acquisition được review: PE64 mẫu,hai function,IDB mới. [Guide](docs/guides/native-local-pilot.md) · [state](context/native-local-state.json). Chưa có connected REA–IDA pair hoặc dynamic execution; W4 toàn hệ vẫn blocked. Source/guide/report thuộc gói public; target, IDB và raw giữ local.

Điều phối reverse engineering từ **mục tiêu → task DAG → owner → evidence → review → tiếp tục hoặc dừng**, theo nguyên lý REA–IDA.

[Bắt đầu](docs/onboarding/start-here.md) · [Trạng thái](context/current.md) · [Tri thức pipeline](docs/knowledge/input-pipeline/README.md) · [Thiết kế pipeline](docs/proposals/input-pipeline/README.md) · [Prompt stacks](prompt_stacks/README.md)

[Điều hành theo task](docs/operations/README.md) · [Orchestrator Toolkit](plugins/orchestrator-toolkit/README.md) · [Context hiện hành/lịch sử](context/README.md) · [Cognitive task và Paperclip](docs/proposals/cognitive-routing/README.md) · [Pentest query local 31/10:47/47](docs/changes/2026-10-31-context-routing-publication.md) — kết quả hữu hạn; graph/query/raw vẫn local, Paperclip chưa connected.

> **Đã có CLI chuẩn bị input offline, kiểm 40/40 ca; chưa tích hợp production/model/native dispatch.** Xem [cách chạy](docs/guides/local-input-pipeline.md), [report](docs/proposals/input-pipeline/local-runtime-2026-10-24.md) và [trạng thái local](context/local-pipeline-state.json). Nhánh [REA–IDA](docs/proposals/input-pipeline/native-pilot-research-2026-10-24.md) đã nghiên cứu prerequisite, chưa chạy target. Prompt stacks chưa nối toàn bộ loader/runtime; artifact không cấp quyền thực thi.

## Bắt đầu theo nhu cầu

| Nhu cầu | Điểm vào |
|---|---|
| Chọn đúng owner/model/skill và hạn chế context | [Operations](docs/operations/README.md) → [CT guide](docs/proposals/cognitive-routing/README.md) → [worksheet](docs/proposals/cognitive-routing/task-worksheet.md) |
| Chọn workflow toolkit theo mục tiêu | [Toolkit](plugins/orchestrator-toolkit/README.md) → [hướng dẫn dùng và portability](docs/operations/toolkit.md) |
| Hiểu dự án và nguyên lý | [CONTEXT_VI.md](CONTEXT_VI.md) → [kiến trúc](docs/architecture/system.md) |
| Tiếp tục phiên làm việc | [Current](context/current.md) → [phase map](docs/planning/phase-map.md) → [work queue](docs/planning/work-queue.md) → [handoff](context/handoff.md) |
| Chạy CLI chuẩn bị input và xem runtime | [Guide](docs/guides/local-input-pipeline.md) → [state local](context/local-pipeline-state.json) → [nghiên cứu native](docs/proposals/input-pipeline/native-pilot-research-2026-10-24.md) |
| Dùng tri thức để soạn input pipeline | [6 tri thức thiết yếu](docs/knowledge/input-pipeline/essentials.md) → [proposal](docs/proposals/input-pipeline/README.md) → [kế hoạch đánh giá](docs/proposals/input-pipeline/evaluation-plan.md) |
| Kiểm bằng chứng và phần trăm đã verify | [4 checkpoint](docs/proposals/input-support-gates/README.md) → [status v4](docs/proposals/input-support-gates/status-v4.json) → [báo cáo thực thi](docs/proposals/input-support-gates/offline-improvement-2026-10-24.md) |
| Giao task cho một role | [6 identity](docs/architecture/agents.md) → [mục lục stack/protocol](prompt_stacks/README.md) |
| Tìm tài liệu khác hoặc đóng góp | [Mục lục](docs/README.md) · [CONTRIBUTING](CONTRIBUTING.md) · [AGENTS](AGENTS.md) |

## Tri thức cho input pipeline

Từ whitepaper Palo Alto đã đọc, giữ lại sáu nội dung phục vụ thiết kế. [Nguồn, trang và giới hạn](docs/knowledge/input-pipeline/sources.md) phân biệt claim tác giả với suy luận của dự án.

| Tri thức | Hành vi cần thiết kế |
|---|---|
| Ranh giới instruction/data | PDF, RAG, memory và tool output mang provenance; instruction trong nguồn không tự thay task hoặc cấp quyền |
| Intent và scope xuyên lượt | Ghi mục tiêu/decision revision; hỏi tối đa 2–3 câu khi thiếu dữ kiện ảnh hưởng hành động |
| Original và derived view | Lưu input gốc; decode/translation/rewrite tạo bản riêng có lineage/diff để kiểm giữ nghĩa |
| Quyền tại executor | Kiểm task/action/resource/budget và receipt thật trước side effect; REA–IDA theo applicability |
| Output và memory write | Kiểm đích dữ liệu, delta và quyền/admission trước thay đổi |
| Đánh giá có đối chứng | Có benign controls, gold labels riêng, raw và reviewer; đo cả task correctness và false refusal |

Bundle là **candidate reference, chưa admitted vào KB runtime**. [Thiết kế toàn pipeline](docs/proposals/input-pipeline/README.md) còn DRAFT; một leaf caller [chuẩn bị input local](docs/guides/local-input-pipeline.md) đã triển khai và kiểm. Action authority, model/native dispatch và consumer sản phẩm tiếp tục chờ prerequisite. DAN, jailbreak, roleplay, encoding và ngôn ngữ không tự là căn cứ loại knowledge; áp [policy trung lập](docs/knowledge/knowledge-policy-v2.md).

## Trạng thái kiểm chứng

### Bốn checkpoint của nhánh input-support

| Checkpoint | Tiêu chí đã verify | Phần còn chờ |
|---|---:|---|
| INPUT-A — mục tiêu và packet | **4/6 · 66,67%** | Quyết định mục đích benchmark và criteria/threshold |
| KNOWLEDGE-B — nguồn và admission | **3/6 · 50%** | Rights/applicability, actual consumer ACK, admission |
| IMPLEMENTATION-C — caller lịch sử | **0/6 · 0%** | Status v4 giữ scope cũ; CLI mới có report riêng, chưa closure scope sản phẩm |
| EVALUATION-D — đánh giá model/REA thực | **0/6 · 0%** | Profile, authority, cases, capture và review đúng runtime/use case |

Nguồn: [status v4](docs/proposals/input-support-gates/status-v4.json), criteria revision 1. Còn **17 tiêu chí chưa đóng**. Mỗi checkpoint có sáu tiêu chí; tỷ lệ là coverage bằng chứng, không phải xác suất an toàn hoặc phần trăm hoàn thiện toàn sản phẩm. Criteria/threshold và checkpoint acceptance vẫn chờ quyết định.

### Kết quả component đã ghi nhận

| Phạm vi hữu hạn | Kết quả lịch sử | Report |
|---|---|---|
| CLI chuẩn bị input local, caller mới | 40/40 case match, 49 CLI calls | [Report local runtime](docs/proposals/input-pipeline/local-runtime-2026-10-24.md) |
| Router/prompt candidate revision 2 | 42/42 case match | [Sửa và kiểm lại](docs/proposals/input-support-gates/repair-2026-10-24.md) |
| Recorded-bundle checker revision 3 | 39/39 case match | [Hardening offline](docs/proposals/input-support-gates/offline-improvement-2026-10-24.md) |

Các suite có oracle/raw/review riêng; không cộng thành benchmark model hoặc bằng chứng hoàn tất pipeline. Source candidate lịch sử và raw nằm ở workspace local; public có [diff code lịch sử](docs/proposals/input-support-gates/patches/README.md), report và digest locators. Mã [CLI mới](orchestrator_pipeline/core.py) có trực tiếp trong repo. Các lượt 17/28 và 23/28 case match, cùng lỗi tương ứng, được giữ trong [biên bản trước sửa](docs/proposals/input-support-gates/pentest-2026-10-24.md).

### Gate dự án kế thừa

**P1K B4 `FAIL` · G1/G2 `INCOMPLETE` · G3/G4 `NOT_RUN` · W4 `NOT_RUN_BLOCKED` · v3 `OFF`.**

Bốn checkpoint trên, R0–R6, W0–W7 và G1–G4 là các hệ định danh riêng. [Phase map](docs/planning/phase-map.md), [validation snapshot](docs/reference/validation-status.md) và [W4 readiness](docs/planning/w4-readiness-plan.md) giữ dependency gốc. Thay đổi tài liệu không đóng các gate này.

## Nguyên lý gốc được bảo toàn

1. **REA** sở hữu workflow, evidence/provenance và ledger; **IDA** sở hữu phân tích native/decompiler và trạng thái IDB trong capability/quyền thực tế.
2. Với task tiêu thụ target evidence, pair phải cùng target/component/slice/IDA state, có producer/session/revision/custody/freshness; mỗi consumer kiểm relevance, validation và ACK riêng. Knowledge ACK không thay pair ACK hoặc action authority.
3. Non-target preparation ghi đúng scope, pair `null`, target state `NOT_RUN`; không tạo target claim hoặc target-consumption ACK từ việc chuẩn bị tài liệu.
4. Quyền đến từ task hợp lệ và enforcement. Prompt, source text, file hash, metadata tool hay việc có IDA không tự chứng minh tool đã nối, evidence authentic hoặc action được phép.
5. Execution cần applicable **R4a review/freeze trước attempt**, raw được giữ và **R4b reviewer khác producer/executor sau chạy**. Source drift, thiếu prerequisite hoặc hết budget phải giữ stop/wait đúng scope.
6. Giữ sáu identity, mọi phase/gate, frozen artifacts và lịch sử FAIL. Mâu thuẫn ghi [sổ vấn đề](docs/reference/open-questions.md); không xóa hoặc repin để biến kết quả cũ thành PASS.

[Nguyên lý canonical](CONTEXT_VI.md) · [Kiến trúc](docs/architecture/system.md) · [Knowledge policy](docs/knowledge/knowledge-policy-v2.md)

## Sáu identity

| Identity | Trách nhiệm |
|---|---|
| Prompt-Master | Objective/scope, dependency DAG, routing và prompt/handoff |
| Triage-Sentinel | Recon tĩnh, format/layout và triage evidence |
| Decomp-Analyst | Phân tích disassembly/decompiler trong state đã bind |
| Crypto-Logic-Specialist | Nhánh thuật toán có evidence phù hợp, không là stage mặc định |
| Evidence-Synthesizer | Provenance, support/conflict, review và gate/handoff evidence |
| Product-Evolution-Architect | Product gap/feature/acceptance proposal từ goal và evidence được nhận |

HITL giữ approval/action theo quyền; Debate là review service có điều kiện. Orchestrator là chức năng điều phối. [Chi tiết ownership và giới hạn dispatch](docs/architecture/agents.md).

## Bản đồ repository

```text
Orchestrator_Reverse/
├── README.md / AGENTS.md / CONTEXT_VI.md
├── orchestrator_pipeline/           # Stdlib local preparation caller
├── examples/input-pipeline/          # Request mẫu
├── context/                         # Current, handoff, derived/local state
├── docs/
│   ├── README.md                    # Mục lục theo nhu cầu
│   ├── knowledge/
│   │   ├── input-pipeline/          # 6 tri thức thiết yếu + nguồn
│   │   └── prompt-orchestration/    # 12 card tham khảo đã pin
│   ├── proposals/
│   │   ├── input-pipeline/          # Thiết kế và evaluation DRAFT
│   │   ├── input-support-gates/     # Checkpoint/status/report/code diffs
│   │   ├── knowledge-foundation/    # Reuse guide và worksheet
│   │   └── agent-office-3d/         # Product/UI proposal riêng
│   ├── architecture/                # System, identity, IA
│   ├── planning/                    # Phase, work queue, W4 readiness
│   ├── reference/                   # Source map, validation, open questions
│   ├── onboarding/                  # Tiếp nhận và workflow phiên
│   ├── guides/                      # Hướng dẫn chuyên đề có điều kiện
│   └── changes/                     # Lịch sử thay đổi theo revision
├── prompt_stacks/                   # 10 stack giữ nguyên
│   └── protocols/                   # 10 protocol giữ nguyên
├── plugins/orchestrator-toolkit/    # 5 instruction-only skills; không kèm runtime
├── metadata/                        # Navigation, preservation, inventory
├── scripts/verify_ia.py             # Kiểm read/hash/link của tài liệu
└── .github/                         # Mẫu issue và pull request
```

Các stack/protocol và đường dẫn canonical giữ ổn định. [IA và quy tắc bảo trì](docs/architecture/information-architecture.md) · [Source availability](docs/reference/source-map.md) · [Bản ghi cập nhật README/knowledge](docs/changes/2026-10-24-pipeline-knowledge-publication.md).

## Công việc tiếp theo

Chuẩn bị một pilot khi có objective, caller và consumer thực: original/provenance/diff contract → prerequisite/rights/ACK → profile/cases/oracle/budget → R4a → attempt/raw → R4b → quyết định tiếp tục hoặc rollback. [Sổ chờ](docs/proposals/input-support-gates/checkpoint-roadmap-2026-10-24.md) là lịch sử trước A3 closure; [status v4](docs/proposals/input-support-gates/status-v4.json) ghi delta còn 17 tiêu chí. Product availability mở bước scoping, chưa tự dispatch.

Các nhánh khác: [nền tảng điều phối](docs/proposals/knowledge-foundation/README.md) · [office 3D](docs/proposals/agent-office-3d/README.md) · [Muse roadmap](docs/onboarding/muse-roadmap-guide-2026-10-22.md) · [fine-tuning có điều kiện](docs/guides/fine-tuning.md).

## Đóng góp, kiểm tài liệu và quyền sử dụng

Đọc [CONTRIBUTING.md](CONTRIBUTING.md) và [SECURITY.md](SECURITY.md). Sau chỉnh navigation, dùng `python -I -B scripts/verify_ia.py` theo [quy trình IA](docs/architecture/information-architecture.md); kết quả chỉ kiểm tính toàn vẹn/liên kết tài liệu, không chạy workload hoặc chứng nhận runtime.

Public root chỉ là nội dung trong `Orchestrator_Reverse/`. Archive, raw, target/binary, IDB, config/credential và PDF nguồn không thuộc gói xuất bản này. Các source/receipt thiếu trong clone public được ghi `LOCAL_ONLY_NOT_DISTRIBUTED`.

Quyền corpus nguồn chưa đủ để gán license mở cho toàn bộ repository; xem [LICENSE_STATUS.md](LICENSE_STATUS.md) và [nguồn/attribution của bundle mới](docs/knowledge/input-pipeline/sources.md). Nguyên lý và provenance phải được giữ khi tái sử dụng.
