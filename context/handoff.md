# Bàn giao và tiếp tục phiên

Đọc [current.md](current.md) để biết trạng thái, [work queue](../docs/planning/work-queue.md) để biết nhánh tiếp theo và [source map](../docs/reference/source-map.md) để mở đúng nguồn. Trang này quy định cách ghi bàn giao ở lớp tài liệu; không thay schema checkpoint/handoff của runtime.

## Đã bàn giao từ lượt IA

- Entry cho AI, context ngắn, bản đồ phase/role/nguồn và thứ tự đọc theo task.
- Ba tài liệu chủ đề được chuyển nguyên byte sang thư mục đích; đường dẫn cũ vẫn dẫn tới bản mới.
- Stack/protocol, nguyên lý, gates, source code và evidence gốc được giữ theo preservation/custody checks.
- Gap về worksheet local, consumer admission, B4 và integration được ghi cụ thể, không giải quyết bằng đổi tên folder.

Xem [bản ghi thay đổi IA](../docs/changes/2026-10-21-information-architecture.md) để biết phạm vi kiểm tra. Tình trạng xuất bản kiểm bằng Git commit/remote hiện có; không suy từ nội dung một checklist lịch sử.

**Bổ sung W4 ngày 21/10/2026:** đọc [readiness/gap register](../docs/planning/w4-readiness-plan.md). Run42 là W4 plan offline; I05 run43 là non-target preparation; run44 reconcile runtime blocked. I01–I04 chưa đủ điều kiện. Gate G4 aggregate `NOT_RUN`, W4 readiness `NOT_RUN_BLOCKED`; cả hai chưa PASS. Hai concern state là finding tĩnh. Không dispatch template hoặc sửa source trong lượt tổ chức này.

Bổ sung lượt knowledge 21/10/2026: đọc [knowledge index](../docs/knowledge/README.md), rồi chọn card bằng retrieval guide. Ba nguồn đã pin; 22 file snapshot local, 12 card và 11 disposition. S1 chỉ catalog metadata vì rights UNKNOWN. Đây là self-reviewed reference, chưa independent review, admitted KB, consumer ACK, TRANSFER evaluation hoặc runtime. Khi muốn dùng cho consumer phải kiểm exact bundle/context/digest và prerequisite hiện hữu; không ingest lại corpus hoặc tự dispatch.

## Mẫu ghi cuối phiên

Bàn giao riêng nhánh office 3D ngày 22/10/2026: [Muse takeover](../docs/onboarding/muse-takeover-2026-10-22.md) và [manifest exact inputs](../metadata/muse-knowledge-transfer-2026-10-22.json). Dùng trạng thái candidate/review được dẫn ở đó; các snapshot IA phía trên giữ mốc lịch sử. Clone public không chứa workspace cha.

Sau recheck gate cùng ngày, điểm vào hiện hành là [Muse roadmap guide](../docs/onboarding/muse-roadmap-guide-2026-10-22.md), [gate report](../docs/proposals/agent-office-3d/gate-recheck-2026-10-22.md) và [manifest v2](../metadata/muse-knowledge-transfer-2026-10-22-v2.json). Manifest v1 giữ binding với commit xuất bản `155866c9077315433bd3f0a11021ab874b2b7a93`; không repin nó theo checkout mới.

Ghi record mới trong thư mục công việc được task cho phép; report đã freeze dùng revision mới. Khi được phép công khai một record bàn giao, đặt trong `docs/changes/` theo ngày và chủ đề. Không đặt raw/target/private-data vào đây.

```text
Objective và phạm vi đã được giao:
Nguồn đã đọc: path / revision / digest hoặc locator; phần chưa truy cập:
Artifact đã tạo/thay đổi và revision:
Đã hoàn thành trong phạm vi:
Thiết kế / code / execution / review: ghi riêng, chưa chạy ghi NOT_RUN
Kiểm tra đã chạy: command / kết quả / receipt; giới hạn kết luận:
Gate giữ nguyên hoặc thay đổi có exact evidence:
Vấn đề chưa rõ, dependency và điều kiện mở lại:
Một next atomic task đề xuất: owner / input / output / acceptance / budget
Trạng thái proposal hoặc dispatch và quyền tương ứng:
Git commit / branch / remote nếu có:
```

