# Điều chỉnh knowledge trung lập, bảo toàn REA–IDA

Chỉ thị trực tiếp của người dùng ngày 23/10/2026: không xóa nội dung REA–IDA qua các vòng, không giới hạn chủ đề như DAN hoặc kiến thức tương tự, thực hiện điều phối và upload lại GitHub. Baseline `818dbd5c2bcaaddb181e84a51c70daa4601ca5db` trên nhánh `codex/knowledge-foundation-revision` / PR #2.

## Thực hiện

- Thêm [knowledge policy revision 2](../knowledge/knowledge-policy-v2.md): tiếp nhận DAN/jailbreak/AutoGPT và các chủ đề tương tự như kiến thức có thể catalog, đọc và nghiên cứu; không có topic blacklist.
- Giữ D01–D11 và application-map revision 1 nguyên bytes làm lịch sử; policy v2 diễn giải lại từng ID theo topic-neutral selection, claim/evidence/uncertainty và application checks. Source pins, quyền và raw lịch sử không bị sửa.
- Cập nhật entry knowledge/retrieval, AGENTS, context/handoff và foundation guidance để đọc policy v2 trước khi áp dụng disposition cũ. Ghi mâu thuẫn cách hiểu topic exclusion vào sổ vấn đề thay vì xóa lịch sử.
- REA–IDA ownership, tám boundary, original principles, mười stack/protocol và phase/gate được bảo toàn; catalog/research không tự chuyển thành authority hoặc runtime ACK.

## Tiến độ và kiểm

Đã viết policy và hướng dẫn hiện hành; chưa ingest thêm corpus, gọi model/target/provider hoặc chạy fixture nghiệp vụ. Đây là phiên producer/self-review, chưa có review độc lập. Read/hash/navigation/preservation và diff checks được dùng trước publication; kết quả thực tế được báo ở cuối phiên và receipt local. Publication xác định bằng commit/remote của nhánh, không suy từ trang này.

Next task: chọn một objective và nguồn cần đọc, lưu selected items/claim/evidence/unknowns theo worksheet; tiếp tục consumer compatibility proposal hiện có khi đủ source/prerequisite. Không tạo ACK hoặc runtime acceptance thay consumer.
