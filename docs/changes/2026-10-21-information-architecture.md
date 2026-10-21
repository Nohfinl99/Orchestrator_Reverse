# Tái tổ chức IA — 21/10/2026

Yêu cầu: giúp AI nhận nhanh mục tiêu, phase, tiến độ, nguồn có thẩm quyền và bước tiếp theo; giữ nguyên các nguyên lý, nội dung và yêu cầu phase. Lượt này chỉ thay kiến trúc tài liệu/điều hướng, được người dùng yêu cầu commit và cập nhật repository GitHub hiện có.

## Thay đổi

- Thêm AGENTS, context/current/handoff và view JSON cho AI mới tiếp nhận.
- Tách onboarding, architecture, planning, reference, guides và change records theo câu hỏi cần trả lời; [docs index](../README.md) dẫn theo nhu cầu.
- Di chuyển ba trang chủ đề nguyên byte; giữ trang chuyển hướng ở đường dẫn cũ. Mười stack và mười protocol giữ nguyên tên, nội dung và bytes.
- Ghi source availability, thứ tự các report local, hai hệ phase, sáu role, work queue và các gap chưa được giải quyết.
- Thêm navigation/preservation/content manifests và verifier read/hash/link. Thêm Git attributes bảo toàn bytes của prompt thay vì chuyển CRLF khi checkout.
- Workspace cha có entry và local source map mới; archive, evidence, source/prototype, manifests và entry đã pin được giữ nguyên.

## Cơ sở và giới hạn

Đã đọc các entry, roadmap, phase stacks/protocols, kiến trúc/status/contribution, source mapping và report alignment/logic liên quan. Knowledge compiler của Reading Companion được đối chiếu theo Git blob ghi trong [IA](../architecture/information-architecture.md). Cây còn lại được kiểm kê/custody; không tuyên bố audit ngữ nghĩa từng dòng vendor hoặc mọi raw artifact.

Không thực thi workload nghiệp vụ, target/provider, training hoặc W4. Không có behavioral benchmark mới hoặc independent multi-agent acceptance trong lượt IA. Verifier chỉ kiểm lớp tài liệu và byte preservation; không thay R4a/R4b hoặc nâng gate.

Verifier workspace được bắt đầu trước sửa IA phát hiện một mismatch có sẵn ở README của archive local, thiếu dòng cuối so với pin; bản nguồn bên ngoài vẫn khớp pin. Receipt và observed digest được lưu ở workspace cha, file/pin không bị thay. Do đó không tuyên bố custody toàn workspace PASS; kiểm public độc lập với file local này.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Proposal consumer vẫn PROPOSED_NOT_DISPATCHED.

## Tái kiểm

Tại root repository public: `python -I -B scripts/verify_ia.py`. Verifier kiểm mọi file trong inventory, các nguồn được bảo toàn/di chuyển, links, navigation, phase IDs và gate view. Raw kết quả kiểm trong lượt bàn giao được giữ local ở workspace cha; clone public không được gọi là lossless copy của archive.

Xem [preservation manifest](../../metadata/preservation.json) để kiểm byte nguồn cũ và [source map](../reference/source-map.md) để biết phần không đóng gói. Handoff sau IA nằm ở [context/handoff.md](../../context/handoff.md). Git commit/remote là nguồn xác định trạng thái xuất bản.
