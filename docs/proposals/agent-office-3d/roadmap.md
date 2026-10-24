# Roadmap sản phẩm: văn phòng agent 3D

| Trường | Giá trị |
|---|---|
| Roadmap ID | `AGENT_OFFICE_PRODUCT_ROADMAP_01` |
| Revision | `1` |
| Ngày | 22/10/2026 |
| Trạng thái | `REVIEWED / CONDITIONAL_GO_AO0_TO_AO4` |
| Phạm vi | Từ proposal tới offline prototype; live/runtime có điều kiện riêng |
| Relation với R0–R6, W0–W7 | Roadmap sản phẩm riêng; không thay thế hoặc nâng trạng thái các phase/gate project hiện hành |

## Mục tiêu và nguyên tắc chạy

**Mục tiêu:** làm một bảng văn phòng 3D để người điều phối xem luồng task và cuộc họp, mở ý kiến/evidence khi nhấp agent, xem bất đồng và tổng hợp; bắt đầu bằng replay offline có thể kiểm tra, phân biệt rõ với agent runtime.

**Giả thuyết cần chứng minh:** lợi thế không phải “3D hấp dẫn”, mà là người điều phối tìm đúng agent/task đang blocked hoặc đang chờ, lần được căn cứ của quyết định và hiểu trạng thái cuộc họp nhanh/chính xác hơn timeline 2D. Giả thuyết UX và market fit chưa được xác thực.

**Nguyên tắc:**

- Mọi avatar/animation suy ra từ event có provenance. `command_requested`, receipt, invite response, joined, contribution và completed là trạng thái khác nhau.
- Tách `work_status`, `location`, `presence`, `meeting_status`; trạng thái thiếu là `unknown/stale`, không đoán thành success.
- Cuộc họp lưu ý kiến có cấu trúc; phản biện nối claim/evidence; giữ bất đồng và câu hỏi mở. Không hiển thị private chain-of-thought.
- Fixture/demo gắn `SIMULATED`; AO-1/AO-2 không gọi model/provider, target, REA/IDA hoặc runtime.
- Giữ sáu identity project. Orchestrator là function điều phối, không phải identity thứ bảy. Người điều phối giữ quyền quyết định theo authority hiện hành.
- Feature 3D phải hỗ trợ câu hỏi vận hành và acceptance kiểm được; không thêm chỉ để avatar sinh động.

## Các phase và điều kiện qua phase

| Phase | Mục tiêu / đầu ra | Acceptance / exit | Dependency / trạng thái |
|---|---|---|---|
| **AO-0 — Chốt bài toán** | Chọn người dùng/scenario ưu tiên; profile, differentiator, event/state vocabulary, risk register và review roadmap | Scenario có ích hơn một màn demo avatar; product hypothesis và giới hạn được ghi; code/README/anecdote được phân loại đúng | Profile/source review đã có; review roadmap đang diễn ra. `PARTIAL` |
| **AO-1 — Offline replay packet** | Schema candidate có version; fixture JSONL `SIMULATED`; expected-state table; storyboard/timeline fallback; acceptance IDs | Có task song song, invite busy/defer, accept/join, contribution/objection, dissent synthesis, cancel, duplicate/out-of-order/gap, stale heartbeat, thiếu evidence và turn/budget limit; cùng fixture cho state xác định; independent review trước code | AO-0. Owner triển khai, codebase, estimate/budget chưa chọn. `NOT_STARTED` |
| **AO-2 — Offline visual vertical slice** | 3D workspace tối giản theo [visual review](visual-review-2026-10-22-01.md): roster sáu identity, cụm bàn/phòng họp, command/event timeline, agent detail, meeting panel, pause/step/replay | Với fixture: pending command không giả thành accepted; chỉ accepted/joined mới dự họp; click claim mở source/evidence hoặc `NO_EVIDENCE_REF`; minutes giữ dissent/actions; SIMULATED luôn rõ; scene/timeline/state khớp nhau | AO-1 được review; chọn Three.js hoặc React Three Fiber sau spike nhỏ. `NOT_STARTED` |
| **AO-3 — Độ đúng và lỗi** | Fixture biên, reducer/replay resilience, tương tác browser và report lỗi | Replay xác định; duplicate không lặp action; gap/reorder không âm thầm lùi state; cancel/failure/no-consensus không bị ẩn; stale/disconnected/unknown rõ; missing contribution không bị tổng hợp bịa | AO-2. Chọn test tooling khi có implementation packet. `NOT_STARTED` |
| **AO-4 — Kiểm chứng giá trị UX** | So sánh 3D với timeline/bảng 2D trên cùng scenario; usability task, baseline và quyết định giữ/giảm 3D | Đo tỷ lệ tìm đúng blocked agent, trạng thái meeting, evidence và decision; thời gian/nỗ lực/lỗi; ghi phản hồi người thử. Chỉ đặt ngưỡng sau baseline và được người điều phối duyệt. Nếu 3D không cải thiện tác vụ hoặc che thông tin thì dừng mở rộng scene | AO-3 và người thử/người điều phối có scope. Chưa có nghiên cứu. `NOT_STARTED` |
| **AO-5 — Read-only live bridge** | Adapter producer→versioned event→snapshot/resync→UI; auth/scope, retention/redaction, latency telemetry | Producer/caller thật, permission/scope, identity/session binding, provenance, reconnect/resync, owner và acceptance được duyệt; live và simulation không thể nhầm; latency/error/staleness được đo; rollback được review | AO-4 + producer/authority ngoài proposal. Orchestrator runtime dispatch hiện chưa triển khai. `BLOCKED / FUTURE` |
| **AO-6 — Command/control và meeting thật** | Thiết kế riêng command broker, invitations, participant invocation, cancel/refusal, budget/approval, receipt và DAG handoff | Chỉ sau contract caller/identity/authority/target/budget, security review, test plan và prerequisite/gates gốc đạt điều kiện. Mọi command có receipt; refusal/error giữ nguyên; decision candidate không tự thành approval/gate | AO-5 + project-level prerequisites. `BLOCKED / FUTURE` |
| **AO-7 — Pilot và quyết định adoption** | Nếu AO-6 được phép: pilot giới hạn, support/rollback, cost/quality/adoption review | User/objective cụ thể; success threshold được duyệt; cost cap, quality baseline, incident/rollback plan; mở rộng/chấm dứt dựa trên evidence | AO-6 accepted. `NOT_PLANNED_UNTIL_PREREQS` |

