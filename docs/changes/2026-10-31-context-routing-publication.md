# Context routing và kiểm thử query local — 31/10/2026

## Sắp xếp và phạm vi public

Gói public có [điểm điều hành theo task](../operations/README.md), [context index](../../context/README.md), [cognitive task guide/worksheet](../proposals/cognitive-routing/README.md), [Paperclip sync spec](../proposals/cognitive-routing/paperclip-sync.md) và [Cloudflare methods chọn lọc](../proposals/cognitive-routing/cloudflare.md). Các entry README/docs/proposals/navigation dẫn theo objective. Không di chuyển hoặc sửa mười stack/mười protocol đã freeze.

Current/handoff rút gọn từ tổng **18.323** còn **6.217 byte** trước normalization xuất bản, giảm khoảng **66% byte**. Hai bản cũ giữ nguyên trong history cùng thư mục. Đây không phải đo model tokens hoặc benchmark ngăn context overflow. Chọn ít nguồn/skill theo task; budget query không bao gồm toàn bộ chat/system/skill context.

Knowledge graph và query CLI thực thi vẫn **LOCAL_ONLY_NOT_DISTRIBUTED** trong workspace đầy đủ. Public clone có tài liệu/sanitized summary này và [metadata digest](../../metadata/offline-query-pentest-2026-10-31.json), không có corpus/raw/runner để tái lập 47 case. Không đưa archive, targets/IDB, config, credentials hoặc source vendor vào publication. Chưa có file lịch sử nào đủ bằng chứng hết hiệu dụng để xóa sau graph ingestion.

## Pentest đã chạy, không phải kết quả CI mới

Chair lập roadmap và freeze. GPT-6 Luna chuẩn bị/thực thi; GPT-6.1-sol high review độc lập R4a trước và R4b sau run. Đây là các phiên tách producer/executor/reviewer, không phải sáu identity runtime được deploy hoặc benchmark so sánh model.

Subject local: query CLI trên bản sao graph thật và 10 source files đã chọn. Một attempt `a01`, **47 CLI calls**, khoảng **16,397 giây**. **16 exact-success envelopes +31 structured-negative cases** khớp oracle; không fail/harness-error/timeout/skipped/not-run. **35/35 frozen files**, gồm **17 original records**, giữ hash/size trước/sau.

| Round | Kết quả | Scope |
|---|---|---|
| R1 | 11/11 | Graph/query thật, source drift/missing, reference và selection |
| R2 | 23/23 | JSON shape/type/provenance/bool/float/hash/path/duplicate keys/NaN và graph/source UTF-8 |
| R3 | 13/13 | Byte budget có LF, mandatory ID, omissions, deterministic output và instruction-like text là dữ liệu |

Các case là regression có chọn lọc từ lỗi query review 31/10 và adaptation các input classes của checker24/10. Không chạy lại nguyên suite28/39 cũ, không cộng mẫu số. Lỗi harness/oracle phát hiện trong preparation đã sửa trước freeze; không sửa oracle sau output. Lone-surrogate regression lịch sử **không được replay trong47case**. Physical symlink/reparse, race, timeout fault injection, sandbox/memory containment và Paperclip live không được kiểm.

R4b verdict: `PASS_BOUNDED_OFFLINE_NAVIGATION_47_CASES_ONLY`. Reviewer đọc94raw streams và dựng lại từng fixture mutation; không rerun subject. Byte boundary841/840 và paperclip pair1.895 byte được kiểm. Output `authority=false`/`semantic_verified=false` và marker không xuất hiện không chứng minh khả năng chống prompt injection của LLM hoặc downstream executor. Không quan sát subject bug mới trong phạm vi47case, không suy toàn hệ không còn lỗ hổng.

Raw/receipts/review đầy đủ có locator text LOCAL_ONLY: `evidence/orchestrator_meetings/20261031_bounded_pentest_01/` trong workspace cha. Clone public không chứa đường dẫn đó. Digest locators trong metadata cho phép đối chiếu khi có quyền truy cập nguồn, không thay chữ ký/receipt hoặc source truth.

## Merge và trạng thái

Lượt publication dùng một nhánh `codex/` cho thay đổi docs/navigation liên quan và PR vào main sau review/check exact head. Workflow mới chỉ chạy read/hash/navigation verifier trên gói public; không chạy pentest local, provider hoặc target. Kết quả CI/publication thực tế theo GitHub PR/checks, không phải từ câu mô tả này.

Paperclip còn là thiết kế chưa connected; Cloudflare là reference chọn lọc chưa cài/admitted runtime. Giữ sáu identity và REA workflow/evidence/ledger–IDA native/decompiler/IDB ownership. **P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF.**
