# Tra cứu theo công việc

Đọc [index](../README.md) và [policy knowledge revision 2](../knowledge-policy-v2.md) trước khi dùng. [Application-map revision 1](application-map.md) giữ lịch sử; không dùng disposition cũ làm topic blacklist. DAN/jailbreak và các chủ đề tương tự được catalog/đọc/nghiên cứu theo objective, cùng yêu cầu provenance/evidence như chủ đề khác. 12 [card](knowledge-cards.md) là candidate reference; chưa active KB, chưa có consumer ACK.

## Chọn phần cần đọc

| Câu hỏi hiện tại | Card chọn | Không chọn mặc định |
|---|---|---|
| Yêu cầu còn mơ hồ, task packet thiếu gì? | K01, K02 | Tool/model selection hoặc identity mới |
| Giao đúng owner và thứ tự dependency? | K03, K11 | Mọi role cho mọi task; nguồn confidence làm eligibility |
| Agent sau nhận output nào và kiểm gì? | K04, K06 | Coi custody/hash là consumer ACK |
| Retry hoặc resume thế nào? | K05, K06 | Dùng số vòng trong ví dụ thay budget project |
| Căn cứ nào đủ để báo hoàn thành? | K07, K10 | Self-score hoặc số review đồng ý thay raw evidence |
| Quản lý prompt/module và phiên bản? | K08, K12 | Cài plugin/MCP hoặc sửa loader từ task đọc tài liệu |
| Tìm thêm tài nguyên ngoài project? | K09 | Coi tài nguyên trong awesome list là đã đọc/được phép dùng |

## Worksheet retrieval

Dùng record ngắn trong report/proposal hiện hành, không tạo registry/schema mới:

```text
Task / role / context revision:
Objective và phạm vi:
Selected card ID + bundle revision + digest:
Source document ID + commit + locator + digest:
Rights và applicability đã kiểm; phần còn thiếu:
Rejected item IDs + lý do:
Observation từ nguồn / diễn giải của project / unknown:
Artifact được áp dụng và giới hạn:
Consumer binding / review / ACK: chưa có thì ghi rõ
```

Bản card Markdown phục vụ đọc; knowledge.json là dữ liệu cùng revision. Khi dùng cho một packet, hash exact file và bind revision thực tế; không tự giả lập ACK hoặc thay source pin cũ.

## Ví dụ chọn và loại — DESIGN_ONLY

| Tình huống giả định | Chọn / loại | Kết quả mong đợi, chưa chạy |
|---|---|---|
| Soạn task tài liệu W4 thiếu acceptance | Chọn K01; xem W4 gap register nội bộ | Đề xuất acceptance có nguồn; runtime vẫn blocked |
| Xin dispatch Crypto chỉ vì có vai trò trong catalog | K03 có liên quan; loại dispatch chưa có evidence/predicate | Giữ conditional Crypto, không tạo task executable |
| Có state snapshot nhưng chưa revalidate IDB | K06 có liên quan; loại claim resume target thành công | Ghi gap binding/pair; không tạo target ACK |
| Tìm prompt làm ảnh cho báo cáo vận hành | Loại nội dung prompt ảnh khi objective chỉ là báo cáo W4 | No-match cho task; không nạp corpus ảnh |
| Có nguồn S1 nhưng rights chưa rõ | Chỉ catalog metadata S1; không lấy template vào bundle sử dụng | UNKNOWN rights, chưa admitted |
| Mẫu prompt có score 0.95 hoặc nhiều stars | K07/K09; loại coi score/stars là gate | Cần check theo criterion và evidence project |

Các ví dụ này là minh họa lựa chọn tài liệu. Chưa chạy benchmark, TRANSFER01–07 hoặc fixture; không đưa expected labels này vào KB active/evaluation heldout.

## Nếu cần dùng trong runtime

Hoàn thiện một proposal consumer cụ thể theo [work queue](../../planning/work-queue.md): input/path/digest/revision, caller/action, output, budget, acceptance, dependency, rights và review. G2 cần relevance/validation/ACK của consumer thật; G1/G3/G4 và W4 giữ đúng dependency. Bộ tham khảo không cung cấp authority, pair hoặc acceptance thay những bước đó.