**Không khóa lịch hoặc effort estimate** khi chưa có implementation owner, codebase, technology spike, capacity và budget. Mỗi phase có quyết định tiếp tục/sửa/dừng riêng.

## First deliverable: AO-1 packet

Task đề xuất: `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01`.

- **Objective:** biến roadmap thành scenario offline đầu-cuối và contract candidate trước khi code.
- **Owner trách nhiệm đề xuất:** Prompt-Master lập packet/DAG; Product-Evolution-Architect chốt user flow/acceptance; Evidence-Synthesizer review provenance/cases/no-go; người điều phối quyết định mở AO-2.
- **Inputs:** profile, architecture, verification-plan, meeting review, exact project role/phase/gate/status sources và pinned competitor revisions.
- **Output:** JSONL synthetic fixture, schema candidate, expected-state table, storyboard/timeline fallback, privacy/redaction notes, acceptance IDs, scope/unknowns. Không gọi provider/target.
- **Acceptance:** cover AO-1 matrix; từng state/action/claim có ID/provenance; simulation có nhãn; busy agent không bị preempt; contradiction không thành consensus; budget/turn stop và missing contribution được thể hiện; replay deterministic; source exact locators.
- **Authority:** chỉ người điều phối chấp nhận deliverable và quyết định start AO-2. Reviewer chỉ ghi findings/recommendation; không tự dispatch implementation.
- **Dispatch:** `PROPOSED_NOT_DISPATCHED`.

## Điều phối và chuyển phase

1. Prompt-Master lập objective, scope, DAG/dependency, acceptance, budget placeholder và missing fields; không tự gán giá trị chưa biết.
2. Chọn owner từ sáu identity hiện hữu theo đúng capability; role không phù hợp không được gọi mặc định. Product-Evolution-Architect phụ trách product framing; Evidence-Synthesizer độc lập review; Triage/Decomp/Crypto chỉ dùng khi có task/source phù hợp.
3. Lưu mỗi task/meeting dưới ID, owner, input revision, acceptance, status, artifact/evidence refs, reviewer finding và decision. Đây là workflow đề xuất, chưa phải runtime contract đã triển khai.
4. Chỉ chuyển `READY_FOR_REVIEW` khi deliverable tồn tại và mỗi acceptance có locator. Reviewer ghi `PASS/FAIL/OPEN` theo từng mục; dissent và missing evidence vẫn nhìn thấy.
5. Chỉ người điều phối có authority ghi `ACCEPTED` hoặc `START_NEXT_PHASE`. Thiếu owner, budget, permission, source binding hoặc acceptance thì `BLOCKED` cùng field còn thiếu; không lấp bằng suy đoán.
6. AO-4+ cần proposal/authorization mới và contract/gates gốc; không thừa kế quyền từ prototype hoặc cuộc họp review.

## Rủi ro và chỉ dấu dừng

- **3D chỉ là novelty:** nếu người thử không tìm trạng thái/đầu ra tốt hơn timeline phẳng hoặc scene che mất thông tin, giảm ưu tiên 3D; giữ timeline/panel làm giao diện chuẩn.
- **Debate echo/đồng thuận giả:** nếu ý kiến phụ thuộc nhau hoặc synthesis xóa dissent, sửa protocol/fixture; chưa chuyển AO-3.
- **Animation gây hiểu lầm:** avatar state không nối event/receipt là lỗi semantics, không phải cosmetic issue.
- **Chi phí/token:** hiển thị budget/cost khi có dữ liệu; không lấy Reddit self-report làm benchmark.
- **Scope drift/runtime coupling:** offline prototype không thêm network/model ngầm. Live bridge và control là phase riêng.
- **Security/provenance:** trước live data cần quyết định redaction, source rights, retention và access. Transcript chỉ gồm output được phép xem.

## Nguồn và giới hạn

Roadmap dựa trên profile và static source review trong thư mục này. Review feasibility ghi **conditional GO tới AO-4**; AO-5/AO-6 bị chặn. Đây là product proposal độc lập, chưa được runtime/gate project chấp thuận. Trạng thái Orchestrator giữ nguyên theo [current context](../../../context/current.md), [phase map](../../planning/phase-map.md) và [work queue](../../planning/work-queue.md). Xem [biên bản review](roadmap-review-2026-10-22-01.md) và [runbook điều phối](execution-runbook.md).
