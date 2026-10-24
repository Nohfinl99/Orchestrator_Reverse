# Thực thi cải thiện offline — 24/10/2026

Người dùng giao chạy [kế hoạch cải thiện](checkpoint-roadmap-2026-10-24.md) và upload GitHub. Nhánh được mở lại: review seed nguồn (A3) và task hardening checker riêng. Phần cần sản phẩm/caller/consumer/runtime thật tiếp tục chờ; không tạo sản phẩm giả để đóng gate.

## Đã cải thiện gì

### 1. Review đúng bộ sáu seed, sửa nhận định quá rộng

Reviewer `/root/preflight_reviewer` đọc nguồn thực của S01–S06: năm seed được nhận, S05 cần sửa câu phủ định “chưa có pentest” vì đã có các lượt candidate offline. Original seed giữ nguyên; reviewer tạo revision 2 với S05 giới hạn claim đúng các artifact tooling/AO được dẫn và thêm nguồn/locator/digest pair protocol cho S06.

Reviewer khác `/root/postrun_reviewer` nhận **6/6 seed revision 2**, kiểm17 source bindings,13 capture và readback10 historical tooling case. Đây là adjudication nguồn/câu hỏi/oracle, không phải model benchmark execution, không hidden heldout, không nạp oracle vào active KB. S02 “main mới hơn” chỉ là timestamp capture, không chứng minh ancestry/installed runtime/freshness hiện tại; S04 chỉ nói chưa có bằng chứng ingestion trong phần nguồn đã đọc.

Original A3 “Input/cases/oracle independently reviewed” được verify cho exact six-seed revision 2. A5 quyết định mục đích benchmark và A6 nhận criteria/threshold vẫn pending. Không suy quyền chạy model từ review seed.

### 2. Code checker revision 3

[Diff code mới](patches/evidence-checker-v3.diff) so với revision 2 đã được kiểm riêng:

- Kiểm type/field của JSON object, list và row; chặn danh sách capture/case rỗng hoặc sai cardinality/ID của **bundle lịch sử cố định**13capture/10case.
- Kiểm hash format, integer và boolean đúng type; tránh nhận `true` như một exit code integer.
- Chặn filename traversal, absolute path và backslash; kiểm resolved-parent containment cho đường dẫn do metadata chỉ định.
- Từ chối duplicate JSON keys, NaN, invalid UTF-8 và malformed JSON với lỗi có cấu trúc.
- Khi không ghi được receipt: trả lỗi trên stdout có `receipt_write_error`; không giả đã tạo file receipt.

Source local ở `src/candidates/revision_3/verify_recorded_evidence.py`; router/prompt vẫn revision 2. Không sửa original candidate hoặc archive, không nối active caller, không chạy sanitizer. Checker này không là JSON Schema engine tổng quát hoặc cơ chế chứng thực authority/receipt. Filesystem races/symlink injection và timeout fault injection chưa được kiểm trong suite này.

## Freeze và kết quả chạy

Producer/chair `/root`; R4a `/root/preflight_reviewer`; executor `/root/pentest_executor`; R4b `/root/postrun_reviewer`. Phiên tách nhau, cùng model kế thừa; không phải human/cross-model independence hoặc các identity runtime đã deploy. Reviewer sản xuất seed revision 2 được reviewer còn lại kiểm riêng.

Packet mới freeze61file; suite39case gồm **10 oracle objects D cũ giữ nguyên +29 hồi quy mới**. Chỉ checker mới chạy trên bản sao evidence do packet sở hữu; source verifier lịch sử chỉ được copy/read, không chạy workload lịch sử. Không gọi model/provider/REA/IDA/native target/network/training/W4.

R4a accepted có outer180giây, child15giây, nestedchecker12giây, giới hạn16MiB fixture mỗi case và cleanup owned descendants nếu timeout. Chair đã chấp nhận trước dispatch. Một attempt: **39/39 case match**, exit0, không timeout,10,109giây;61/61 nguồn SHA/size giữ nguyên trước/sau.

| Nhóm | Kết quả | Ý nghĩa |
|---|---|---|
| D01–D10 | 10/10 | Positive baseline accepted; tamper/missing-file/malformed JSON giữ oracle cũ |
| D11–D20 | 10/10 | Capture shape, empty list, wrong field type/hash và path syntax bị structured rejection |
| D21–D26 | 6/6 | Capability/tool/selected metadata sai shape/type bị structured rejection |
| D27–D34 | 8/8 | Plan/cases/freeze/pins/receipt/stdout sai shape, empty cases, bool exit bị rejection |
| D35–D39 | 5/5 | Duplicate key, NaN, receipt destination failure, invalid UTF-8, null package metadata |

