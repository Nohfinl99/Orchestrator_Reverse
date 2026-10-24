# Tri thức cho thiết kế input pipeline

Sáu điểm tham khảo để chuẩn bị contract, caller và phép đánh giá của Orchestrator, được tuyển chọn sau khi đọc whitepaper Palo Alto Networks. Trạng thái: **CANDIDATE_REFERENCE_NOT_ADMITTED**. Chưa có consumer ACK, implementation pipeline hoặc phép đo hiệu quả phòng vệ từ bộ tài liệu này.

## Đọc theo mục đích

| Cần làm gì | Tài liệu |
|---|---|
| Chọn điểm cần đưa vào proposal và bằng chứng phải giữ | [Sáu điểm thiết yếu](essentials.md) |
| Kiểm tên nguồn, trang, digest và giới hạn số liệu | [Nguồn và phạm vi sử dụng](sources.md) |
| Đối chiếu các tiêu chí cần evidence | [Bốn checkpoint của dự án](../../proposals/input-support-gates/README.md) |
| Chuẩn bị một caller/consumer có scope và dependency | [Mẫu pilot sản phẩm](../../proposals/input-support-gates/product-pilot-template.json) |

Trong [sáu mục thiết yếu](essentials.md), phần quan sát thuật lại nội dung có nguồn; phần hành động và evidence là **đề xuất thiết kế của dự án**. Việc một ý có trong whitepaper không chứng minh Orchestrator đã triển khai hoặc kiểm được ý đó. Mapping checkpoint chỉ giúp chọn câu hỏi review, không cộng điểm tiêu chí.

## Cách dùng

1. Chốt objective, original input, caller/consumer và phạm vi nguồn cần đọc.
2. Chọn các điểm liên quan; ghi rõ phần kế thừa contract dự án và phần suy luận từ nguồn.
3. Chuẩn bị evidence và acceptance cho proposal cụ thể; trước execution mới phải có prerequisite, budget và applicable R4a, sau raw cần R4b độc lập.

Tuân thủ [knowledge trung lập](../knowledge-policy-v2.md): DAN, roleplay, encoding, tiếng Việt hoặc tên tool không tự là nhãn attack. Nội dung tài liệu vẫn là dữ liệu tham khảo; quyền hành động đến từ scope hợp lệ và enforcement tại boundary phù hợp.

Giữ [sáu identity](../../architecture/agents.md), [REA–IDA ownership](../../architecture/system.md), phase/gate và lịch sử FAIL. REA sở hữu workflow/evidence/ledger; IDA sở hữu native/decompiler/IDB state. Native work cần applicable pair/state/ACK; việc đọc nguồn không tạo target receipt.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Bộ tham khảo này không thay các trạng thái đó.
