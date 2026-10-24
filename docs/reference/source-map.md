# Bản đồ nguồn và phạm vi sử dụng

Chỉ thị hợp lệ hiện hành quyết định task/scope. Với claim kỹ thuật, exact frozen source, raw receipt và review đúng revision quyết định phần được chấp nhận; context/README là view dẫn xuất. Không chọn nguồn theo filename “current”, ngày sửa file hoặc số lượng file.

## Nguồn trong clone public

| Câu hỏi | Nguồn canonical | Loại / giới hạn |
|---|---|---|
| Mục tiêu/nguyên lý | [CONTEXT_VI.md](../../CONTEXT_VI.md) | Văn bản gốc public, giữ nguyên bytes |
| Thành phần và boundary | [System](../architecture/system.md) | Tài liệu gốc được di chuyển nguyên byte; mô hình đích |
| Gate tại thời điểm đóng gói | [Validation status](validation-status.md) | Snapshot lịch sử, không xác nhận runtime hiện tại |
| W4 I01–I05 readiness | [W4 gap register](../planning/w4-readiness-plan.md) | Đối chiếu run44 và template nguồn; run I05 chỉ là non-target preparation |
| Phương pháp điều phối tham khảo từ bên ngoài | [Knowledge index](../knowledge/README.md), [source catalog pin commit](../knowledge/prompt-orchestration/sources.json) | 12 candidate reference; source guidance/static observation, chưa admitted KB/consumer ACK; S1 rights UNKNOWN |
| Văn phòng 3D / họp agent | [Profile và source review](../proposals/agent-office-3d/README.md) | Repo/commit và file đã đọc có liệt kê; static review có chọn lọc, proposal offline-only, không chứng minh tích hợp hoặc runtime |
| Instruction từng phase | [Prompt stack index](../../prompt_stacks/README.md) | Mười overlay/protocol nguyên bản; chưa nối loader |
| Hiện đang làm gì / tiếp theo | [Context](../../context/current.md), [work queue](../planning/work-queue.md) | View IA kế thừa nguồn, không là accepted task packet |
| Tiếp nhận và tìm tài liệu | [Navigation manifest](../../metadata/navigation.json) | Map canonical theo task; không chứng nhận các section đã được đọc |
| Fine-tuning | [Guide nguyên bản](../guides/fine-tuning.md) | Có thông tin theo thời điểm; kiểm nguồn chính thức khi dùng cho quyết định mới |
| File nào được bảo toàn | [Preservation](../../metadata/preservation.json) | SHA-256 và đường dẫn trước/sau IA; chỉ chứng minh byte match |

## Nguồn chỉ có trong workspace đầy đủ

Locator sau tính từ root workspace **cha**, không phải link local trong clone public. `LOCAL_ONLY_NOT_DISTRIBUTED` nghĩa là bản public không mang theo artifact đó; không có nghĩa nó đã được xác minh trong phiên mới.

| Locator workspace-relative | Dùng cho claim nào | Availability |
|---|---|---|
| `docs/roadmap-reading-companion.md` | Roadmap revision 3, R0–R6 và criteria | LOCAL_ONLY_NOT_DISTRIBUTED |
| `CURRENT.md` → `NEXT.md` → `LOGIC_REVIEW.md` | Chuỗi entry theo các lần bàn giao | LOCAL_ONLY_NOT_DISTRIBUTED |
| `evidence/agent_alignment/20261021_01/report.md` | Projection/agent map/checklist đã làm; full sync chưa đạt | LOCAL_ONLY_NOT_DISTRIBUTED |
| `evidence/agent_alignment/20261021_01/next_atomic_task.json` | Exact proposal ID và PROPOSED_NOT_DISPATCHED | LOCAL_ONLY_NOT_DISTRIBUTED |
| `evidence/orchestrator_meetings/20261021_logic_audit_01/report.md` | Logic findings, verifier v2 và admission gap | LOCAL_ONLY_NOT_DISTRIBUTED |
| `evidence/orchestrator_meetings/20261021_logic_audit_01/candidate/proposal_admission.json` | Field thiếu trước dispatch | LOCAL_ONLY_NOT_DISTRIBUTED |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/04_artifacts/implementation_runs/20261020_gate_closure_meeting_44/W4_gate_readiness.json` (SHA-256 `1d5e1fad56b1990239151e3b15ca773c16a9e15005fab615e097d284cbb7aa3e`) | Gate run44 và I01–I05 readiness | LOCAL_ONLY_NOT_DISTRIBUTED; workspace manifest pin match |
| `archive/RE-Decom/02_workspaces/AI_REA_SI_Engineer/01_control_plane/prompt_stacks/handoff_atomic_v1/05_W4_integration.md` (SHA-256 `1e2eef0e0bf02e41f65c68f2af43c6f077ff608d9fd4c5e0b512324fc9e3d562`) | I01–I05 objectives/dependencies/outputs | LOCAL_ONLY_NOT_DISTRIBUTED; workspace manifest pin match |
| `prompt_stacks/offline_revision_20261021/source_pins.json` | Source pins mà public overlay nhắc tới | LOCAL_ONLY_NOT_DISTRIBUTED |
| Cùng gói local: `authority_binding.json`, `boundary_preservation.json`, `criterion_crosswalk.json`, `decision_appendix.json`, `future_cases_design_only.json`, `legacy_roles.json`, `task_disposition.json` | Contract worksheet và disposition của delivery gốc | LOCAL_ONLY_NOT_DISTRIBUTED |
| `archive/RE-Decom/` và các manifests/raw tương ứng | Source/case/oracle/attempt lịch sử, exact gate custody | LOCAL_ONLY_NOT_DISTRIBUTED |

Người có workspace mở `docs/ia/workspace-map.md` tại root cha để đi theo link local chính xác. Người chỉ có clone public giữ dependent claims ở mức chưa truy cập; không tạo các file giả trùng basename để làm prompt “chạy được”. Nhận được nguồn thì kiểm exact path/digest/revision và quyền, không mặc định source map là receipt.

## Tham chiếu tổ chức thông tin

[Knowledge compiler](https://github.com/Nohfinl99/Reading_Companion/blob/main/skills/sid-reading-companion/references/knowledge-compiler.md), Git blob `094a47a25cd8cf1906049fd4114ff2c58288659f`, là nguồn phương pháp đã đối chiếu trong lượt IA. [IA](../architecture/information-architecture.md) ghi cách áp dụng KC01–KC04; không chuyển nội dung học sách thành contract nghiệp vụ REA–IDA.

## Khi nguồn khác nhau

Ghi claim, hai locator, revision/digest, phạm vi đã đọc và tác động vào [open questions](open-questions.md). Source integrity sai thì dừng nhánh phụ thuộc và giữ expected/actual. Evidence toàn vẹn nhưng mâu thuẫn cần review theo contract; không refresh pin hoặc ép thống nhất bằng sửa view IA.