D37 tạo directory tại đường dẫn receipt trong owned fixture, không đổi ACL hoặc quyền của workspace. Checker exit2, stdout ghi structured error và receipt-write failure; inner stderr rỗng. Hệ thống không thể đảm bảo disk receipt khi đích không ghi được. Positive D01 đạt success, tránh coi checker từ chối mọi thứ là đúng.

## Review sau chạy

R4b: **PASS_BOUNDED_FIXED_BUNDLE_CHECKER_HARDENING_ONLY**. Reviewer tự đối chiếu39/39 raw với oracle,61/61 SHA/size,10 oracle objects D cũ,39 bản sao checker đúng revision3 và từng mutation trên copied inputs. D01 accepted; D02–D05 mismatch exit1; D06–D39 structured exit2; inner stderr đều rỗng. D37 stdout fallback và receipt-write error được quan sát thực. Reviewer không rerun hoặc sửa source. Verdict không nghiệm thu toàn bộ JSON/schema/filesystem/runtime hoặc EVALUATION-D.

## Trạng thái tiêu chí sau cải thiện

| Checkpoint | Trước | Sau | Căn cứ |
|---|---|---|---|
| INPUT-A | 3/6 — 50% | **4/6 — 66,67%** | Chỉ thêm A3 bằng independent review exact6seedr2 |
| KNOWLEDGE-B | 3/6 — 50% | 3/6 — 50% | Rights/consumer ACK/admission còn chờ |
| IMPLEMENTATION-C | 0/6 | 0/6 | C6 component partial; pipeline thật chưa có |
| EVALUATION-D | 0/6 | 0/6 | Checker39case không là benchmark model/REA thực |

[Status v4](status-v4.json) giữ criteria revision1 và mẫu số sáu; status v1/v2/v3 giữ lịch sử. Còn **17 tiêu chí chưa đóng**, cùng gap timeout/schema/filesystem chưa bao phủ hết. Thay đổi A3 không nhận checkpoint hoặc threshold thay anh. Không cộng39ca với42ca cũ thành benchmark chung.

## Bằng chứng local và digest public

Packet `evidence/orchestrator_meetings/20261024_offline_improvement_01` chứa source pins, runner/oracle, seed revisions/reviews và raw. Public chỉ xuất summary/status/diff code; raw/oracle development không phân phối.

| Artifact | SHA-256 |
|---|---|
| seed revision 2 | `ed4c658dfaf30754355ac29fd3b68d4931698e67c80b8d9597a715124919aa8d` |
| seed independent review | `b2bd0ac6db32cb3e23fe6b92b42e1276c950ab68be6ff27a680bf6af6af4d81a` |
| seed review verdict | `83a0c8d9ddccc64810e5888897a2452cee5fa47ce7f9c4d0e099b0a50df3e17d` |
| checker revision 3 | `d03d2d62f28489192225adcc441e9962cd9359808c9e2152a9ee46d836540a66` |
| freeze61 | `da5876c86c5607d41b9c5e5f8272e4514e8521dfd4d9a1c3c704b6e2a4cb5cac` |
| runner | `e647ce88af45dce83484da19cf7fb99a1ef7ea514fbec25858b0b37bb41aefb9` |
| oracle | `ceaa501edcd468ce6715dac525cc32b93dbc92d02c47c009dcf9cd9d8c1b914a` |
| R4a | `dc28eb2745cebb7d8b37b217673ac62e5791ef30ffc347f1d0b69f94f4a6b819` |
| execution summary | `440d2ca60fca3593669058903aa097f033e1c0e3c4d0e62c482b09aeca7ee52a` |
| executor receipt | `5dae5a6afb5a491c91382ea7880502ef46d518cea0c2f448210c3ef087cee582` |
| R4b report | `79a4583aa3a6afbca68430cb44f2017dddfb0ce6957c138bd6d62fae9581c09f` |
| R4b verdict | `dd6ab482f7fdf5acc6f566642cc5b1c4f5608d0e16d73d561c5f712290fb2178` |

## Phần tiếp tục chờ

Lộ trình sản phẩm không đổi: một objective/caller/consumer có pin thật, original input và diff/clarification/taxonomy trong flow; bundle/use/rights/ACK/admission thật; profile/data/budget/metrics và prerequisite trước run. Khi có task sản phẩm thì kiểm điều kiện rồi mới mở từng nhánh. Không tự bật W4/v3 hoặc benchmark provider.

Giữ P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. REA–IDA ownership, sáu identity, policy knowledge trung lập và lịch sử FAIL vẫn được kế thừa.
