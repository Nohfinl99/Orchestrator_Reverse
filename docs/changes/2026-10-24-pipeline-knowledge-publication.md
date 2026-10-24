# Xuất bản tri thức pipeline và cập nhật README

Ngày24/10/2026. Người dùng yêu cầu upload phần trích tri thức, viết lại README và tạo tài liệu GitHub dễ tìm, giữ nguyên nguyên lý gốc.

## Thay đổi

- README mới có lối đọc theo nhu cầu, bảng6tri thức, checkpoint/status v4, kết quả component theo scope, nguyên lý REA–IDA, sáu identity và bản đồ folder.
- [Knowledge input pipeline](../knowledge/input-pipeline/README.md) gồm `essentials.md` và `sources.md`: giữ6điểm cần cho thiết kế, page/digest/official URL, phân biệt paper claim với suy luận/contract dự án.
- [Input pipeline proposal](../proposals/input-pipeline/README.md) và [evaluation plan](../proposals/input-pipeline/evaluation-plan.md): responsibility/boundary/gap, nhóm benign đối chứng, metrics và prerequisite; DRAFT/NOT_IMPLEMENTED/NOT_APPLIED/NOT_RUN theo từng trang.
- Mục lục, knowledge index, current/handoff, work queue và [navigation](../../metadata/navigation.json) dẫn vào các vùng trên. Route status hiện hành dẫn v4; v1–v3 và các report lịch sử giữ đường dẫn/bytes.
- [Mục lục proposals](../proposals/README.md) phân loại bốn nhánh và giới hạn của từng loại artifact khi mở folder trên GitHub.
- [Provenance metadata](../../metadata/pipeline-knowledge-source-pins.json) chỉ chứa source identity và giới hạn tài liệu, không là runtime schema hoặc consumer admission.

## Tổ chức thông tin

`docs/knowledge/input-pipeline/` trả lời “tri thức nào cần và từ đâu”; `docs/proposals/input-pipeline/` trả lời “thiết kế/đánh giá sẽ ra sao”; `docs/proposals/input-support-gates/` giữ criterion/status, kết quả đã chạy và code diff. Giữ canonical principle/system/protocol tại đường dẫn hiện hữu, không nhân bản contract hoặc di chuyển artifact đã freeze.

## Bảo toàn và giới hạn

REA giữ workflow/evidence/ledger; IDA giữ native/decompiler/IDB state. Giữ sáu identity, các hệ phase, applicable pair/state/consumer ACK, R4a trước attempt/R4b sau raw, policy knowledge trung lập và lịch sử FAIL. Không nhận knowledge/topic label làm authority, không coi named tools hoặc file hash là enforcement.

P1K B4 FAIL;G1/G2 INCOMPLETE;G3/G4 NOT_RUN;W4 NOT_RUN_BLOCKED;v3 OFF. [Status v4](../proposals/input-support-gates/status-v4.json) vẫn66,67/50/0/0 với17tiêu chí chưa đóng; việc viết README hoặc xuất bản knowledge không tăng các tỷ lệ đó.42/42component và39/39checker là kết quả lịch sử của hai suite, chưa rerun trong task publication.

Public chỉ có paraphrase tuyển chọn, proposal, locator/digest và navigation. PDF/extraction/render, raw/oracle, archive, IDB, config và credential không được xuất bản. Source có thể đọc theo chỉ thị hiện hành; runtime admission/ACK/training hoặc provider upload vẫn là hành động riêng.

## Kiểm và review

Áp dụng `scripts/verify_ia.py` cho read/hash/navigation và byte preservation; không dùng nó làm business/semantic/runtime acceptance. Kiểm cả staged export trước publication, diff của file tài liệu và content review riêng với producer. Kết quả/commit/receipt publication nằm ở hồ sơ local `evidence/orchestrator_meetings/20261024_public_pipeline_01`, không giả mọi raw đã có trong clone public.

Các nguồn đã đọc gồm bản trích6tri thức và phân tích PDF đã review, README/AGENTS/current/handoff, source map/phase/work queue, status v4, knowledge policy, preservation và nguồn principle/identity hiện hữu. Không tuyên bố audit lại toàn bộ archive hoặc toàn bộ bibliography trong PDF.
