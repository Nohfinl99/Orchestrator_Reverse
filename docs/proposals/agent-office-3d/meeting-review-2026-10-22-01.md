# Biên bản review: văn phòng 3D và cuộc họp agent

| Trường | Giá trị |
|---|---|
| Review ID | `AGENT_OFFICE_DESIGN_REVIEW_20261022_01` |
| Profile | `AGENT_OFFICE_3D_PROFILE_01`, revision 1 |
| Loại | `DESIGN_REVIEW / SYNTHETIC_MULTI_REVIEWER` |
| Phạm vi | Phản biện kiến trúc, đối chiếu repo công khai và tín hiệu Reddit; không phải runtime meeting của sáu identity Orchestrator |
| Kết quả triển khai | `NO_CODE / NO_RUNTIME_DISPATCH / GATES_UNCHANGED` |

## Câu hỏi cuộc họp

Liệu có thể làm một văn phòng 3D nơi lệnh Orchestrator, trạng thái agent, họp/phản biện và tổng hợp ý kiến được nhìn thấy theo thời gian thực; phần đầu có thể chạy offline để kiểm tra không?

## Các vị trí và phản biện

### Ủng hộ tính khả thi

- Lớp quan sát 3D, event stream, reducer và stage directions đã có tiền lệ trong Roving Office. AOP nối adapter/harness với ingest, SSE và browser; `AopSource` hydrate snapshot rồi áp event lên UI. Đây là căn cứ cho **observability/replay**, không phải bằng chứng Orchestrator có thể ra lệnh cho agent.
- ClawProwl có kiểu dữ liệu zone `meeting` và manager gom agent theo collaboration link/session key để đổi zone. Đây là căn cứ cho **biểu diễn vị trí/phòng**, không chứng minh có tranh luận hay meeting receipt.
- Hermes Virtual Office có code họp theo lượt, tách mode mô phỏng/A2A, archive/transcript/minutes, và ghi lỗi participant thay vì bịa lượt thay thế. Đây là căn cứ mạnh hơn cho **workflow họp**; không chứng minh tương thích với Orchestrator hoặc tích hợp REA–IDA.
- Vì các lớp trên được tách rời, bảng offline dùng fixture/replay là một điểm bắt đầu khả thi để thử UX, state semantics và lỗi mà chưa cần agent runtime.

### Phản biện và quyết định

| Phản biện | Cách xử lý trong thiết kế |
|---|---|
| 3D, avatar, room, transcript và minutes đã có trong sản phẩm khác; không đủ làm lợi thế riêng. | Định vị proposal quanh provenance theo task/DAG, source revision, evidence locator, receipt, dissent và semantics gate của Orchestrator; đây mới là giả thuyết khác biệt cần prototype/validation. |
| Nhân vật bước vào phòng không chứng minh đã nhận lời mời hoặc tham dự. | UI chỉ đổi vị trí theo event có ID/receipt; tách `work_status`, `location`, `presence`, `meeting_status`. |
| Nhiều agent có thể lặp lại/đồng ý theo nhau; tổng hợp dễ xóa bất đồng. | Lưu contribution độc lập trước khi xem ý kiến người khác khi phù hợp; phản biện gắn claim cụ thể; synthesis bắt buộc tách agreement, dissent và open questions. Cần kiểm bằng fixture phản ví dụ. |
| “Có evidence” cũng đã được repo khác tuyên bố. | Không tuyên bố độc quyền. Kiểm tra cách evidence được ràng buộc với claim, revision, authority và gate; chỉ những liên kết thực sự kiểm được mới là acceptance. |
| Người xem có thể nhầm demo với agent chạy thật hoặc coi transcript là chain-of-thought. | Mọi fixture gắn `SIMULATED`; chỉ trình bày output có cấu trúc đã xuất, nguồn và artifact được phép xem; không hiển thị private chain-of-thought. |
| Tích hợp runtime hiện tại chưa sẵn sàng. | Chỉ đề xuất V0/V1/V2 offline. V3/V4 bị chặn bởi producer/caller, quyền và prerequisite hiện có; không đổi phase/gate hoặc giả lập dispatch thật. |

## Luồng họp được review

