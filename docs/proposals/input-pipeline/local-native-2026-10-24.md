# W4 local: target mẫu và acquisition IDA

Ngày24/10/2026. Người dùng chọn chuẩn bị target mẫu, kiểm provider/isolation và chạy phần đủ điều kiện trước trên local. Report này mô tả lượt chạy local; source/guide/state thuộc gói public, raw/target/IDB giữ local. [Guide](../../guides/native-local-pilot.md) · [State local](../../../context/native-local-state.json).

## Trạng thái quan sát

| Phần | Kết quả |
|---|---|
| Build target mẫu | Một invocation thành công; PE32+ x64,1.024byte, hash/readback/source pins khớp |
| Review byte PE | Reviewer riêng đã đọc header/section/export/machine bytes từ binary thật; không launch target |
| IDA static acquisition | **Đã chạy một lượt và được R4b review**, exit0, không timeout; auto-analysis hoàn tất, metapc64-bit, hai function |
| REA native provider | `not_configured`, chưa live connection probe; không có target mở |
| Pair/consumer ACK | Chưa có; direct IDA riêng không tự tạo REA–IDA pair |
| Dynamic/isolation | Chưa chạy; chưa chứng minh môi trường cách ly và chưa có harness gọi export |
| Global W4 | Giữ `NOT_RUN_BLOCKED`; không nâng gate kế thừa |

Target SHA-256: `50416ee3324f2847da9708271d2d9d9364834d400ddd58420812bab8119b1567`. [Builder](../../../scripts/build_native_pilot.py) ghi PE/machine code xác định trước; reference C không được compile. Entry tại RVA0x1000 chỉ return0; export `pilot_transform` tại RVA0x1010 có hai nhánh unsigned. Các giá trị gold là expected, chưa phải kết quả hành vi.

## Bằng chứng và phân vai

Packet local: `evidence/orchestrator_meetings/20261024_native_local_01`. Root producer/chair; preflight_reviewer duyệt build, native_static_preflight là phiên thay thế duyệt static, pentest_executor chạy, postrun_reviewer kiểm raw sau. Ba chức năng pre-review/executor/post-review được giữ tách; phiên preflight trước đã được dừng khi thay thế. Đây là các phiên agent cùng model, chưa là human/cross-model review hoặc runtime triển khai sáu identity.

| Artifact local | SHA-256 |
|---|---|
| build-freeze.json | `2ec78e2c2c9f3d6937b9fbcec53faf9b1059b5327083e985ac4aa535b3b12db8` |
| r4a-build-review.md | `433b106f085e5f3867ebd0a6729a3ec0b3aa0a0a2a9a34eeb0c98647c6b97474` |
| build-execution/build-receipt.json | `36ffa8d12f5c6c483c296b2e2fae29a0a486619fd9d0dc12cf323903c0386328` |
| static-freeze.json — giữ lịch sử, superseded trước execution | `4b20a42b9b733cbd3f6880cb19b79d35b73eaae25803c5a87754fb6c96e9d89a` |
| static-freeze-v2.json — actual run | `a03bfa05d3bf79cc5adfe3b32930dc57881d4b90d3fda9646fa9217af92b0909` |
| r4a-static-review-v2.md | `1a478a3c948ac2b3895a1b03b060d77cfecd2436ca50d2b82657827105e366d9` |
| static-execution/executor-receipt.json | `858eaa40dfabe0a7812699eb4649b5bcab4ad86072c1c0a870ee6655a2f12e6b` |
| ida-analysis/analysis.json | `45ef24b1664bb01ef6c8610b07294486fba277a3aa5a01fa0589eaa4c1d4a7c9` |
| ida-analysis/analysis.i64 | `70df05f1509c39c1fbf4a6f28ba3807a1ac1e638c62e741a44ae7054d285d80a` |
| r4b-static-review.md | `06beb4a3091cdc786dfa0610d5e11c41cc90434922360f08be25594916de0950` |
| r4b-static-verdict.json | `6e558bbc73fb3330e66aee44bbd41c03546c63bf6d00608d1933029e2b048a62` |

Build chỉ ghi file mới, một lượt trong giới hạn5giây, không có target process. Static phase đã chạy một IDA9.1 headless function inventory, helper120giây và outer child wait180giây cộng tối đa20giây cleanup và thêm thời gian ghi receipt không định lượng; wrapper thực tế7,734giây, không timeout. Job Object đã configure/assign self trước helper; snapshot sau wrapper có0process khớp exactownedpath. Timeout cleanup fault injection chưa kiểm. Output thực tế81.987byte, trong envelope16MiB kiểm sau run. Không nhận đó là hard disk quota hoặc network sandbox. Mỗi phase cần exact R4a trước dispatch; receipt build không mở quyền IDA/dynamic. Raw/IDB/config/target/gold giữ ngoài public package; clone public không tự có bằng chứng local này.

## Kết quả static được R4b xác nhận

15/15pin và14/14raw artifact hash khớp. Input gốc/copy giữ đúng digest; database mới74.097byte có headerIDA2, chưa được reviewer mở lại bằng engine. Các predicate hash, auto-analysis, architecture, function inventory và owned output đạt trong scope này.

| Function inventory thực tế | Địa chỉ |
|---|---|
| start | `0x140001000` |
| pilot_transform | `0x140001010` |

Cảnh báo **`lumina: bad signature`** giữ nguyên trong log; không có kết luận Lumina thành công hoặc engine hoàn toàn không dùng mạng. Network không được đo. Plugin MCP đã được IDA nạp từ user profile, nhưng chưa start/probe server hay chứng minh transport tương thích REA; plugin được phát hiện sau run, không giả đã nằm trong15pin hoặc toàn plugin/config environment hermetic. Job Object quản lý process cleanup, không là VM/filesystem/network sandbox.

R4b verdict: **PASS_BOUNDED_DIRECT_IDA_STATIC_INVENTORY_ONLY**. Không rerun build/IDA để nâng kết quả, không có v1 static attempt.

## Phần còn chờ

REA6.7.0 cần bridge/provider hợp lệ và actual session/target/IDA state để tạo pair. Windows11Pro/hypervisor hiện diện chưa chứng minh isolation; WSL báo chưa cài và query Sandbox feature yêu cầu quyền Administrator. Không tự cài, sửa config/license, chấp nhận license hoặc leo quyền trong lượt này. [Nguồn nghiên cứu](native-pilot-research-2026-10-24.md) giữ điều kiện và giới hạn; diagnosis/proposal cụ thể ở packet local `provider-isolation-next.md`.

Dynamic còn cần harness có ABI đúng gọi export trong isolation. Chỉ chạy entrypoint và nhìn exit0 chưa kiểm được các gold values. Function inventory cũng chưa chứng minh decompiler, pseudocode hoặc semantics. Không dùng sample này làm benchmark sản phẩm thật.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Status v4 và lịch sử FAIL giữ nguyên. Khi tiếp tục, revalidate exact pins; không rerun/ghi đè một attempt để thay kết quả. Đã đọc nguồn task/skill/helper/builder/plan và evidence được dẫn; không tuyên bố audit toàn archive hoặc chứng minh toàn host không còn process/network side effect.
