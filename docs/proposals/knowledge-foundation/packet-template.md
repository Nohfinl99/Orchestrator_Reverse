# Worksheet task và handoff

Mẫu soạn tài liệu, không phải contract/schema runtime mới. Tham chiếu [intake](../../../prompt_stacks/protocols/intake_protocol.md), [knowledge](../../../prompt_stacks/protocols/knowledge_protocol.md), [pair](../../../prompt_stacks/protocols/pair_protocol.md) và [handoff](../../../prompt_stacks/protocols/handoff_protocol.md). Chưa điền input hoặc chưa review prerequisite thì giữ PROPOSED_NOT_DISPATCHED.

## Task frame

- Task ID / context ID / revision:
- Objective và câu hỏi phải trả lời:
- Scope, action và consumer/call site cụ thể:
- Loại công việc / applicability source-policy:
- Owner identity hiện hữu / actual producer session:
- Reviewer thực / quan hệ với producer-executor / chưa có ghi UNKNOWN:
- Output paths / acceptance predicates:
- Dependencies, exact gate refs và disposition từng nhánh:
- Budget số cụ thể theo scope / stop / điều kiện mở lại:

## Input và knowledge selection

| Input hoặc card | Path/locator | Revision/digest | Phạm vi đã đọc | Rights/relevance | Selected/rejected và lý do |
|---|---|---|---|---|---|
| Chưa bind | UNKNOWN | UNKNOWN | Chưa đọc | UNKNOWN | Chưa chọn |

## Binding cần kiểm

| Facet | Value/reference | Validator hoặc issuer | Receipt/revision/context | Thiếu gì / khi nào chặn |
|---|---|---|---|---|
| Context/input integrity | UNKNOWN | UNKNOWN | UNKNOWN | Chưa xác minh |
| Authority/capability | UNKNOWN | UNKNOWN | UNKNOWN | Chưa xác minh |
| Required gates/applicability | UNKNOWN | UNKNOWN | UNKNOWN | Không tự khai NOT_REQUIRED |
| Knowledge rights/admission/ACK | UNKNOWN | UNKNOWN | UNKNOWN | ACK cần bind exact bundle/context |
| Target pair/consumer ACK nếu applicable | UNKNOWN | UNKNOWN | UNKNOWN | Same target/component/slice/IDB state, fresh/related |

Chuẩn bị ngoài target: ghi rõ NON_TARGET_PREPARATION, pair=null, NOT_RUN; không tạo target claim/ACK. Mọi miễn applicability cần nguồn task/policy phù hợp. Không điền receipt giả để hoàn thiện mẫu.

## Review và handoff

- Candidate/output revision và digest:
- Source facts / inferences / hypotheses / conflicts / unknowns:
- Check đã chạy + raw/receipt locator + scope kết luận:
- Review performed/not performed + reviewer thật + exact candidate:
- Design / implementation / execution / acceptance: ghi từng loại riêng:
- Budget đã dùng/còn lại, attempt, stop hoặc next action:
- Upstream đổi gì / downstream evidence và ACK cần invalidate-revalidate:
- Next owner / input-output-acceptance / dependency chưa đủ:
- Publication branch/commit/URL nếu có:

Self-review, chữ ký/hash, JSON hợp lệ hoặc số người đồng ý không thay evidence/gate acceptance.
