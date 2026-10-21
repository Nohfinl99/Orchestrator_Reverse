# Đóng góp

1. Mỗi thay đổi có một objective, owner, input/source refs, output và acceptance predicate.
2. Ghi `DESIGN`, `IMPLEMENTED`, `EXECUTED` và `REVIEWED` riêng. Không gọi review tài liệu là test PASS.
3. Giữ nguyên raw, attempt history, FAIL và frozen artifacts. Thay đổi accepted contract/prompt tạo revision mới, không sửa lịch sử.
4. Trước execution, freeze packet R4a gồm criteria, cases/oracles, inputs/environment, capture, budget và reviewer. Sau execution, giữ raw và dùng reviewer R4b riêng.
5. Với target consumption, giữ REA–IDA pair/scope/state/provenance/freshness và ACK của từng consumer. Chuẩn bị ngoài target phải ghi `NOT_RUN`.
6. Kiểm tra quyền và license cho source/dataset/model/asset trước khi commit hoặc phân phối. Không commit credentials, target binaries/IDBs hay local config.

PR nên nêu thay đổi, lý do, đường dẫn evidence, kiểm tra đã chạy và phần chưa chứng minh. Không ghi kết quả chưa có.
