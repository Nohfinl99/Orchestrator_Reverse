# Knowledge và công cụ điều phối kèm theo

## Knowledge cards phù hợp

Các card dưới đây được chọn từ [retrieval guide](../../knowledge/prompt-orchestration/retrieval-guide.md) cho mục tiêu lập profile và tiêu chí offline. Chúng là candidate reference; ghi nhận không có nghĩa là runtime đã nạp, G2 đã đóng hoặc consumer đã ACK.

| Card | Dùng cho hồ sơ này |
|---|---|
| K01 — Task có đầu ra và tiêu chí kiểm được | Viết goal, output, acceptance, scope và stop condition cho V0–V4. |
| K02 — Nạp context theo câu hỏi và giữ locator | Ghi exact repo/commit/file, phần đã đọc và giới hạn khảo sát. |
| K03 — Chọn dạng dependency trước khi chọn agent | Tách nghiên cứu, design, offline UI, read-only bridge và control phase theo thứ tự. |
| K04 — Kiểm artifact trước khi chuyển giao | Kiểm event/schema cùng ý nghĩa/provenance, không chỉ JSON parse thành công. |
| K05 — Vòng lặp có tiêu chí thành công, lỗi và hết ngân sách | Chuẩn bị retry/cancel/timeout và tiến triển có giới hạn cho cuộc họp thật về sau. |
| K06 — State để tiếp tục phiên là record quyết định và bằng chứng | Lưu event history, meeting summary, revision, gap và next action. |
| K07 — Bằng chứng từ môi trường và vai trò người kiểm | Phân biệt mô phỏng, source review, implementation, execution và independent review. |
| K08 — Version prompt và kiểm biến chưa được điền | Version hóa prompt/scope/context khi thiết kế meeting contribution, không để placeholder thiếu. |
| K10 — Thiết kế ca biên và no-match từ trước | Bao gồm busy agent, decline, timeout, event gap, disagreement và no evidence. |
| K11 — Prompt hướng dẫn; harness và tool thực thi quyền | Không để prompt, role label hay vị trí avatar tự cấp authority. |
| K12 — Chỉ mở module phù hợp, có chỉ dẫn sử dụng và giới hạn | Nạp kiến thức theo mục tiêu; không nạp toàn bộ corpus vào mọi agent. |

K09 chỉ cần khi task đi tìm thêm nguồn; trong hồ sơ này đã có exact repos và source files được pin ở [competitor review](competitor-review.md), nên không dùng popularity/star count làm tiêu chí kỹ thuật.

**Trạng thái:** toàn bộ K01–K12 đang `CANDIDATE_REFERENCE_NOT_ADMITTED`, chưa independent review, chưa TRANSFER và chưa consumer ACK. Hãy dùng như hỗ trợ soạn proposal, không là policy mới hoặc nguồn thẩm quyền thay thế project.

## Prompt stack/protocol theo objective

Khi chuyển sang một task riêng, chọn theo [index hiện hành](../../../prompt_stacks/README.md), không bật cả stack:

- Goal/scope và ambiguity: Stack 00 + intake protocol.
- Owner/dependency/stop: Stack 02 + routing protocol; giữ sáu identity.
- Gói knowledge consumer: Stack 03 + knowledge protocol nếu objective thật sự nạp bundle.
- State, retry, immutable event/attempt: Stack 05 + state protocol khi đã có implementation scope.
- Testcase/oracle: Stack 06 + evaluation protocol; R4a trước attempt, R4b độc lập sau raw cho workload nghiệp vụ.
- Handoff/review: Stack 09 + handoff protocol.

## Tool stack prototype

| Nhu cầu | Công cụ gợi ý | Chưa quyết định |
|---|---|---|
| Văn phòng 3D | Three.js hoặc React Three Fiber | Chưa chọn; làm spike ngắn so tương tác, accessibility và hiệu năng. |
| Sự kiện có version | TypeScript + JSON Schema/Ajv | Event contract chưa được chấp thuận. |
| Bảng offline | JSONL fixture + reducer/replay local | Chưa có app/package implementation. |
| Kiểm UI | Playwright; Vitest cho reducer | Chưa cài/chạy. |
| Feed thật | SSE một chiều hoặc WebSocket hai chiều | Chỉ chọn sau khi có event producer; lệnh đi qua Orchestrator/broker. |

## Knowledge nên phản ánh vào output của cuộc họp

Meeting packet cần có topic, goal, scope, context revision, participant, role/capability, agenda, criteria, budget, stop rules và dependency. Contribution cần claim, evidence locator, assumption, uncertainty, counterargument, response và status. Minutes cần agreement, dissent, open question, unsupported claim, decision, action owner, acceptance và event IDs. Đây là nội dung thiết kế đề xuất để có thể kiểm; không cần lưu private chain-of-thought.

