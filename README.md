# Orchestrator_Reverse

**Bộ tài liệu thiết kế và điều phối agent cho công việc reverse engineering có ranh giới bằng chứng REA–IDA.** Thư mục này được chuẩn bị thành một gói public độc lập trong workspace Orchestrator. Nội dung gồm bối cảnh dự án, kiến trúc, quy ước đóng góp và mười Prompt Stack offline.

> Trạng thái hiện tại: **tài liệu thiết kế / offline**. Đây chưa phải orchestrator tích hợp production. Các prompt và protocol mô tả yêu cầu và cách làm; chúng chưa được nối vào loader/runtime và không cấp quyền cho công cụ.

## Mục tiêu

Orchestrator_Reverse hướng tới điều phối các bước từ ý định đến kết quả có thể kiểm chứng: làm rõ mục tiêu và phạm vi, kiểm capability và evidence, lập dependency DAG, chọn đúng role hiện có, giữ checkpoint/attempt, đánh giá theo testcase và chuyển tiếp hoặc dừng có lý do.

Nguyên tắc xuyên suốt là **bảo toàn REA–IDA qua mọi cấu trúc và boundary**:

- REA giữ workflow, evidence/provenance và ledger.
- IDA giữ phân tích native/decompiler và trạng thái IDB trong capability thực tế được cấp.
- Khi task tiêu thụ target evidence, pair phải cùng target/component/slice/IDA state, có producer/session/revision/custody/freshness, và mỗi consumer tham gia phải kiểm tính liên quan, xác thực và ACK riêng.
- Chuẩn bị tài liệu ngoài target được ghi `NON_TARGET_PREPARATION`, pair `null`, trạng thái `NOT_RUN`; không tạo target claim hoặc target-consumption ACK.
- Prompt, hash file hoặc sự tồn tại của IDA không tự chứng minh tool đã nối, evidence authentic, quyền hành động hoặc kết quả đã chạy.

## Tiếp nhận theo IA — 21/10/2026

**Đọc trước:** [context hiện tại](context/current.md) → [bản đồ phase](docs/planning/phase-map.md) → [việc tiếp theo](docs/planning/work-queue.md). AI đọc [AGENTS.md](AGENTS.md); khi đổi phiên dùng [handoff](context/handoff.md).

- [Mục lục theo nhu cầu](docs/README.md) và [start here](docs/onboarding/start-here.md).
- [Nguồn chính và mức truy cập](docs/reference/source-map.md); một số worksheet/pins chỉ có trong workspace local.
- [Kiến trúc thông tin](docs/architecture/information-architecture.md), [sáu role](docs/architecture/agents.md) và [vấn đề mở](docs/reference/open-questions.md).
- [W4: gate còn thiếu, trạng thái I01–I05 và dependency](docs/planning/w4-readiness-plan.md).
- [Kiến thức tham khảo cho điều phối](docs/knowledge/README.md): 12 card từ ba nguồn GitHub, source pins và cách chọn theo task; chưa admitted KB.
- [Profile IA văn phòng agent 3D](docs/proposals/agent-office-3d/README.md): proposal offline-first, so sánh mã nguồn tương tự, meeting model và acceptance; chưa có UI/runtime.
- [Muse đi theo roadmap office 3D](docs/onboarding/muse-roadmap-guide-2026-10-22.md): điểm vào sau recheck gate, cách tận dụng artifact/knowledge, điều kiện trước AO-2 và prompt bàn giao; [handoff v1](docs/onboarding/muse-takeover-2026-10-22.md) giữ lịch sử.
- Gate kế thừa: **P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF**. IA không đổi trạng thái nghiệm thu.

Các phần bên dưới giữ mục tiêu, nguyên lý và phạm vi gốc; ba đường dẫn docs cũ vẫn chuyển tới bản canonical mới. [Bản ghi IA](docs/changes/2026-10-21-information-architecture.md) nêu phạm vi và cách kiểm bảo toàn.

## Bắt đầu

1. Đọc [bối cảnh và phạm vi](CONTEXT_VI.md).
2. Xem [kiến trúc và ranh giới](docs/architecture/system.md) cùng [trạng thái nghiệm thu](docs/reference/validation-status.md).
3. Chọn stack theo mục tiêu tại [mục lục Prompt Stack](prompt_stacks/README.md).
4. Nếu cần tinh chỉnh model, đọc [hướng dẫn fine-tuning](docs/guides/fine-tuning.md); training không thay thế tool authority hay các gate REA–IDA.
5. Trước khi áp dụng vào hệ đang chạy, kiểm quyền, source binding, consumer và các gate liên quan. Mọi execution cần bộ pre-run R4a được review/freeze trước attempt và R4b độc lập sau khi thu raw evidence.

## Cấu trúc

