# Kiến trúc thông tin

IA tổ chức cách tìm hiểu và tiếp tục project; các nguyên lý, phase, protocol và gate được kế thừa nguyên trạng. [Context](../../context/current.md) là view ngắn; [source map](../reference/source-map.md) chỉ nơi quyết định claim cụ thể.

## Phân vùng và nguồn sở hữu

| Vùng | Câu hỏi chính | Quy tắc |
|---|---|---|
| Root README, AGENTS | Bắt đầu ở đâu? | Entry và chỉ dẫn đọc; không chứa state machine mới |
| `context/` | Đang làm gì, xong gì, tiếp theo gì? | Snapshot có nguồn/thời điểm; không giả quan sát runtime mới |
| `docs/onboarding/` | Tiếp nhận và làm việc thế nào? | Thứ tự đọc, chọn context theo task, bàn giao |
| `docs/architecture/` | Thành phần, role và thông tin liên hệ ra sao? | View kiến trúc và trách nhiệm; không tự đổi topology |
| `docs/planning/` | Phase/dependency và công việc nào? | Tách W, R và gate; đề xuất khác dispatch |
| `docs/reference/` | Nguồn nào chính, còn thiếu gì? | Provenance, availability, validation và câu hỏi mở |
| `docs/guides/` | Hướng dẫn chuyên đề nào? | Chỉ mở khi task cần; nội dung phụ thuộc thời gian phải kiểm lại lúc dùng |
| `docs/changes/` | Lượt thay đổi nào đã làm gì? | Record theo revision, không thay raw/frozen history |
| `prompt_stacks/` | Hợp đồng instruction nào? | Giữ nguyên mười stack/protocol, tên và bytes |
| `metadata/` | File nào có digest và mapping? | Navigation/relocation/custody, không chứng minh semantic support |
| `scripts/` | Kiểm lớp tài liệu ra sao? | Standard library, read/hash, không import project hoặc gọi runtime |

## Áp dụng tham chiếu knowledge compiler

[Knowledge compiler của Reading Companion](https://github.com/Nohfinl99/Reading_Companion/blob/main/skills/sid-reading-companion/references/knowledge-compiler.md), Git blob `094a47a25cd8cf1906049fd4114ff2c58288659f`, là bản được roadmap local dẫn và đã được đối chiếu trong lượt IA. Blob ID là Git object ID, không phải SHA-256 hoặc commit SHA.

| Phần tham chiếu | Áp dụng ở lớp IA |
|---|---|
| KC01 source/task frame | Source map ghi path, phạm vi và mức truy cập; public clone thiếu raw được ghi LOCAL_ONLY |
| KC02 units/decomposition | Chia tài liệu theo câu hỏi/mục tiêu, giữ nguyên từng đơn vị contract gốc; tránh nhân bản định nghĩa |
| KC03 relations/prerequisites | Phase map phân biệt liên quan, thứ tự đọc và dependency thực; không suy gate từ số thứ tự file |
| KC04 select/plan | Navigation chọn ít nguồn đủ cho task; work queue giữ blocked/gaps và nhánh độc lập |

Đây là áp dụng phương pháp tổ chức thông tin, không import compiler, enums, learner levels, API hoặc workflow Reading Companion vào Orchestrator.

## Định danh, di chuyển và tương thích

Ba trang chủ đề từ `docs/ARCHITECTURE.md`, `docs/FINE_TUNING.md`, `docs/VALIDATION_STATUS.md` được chuyển nguyên byte tới đường dẫn canonical trong từng vùng. Trang cũ chỉ dẫn chuyển hướng. Stack/protocol và `CONTEXT_VI.md` giữ đường dẫn ổn định. Mapping chi tiết và digests trước IA nằm ở [preservation.json](../../metadata/preservation.json).

Tài liệu mới dùng tên lowercase, dấu gạch ngang. Không đổi ID phase, run, task, role hoặc tên trong raw. Không đổi đường dẫn opaque/binding trong evidence. Future candidate giữ revision riêng theo contract gốc; lớp IA không được dùng để refresh pin cũ khi có mismatch.

## Bảo trì và kiểm tra

Sau thay đổi, cập nhật link và [navigation.json](../../metadata/navigation.json) nếu có đường dẫn canonical mới. Chạy `python -I -B scripts/verify_ia.py` từ repository root. Verifier kiểm digest inventory, byte preservation, local links, canonical routes, phase counts và gate view. Nó không chạy fixture nghiệp vụ hoặc chứng nhận toàn bộ nguồn local.

Nếu lớp navigation được chỉnh có chủ đích, xuất inventory mới bằng `python -I -B scripts/verify_ia.py --inventory` vào file tạm ngoài repository; review diff rồi thay `metadata/content-manifest.json`. Không cập nhật `metadata/preservation.json` để hợp thức hóa thay đổi contract gốc. Inventory không tự là acceptance, chữ ký hay bằng chứng nguồn đầy đủ.

Phiên sau cần cập nhật current view từ report mới có evidence; report freeze, FAIL và source gốc vẫn giữ. Mọi gap về nguồn/quyền được ghi [open questions](../reference/open-questions.md); không thêm implementation trong task IA.
