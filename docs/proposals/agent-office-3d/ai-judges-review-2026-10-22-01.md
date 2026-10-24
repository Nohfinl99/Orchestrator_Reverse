# AI_Judges review: hình ảnh và phòng ban liên kết

| Trường | Giá trị |
|---|---|
| Review ID | `AGENT_OFFICE_AI_JUDGES_20261022_01` |
| Proposal reviewed | `AGENT_OFFICE_PRODUCT_ROADMAP_01`, `AGENT_OFFICE_PREFLIGHT_01`, visual review |
| Review type | `ADVISORY_CROSS_FUNCTIONAL_PANEL` |
| Panel lenses | Product, UX/Visual, Frontend/3D, Event/Data, Runtime Integration, Evidence/Security/Privacy, Accessibility, QA/Evaluation, Operations/Cost, Human Operator/HITL |
| Result | `GO_AO1_KICKOFF / AO2_AFTER_PACKET_ACCEPTANCE / LIVE_CONTROL_BLOCKED` |
| Runtime / code changes | `NONE` |

## AI_Judges verdict

**Đề xuất khởi động dự án offline thật ở AO-1.** Chưa mở AO-2 implementation cho đến khi scenario, event contract, expected-state/oracle và acceptance packet được review; chưa mở live bridge/command-control. Một concept frame không phải implementation evidence.

Không tìm thấy `AI_Judges` như một module/runtime có trong source package được kiểm kê. Vì vậy lượt này dùng panel reviewer advisory được gọi theo các lăng kính người dùng yêu cầu; kết quả không phải ACK hoặc dispatch của sáu identity Orchestrator.

## Phòng ban/lăng kính liên kết mở rộng

Các “phòng ban” dưới đây là stakeholder disciplines để review sản phẩm. Chúng **không phải identity mới** trong Orchestrator. Owner trong product implementation còn phải được chỉ định riêng.

| Lăng kính | Câu hỏi cần quyết định | Mapping trách nhiệm hiện hữu | Điều kiện/đầu ra |
|---|---|---|---|
| Product & Workflow | Ai là operator đầu tiên? Việc gì cần hoàn thành? Vì sao cần 3D? | Product-Evolution-Architect; Prompt-Master điều phối | User/scenario, task outcomes, problem statement và stop criteria |
| UX / Visual Design | Scene/panel/timeline hierarchy, trạng thái, thao tác, zoom/filter? | Product-Evolution-Architect; Evidence-Synthesizer review claim/state semantics | Storyboard, labels, state transition, 2D fallback |
| Frontend / 3D Engineering | App/codebase, renderer, state binding, browser/device, perf? | Chưa có identity chuyên biệt; implementation owner/capacity TBD | Stack choice sau spike; scene nhận state từ reducer; không scene→agent command |
| Event / Data | Event schema/version, sequence, dedupe, replay/resync, provenance? | Prompt-Master packet; technical owner TBD; Evidence-Synthesizer review | Versioned local event contract, reducer, fixture/oracle |
| Runtime Integration | Producer, caller, authority, permission, transport, failure? | Gắn với owner/code contract phù hợp; chưa map capability dispatch hiện tại | AO-5/6 blocked tới khi source/permission/contract thật sẵn sàng |
| Evidence / Security / Privacy | Claim locator, source rights, access, redaction, retention, export/delete? | Evidence-Synthesizer review; security/privacy owner TBD | Threat/privacy questions và data policy trước live transcript |
| Accessibility | Keyboard, text/table, color labels, reduced motion, screen-reader semantics? | Chưa có identity chuyên biệt; Product-Evolution-Architect đưa acceptance, reviewer độc lập | A11y checklist và fallback không gian 2D |
| QA / Evaluation | Oracle, hard failure, regressions, visual vs functional result? | Evidence-Synthesizer độc lập review; producer/tester khác evaluator | R4a freeze trước attempt; R4b raw review sau; UI/UX benchmark riêng |
| Operations / Cost / Support | Browser/device, offline storage, latency, budget, incident/rollback? | Prompt-Master ghi dependency; owner TBD | Không chọn numeric runtime budget khi chưa có target/model/pricing/capacity |
| Human Operator / HITL | Ai ra lệnh, ai duyệt decision/action, lúc nào block/stop? | User/người điều phối giữ authority; HITL không là identity thứ bảy | Authority/approval boundary và audit trail |

