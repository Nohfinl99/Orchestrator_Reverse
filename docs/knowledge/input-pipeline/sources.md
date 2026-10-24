# Nguồn và giới hạn

## Nguồn chính

**Palo Alto Networks. _Securing GenAI: A Comprehensive Report on Prompt Attacks: Taxonomy, Risks, and Solutions_.** Whitepaper, ©2025, 34 trang.

- [Trang whitepaper chính thức](https://www.paloaltonetworks.com/resources/whitepapers/prompt-attack).
- [Bản giới thiệu chính thức của Unit 42](https://unit42.paloaltonetworks.com/new-frontier-of-genai-threats-a-comprehensive-guide-to-prompt-attacks/).
- SHA-256 của PDF đã phân tích: `b250ca8a780dd07517b578766522e5d1b53a45e351a2221d64d019c3bd822ec3`.

Digest định danh đúng file đã đọc; không khẳng định bản tải từ website hiện tại giống từng byte. Ngày tạo trong metadata không được dùng thay ngày xuất bản nghiên cứu. Danh sách tác giả nằm ở trang33; metadata author không thay danh sách này. Tài liệu là whitepaper của nhà cung cấp; chưa có căn cứ trong hồ sơ đọc để gọi là nghiên cứu đã peer review.

[Provenance metadata](../../../metadata/pipeline-knowledge-source-pins.json) ghi source identity, locator và digest của hồ sơ phân tích local. Đây là metadata tài liệu; không là chữ ký, runtime schema hoặc consumer admission.

Bộ public này chỉ phân phối diễn giải tuyển chọn và locator. PDF, extraction, hình render, raw, payload, oracle và receipt cục bộ không nằm trong bộ tài liệu này. Việc tham khảo không tự tạo quyền sao chép/phân phối nguồn, training hoặc consumer admission.

## Trang dùng cho sáu điểm

| Trang | Nội dung được dùng | Phạm vi diễn giải |
|---|---|---|
| 7–13 | Component exchanges, agent memory/tool risks, impact/technique/delivery taxonomy | Định vị bề mặt và ranh giới; chưa chứng minh enforcement |
| 17–20 | Cách tương tác nhiều lượt và thay đổi ngữ cảnh/mục tiêu | Gợi ý câu hỏi về lineage/intent; không coi roleplay hoặc giọng văn là attack mặc định |
| 20–22 | Obfuscation, encoding, ngôn ngữ, knowledge poisoning | Cần phân biệt biểu diễn với ý định; original/diff là suy luận thiết kế của dự án |
| 23–25 | Hướng dẫn detection, output/memory/tool risks và ví dụ incident | Guidance/incident do tác giả thuật lại; chưa tái lập incident hoặc đo sản phẩm |
| 28–30 | Appendix kết quả trên CyberSecEval, Tensor Trust, HackAPrompt | Số liệu susceptibility tác giả báo cáo; chưa là benchmark của Orchestrator |
| 31–34 | Bibliography, authors và thông tin nhà cung cấp | Kiểm xuất xứ/claim; bibliography chưa được đọc và tái xác minh toàn bộ |

Các phần trên đã được đọc theo phạm vi liên quan. Bảng taxonomy trang12–13 và bảng số liệu trang29–30 được đối chiếu trực quan. Không tuyên bố đã kiểm mọi hình, từng incident hoặc mọi nghiên cứu được dẫn.

## Không suy rộng số liệu hoặc hiệu quả

Table2 trang12–13 có **35 dòng cách tiếp cận hiển thị**, do reviewer đếm 14+13+7+1 theo bốn họ. Đây không phải 35 trials, 35 rule chặn hoặc bằng chứng coverage đầy đủ. Impact, technique family và direct/indirect delivery là các trục khác nhau; một trường hợp có thể mang nhiều nhãn.

Appendix trang28–30 cho biết tên ba dataset, có tám cột model ẩn danh và các tỷ lệ phần trăm. Phần này không cung cấp đủ sample N, exact model/version, settings, judge, retry cap hoặc raw mỗi ca để tái lập kết quả. Không lấy các tỷ lệ đó làm efficacy, xác suất thành công hoặc threshold của pipeline dự án. Các tuyên bố bảo vệ sản phẩm ở trang24–27/34 là claim nhà cung cấp, không phải kết quả kiểm độc lập trên Orchestrator.

## Quan hệ với contract dự án

[Sáu điểm thiết yếu](essentials.md) tách quan sát từ bài với action/evidence đề xuất. Giữ [knowledge trung lập](../knowledge-policy-v2.md): DAN và chủ đề tương tự được catalog/nghiên cứu theo objective; admission, rights, authority và consumer ACK được xét riêng. REA–IDA, sáu identity và gate hiện hữu do nguồn project quyết định. Đọc whitepaper không thay các contract đó, không chứng minh REA capture hoặc pipeline protection đã chạy.
