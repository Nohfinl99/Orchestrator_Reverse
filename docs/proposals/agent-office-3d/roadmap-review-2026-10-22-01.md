# Biên bản review roadmap và quyết định điều phối

| Trường | Giá trị |
|---|---|
| Review ID | `AGENT_OFFICE_ROADMAP_REVIEW_20261022_01` |
| Roadmap | `AGENT_OFFICE_PRODUCT_ROADMAP_01`, revision 1 |
| Loại | `FEASIBILITY_DEBATE / MULTI_REVIEWER` |
| Phạm vi | Thứ tự phase, feasibility, acceptance, differentiation, dependencies |
| Kết quả | `CONDITIONAL_GO_AO0_TO_AO4 / BLOCKED_AO5_AO6` |
| Dispatch/code | `NO_RUNTIME_DISPATCH / NO_IMPLEMENTATION` |

## Câu hỏi

Có thể đi từ đề xuất văn phòng 3D tới sản phẩm chạy thật bằng roadmap nào, và phần nào được phép bắt đầu trong trạng thái hiện tại?

## Các luận điểm

### Luận điểm kiến trúc

Xây theo chuỗi contract/event trước, visual offline sau, robustness rồi mới bridge/control. Event log là nguồn xác thực; scene là projection. Nếu avatar chạy ngay lúc command gửi thì UI làm lẫn intent với receipt. Nếu không có source/caller binding, live integration không có cơ sở.

### Luận điểm feasibility

Offline fixture/replay khả thi và phù hợp trạng thái tài liệu hiện nay. Runtime dispatch chưa implement, W4 `NOT_RUN_BLOCKED`; do đó live observation/control không thể là phần nối tự động sau prototype. Cần producer/caller, authority, budget, event binding và prerequisite/gates cụ thể.

### Luận điểm product/UX phản biện

Không nên xây đầy đủ văn phòng trước khi biết 3D giúp tác vụ nào. 3D cần so với timeline/bảng 2D bằng cùng scenario; nếu không cải thiện tìm blocker, trạng thái họp, evidence/decision hoặc gây thêm nhầm lẫn thì giữ giao diện thường và dừng mở rộng scene.

## Phản biện và cách giải quyết

| Đề xuất / lo ngại | Phản biện | Quyết định |
|---|---|---|
| Tạo văn phòng 3D hoàn chỉnh để thể hiện ý tưởng ngay | Có nguy  tcơ ưu tiên animation hơn trạng thái đúng, đầu ra và giárị UX | Chỉ làm vertical slice nhỏ sau AO-1; timeline/panel 2D là fallback và đối chứng |
| Bắt đầu từ bảng offline rồi chuyển sang agent thật | Demo dễ bị tưởng là live; offline schema chưa có quyền/producer | `SIMULATED` badge, event provenance, source binding; AO-5/AO-6 cần quyết định/contract riêng |
| Họp agent phải tạo consensus cuối | Consensus có thể che dissent, thiếu evidence hoặc lặp ý kiến | Synthesis bắt buộc agreement/dissent/open questions/unsupported claims; quyết định và approval là hai trạng thái riêng |
| Chốt lịch triển khai ngay | Chưa có owner codebase, capacity, budget, tech spike, baseline UX | Điều phối theo deliverable/exit; lịch và estimate để trống cho tới khi có dữ kiện |
| Mở tất cả sáu role cho mọi task | Không đúng capability/dependency, tạo overhead và giả cảm giác phối hợp | Chọn role phù hợp cho từng node; giữ sáu identity, không tạo alias/identity mới |

## Đánh giá khả thi

| Nhánh | Kết luận | Vì sao |
|---|---|---|
| Scenario, contract và offline fixtures | **GO có điều kiện** | Tài liệu hiện có đã xác định state/event semantics và acceptance đề xuất; cần AO-1 packet cụ thể được review trước code |
| 3D offline vertical slice | **GO sau AO-1** | Repo công khai cho thấy phần visualization/animation có tiền lệ; chưa có implementation trong workspace |
| Replay/error integrity | **GO sau AO-2** | Tiêu chí có thể quan sát bằng fixtures; execution chưa chạy |
| Giá trị UX/khác biệt | **CHƯA XÁC THỰC** | Reddit và README là tín hiệu/claim; cần thử nghiệm so sánh 3D với timeline thường |
| Read-only live bridge | **BLOCKED / FUTURE** | Chưa có producer/caller/permission/event binding được chấp thuận |
| Command/control thật | **BLOCKED / FUTURE** | Cần authority, broker, budget, receipt, security review và prerequisites/gates project gốc |

## Quyết định họp

**Chấp thuận roadmap theo điều kiện cho AO-0–AO-4; chưa chấp thuận runtime AO-5/AO-6.** Bước điều phối kế tiếp là soạn `AGENT_OFFICE_OFFLINE_REPLAY_PACKET_01`, không viết UI ngay. AO-2 chỉ mở sau khi AO-1 packet được review; AO-4 cần so sánh UX trước khi đầu tư thêm. Không ấn định ngày hoặc ngân sách khi còn thiếu owner/capacity/budget.

## Điều kiện bất biến

- Sáu identity, REA–IDA principle, phase/gate và lịch sử FAIL giữ nguyên.
- Product roadmap AO-0…AO-7 là mã cục bộ; không thay R0–R6, W0–W7 hay G1–G4.
- Gate hiện hành: P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF`.
- Review này là recommendation, không phải receipt của runtime Orchestrator, không dispatch task và không chứng minh implementation/market fit.

## Reviewer inputs

Đã thu thập review riêng về (1) kiến trúc/sự kiện, (2) dependencies và feasibility theo gate, (3) product differentiation/usability. Các reviewer đều không sửa code, không chạy test/fixture/provider/runtime. Quyết định này hợp nhất các nhận định; người điều phối project vẫn là người chấp thuận mở task tiếp theo.