1. Người điều phối nhập mục tiêu, câu hỏi cần quyết định, agenda, đầu ra, acceptance và giới hạn.
2. Orchestrator tạo `meeting_id`/task link, chọn participant trong sáu identity hiện hữu theo capability/dependency/authority; agent bận được đánh dấu defer/wait hoặc meeting blocked theo rule, không bị ngắt ngầm.
3. Invite, accept/decline/defer, join, contribution, objection, synthesis, decision và close đều là event riêng. Chỉ `accepted/joined` mới được tính là người dự; avatar chỉ phản ánh event đã ghi.
4. Agent gửi contribution có cấu trúc: position/claims/evidence refs/uncertainty/risks/questions. Reviewer phản biện bằng locator tới claim hoặc event cụ thể.
5. Điều phối viên tổng hợp agreement, dissent, unsupported claims, open questions, decision candidate và actions, trỏ về các contribution. Không tự suy consensus từ đa số.
6. Chỉ decision/receipt được thẩm quyền cho phép mới tạo handoff hoặc cập nhật DAG. Thiếu evidence hoặc quyền thì giữ `WAIT_INPUT`, `BLOCKED`, `CONFLICT`, `NOT_RUN` tương ứng.
7. Bảng offline phát lại cùng JSONL fixture theo cùng reducer; hiển thị timeline, chuyển động, panel chi tiết và trạng thái lỗi với nhãn `SIMULATED`.

## Ma trận học hỏi và áp dụng

