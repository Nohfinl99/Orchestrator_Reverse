# Bối cảnh dự án Orchestrator_Reverse

## Yêu cầu

Xây dựng một lớp điều phối có thể nhận yêu cầu cấp dự án, làm rõ mục tiêu/phạm vi/tiêu chí, phân rã thành tác vụ atomic, chọn đúng agent đã đăng ký, cấp context/evidence phù hợp, giữ checkpoint và lịch sử, rồi đánh giá kết quả để quyết định tiếp tục, retry, backtrack, chờ hoặc dừng.

Mục tiêu là hỗ trợ quá trình reverse engineering với hai engine trách nhiệm riêng. REA cung cấp workflow và evidence lifecycle; IDA cung cấp phân tích native/decompiler và database state trong capability thực tế. Không để routing, handoff, resume hoặc fine-tuning làm mất binding này.

## Nguyên tắc kiến trúc

1. **Giữ identity hiện hữu:** Prompt-Master, Triage-Sentinel, Decomp-Analyst, Crypto-Logic-Specialist, Evidence-Synthesizer và Product-Evolution-Architect. Tên role đề xuất không tự trở thành registry identity.
2. **Routing có điều kiện:** phân biệt integrity reject, gate/capability blocked, yêu cầu cần làm rõ, conflict cần review, no-match và unique eligible owner. Một owner duy nhất vẫn chưa đủ nếu thiếu prerequisite.
3. **Knowledge có nguồn:** mọi claim tri thức cần provenance, version, locator, rights, applicability và consumer ACK. Few-shot là ví dụ hành vi, không phải target fact.
4. **State có lịch sử:** giữ attempt bất biến, dependency revision, checkpoint, ngân sách retry và các node/ACK bị invalidation. Khôi phục bytes không tự chứng minh sửa được nguyên nhân logic.
5. **Đánh giá trước và sau attempt:** đóng packet R4a trước khi chạy để khóa case/oracle/input/environment/budget/capture. Thu raw output rồi reviewer độc lập làm R4b.
6. **Không bịa kết quả:** `DESIGN_ONLY`, `NOT_RUN`, `BLOCKED`, `FAIL`, `PARTIAL` và `PASS` mang ý nghĩa riêng, phải gắn evidence tương ứng.

## Mô hình agent

Sáu role trên có nhiệm vụ chuyên biệt. Orchestrator là trách nhiệm điều phối. Debate và HITL là service/coverage slots có điều kiện, không mặc định là agent đã đăng ký. Tool allowlist hoặc prompt không tự cấp quyền; broker, validator và phê duyệt con người giữ enforcement.

## Phạm vi bản public

Thư mục này là một tài liệu nền có thể đọc độc lập. Nó tập trung vào bối cảnh, cấu trúc đích và Prompt Stack. Nó không kèm workspace snapshot, source archive đầy đủ, target data, database phân tích, credential, config cục bộ hoặc bản sao dependency bên thứ ba.

Mọi implementation mới cần source mapping và compatibility review. Mọi task phụ thuộc target execution cần pair REA–IDA authentic và các gate theo phạm vi. Training chỉ cân nhắc sau khi có lỗi hành vi đo được, dữ liệu được phép dùng, ground truth được review và evaluation set tách biệt.