Sáu identity tiếp tục giữ nguyên: Prompt-Master, Triage-Sentinel, Decomp-Analyst, Crypto-Logic-Specialist, Evidence-Synthesizer, Product-Evolution-Architect. Product office không cần gọi Decomp/Crypto/Triage mặc định; chỉ route khi có task/source phù hợp. Orchestrator là function điều phối, không phải thành viên thứ bảy.

## Kết quả theo lăng kính

- **Product:** điểm khác biệt cần kiểm là nối lệnh/ý kiến/dissent/action tới task, source, evidence và receipt, không phải văn phòng giả lập.
- **Visual/UX:** hướng “phòng quan sát điều phối”; 3D là spatial overview, timeline/evidence là nơi xác thực. Màu đi cùng nhãn/icon. Agent bận/deferred vẫn ở bàn; chỉ event xác nhận mới chuyển động.
- **Frontend/3D:** codebase app chưa có trong package này; workspace `src/` chứa ba prototype Python offline khác, router vẫn `dispatch_status=NOT_IMPLEMENTED`. Không giả định có thể mở UI bằng cách nối vào candidate router.
- **Event/Data:** local `SIMULATED` event stream và deterministic reducer trước; avatar là projection, không là nguồn sự thật.
- **Security/Privacy:** chỉ hiện submitted structured outputs và artifacts được phép. Không private chain-of-thought, prompt ẩn, credentials hoặc context ngoài scope. Live transcript cần access/redaction/retention decision trước.
- **Accessibility:** keyboard, giảm chuyển động, status không phụ thuộc riêng màu và text/table fallback là acceptance, không phải việc polish sau.
- **QA/Evaluation:** không gọi screenshot/meeting consensus là test. Freeze expected output/hard fail trước; phân biệt deterministic correctness với visual judgement và user study.
- **Operations/Cost:** chọn browser/device, offline persistence, perf/cost budget khi task target/owner đã có. Không suy ngân sách từ Reddit hoặc concept art.
- **Human operator:** meeting recommendation không cấp quyền dispatch; decision/action cần receipt/authority riêng.

## Việc tiếp theo đề xuất

1. Khởi động AO-1 task packet `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01`: chốt scenario, event schema, synthetic fixture, expected states/oracle, visual storyboard, accessibility/privacy criteria và scope/budget placeholders.
2. Review AO-1 theo source/acceptance; unresolved material gaps là `OPEN/BLOCKED`, không ép PASS.
3. Chọn app codebase/implementation owner/capacity/technology/browser target. Vì public Orchestrator package hiện chỉ là docs/điều phối, đánh giá tạo app trong project folder riêng để không trộn UI code với gói tài liệu.
4. Sau AO-1 accepted và R4a phù hợp được freeze, triển khai AO-2 vertical slice offline: local fixture; roster sáu identity nhưng chỉ participant có event thay đổi vị trí; một bàn/meeting room; timeline + detail panel; click claim/evidence/dissent; reduced-motion và 2D fallback; persistent `SIMULATED` label.
5. Sau đó AO-3 integrity, AO-4 3D-vs-2D user-value comparison. Chỉ xem AO-5 live observation/ AO-6 command control sau producer, authority, permission, budget và prerequisite/gate review riêng.

## Gate và mức sẵn sàng

- Profile, roadmap, knowledge prep và concept art đã có; **chưa có UI implementation**.
- AO-1 vẫn `PROPOSED_NOT_DISPATCHED`; AO-2 chờ AO-1 acceptance và lựa chọn codebase/owner.
- P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 `NOT_RUN_BLOCKED`; v3 `OFF`.
- Không chạy code, fixture, benchmark, provider, target, training hoặc W4 trong lượt review.
- AI_Judges recommendation là advisory; không nâng project gate, không tạo consumer ACK và không phải runtime receipt.
