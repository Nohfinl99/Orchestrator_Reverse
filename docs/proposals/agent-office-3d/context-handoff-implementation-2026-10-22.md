# Handoff sang context triển khai: văn phòng agent 3D

Dùng mục “Prompt chuyển context” bên dưới để bắt đầu một context mới. Handoff này gom trạng thái và nguồn cần thiết, không đòi context mới nạp toàn bộ archive.

## Trạng thái đã biết

- Proposal: `AGENT_OFFICE_3D_PROFILE_01`; roadmap `AGENT_OFFICE_PRODUCT_ROADMAP_01`.
- AI_Judges advisory review đề xuất **GO bắt đầu AO-1**, rồi chỉ làm AO-2 sau khi packet được review/chấp thuận và app codebase/owner/budget được chọn.
- Visual direction: “phòng quan sát điều phối”; 3D scene nhỏ + timeline/evidence panel; event log/reducer là nguồn sự thật; 2D fallback, keyboard, reduced motion, status color+text.
- Workspace hiện không có app 3D agent-office. `src/README.md` liệt kê ba prototype Python offline không liên quan trực tiếp; `src/candidates/README.md` ghi role router `PREPARED_NOT_DISPATCHED`, `dispatch_status=NOT_IMPLEMENTED`.
- Current project snapshot: P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`. Sáu identity và REA–IDA boundaries giữ nguyên.
- No actual benchmark/user study/runtime execution. Concept image is illustrative only.

## Prompt chuyển context

```text
Tiếp tục dự án “văn phòng agent 3D cho Orchestrator” từ hồ sơ hiện có trong workspace `E:\Kiến Trúc Thông Tin\Orchestrator`.

ĐỌC TRƯỚC KHI LÀM:
1. `START_HERE.md`, `docs/ia/workspace-map.md`, `Orchestrator_Reverse/AGENTS.md`.
2. `Orchestrator_Reverse/docs/proposals/agent-office-3d/README.md`.
3. `roadmap.md`, `execution-runbook.md`, `preflight-knowledge-and-benchmark.md`, `visual-review-2026-10-22-01.md`, `ai-judges-review-2026-10-22-01.md`, và file handoff này trong cùng thư mục proposal.
4. `Orchestrator_Reverse/docs/architecture/agents.md`, `docs/planning/phase-map.md`, `docs/planning/work-queue.md`, `docs/planning/w4-readiness-plan.md`, `Orchestrator_Reverse/context/current.md`, `src/README.md`, `src/candidates/README.md`.

MỤC TIÊU:
Thực hiện theo AO roadmap. Bắt đầu bằng AO-1 `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01`: chốt một scenario offline đầu-cuối, event schema/version candidate, synthetic fixture, expected-state/oracle, storyboard visual, privacy/accessibility acceptance, exact acceptance IDs và missing inputs. Sau review, nếu không còn blocker thuộc quyền người dùng, chuyển sang AO-2 offline visual vertical slice trong một app project riêng; không đặt code vào gói tài liệu `Orchestrator_Reverse` nếu không có quyết định project rõ ràng.

HƯỚNG HÌNH ẢNH:
“Phòng quan sát điều phối”: scene 3D isometric nhỏ, roster sáu identity hiện hữu, một cụm bàn và một phòng họp; timeline và panel meeting/evidence là phần đọc chính xác. Agent đang bận/deferred giữ bàn và task. Chỉ event receipt/accept/join/contribution làm avatar chuyển động. Hiện `SIMULATED/OFFLINE` luôn rõ. Có keyboard access, reduced motion, status bằng màu + text/icon và bảng/timeline 2D fallback. Không xây full game-like office trước khi chứng minh 3D giúp việc điều phối.

SCOPE CỦA AO-2 NẾU ĐỦ ĐIỀU KIỆN:
Dữ liệu local/fixture בלבד; không model/provider/network, live agent, target, REA/IDA hoặc command control. UI một lát cắt: invite/defer, accept/join, contribution/objection, dissent synthesis, close, timeline replay và click-through evidence. Giữ private chain-of-thought, prompt/credentials và context ngoài scope khỏi giao diện.

PHÒNG BAN LIÊN KẾT:
Review theo các stakeholder lens: Product/Workflow; Visual UX; Frontend/3D; Event/Data; Runtime Integration; Evidence/Security/Privacy; Accessibility; QA/Evaluation; Operations/Cost/Support; Human Operator/HITL. Đây là lăng kính dự án, KHÔNG phải identity mới. Giữ đúng sáu identity của project; Prompt-Master điều phối packet, Product-Evolution-Architect phụ trách product acceptance, Evidence-Synthesizer review độc lập; Triage/Decomp/Crypto chỉ khi task thực sự phù hợp.

GATE/EVALUATION:
Prompt stack/protocol hiện là tài liệu offline, chưa nối runtime. Chọn stack theo objective, không nạp toàn corpus. Mọi benchmark/fixture execution theo project protocol cần R4a được accepted/frozen trước attempt và R4b độc lập từ raw evidence sau attempt. Không chạy benchmark trước freeze. Tách AO acceptance khỏi R0–R6/W0–W7/G1–G4/P1. Không sửa historical FAIL, không promote gate bằng review, UI demo, scorecard hoặc custody.

PROJECT STATUS TO PRESERVE:
P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF; prompt stack/router dispatch chưa tích hợp. Không tạo identity, quyền, ACK, receipt hoặc runtime capability. AO-1 hiện đề xuất, chưa được dispatch; review/advisory không phải runtime execution.

THỰC HIỆN:
- Tiếp tục độc lập, làm AO-1 packet cụ thể và review theo hai vòng tài liệu tối đa; nếu thiếu authority/owner/budget/target decision thì ghi BLOCKED/UNKNOWN và tiếp tục phần độc lập.
- Không bắt đầu AO-2 cho tới khi AO-1 packet có acceptance rõ, owner/codebase/capacity được xác định, R4a freeze phù hợp và người điều phối chấp thuận implementation task.
- Nếu cần app project mới, tạo thư mục/repository riêng sau khi xác định vị trí phù hợp; kiểm tra license/assets, browser target và toolchain trước khi cài dependency. Không copy repo artwork/code.
- Bàn giao mỗi bước bằng status, artifact path/revision, acceptance verdict, gap, next dependency; chỉ nói tests/benchmarks đã chạy khi có raw output.

Kết quả yêu cầu ở context này: hoàn thành AO-1 packet và đưa ra quyết định rõ `READY_FOR_AO2`, `REVISE`, `BLOCKED` hoặc `STOP`, có evidence locator và lý do. Không tự động mở live integration.
```

## Khi nhận context mới

Prompt trên cho phép tiếp tục chuẩn bị và implementation offline trong giới hạn dự án. Nó không tự cấp runtime permission, human approval, budget, external system access hay gate acceptance. Nếu context mới không có workspace này, trước tiên yêu cầu người dùng mở/mount cùng thư mục hoặc attach các tài liệu được liệt kê; không bịa project state từ prompt.
