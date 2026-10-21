# Vấn đề mở và giới hạn bằng chứng

Sổ IA dẫn lại vấn đề đã có nguồn; không là quyết định sửa logic, exploit report hoặc kết quả runtime mới. Phạm vi nguồn trong [source map](source-map.md).

| ID | Vấn đề / căn cứ | Cách xử lý hiện tại / điều kiện mở |
|---|---|---|
| IA-01 | README/status của workspace bàn giao 20/10 được giữ pin, còn CURRENT/NEXT/LOGIC_REVIEW bổ sung sau | Entry mới dẫn theo dependency report; không sửa lịch sử để làm đồng nhất |
| IA-02 | Overlay public nhắc source_pins/worksheets chưa đóng gói public | Ghi LOCAL_ONLY; chưa thể xác minh các binding chỉ bằng clone; phân phối thêm cần phạm vi/quyền riêng |
| IA-03 | “Current phase” có W0–W7, R0–R6 và gate P1/G | Giữ ba hệ; phase map mô tả progress theo artifact/dependency, không quy đổi |
| IA-04 | Verifier workspace chạy trước sửa IA phát hiện README trong archive local lệch pin một dòng cuối; nguồn gốc bên ngoài vẫn khớp pin | Lưu receipt local, không sửa file hoặc repin trong task IA; custody toàn workspace chưa PASS. Gói public không chứa file này |
| TECH-01 | P1K B4 oracle scalar-encodable không nhất quán catalog; docs local project-status/development | Giữ FAIL; correction candidate mới + independent review trước implementation phụ thuộc |
| TECH-02 | Consumer proposal thiếu input/digest/revision/output/budget để admission; logic review F4 | Giữ PROPOSED_NOT_DISPATCHED; hoàn thiện packet khi được giao |
| TECH-03 | Stage1 caller parse Triage trực tiếp; binding projection/logic review | Chọn consumer thật; training không tự thay parser, không ngầm nối LLM |
| TECH-04 | Context/authority/pair/knowledge admission và ACK chưa đầy đủ; agent alignment | Cần projection/validation và consumer receipts thực theo phạm vi |
| TECH-05 | Crypto conditional chưa khớp fixed SOP; Product executable dispatch chưa map | Giữ UNRESOLVED, proposal compatibility riêng, không đổi identity/routing trong IA |
| TECH-06 | rev/revision và RETRY/caller-halt compatibility còn mở | Source repair/proposal riêng; fixture nghiệp vụ cần R4a/R4b |
| TECH-07 | Không có authentic full-flow pair hoặc W4 run; gate snapshot | G3/G4 NOT_RUN, W4 NOT_RUN_BLOCKED, v3 OFF; active runtime/session chưa được kiểm lại trong IA |
| TECH-08 | Verifier cũ nhận manifest thiếu/rỗng; LOGIC_REVIEW đã có v2 | Workspace dùng v2 theo entry local; giữ code cũ có pin, không gọi custody là semantic acceptance |
| W4-01 | I01–I04 chưa đủ G1/G2/G3 hoặc model/budget prerequisite; G4 blocked trong run44 | Giữ I01–I04 ineligible và runtime NOT_RUN; xem [W4 gap register](../planning/w4-readiness-plan.md) |
| W4-02 | Template I01–I05 ghi A0/A1/A4; A0–A7 không phải identity đã đăng ký. State review ghi rev/revision, Verified/revalidation và RETRY/caller-halt mapping chưa được resolve | Không dispatch từ template hoặc tự đổi field/owner; source-map caller/state, compatibility và G1 review trước branch phụ thuộc |

Tài liệu fine-tuning chứa thông tin sản phẩm theo thời điểm đã ghi. Lượt IA giữ nguyên nội dung đó; mọi quyết định model/provider/eligibility mới phải kiểm lại nguồn chính thức khi có task liên quan.

Để thêm finding: ghi observation hay inference, exact source/version/locator, phần chưa truy cập, tác động, owner trách nhiệm và điều kiện đóng. Chỉ đóng khi có evidence/review đúng scope; tên folder, navigation PASS hoặc consensus không đủ.