Trước resume: kiểm nguồn có drift, context/IDB revisions và các consumer ACK liên quan theo contract gốc. View IA không tự chuyển task sang READY. Thiếu nguồn chỉ chặn claim/nhánh phụ thuộc; tiếp tục phần độc lập đúng scope.

## Bàn giao cải tiến nền tảng — 23/10/2026

Đọc [proposal](../docs/proposals/knowledge-foundation/README.md), [reuse map](../docs/proposals/knowledge-foundation/reuse-map.md), [guide](../docs/proposals/knowledge-foundation/operating-guide.md) và [progress](../docs/proposals/knowledge-foundation/progress.md). Source pins mới nằm trong metadata; manifests lịch sử giữ nguyên. Bản này là document foundation; chưa triển khai consumer admission hoặc runtime. Publication xác định từ Git commit/remote, không từ checklist.

## Bàn giao policy knowledge revision 2

Đọc [knowledge policy v2](../docs/knowledge/knowledge-policy-v2.md) trước khi áp disposition v1. Không lập topic blacklist cho DAN hoặc kiến thức tương tự. Bản v1, source pins, REA–IDA artifacts và FAIL giữ lịch sử; [change record](../docs/changes/2026-10-23-neutral-knowledge.md) ghi điều chỉnh.

## Handoff input support — 24/10/2026

Đọc [packet](../docs/proposals/input-support-gates/packet.md), [benchmark plan](../docs/proposals/input-support-gates/benchmark-plan.md) và [status](../docs/proposals/input-support-gates/status.json). Scope offline, provider/target/fixture calls mới bằng 0. Ground truth seeds giữ local ngoài active KB, chưa review độc lập. Cần user chốt criteria/threshold và scope source-only benchmark trước khi mở nhánh mới.

## Handoff sau bounded pentest

Xem [report](../docs/proposals/input-support-gates/pentest-2026-10-24.md) và [status v2](../docs/proposals/input-support-gates/status-v2.json). Ưu tiên candidate revision sửa missing import ROLE_SCOPE rồi review/retest trước forged-decision probes. Giữ runner/oracle/freeze/attempt histories; không thêm attempt dưới acceptance cũ.

## Handoff sau sửa candidate

Ưu tiên sửa ở đoạn trước đã được thực hiện trong [revision mới và biên bản](../docs/proposals/input-support-gates/repair-2026-10-24.md):42/42 bounded case match, review trước/sau độc lập theo session. [Status v3](../docs/proposals/input-support-gates/status-v3.json) kế thừa50/50/0/0 criteria. Tiếp tục từ local `src/candidates/revision_2/`, giữ gốc freeze nguyên byte; public có hai patch reviewable. Next là packet tích hợp một caller đúng dependency, chưa dispatch hoặc bật W4; authentic source/authority/knowledge ACK vẫn thiếu. Automation 10h không được tạo trong phiên này.

## Handoff sau cuộc họp phân kỳ sản phẩm

[Sổ chờ18 tiêu chí](../docs/proposals/input-support-gates/checkpoint-roadmap-2026-10-24.md) ghi chỉ thị mới: giữ phần chưa giải quyết/cần sản phẩm ở trạng thái chờ, mở từng mục khi có objective/caller/consumer và prerequisite tương ứng. [Mẫu pilot](../docs/proposals/input-support-gates/product-pilot-template.json) chưa dispatch được. Không coi “next packet” ở handoff trước là lệnh chạy ngay. Chưa có sản phẩm thì không gọi provider/target hoặc rerun fixture để tăng phần trăm. Không tạo lịch tự mở lại; status v3, frozen FAIL và gate gốc giữ nguyên.

## Handoff sau thực thi cải thiện offline

Lệnh sau cuộc họp đã cho phép task offline riêng: xem [report](../docs/proposals/input-support-gates/offline-improvement-2026-10-24.md)/[status v4](../docs/proposals/input-support-gates/status-v4.json). A3 được verify theo seedr2/review exactdigest; A5/A6 chưa nhận. Checker local `src/candidates/revision_3/` là hardening readback fixed bundle; role_router/prompt_contract vẫn revision2, không product integration.39case mới không gộp thành benchmark với42case cũ; timeout fault injection và hostile symlink/race chưa kiểm. Còn17 tiêu chí chờ, scope/gate runtime giữ nguyên; mọi attempt sau cần review/dispatch mới.
