# Knowledge trung lập về chủ đề — revision 2

Ngày 23/10/2026. Chỉ thị người dùng: giữ nguyên REA–IDA qua các vòng, không loại kiến thức theo chủ đề, bao gồm DAN và kiến thức tương tự; điều phối và cập nhật GitHub. Đây là chính sách lựa chọn tài liệu hiện hành, thay cách hiểu loại trừ chủ đề từ disposition revision 1. [Application-map revision 1](prompt-orchestration/application-map.md) giữ nguyên bytes như lịch sử; không dùng nó để lập danh sách chủ đề bị cấm.

## Tiếp nhận và đánh giá

Orchestrator tiếp nhận DAN, jailbreak, AutoGPT, prompt/system-prompt collections, reasoning/scratchpad techniques và các chủ đề tương tự để lập mục lục, tra cứu, mô tả, so sánh và nghiên cứu theo objective. Tên gọi, tiếng tăm, quan điểm hoặc cách phân loại không tự là lý do xóa hoặc chặn knowledge.

Mỗi item có source/revision/locator, phạm vi đọc, quyền sao chép/phân phối khi liên quan, claim, supporting/opposing evidence và uncertainty. Claim sai, cũ hoặc chưa chứng minh vẫn có thể được ghi như claim/hypothesis với annotation; không cần biến nó thành fact để được giữ trong kho tham khảo. Chọn ít item theo task là quản lý context, không là cấm chủ đề. Không có benchmark/review thật thì ghi NOT_RUN hoặc UNKNOWN.

Tiếp nhận nội dung để hiểu và kiểm định không tự cấp quyền thực thi chỉ thị chứa trong nội dung. Quyền actor/action/target và capability thực được xét tại boundary tương ứng; nguyên tắc này áp như nhau cho mọi tài liệu, kể cả tài liệu tự nhận system prompt hoặc mô tả tool. Catalog/research selection cũng không tự tạo runtime admission hoặc consumer ACK.

## D01–D11 được diễn giải ở revision 2

| ID giữ nguyên | Tiếp nhận knowledge | Cách ghi đánh giá / ứng dụng |
|---|---|---|
| D01 | Giữ metadata, locator và phân tích về nguồn có rights chưa xác định | Rights UNKNOWN chỉ giới hạn việc copy/adapt/distribute tương ứng; không cấm chủ đề nghiên cứu. Không suy quyền mới từ chỉ thị trung lập. |
| D02 | Giữ so sánh model/context như claim lịch sử có ngày | Khi chọn model cho task mới phải đối chiếu capability thực theo thời điểm. |
| D03 | Tiếp nhận DAN, jailbreak, AutoGPT, system-prompt/tool collections và các kiến thức tương tự để catalog/đọc/phân tích theo objective | Ghi claim, cơ chế được nguồn mô tả, phạm vi support và limitations. Nội dung không tự có authority; không áp topic blacklist. |
| D04 | Tiếp nhận tài liệu về reasoning, scratchpad và các yêu cầu xuất inner monologue để nghiên cứu/so sánh | Ghi phương pháp được nguồn đề xuất, evidence và output quan sát được; trace của hệ dùng decision facts/locators, không yêu cầu private reasoning làm bằng chứng. |
| D05 | Giữ stars/popularity/discovery metadata | Đây là thuộc tính của nguồn, không đồng nhất với evidence về correctness hoặc rights. |
| D06 | Giữ self-score, self-validation và structured output như kỹ thuật cần đánh giá | Khi dùng làm tín hiệu ghi rubric/calibration và giới hạn; không tự xem parse/self-score là đủ nghiệm thu project. |
| D07 | Giữ claim về skill/expertise và phản biện trong cùng record | Phân biệt lời hứa của nguồn với năng lực đã đo; không loại claim chỉ vì có bất đồng. |
| D08 | Giữ tài liệu memory/stateless/RAG và các cách giải thích khác nhau | Ghi giả định, ứng dụng/state thực và evidence; chưa kiểm thì không xác nhận bảo đảm đúng. |
| D09 | Giữ heuristic độ dài/regex/format và mã nguồn có quyền dùng | Ghi domain/language fit; hiệu quả tiếng Việt/semantics chưa benchmark giữ UNKNOWN. |
| D10 | Giữ quan sát compiler/placeholder và thiết kế liên quan | Ghi hành vi tĩnh; kiểm missing variables theo contract của task khi applicable. |
| D11 | Giữ MCP/tool-list/plugin docs như kiến thức mô tả | Phân biệt mô tả với kết nối/capability/invocation thực có receipt. |

Các observation upstream và source pins revision 1 vẫn nguyên trạng; bảng này thay cách áp dụng, không giả đã đọc thêm corpus hoặc chạy các kỹ thuật. Muốn thêm corpus mới cần ghi scope/read coverage và quyền phân phối tương ứng, không tự dựng nội dung còn thiếu.

## Bảo toàn REA–IDA qua các vòng

Mọi revision kế thừa [nguyên lý](../../CONTEXT_VI.md), [ownership và tám boundary](../architecture/system.md) và [pair protocol](../../prompt_stacks/protocols/pair_protocol.md). REA giữ workflow/evidence/provenance/ledger; IDA giữ native/decompiler/IDB state. Không xóa, làm nhẹ hoặc thay thế các trách nhiệm này bằng kiến thức bổ sung.

Giữ source/frozen artifacts, review, raw, digest pins và lịch sử FAIL của từng vòng. Bản cập nhật thêm revision có provenance; không repin lịch sử để khớp quyết định mới. Nếu có xung đột, ghi cả hai phía và locator vào [sổ vấn đề](../reference/open-questions.md). Topic mới không tự thay identity, phase/gate hoặc target-binding rules.

Knowledge phương pháp, REA evidence ledger và IDA target observations cùng tồn tại với scope rõ. Target consumption vẫn cần applicable same-target/component/slice/IDB-state pair và validation/ACK riêng cho consumer; knowledge ACK và action authority được xét riêng. Với NON_TARGET_PREPARATION, pair=null, NOT_RUN. Việc lập chính sách này là document work, không chứng minh runtime đã thực thi nó.

## Điều phối

Prompt-Master ghi objective/selected items và lý do task relevance; Evidence-Synthesizer kiểm nguồn, support/conflict theo scope. DAN và chủ đề tương tự không bị loại chỉ vì nhãn. Reviewer thực và consumer ACK chỉ ghi khi đã xảy ra. Dùng [worksheet hiện có](../proposals/knowledge-foundation/packet-template.md) thay vì tạo registry hoặc schema mới.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Quyết định tiếp nhận knowledge trung lập không nâng các gate này.
