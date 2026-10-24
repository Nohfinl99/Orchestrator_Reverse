# Pilot native local REA–IDA

**Kết quả local đã có:** xem [report acquisition](../proposals/input-pipeline/local-native-2026-10-24.md) và [state](../../context/native-local-state.json). Guide dưới đây không thay raw/review hoặc cấp quyền attempt mới.

Đây là nhánh acquisition nhỏ để từng bước tạo evidence cho W4. [Readiness gốc](../planning/w4-readiness-plan.md) và các gate kế thừa vẫn giữ nguyên. Chỉ có local task được cấp quyền mới chạy; kiến thức hoặc template không tự dispatch.

## Target mẫu

[build_native_pilot.py](../../scripts/build_native_pilot.py) tạo một PE32+ x64 dài1.024byte, bằng headers và machine code xác định trước. Đây là binary tự mã hóa, **không phải kết quả compile C**. Semantic reference/gold giữ trong packet local riêng. PE có entrypoint return0 và export `pilot_transform` tại RVA0x1010; entrypoint không gọi export, nên chỉ chạy EXE/nhìn exit0 chưa kiểm được hàm đó.

Builder dùng stdlib, nhận `--output` là đường dẫn tuyệt đối tới file `.exe` mới trong thư mục đã có, exclusive write và readback/hash; không chạy binary. Output binary, IDB, config và raw phải ở ngoài public package.

## Các chặng được tách riêng

| Chặng | Đầu ra cần kiểm | Không suy thêm |
|---|---|---|
| Build | Source freeze/review, argv/raw/exit, bytes/hash, original inputs không đổi | PE hợp lệ theo cấu trúc chưa là loader/runtime acceptance |
| IDA acquisition tĩnh | Exact binary hash, completed autoanalysis, architecture, function inventory, fresh owned IDB/log/report | Inventory chưa là pseudocode, semantics hoặc target execution |
| REA provider và pair | Bridge hoạt động, same target/component/slice/IDA state, producer/session/custody/freshness và consumer validation/ACK | Direct IDA evidence không tự trở thành REA evidence hoặc G3 PASS |
| Dynamic trong isolation | Probe isolation, harness ABI đúng gọi export, gold/raw/capture/cleanup, quyền và budget riêng | Hypervisor hiện diện hoặc config text chưa chứng minh isolation |
| Gate/handoff | Independent review đúng revision, failure/unknown giữ nguyên và dependency được đánh giá | Không đổi W4/G1–G4 bằng số lượng file hoặc tự chấm điểm |

Trong task hiện tại, budget tách build và một static acquisition. Target không được launch/debug/appcall; không tự đổi config/license hoặc cài engine. Mỗi execution phase có freeze/R4a riêng trước attempt và R4b khác producer/executor sau raw. Khi thiếu provider/isolation hoặc vượt budget, phần phụ thuộc giữ chờ, vẫn bàn giao evidence đã có.

## Tiếp tục phiên

Đọc [context](../../context/current.md), report/state mới được dẫn tại đó, rồi exact packet local `evidence/orchestrator_meetings/20261024_native_local_01`. Revalidate pins trước reuse; không ghi đè output hoặc rerun một attempt để thay kết quả. Nếu chỉ có clone public, raw/IDB/gold giữ `LOCAL_ONLY`, không giả đã kiểm.

Nguồn và điều kiện môi trường: [nghiên cứu pilot](../proposals/input-pipeline/native-pilot-research-2026-10-24.md). Đây là guide sử dụng thiết kế, không thay receipt hoặc trạng thái thực thi của từng lượt.
