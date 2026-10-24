# Native local acquisition — build và một lượt IDA

Theo yêu cầu W4 local, bổ sung [builder PE mẫu](../../scripts/build_native_pilot.py), [guide](../guides/native-local-pilot.md), [report](../proposals/input-pipeline/local-native-2026-10-24.md) và [state riêng](../../context/native-local-state.json). Build một lượt; direct IDA static acquisition một lượt sau exact supplemental R4a, có executor riêng và R4b độc lập. Không launch/debug/appcall target, không model/provider LLM, không cài/sửa config/license/elevation hoặc push GitHub trong lượt acquisition ban đầu.

Freeze staticv1 và wrapper cũ được giữ ở parent evidence trước execution. V2 bổ sung Job Object KILL_ON_JOB_CLOSE để quản lý process con; nếu assignment thất bại thì dừng trước helper. Guard setup đã thành công trong actualrun; timeout fault injection chưa kiểm. Source15pin và raw14entry khớp, target/copy digest đúng, IDA9.1/metapc64/completed analysis/twofunctions/newownedIDB được R4b xác nhận; không suy từ exit0 một mình.

Cảnh báo Lumina giữ nguyên; không có network absence proof hoặc full plugin/config hermeticity. MCP plugin đã load nhưng server/transport/REA connection chưa được probe; không tự cài thêm chỉ vì registration chưa có. Dynamic còn cần isolation và harness gọi export; entrypoint return0 chưa kiểm semantics. Không gán pair, consumer ACK, decompiler hoặc W4 PASS từ inventory.

README/current/handoff, hướng dẫn agent, work queue/mục lục và navigation dẫn riêng scope này. Global project-state, statusv4, preservation nguyên bản, sáu identity, mười stack/protocol, nguyên lý REA–IDA và lịch sử FAIL không đổi. Raw/IDB/target/gold/config giữ ngoài public package tại packet native_local_01; public local files chỉ có source/guide/report/state và digest locators. Các check IA/staged export chỉ kiểm read/hash/navigation, không rerun business để tăng tỷ lệ.

## Phạm vi xuất bản theo yêu cầu sau đó

Người dùng tiếp tục yêu cầu upload và merge vào main. Gói xuất bản gồm source builder, guide, report/state có digest locators và navigation; không đưa target, IDB, raw, oracle, profile hoặc config máy lên GitHub. Sửa các nhãn chỉ-local ở view hiện hành để phân biệt vị trí execution với phạm vi artifact public; kết quả acquisition, pins, warnings, limits và gate giữ nguyên. Kiểm lại content inventory/staged export và review delta tài liệu, không chạy lại target hoặc IDA.
