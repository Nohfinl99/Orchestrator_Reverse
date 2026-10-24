# Phần hữu ích được áp dụng vào folder

Đọc [knowledge cards revision 1](../../knowledge/prompt-orchestration/knowledge-cards.md), [source catalog](../../knowledge/prompt-orchestration/sources.json) và [disposition D01–D11](../../knowledge/prompt-orchestration/application-map.md). Bảng này là diễn giải ứng dụng tài liệu mới, không phải benchmark hoặc bundle đã admitted.

| Selected | Giá trị giữ lại | Đưa vào bản cải tiến | Bằng chứng có thể yêu cầu khi dùng |
|---|---|---|---|
| K01 | Một task có output/acceptance rõ | Worksheet objective/input/output/acceptance | Reviewer chỉ được task giải quyết câu hỏi nào |
| K02, K12 | Context vừa đủ và có locator | Guide chọn ít nguồn theo objective, giữ unknown | Selected/rejected log, source/context revision |
| K03 | Dependency trước routing | Guide DAG và eligibility cho từng cạnh | Owner hiện hữu và predicate có nguồn; không mặc định gọi cả sáu role |
| K04, K11 | Kiểm handoff và giữ trust boundary | Worksheet tách instructions, refs, validator/receipt và ACK | Source/tool text được xử lý như dữ liệu; receipt kiểm ở boundary có thẩm quyền |
| K05, K06 | Attempt/history, budget và stop | Worksheet ngân sách, progress, invalidation, next action | Attempt mới, gap và dependency state; không xem restore là semantic repair |
| K07, K10 | Criteria trước run và kiểm độc lập sau raw | Guide tách document check, implementation, execution, review | R4a/R4b applicable; gold/heldout tách khỏi active KB |
| K08 | Revision và missing variables | Worksheet liệt kê biến chưa bind; sửa sau review tạo revision | Exact input/output digest, không tự điền authority/budget |
| K09 | Discovery có provenance | Guide tra nguồn có quyền/commit/read scope | Không xem awesome list/stars là source đã kiểm |

Tất cả K01–K12 được dùng để soạn tài liệu trong scope hiện tại. Từng task tương lai chỉ chọn item liên quan; selection tổng hợp ở đây không tự là runtime ingestion/consumer ACK.

## Cập nhật áp dụng — policy revision 2

[Policy hiện hành](../../knowledge/knowledge-policy-v2.md) tiếp nhận mọi chủ đề knowledge, bao gồm DAN/jailbreak/AutoGPT và nội dung tương tự. Các nhận định dưới đây giữ bối cảnh revision 1 về cách áp dụng; không được diễn giải thành danh sách cấm đọc hoặc cấm lưu tri thức. Claim và bằng chứng được ghi riêng với quyền thực thi.

## Phạm vi áp dụng ở revision 1, giữ để đối chiếu

D01 giữ S1 catalog metadata only khi rights UNKNOWN. D02 không dùng model claims cũ để chọn provider. D03–D04 không kế thừa bypass, tool authority hoặc yêu cầu private reasoning. D05–D06/D09 không dùng popularity, self-score, JSON hợp lệ hoặc regex/độ dài làm gate đúng/sai. D07–D08 không kế thừa bảo đảm expertise/RAG đúng hoặc stateless tuyệt đối. D10 cần check biến thiếu trong proposal; D11 mô tả tool không chứng minh đã nối tool.

Nguồn S2/S3 có attribution/license khai báo ở [third-party notices](../../knowledge/prompt-orchestration/third-party-notices.md). Lượt này viết diễn giải ứng dụng từ card đã có; không ingest corpus, copy template S1, import code hoặc sửa license. Không mở thêm các link nghiên cứu chưa được đọc trong upstream để gọi chúng là primary evidence đã kiểm.

## Cách nối với REA–IDA

Knowledge trả lời “cách kiểm/điều phối”; REA evidence ledger trả lời “quan sát nào từ producer/run nào”; IDA observations trả lời “tọa độ và IDB state nào hỗ trợ claim”. Consumer nối ba phần bằng relevance, binding và ACK; giữ conflict/unknown khi evidence chưa hỗ trợ. Không gộp knowledge guidance vào target facts chỉ vì cả hai cùng có citation.
