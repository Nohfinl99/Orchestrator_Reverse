# Nguồn đọc được và cách áp dụng có giới hạn

## Ba nguồn đã được phân biệt

| Nguồn pin | Đã đọc / kiểm | Giá trị cho Orchestrator | Giới hạn |
|---|---|---|---|
| [S1: Claude prompts fork](https://github.com/hesreallyhim-forks/awesome-claude-prompts-fork/tree/2be4e1085e8c026cd12ad67fdd2ce61c1c42b2d6) | Kiểm kê 10 file; đọc index và các section README liên quan | Metadata/locator cho task assignment, cấu trúc prompt và source citation | Không có LICENSE trong cây; metadata license null; badge README trỏ sang repo khác. UNKNOWN rights, catalog only; chưa đưa template vào KB |
| [S2: awesome-awesome-ai](https://github.com/dukeluo/awesome-awesome-ai/tree/03173a28827eb48d6d5577421825b2e1f06639db) | Kiểm kê 6 file; đọc README, guidance, audit workflow và LICENSE | Phân loại discovery, link canonical và ghi tình trạng nguồn (K09) | Danh sách tài nguyên không là bằng chứng các tài nguyên liên kết đã được đọc/đánh giá |
| [S3: prompts.chat](https://github.com/f/prompts.chat/tree/f8fe2385244a6188c976e352ea7ca849e3d20b1e) | Kiểm kê 1.574 file; đọc chọn lọc 8 chương, plugin docs, source/schema và licenses | K01–K08, K10–K12; quan sát versioning/variables | Không audit toàn ứng dụng, không ingest prompt corpus; guidance không chứng minh hiệu quả trong project |

[Sources.json](sources.json) ghi 22 file snapshot có Git blob SHA, SHA-256, số byte và phạm vi đọc. Raw local đã đối chiếu Git blob; kiểm kê không đồng nghĩa đọc từng file. LICENSE/source đã kiểm chỉ hỗ trợ phần quyền khai báo, không tự đóng G2 hay bảo đảm quyền mọi tài liệu liên kết.

## Đối chiếu với các phần project

| Phần project | Card hỗ trợ chuẩn bị | Điều kiện giữ nguyên |
|---|---|---|
| W0/W1 intake, context, master prompt/routing | K01, K02, K03, K08, K12 | Identity/capability/authority và admission theo nguồn gốc |
| W2 knowledge transfer | K02, K04, K09, K12 | Rights, WHAT/WHY/HOW review, TRANSFER01–07, consumer ACK |
| W3 REA–IDA | K04, K11 chỉ hỗ trợ mô tả handoff | Không nguồn nào cung cấp authentic pair, session/revision/custody/freshness |
| W4 I01–I05 | K03–K08, K11 hỗ trợ proposal/checklist | [Readiness](../../planning/w4-readiness-plan.md) vẫn blocked; không sửa runtime state/caller |
| W5 evaluation | K07, K10 | R4a trước attempt; raw; R4b độc lập; giữ oracle/gold/heldout riêng |
| W6 pilot / W7 training | Không mở công việc từ lần đọc này | Các điều kiện pilot/training và explicit scope giữ nguyên |

Prompt-Master là trách nhiệm intake/routing; Evidence-Synthesizer là trách nhiệm nguồn/review. Đây là mapping trách nhiệm tài liệu, chưa có record giao việc hay phiên agent mới. Các role khác chỉ nhận knowledge khi có relevance và consumer binding cụ thể.

## Nội dung không tiếp nhận hoặc cần sửa cách hiểu

| Finding | Nguồn / observation | Disposition trong bộ này |
|---|---|---|
| D01 — quyền S1 chưa xác định | S1 README L4 badge MIT trỏ repo khác; cây 10 file không có LICENSE | CATALOG_METADATA_ONLY, không copy/adapt template S1 vào active KB |
| D02 — năng lực model theo thời điểm | S1 README L10 có so sánh Claude/ChatGPT và context 100k | Không dùng cho chọn provider/model; cần nguồn chính thức khi có task quyết định |
| D03 — blanket autonomy/jailbreak/system prompt copy | S1 README có AutoGPT, DAN, jailbreak và phần tự nhận system/tools Claude Code | Không adopt bypass, authority hoặc tool schema từ các section này |
| D04 — yêu cầu scratchpad/inner monologue | S1 MetaPrompt chứa instruction xuất reasoning nội bộ | Không lưu/đòi private reasoning; chỉ ghi facts, quyết định và source locator |
| D05 — popularity/discovery | S2 dùng badges, star order; có link tới cả system prompt collections | Chỉ metadata để tìm nguồn; không chứng minh đúng/quyền/relevance, không theo link tự động |
| D06 — self-score/JSON đẹp | S3 chaining dùng điểm model để thoát loop; output chapter có self-validation | Không dùng tự điểm hoặc parse làm gate; cần exact criterion/evidence project |
| D07 — skill bảo đảm expertise | S3 chapter 25 mô tả skill làm agent thành chuyên gia tức thời; chapter 26 nêu skill không train/bảo đảm expertise | Ghi tension, không kế thừa claim bảo đảm. Chỉ nhận cách đóng gói/tra cứu có giới hạn |
| D08 — stateless tuyệt đối và RAG bảo đảm đúng | S3 context chapter dùng mô tả giản lược về memory/RAG | Chỉ nhận yêu cầu kiểm context thực đã load; không phủ nhận memory do ứng dụng quản lý hay bảo đảm RAG đúng |
| D09 — quality score heuristic | S3 quality/index.ts dùng độ dài, regex tiếng Anh, dấu ngoặc và trọng số hình thức | Không tích hợp làm oracle chất lượng/đúng; chưa kiểm phù hợp tiếng Việt và semantics |
| D10 — compile không fail khi thiếu biến | S3 variables/index.ts L277–298 giữ placeholder gốc khi thiếu value/default | Quan sát tĩnh; proposal cần check biến thiếu riêng, không khẳng định library có strict validation |
| D11 — instructions/tool list không là kết nối thật | S3 prompt-manager/lookup mô tả MCP, lưu/improve prompt | Không cài/chạy; dùng như metadata tham khảo, không đưa dữ liệu project lên dịch vụ |

Các giới hạn D07/D08 là đánh giá cách áp dụng từ các đoạn nguồn, chưa là kết quả benchmark. Các link tài liệu nghiên cứu/provider nằm trong nguồn được giữ là chưa mở; không viện chúng làm primary evidence đã đọc.

## Trạng thái sau trích xuất

Đã có 12 candidate card, navigation, source catalog và ví dụ retrieval. Self-review đã đối chiếu nguồn/giới hạn; independent review, G2 admission, TRANSFER evaluation, consumer ACK và runtime đều chưa thực hiện. G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; P1K B4 FAIL; v3 OFF.

Bước tiếp theo nếu được giao nhánh dùng knowledge: chọn một consumer và một objective; chuẩn bị exact bundle/context binding và review packet theo contract hiện hữu. Chưa tự dispatch hoặc đóng gate từ lần đọc này.
