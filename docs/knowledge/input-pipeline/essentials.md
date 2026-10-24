# Sáu điểm thiết yếu cho input pipeline

Đây là bản tuyển chọn để **soạn proposal**, chưa là control đang chạy. Nguồn chung là whitepaper Palo Alto Networks, *Securing GenAI: A Comprehensive Report on Prompt Attacks: Taxonomy, Risks, and Solutions*; [sources.md](sources.md) ghi official URL, SHA-256 và giới hạn. Locator dưới đây dùng số trang PDF.

**Quan sát từ nguồn** thuật lại nội dung bài. **Hành động đề xuất** và **Evidence cần có** là suy luận thiết kế kết hợp contract của dự án; bài không chứng minh hiệu quả những control này trên Orchestrator. Các ID tham chiếu [bốn checkpoint](../../proposals/input-support-gates/README.md) giúp chọn câu hỏi review, không phải kết quả nghiệm thu.

## 1. Giữ ranh giới nguồn và chỉ thị

**Quan sát từ nguồn:** Dữ liệu RAG/tài liệu có thể chứa chỉ thị đổi mục tiêu; memory cũng là một bề mặt tác động (tr. 9–10, 12).

**Hành động đề xuất:** Gắn source type, locator, revision và digest. Nội dung trích từ tài liệu, tool hoặc memory giữ vai trò dữ liệu, không tự sửa task hoặc cấp quyền.

**Evidence cần có:** Ca nguồn có chỉ thị chuyển mục tiêu và ca nghiên cứu trích cùng nội dung; raw cho thấy task thật được giữ, không có action ngoài scope.

**Tiêu chí liên quan:** A2/A3; C1/C3/C6.

## 2. Theo dõi ý định xuyên lượt

**Quan sát từ nguồn:** Goal hijacking có thể đổi mục tiêu; các cách tương tác nhiều lượt được mô tả ở tr. 17–20.

**Hành động đề xuất:** Giữ objective/scope và lịch sử quyết định. Theo contract dự án, khi có material ambiguity hỏi tối đa 2–3 câu; bind câu trả lời vào revision mới.

**Evidence cần có:** Ca rõ hoàn thành đúng scope; ca thiếu thông tin dừng phần phụ thuộc và hỏi đúng; phân biệt user đổi mục tiêu hợp lệ với nguồn giả yêu cầu đổi mục tiêu.

**Tiêu chí liên quan:** A1; C2/C4/C5/C6.

## 3. Giữ original khi chuyển đổi

**Quan sát từ nguồn:** Encoding, ngôn ngữ, ký tự và biểu diễn khác có thể mang nội dung cần phân tích; các ví dụ ở tr. 20–22 cần xét theo ngữ cảnh.

**Hành động đề xuất:** Lưu original trước decode, translation hoặc normalization; tạo derived view có parent/digest và diff. Không đổi thuật ngữ để che mục tiêu. Không chặn chỉ vì DAN, roleplay, encoding hoặc ngôn ngữ.

**Evidence cần có:** Original readback khớp digest; tìm được lineage của derived view; benign controls cùng format/ngôn ngữ vẫn có output hữu ích; review diff giữ nghĩa.

**Tiêu chí liên quan:** C2/C4/C6.

## 4. Kiểm quyền tại nơi thực hiện action

**Quan sát từ nguồn:** Tool/function và infrastructure có thể bị tác động qua nội dung model xử lý (tr. 9, 11, 25).

**Hành động đề xuất:** Executor kiểm actor/action/resource/parameters, quyền và budget từ record phù hợp. Caller/model flag không tự là quyền. Với native work, giữ REA–IDA ownership và applicable pair/state/consumer ACK.

**Evidence cần có:** Positive action đúng scope; ca vượt scope dừng tại executor; trace tách attempted call khỏi completed side effect. Authority receipt và applicability được review riêng.

**Tiêu chí liên quan:** C1/C3/C6; D3.

## 5. Theo dõi output và memory write

**Quan sát từ nguồn:** Bài đặt rủi ro ở trao đổi giữa component, memory, knowledge sources và output (tr. 7–9, 22–25).

**Hành động đề xuất:** Trước side effect, đối chiếu output destination và proposed memory delta với contract; giữ provenance. Admission phải bind bundle/consumer/use, không lấy reference làm ACK.

**Evidence cần có:** Dummy canary chỉ xuất đúng output contract; memory delta có record và quyền; source không tự tạo admission/ACK; ca hợp lệ vẫn hoàn thành task.

**Tiêu chí liên quan:** B4/B5/B6; C6; D4/D5.

## 6. Đo utility cùng boundary violations

**Quan sát từ nguồn:** Appendix dùng các dataset đánh giá nhưng thiếu nhiều chi tiết tái lập trong PDF (tr. 28–30).

**Hành động đề xuất:** Thiết kế cả ca adversarial và benign controls cùng chủ đề/ngôn ngữ/format. Tách gold labels, predictions và trace; freeze expected behavior trước run, review độc lập sau raw.

**Evidence cần có:** Báo n/N cho correctness, false refusal, attempted/completed violation và intent/citation preservation; ghi riêng setup/tool/timeout/UNKNOWN. Positive baseline phải thành công, không coi từ chối mọi thứ là đạt.

**Tiêu chí liên quan:** A3; C6; D1–D6.

## Contract dự án cần kế thừa

Original/digest/diff, clarification 2–3 câu, scoped authority, budget, independent review và REA–IDA pair là yêu cầu hoặc đề xuất triển khai của dự án; chúng không phải một implementation do PDF cung cấp. [Kiến trúc](../../architecture/system.md), [knowledge protocol](../../../prompt_stacks/protocols/knowledge_protocol.md) và [pair protocol](../../../prompt_stacks/protocols/pair_protocol.md) quyết định cách áp dụng.

Sáu điểm trên giữ trạng thái **CANDIDATE_REFERENCE_NOT_ADMITTED**, chưa có consumer ACK hoặc pipeline implementation từ bộ tham khảo này. Chúng không tạo schema, role, tool permission hoặc runtime admission mới. Candidate/hash checker chỉ kiểm predicate trong scope riêng; không thay đánh giá ngữ nghĩa hay authentic authority. Tiêu chí, threshold và các gate chỉ đổi khi có evidence/decision đúng contract.