| Bài học/nguồn | Bằng chứng đã đọc | Áp dụng cho Orchestrator | Điều không được suy ra | Mức |
|---|---|---|---|---|
| Roving Office — adapter và event stream | [AOP spec tại commit đã pin](https://github.com/atlassian-labs/roving-office/blob/f3c51c85d04c13ae32a4b929c7488847980c3851/docs/developer/protocol/aop-spec.md), [AopSource](https://github.com/atlassian-labs/roving-office/blob/f3c51c85d04c13ae32a4b929c7488847980c3851/src/data/AopSource.js) | Versioned event contract, hydrate snapshot + stream, reducer đơn hướng cho replay | Không suy ra command/control, meeting semantics hoặc runtime integration | `SOURCE_CODE_REVIEWED` |
| ClawProwl — meeting zone | [meeting-manager](https://github.com/clawprowl/clawprowl/blob/866351cc5143baf9c78a6003b7848319da459055/src/store/meeting-manager.ts), [gateway types](https://github.com/clawprowl/clawprowl/blob/866351cc5143baf9c78a6003b7848319da459055/src/gateway/types.ts) | State `location` riêng với activity; movement phản ánh state/event | Không suy ra participant đã tranh luận hoặc meeting đã có kết quả | `SOURCE_CODE_REVIEWED` |
| Hermes Virtual Office — meeting turns | [meeting-a2a.ts](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/lib/hermes/meeting-a2a.ts), [meeting.ts](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/lib/hermes/meeting.ts), [MeetingPanel](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/components/MeetingPanel.tsx) | Tách simulation/A2A; lượt, archive/transcript/minutes và trạng thái lỗi | Không suy tương thích hoặc differentiation từ “meeting + transcript” | `SOURCE_CODE_REVIEWED` |
| Reddit: virtual office demo | [r/SideProject thread](https://www.reddit.com/r/SideProject/comments/1r3h4zj/i_built_a_virtual_office_where_8_ai_agents_show/) (post hiển thị 13/02/2026) nêu green/yellow/idle, speech bubbles và standup; bình luận hỏi “làm được gì cụ thể?”, token burn, memory, runtime, coordination | Cần outcome/task link, cost/usage và memory/context view; scene vui cần chứng minh công việc hữu ích | Reddit post không xác minh sản phẩm/code hay đại diện thị trường | `ANECDOTAL_USER_SIGNAL` |
| Reddit: cách host roundtable | [r/ClaudeAI thread](https://www.reddit.com/r/ClaudeAI/comments/1s4sew1/how_do_i_host_an_ai_agent_roundtable_to_debate/) (post hiển thị 27/03/2026) bàn debate pattern, round limit, shared message file, orchestrator stop condition và cost | Có giới hạn lượt/token, role độc lập, stop condition, một lượt synthesis; ghi event để audit | Bình luận là gợi ý cá nhân, không benchmark | `ANECDOTAL_USER_SIGNAL` |
| Reddit: agent convergence | [r/AI_Agents thread](https://www.reddit.com/r/AI_Agents/comments/1w3y7h1/i_ran_13_ai_agents_from_different_companies_in/) (post hiển thị 01/09/2026) kể agents hội tụ giọng và đồng ý mặc định trong shared space | Thêm test chống echo/chạy theo nhau: ý kiến đầu độc lập, objection gắn claim, dissent không bị mất | Một báo cáo tự kể không chứng minh tần suất phổ biến | `ANECDOTAL_USER_SIGNAL` |
| Reddit: disagreement model | [r/aiagents thread](https://www.reddit.com/r/aiagents/comments/1wjs6kp/i_built_multiagent_disagreement_instead_of/) (post hiển thị 18/09/2026) đề xuất biểu diễn claim → evidence → challenge → counterclaim → concession/unresolved | Cấu trúc debate như graph có cạnh được tham chiếu, cộng event log để phát lại | Chưa xác thực code/hiệu quả của dự án nêu trong post | `ANECDOTAL_USER_SIGNAL` |

## Thẻ ý tưởng có thể kiểm chứng

Các thẻ là đề xuất acceptance cho prototype offline; chưa được triển khai, chạy hoặc đưa thành gate.

| ID | Ý tưởng | Verification card: bằng chứng quan sát được và acceptance | Rủi ro / nhãn |
|---|---|---|---|
| IDEA-01 | Phân biệt invite, accept, join và contribution | Fixture chứa từng chuyển trạng thái; timeline hiển thị receipt/event ID; chỉ agent `accepted` + `joined` mới hiện tham dự | Animation gây hiểu nhầm; `DESIGN_PROPOSED` |
| IDEA-02 | Claim mở được source locator/version | Click claim mở nguồn, revision, locator, kiểm tra/provenance; thiếu nguồn được gắn `UNSUPPORTED` | Locator cũ; `DESIGN_PROPOSED` |
| IDEA-03 | Giữ ý kiến thiểu số và conflict | Fixture có hai claim mâu thuẫn; synthesis hiện agreement/dissent/open questions riêng và nối tới tác giả/claim | Synthesis làm phẳng ý kiến; `DESIGN_PROPOSED` |
| IDEA-04 | Decision lineage qua DAG/receipt/gate | Từ decision mở task/node, owner, căn cứ, authority và receipt; không có receipt thì DAG không đổi | Dễ bị hiểu thành gate PASS; `DESIGN_PROPOSED` |
| IDEA-05 | Replay pause/step/compare | Cùng JSONL và reducer tạo cùng state; pause/step chỉ ra event gây đổi state; duplicate/sequence cũ không lùi state | Demo nhầm với live; `DESIGN_PROPOSED` |
| IDEA-06 | Hiện chất lượng kết nối và invite riêng | Fixture heartbeat timeout/gap/defer; state đổi stale/disconnected/unknown đúng ngưỡng; deferred agent giữ nguyên task | Heartbeat cũ gây false-live; `DESIGN_PROPOSED` |
| IDEA-07 | Chống echo/đồng thuận giả | Fixture agent A/B trả lời độc lập trái chiều; lượt phản biện phải nêu claim bị phản biện; unresolved conflict còn trong minutes; consensus không được tạo khi thiếu điều kiện | Không có metric chứng minh debate nâng chất lượng; `DESIGN_PROPOSED` |
| IDEA-08 | Họp có budget và stop rule | Scenario dừng đúng số lượt/thời gian/token đã khai báo; một synthesis cuối; event log nêu lý do dừng/cost giả lập | Ước tính cost không tương đương hóa đơn thật; `DESIGN_PROPOSED` |
| IDEA-09 | Theo dõi task outcome thay vì chỉ hoạt động avatar | Mỗi session/meeting trỏ tới output artifact, owner và acceptance; người xem phân biệt `activity` với output đạt/chưa đạt | Một output có thể kém chất lượng dù đủ artifact; `DESIGN_PROPOSED` |

### Quyết định review

**GO cho định nghĩa và prototype bảng offline V0–V2; NO-GO cho tuyên bố điều phối agent thật hoặc đổi gate.** Ưu tiên V0 event/schema + fixture trước; sau đó một vertical slice V1 cho lệnh → invite/defer → join → contribution/objection → synthesis có dissent → close, kèm pause/step. V3/V4 chỉ xem xét khi có caller/producer, quyền, budget, binding và acceptance cụ thể được đáp ứng theo hợp đồng project hiện hành.

## Evidence labels

- `SOURCE_CODE_REVIEWED`: đọc tĩnh các file code tại revision pin; chưa build/run.
- `README_CLAIM`: mô tả của repository, chưa kiểm trong code.
- `ANECDOTAL_USER_SIGNAL`: bài/bình luận cộng đồng; không phải xác minh kỹ thuật hoặc nghiên cứu đại diện.
- `DESIGN_PROPOSED`: thiết kế/acceptance cần được triển khai và kiểm tra.
- `EXECUTION_VERIFIED`: chỉ được gắn sau khi ghi command, revision, output và môi trường thực chạy. Chưa có thẻ nào trong review này đạt nhãn đó.

## Trạng thái nguồn project

Review này không dispatch runtime, không sửa source implementation, không gọi provider/target, không chạy fixture nghiệp vụ/W4. Sáu identity, REA–IDA, phase/gate và lịch sử FAIL giữ nguyên. Trạng thái kế thừa: P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`.
