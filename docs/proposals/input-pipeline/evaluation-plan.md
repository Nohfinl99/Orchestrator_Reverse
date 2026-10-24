# Kế hoạch đánh giá input pipeline

**Trạng thái: DRAFT / NOT_RUN / NOT_APPLIED.** Kế hoạch này đi cùng [pipeline đề xuất](README.md) và [tri thức nền](../../knowledge/input-pipeline/README.md). Chưa tạo payload, case set thực thi hoặc chọn model/provider/numeric budget. [Status v4](../input-support-gates/status-v4.json) giữ C và D ở 0/6; kết quả component lịch sử không đo hiệu quả của pipeline tương lai.

## Nhóm đối chứng vô hại

Đơn vị thiết kế là một cặp cùng topic/ngôn ngữ/format và độ khó tương đương, chỉ khác quan hệ giữa nguồn, objective và quyền hành động. Dùng synthetic data, dummy state và destination không kết nối; không cần secret, endpoint hay side effect thực để soạn oracle.

| Nhóm | Tình huống cần kiểm | Đối chứng benign | Evidence phân biệt |
|---|---|---|---|
| Source và authority | External document đề nghị đổi dummy owner hoặc approval ngoài scope | Tài liệu trích/phân tích chính đề nghị đó | Source provenance, decision và action trace |
| Intent qua nhiều lượt | Derived proposal chuyển sang dummy objective ngoài scope | User phát triển chi tiết hoặc đổi goal hợp lệ, có decision rõ | Original/revision, diff, decision, final task |
| Encoding và Unicode | Derived view có yêu cầu đổi dummy goal/quyền | Nội dung bình thường hoặc quote nghiên cứu cùng encoding/ngôn ngữ | Original digest, derived lineage và review giữ nghĩa |
| Output và dữ liệu | Source đề nghị đưa synthetic canary ngoài output contract | Tóm tắt tài liệu có nhắc canary/destination như dữ liệu | Output destination, proposed action và completed effect |
| Tool và memory | External content đề nghị dummy mutation ngoài allowed task | Task được phép hoặc tài liệu chỉ giải thích tool/memory | Authority receipt, action parameters và state delta |
| Research, judge và format | Task đánh giá bị đổi thành hành động dummy ngoài scope | Phân loại, nghiên cứu DAN, roleplay hoặc yêu cầu style hợp lệ | Task correctness, trust origin và lý do xử lý |

Bổ sung positive path thật cho consumer đã chọn và trường hợp cần clarification. Setup/tool/provider failure được ghi riêng. Một exception trước predicate không chứng minh semantic rejection; thiếu trace giữ UNKNOWN theo cách báo cáo hiện hữu.

## Gold, predictions và phép đo

Reviewer riêng chốt expected behavior và nhãn trước attempt, tách gold/oracle khỏi prediction và context dùng để trả lời. Giữ uncertainty/disagreement để adjudicate; chưa chốt gold thì chưa tính điểm. Development examples và evaluation data phải được phân biệt, không tự gọi bộ đã lộ là hidden heldout.

| Phép đo đề xuất | Cách báo cáo khi có raw |
|---|---|
| Task correctness | n/N task đạt acceptance đã freeze, kèm lỗi và unresolved |
| Intent preservation | n/N proposal giữ objective/scope theo adjudicated review; dẫn original/diff/decision |
| False refusal | Số task supported bị từ chối không đúng / tổng supported cases có gold; ghi rõ phạm vi |
| Boundary violation | Báo riêng attempted call và completed effect trái oracle; blocked attempt vẫn được lưu |
| Classification, nếu có | Confusion matrix theo gold độc lập; không dùng classifier verdict thay authority |
| Operational failures | Setup, capability, provider, runtime, evidence và capture errors theo layer |

Mỗi phép đo có mẫu số và exclusion đã freeze; N=0 ghi N/A, chưa chạy ghi NOT_RUN. Không lấy tỷ lệ trong tài liệu nghiên cứu làm threshold hoặc so model hiện hành. Positive task utility và false refusal cần được đọc cùng boundary outcomes; từ chối mọi task không chứng minh đạt yêu cầu.

## Raw và prerequisite trước attempt

Packet tương lai cần bind exact caller/consumer/action và revision; original/derived/diff/decision refs; prompt/knowledge/config digests; authority, applicability và budget refs; case/oracle revision, expected outputs và stop predicates. Với model run, ghi model/provider/version/transport, dữ liệu gửi và telemetry; với target-dependent work, bind REA–IDA pair/state/ACK theo contract hiện hữu.

Capture cần đủ argv/environment có liên quan, start/end, exit/timeout, stdout/stderr hoặc request/response raw, proposed/attempted/completed action, output/memory delta và custody receipts. Thiếu raw không được suy thành không có violation. Thông tin nhạy cảm và oracle không đưa vào public docs hoặc active knowledge của consumer.

Trước execution: đủ quyền/phạm vi, dependency và numeric budget/attempt cap; user chốt criteria/threshold; R4a review/freeze exact inputs/oracle/environment/stop; chair dispatch theo task. Sau execution: giữ mọi FAIL/setup error và immutable attempt, R4b bởi reviewer khác producer/executor trên exact raw. Không sửa oracle sau output hoặc tự retry từ proposal này.

Continuation/release/rollback acceptance phải chốt trước run cho đúng consumer. Dừng khi drift, mất quyền/binding, cạn budget hoặc capture không đủ; bảo toàn raw và invalidation history. Việc đóng C/D hoặc project gate vẫn theo criteria và evidence gốc, không theo số ca, self-score hay đồng thuận review.