```text
Orchestrator_Reverse/
├── README.md / AGENTS.md / CONTEXT_VI.md
├── CONTRIBUTING.md / SECURITY.md / LICENSE_STATUS.md / CITATION.cff
├── .github/
├── context/                     # Current view, handoff, project-state.json
├── docs/
│   ├── README.md                 # Navigation by question
│   ├── onboarding/              # Start here and session workflow
│   ├── architecture/            # System, agents, information architecture
│   ├── planning/                # Phase map and work queue
│   ├── reference/               # Sources, validation, open questions
│   ├── proposals/               # Revision-scoped product/architecture proposals
│   ├── guides/                  # Conditional fine-tuning guide
│   ├── changes/                 # Revision-scoped change records
│   └── ARCHITECTURE.md ...       # Compatibility redirects
├── prompt_stacks/               # Ten unchanged stacks
│   └── protocols/               # Ten unchanged protocols
├── metadata/                    # Navigation, preservation, content inventory
└── scripts/verify_ia.py          # Read/hash/link verification only
```

Repository công khai [Nohfinl99/Orchestrator_Reverse](https://github.com/Nohfinl99/Orchestrator_Reverse) được tạo từ **nội dung bên trong folder này** làm repository root. Không upload hoặc push folder cha `Orchestrator`, vì folder đó còn workspace archive và evidence riêng.

## Mười Prompt Stack

| Stack | Vai trò của stack |
|---|---|
| `00_bootstrap` | Tiếp nhận mục tiêu, làm rõ điểm thiếu trọng yếu, lập DAG và handoff atomic. |
| `01_W0_context_baseline` | Ghi baseline, scope, revision và khả năng phục hồi. |
| `02_W1_masters_prompts` | Quy tắc routing, owner, no-match, conflict và stop. |
| `03_W2_knowledge_transfer` | Nguồn tri thức, quyền, applicability và ACK riêng của consumer. |
| `04_W3_REA_IDA` | Bảo toàn trách nhiệm và evidence qua boundary REA–IDA. |
| `05_W4_integration` | Checkpoint, history, resume, invalidation và retry. |
| `06_W5_evaluation` | R4a trước chạy; R4b grading độc lập sau attempt. |
| `07_W6_pilot_release` | Điều kiện pilot, phạm vi phát hành và rollback. |
| `08_W7_training_conditional` | Training là nhánh tùy điều kiện, yêu cầu dữ liệu/quyền/eval. |
| `09_review_gate_handoff` | Review theo digest, tổng hợp gate và chuyển giao context. |

Mỗi stack có protocol chuyên trách trong `prompt_stacks/protocols/`. Xem [mục lục chi tiết](prompt_stacks/README.md).

## Agent và trách nhiệm

| Agent | Trách nhiệm chính | Bàn giao tiêu biểu |
|---|---|---|
| Prompt-Master | Tiếp nhận mục tiêu, scope, dependency và điều phối prompt. | Task DAG/prompt cho owner chuyên trách. |
| Triage-Sentinel | Reconnaissance tĩnh, format/layout và ưu tiên phân tích. | Triage evidence cho Prompt-Master/Decomp-Analyst. |
| Decomp-Analyst | Phân tích sâu disassembly/decompiler trong state đã binding. | Phân tích có locator và proposal; Crypto khi evidence phù hợp. |
| Crypto-Logic-Specialist | Phân tích logic thuật toán có bằng chứng. | Claim/hypothesis và phản chứng cho Evidence-Synthesizer. |
| Evidence-Synthesizer | Kiểm provenance, support, conflict và handoff. | Report/receipt hoặc unresolved findings cho owner/HITL. |
| Product-Evolution-Architect | Phân tích product gap từ goal và evidence được chấp nhận. | Feature/acceptance proposal về Prompt-Master. |

HITL giữ approval/action theo quyền được cấp. Debate là review service có điều kiện. Orchestrator là chức năng điều phối, không phải identity thứ bảy.

## Phạm vi và giới hạn

Gói này chứa instruction overlay và tài liệu mô tả. Nó không chứa RE-Decom archive đầy đủ, raw capture, target/binary, database IDA, local config/credential, snapshot backup, output fine-tuning hoặc các artefact riêng của máy.

Mười stack là bộ tài liệu, không có nghĩa toàn bộ task đã chạy. Mười protocol không chứng nhận code thực thi. Coverage design, hash/locator checks, benchmark execution và review độc lập là những loại bằng chứng khác nhau. Xem [trạng thái nghiệm thu](docs/reference/validation-status.md).

## Quyền và giấy phép

Quyền của corpus nguồn chưa được xác nhận đủ để gán một license mở cho mọi nội dung. Theo mặc định không cấp quyền sao chép, sửa đổi hoặc phân phối vượt quá các quyền hiện có. Xem [LICENSE_STATUS.md](LICENSE_STATUS.md) trước khi tái sử dụng hoặc thêm code/asset bên thứ ba.

## Đóng góp và báo lỗi

Xem [CONTRIBUTING.md](CONTRIBUTING.md) và [SECURITY.md](SECURITY.md). Mọi thay đổi phải giữ provenance, phân biệt thiết kế với execution, và không sửa lịch sử để biến FAIL/NOT_RUN thành PASS.
