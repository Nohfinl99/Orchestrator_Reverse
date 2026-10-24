# Context hiện tại — snapshot 21/10/2026

Orchestrator_Reverse xây lớp điều phối reverse engineering theo goal, task DAG, identity hiện hữu, evidence và gate. REA sở hữu workflow/evidence/ledger; IDA sở hữu native/decompiler/IDB state. Xem [nguyên lý gốc](../CONTEXT_VI.md).

**Lượt công việc gần nhất:** đã trích xuất [12 knowledge card cho điều phối](../docs/knowledge/README.md) từ ba nguồn GitHub, có source pins, WHAT/WHY/HOW, retrieval và giới hạn; đây là candidate reference, chưa admitted KB/ACK. [W4 readiness/gap register](../docs/planning/w4-readiness-plan.md) giữ runtime `NOT_RUN_BLOCKED`; I01–I04 không eligible ở run44, I05 chỉ verified non-target preparation. Nhánh nghiệp vụ tiếp theo vẫn là proposal consumer, chưa dispatch. Prompt/protocol chưa nối loader/runtime.

| Đã có | Giới hạn cần giữ |
|---|---|
| Mười stack và mười protocol offline | Hoàn thành tài liệu không phải hoàn thành W0–W7 hoặc 57 task cũ |
| Mapping sáu role và một projection consumer Triage | Chưa đồng bộ toàn hệ; Stage1 thực tế còn parse trực tiếp |
| Báo cáo logic và verifier custody v2 trong hồ sơ local | Verifier không chứng minh hành vi agent hoặc runtime |
| P1J bounded implementation, lịch sử 53/53 fixture | Kết quả hữu hạn trước IA, không phải test mới hoặc nghiệm thu toàn hệ |
| Navigation IA và chỉ dẫn bàn giao | Chỉ giúp tìm đúng nguồn, không tạo quyền/receipt/ACK |

## Gate kế thừa

| Gate | Trạng thái |
|---|---|
| P1K B4 | FAIL |
| G1 | INCOMPLETE |
| G2 | INCOMPLETE |
| G3 | NOT_RUN |
| G4 | NOT_RUN |
| W4 runtime | NOT_RUN_BLOCKED |
| v3 | OFF |

Nguồn: [validation snapshot gốc](../docs/reference/validation-status.md); locator report local được nêu trong [source map](../docs/reference/source-map.md). [project-state.json](project-state.json) là biểu diễn máy đọc của view này, không phải state machine thực thi. Chưa tái xác minh active REA/IDA session trong task IA.

## Việc tiếp theo

Đề xuất mới nhất là hoàn thiện packet cho **một consumer/call site cụ thể**, giữ `PROPOSED_NOT_DISPATCHED` đến khi có đủ input path/digest/revision, output, budget và acceptance. Selected-consumer projection đã có; không lập lại task như chưa làm. B4 correction là nhánh riêng trước implementation phụ thuộc.

Đọc [work queue](../docs/planning/work-queue.md) để chọn nhánh. Task IA hiện tại không tự dispatch các nhánh này. Các quyết định target/model/provider/numeric runtime budget và quyền pilot chưa được chọn thay người dùng.

## Khi đổi phiên

Đọc [handoff](handoff.md), kiểm scope và revision theo [source map](../docs/reference/source-map.md), rồi chỉ nạp stack/protocol cần thiết. Không lấy README lịch sử hoặc mtime làm bằng chứng trạng thái mới. Nếu chỉ có clone public, các report local chưa có được giữ là `LOCAL_ONLY`, không coi là đã đọc hay xác thực.

## Bổ sung tài liệu 23/10/2026

[Đề xuất cải tiến nền tảng](../docs/proposals/knowledge-foundation/README.md) đưa knowledge card có sẵn vào guide/worksheet; [progress](../docs/proposals/knowledge-foundation/progress.md) ghi việc đã viết và nhánh integration còn đề xuất. Đây là cập nhật documentation, không thay gate snapshot 21/10 hoặc tạo admission/ACK.

## Chỉ thị knowledge trung lập — 23/10/2026

[Policy revision 2](../docs/knowledge/knowledge-policy-v2.md) thay cách hiểu loại trừ chủ đề từ D01–D11: DAN/jailbreak/AutoGPT và các kiến thức tương tự được tiếp nhận để catalog/đọc/nghiên cứu theo objective. Giữ REA–IDA xuyên suốt revision, evidence và quyền thực thi theo task; không xóa lịch sử hoặc nâng gate.

## Input support theo checkpoint — 24/10/2026

Người dùng chọn chuẩn bị/verify packet offline và giao chọn model theo độ khó cho run tương lai. [Bốn checkpoint đề xuất](../docs/proposals/input-support-gates/README.md) có mẫu số cố định và [status](../docs/proposals/input-support-gates/status.json); criteria/threshold chờ user quyết định, chưa đóng gate dự án. Nguồn và raw lịch sử được recheck riêng; chưa có benchmark model mới.

## Bounded pentest bốn checkpoint — 24/10/2026

[Biên bản có execution](../docs/proposals/input-support-gates/pentest-2026-10-24.md): hai attempt có reviewer/executor riêng, final23/28case match; năm prompt-composition paths crash vì ROLE_SCOPE chưa import. [Status v2](../docs/proposals/input-support-gates/status-v2.json) vẫn50/50/0/0 criterion coverage; chưa closure hoặc model/REA runtime run.

## Sửa và kiểm lại candidate — 24/10/2026

[Biên bản sửa](../docs/proposals/input-support-gates/repair-2026-10-24.md) và [status v3](../docs/proposals/input-support-gates/status-v3.json): revision 2 sửa import, recompute eligibility/owner và structured evidence errors; suite mới42/42 có R4a/executor/R4b riêng. [Diff code](../docs/proposals/input-support-gates/patches/README.md) để review; bản gốc và FAIL vẫn giữ. Criterion coverage50/50/0/0; chưa caller integration, authentic ACK/authority hoặc model/target benchmark.

## Chỉ thị điều phối theo giai đoạn sản phẩm

[Cuộc họp và sổ chờ](../docs/proposals/input-support-gates/checkpoint-roadmap-2026-10-24.md) giữ18 tiêu chí chưa đóng, có owner/evidence/điều kiện mở lại. Ưu tiên hiện hành là bảo toàn baseline và dùng [mẫu pilot](../docs/proposals/input-support-gates/product-pilot-template.json) khi bắt đầu một caller/consumer sản phẩm thật; không tiếp tục cố đóng checkpoint bằng fixture hoặc hồ sơ giả. Coverage và gate giữ nguyên. Lượt họp chỉ lập kế hoạch, không test hoặc code mới.

## Thực thi phần offline theo chỉ thị sau cuộc họp

[Báo cáo mới](../docs/proposals/input-support-gates/offline-improvement-2026-10-24.md) mở lại A3 và checker hardening riêng:6/6seed revision2 được review độc lập,39/39case checker mới có capture/review riêng. [Status v4](../docs/proposals/input-support-gates/status-v4.json) là view mới nhất nhánh input-support: **A4/6=66,67%,B3/6=50%,C/D0/6**, còn17 tiêu chí chưa đóng. A5/A6 và product-dependent work vẫn chờ; không có model/REA/IDA/target runtime call hoặc thay gate dự án.
