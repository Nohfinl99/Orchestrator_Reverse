# Code sửa candidate revision 2

Hai patch do phiên sửa 24/10 tạo, áp dụng vào **bản sao revision mới** trong workspace đầy đủ:

- [Prompt contract](prompt-contract-v2.diff): sửa import ROLE_SCOPE; kiểm typed input; tính lại eligibility và owner trước compose, giữ task digest/dispatch và canonical scope.
- [Evidence checker](evidence-checker-v2.diff): giữ predicate readback; bổ sung status và structured errors cho các exception đã chỉ rõ.

Đây là diff code thực, không phải bộ runtime độc lập. Public clone không chứa baseline candidate/evidence local; không tự áp patch vào archive hoặc source đã freeze. File nguồn đã sửa nằm local ở `src/candidates/revision_2/`; router được sao nguyên byte. Xem [biên bản sửa và kiểm lại](../repair-2026-10-24.md) để lấy digest và scope.

Không chạy sanitizer hoặc đổi input để che ý định. Compose giữ nguyên goal trong task JSON; điều này chỉ được kiểm trong các ca hữu hạn, chưa triển khai normalization ngôn ngữ tự nhiên hoặc xác thực authority bên ngoài. Checker chưa schema-validate mọi dạng JSON hợp lệ nhưng sai cấu trúc.

## Checker revision 3

[Patch v3](evidence-checker-v3.diff) bổ sung shape/cardinality/field/path/JSON validation cho fixed recorded bundle và diagnostic receipt-write failure. Baseline là checker revision2 đã pin; chỉ áp vào bản sao revision mới, không ghi đè source/freeze cũ. [Báo cáo hardening](../offline-improvement-2026-10-24.md) ghi39/39case kiểm riêng. Không gọi đây là schema engine tổng quát, authenticity validator hoặc runtime model protection; resolved-parent check có code nhưng suite chỉ kiểm lexical path rejection, chưa hostile symlink/race.
