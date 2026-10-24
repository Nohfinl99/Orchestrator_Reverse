# Nghiên cứu pilot REA–IDA trước khi chạy target

Ngày kiểm: 24/10/2026. Theo yêu cầu dùng Reading Companion, bản này chọn tri thức phục vụ một pilot có thể kiểm chứng. Đây là **nghiên cứu và đề xuất**, chưa là kết quả phân tích native hoặc benchmark. Người dùng cho phép chạy target trong môi trường kiểm thử riêng; chưa có target cụ thể được bind.

## Kết quả đọc và quan sát

Các ý dưới được AI chọn từ phần đã đọc theo tiêu chí: ảnh hưởng trực tiếp đến target identity, khả năng phân tích, isolation hoặc chất lượng evidence. Đây là tập chọn cho pilot, không là toàn bộ kiến thức reverse engineering.

| ID | Tri thức cần dùng | Nguồn và giới hạn |
|---|---|---|
| N01 | Chạy IDA headless cần log/script/output cụ thể; autonomous mode không tự chứng minh analysis hoàn tất hoặc decompiler thành công | [Hex-Rays IDA 9.1, command-line switches](https://docs.hex-rays.com/9.1/user-guide/configuration/command-line-switches), các mục `-A`, `-B`, `-L`, `-S`. Phần yêu cầu evidence hoàn tất là acceptance do dự án đề xuất |
| N02 | REA và IDA phải cùng artifact/slice/state; executable IDA tồn tại chưa đồng nghĩa REA provider đã nối | Contract [REA–IDA](../../../prompt_stacks/protocols/pair_protocol.md); quan sát local `binary_session`: REA 6.7.0, không mở target, IDA provider `not_configured`, chưa live probe. Đây là metadata readiness, chưa là evidence target |
| N03 | Môi trường thực thi riêng cần isolation được kiểm; thư mục riêng hoặc process timeout chưa chứng minh cách ly OS | [Microsoft Windows Sandbox, Overview](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/), phần mô tả virtualization/disposable VM. Chưa xác minh sandbox hoạt động trên máy hiện tại |
| N04 | Phải bind network, clipboard, mapped folders và đường xuất evidence trước run | [Microsoft, Use and configure Windows Sandbox](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file), các mục Networking, Mapped folders, Clipboard redirection. Đề xuất tắt network/clipboard, chỉ map input đọc; cơ chế thu output cần review riêng |

Quan sát file local: `idat.exe` có version resource **9.1.25.0226**, chưa khởi chạy. REA báo các native provider chưa sẵn sàng trên phiên đang dùng. Các tên `WindowsSandbox.exe`, `clang.exe`, `cl.exe`, `gcc.exe` không được tìm thấy qua PATH trong lượt kiểm; điều này **không chứng minh không cài ở nơi khác**. Không tự cài, đổi license hoặc sửa provider config.

README của package REA 6.7.0 được đọc cho định danh/upstream. Tài liệu `docs/ida-provider.md` mà session dẫn không nằm trong package cài; URL tag `v6.7.0` thử đọc trả 404. Do đó chưa kiểm được hướng dẫn provider đúng revision; không lấy tài liệu main hiện tại thay bằng chứng của 6.7.0. Raw quan sát giữ local, không public config/path máy.

## Target và evidence em đề xuất

**Target đề xuất do AI thiết kế:** một PE x64 nhỏ do dự án tự viết, có một hàm mục tiêu xử lý số nguyên fixed-width với nhánh điều kiện và tập input/output xác định trước; tránh undefined behavior, không network hoặc ghi file. PE còn entry point/runtime glue phải kiểm kê riêng, không nhận toàn binary chỉ có một hàm. Source dùng làm gold riêng; reviewer phân tích artifact không được lấy tên hàm/source làm bằng chứng decompile. Chưa tạo/compile/chạy fixture này. Fixture kiểm cơ chế thu evidence, chưa đại diện phần mềm thật hoặc hiệu quả pentest trên sản phẩm.

Luồng pilot: source + build recipe + toolchain/version → target SHA-256/architecture → R4a/freeze cho acquisition/bootstrap → IDA static analysis → REA evidence cùng artifact/state → pair validation/consumer ACK trước target consumption → nếu đủ isolation và quyền thì dynamic run → so gold riêng → R4b. Pair là đầu ra của acquisition được phép, không yêu cầu có sẵn pair trước lần tạo đầu tiên; quyền acquisition và gate áp dụng vẫn phải bind trước. REA giữ workflow/evidence/ledger; IDA giữ native/decompiler/IDB state. Không ghép hai report cùng tên file để nhận pair. IDA batch mode không là sandbox và không chứng minh MCP bridge được nạp.

| Chặng | Evidence tối thiểu cần giữ | Điều kiện dừng |
|---|---|---|
| Target/build | Source digest, compiler flags/version, binary digest, format/arch/slice và expected cases đã freeze | Thiếu toolchain/provenance hoặc digest drift |
| Static | Actual tool/session/version, command/log, analysis-completed signal, entry/function/branch evidence, output/IDB digest và failed capabilities | Provider unavailable; arch/state không khớp; hết budget |
| Pair | Same target/component/slice/state, producer/session/revision/custody/freshness; validation và actual consumer ACK riêng | Thiếu binding/ACK; metadata tự khai chưa được kiểm |
| Dynamic | Isolation profile/instance, network/mount policy đã kiểm, invocation/stdout/stderr/exit/timing, cleanup receipt và exact case comparison | Isolation chưa kiểm; output path ngoài scope; timeout hoặc drift |
| Review | Reviewer khác producer/executor, raw locators, gold tách biệt, failed/unknown cases giữ nguyên | Không có raw hoặc chỉ có self-score |

Budget **đề xuất**, chưa là dispatch: một target ≤1 MiB; tối đa 1 static attempt mỗi engine, 120 giây/engine; 3 dynamic cases, 5 giây/case; tổng execution ≤300 giây, output ≤16 MiB, không gọi model hoặc provider LLM. Native-provider calls chỉ trong static scope đã freeze. Cần bổ sung cap build/connection/open/script/retry, kiểm tính khả thi theo tool/profile và freeze trong packet mới trước run; không mượn acceptance của suite CLI.

## Quyết định hiện tại

**Native pilot: `RESEARCH_COMPLETE_WITH_GAPS / NOT_RUN_PREREQUISITES_UNBOUND`.** Bước tiếp theo là chuẩn bị fixture/build và isolation profile có evidence, đối chiếu provider đúng revision, rồi trình R4a packet riêng. Nếu không có môi trường cách ly, phần dynamic tiếp tục chờ; static analysis cũng cần packet riêng. CLI offline không mở quyền thực thi này.

Không đổi [W4 readiness](../../planning/w4-readiness-plan.md), status v4, sáu identity hay lịch sử FAIL. Chưa có native pair, runtime ACK hoặc đánh giá model mới. Phạm vi đã đọc: các section nguồn nêu trên, contract pair, skill REA/IDA và quan sát phiên; chưa audit toàn bộ upstream, firmware, malware hoặc corpus jailbreak. Trạng thái đọc nguồn: PARTIAL đối với provider guide đúng version; không có tuyên bố mastery/training hay admission KB.
