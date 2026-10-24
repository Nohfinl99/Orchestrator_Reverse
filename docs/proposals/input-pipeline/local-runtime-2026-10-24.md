# CLI input pipeline: implementation và kiểm thực tế

Ngày24/10/2026. **Đã triển khai caller chuẩn bị input local; chưa có model/tool/native dispatch.** [Cách dùng](../../guides/local-input-pipeline.md) · [Trạng thái máy đọc](../../../context/local-pipeline-state.json) · [Nghiên cứu REA–IDA tiếp theo](native-pilot-research-2026-10-24.md).

## Thay đổi đã chạy

`scripts/prepare_input.py` gọi package `orchestrator_pipeline` mới, dùng stdlib. Caller giữ original bytes trong cap, request revision/source provenance, câu hỏi khi thiếu field, proposal/diff/digest tùy chọn, resume lineage, prepared artifact và receipt/manifest có readback/hash. Không sửa archived Stage1 parser/broker, không import candidate cũ và không kế thừa quyền từ metadata khai trong request.

Task `INTAKE_AND_PLAN` chuẩn bị artifact cho Prompt-Master. Năm task kind khác giữ mapping identity hiện hữu nhưng dừng vì prerequisite runtime chưa bind. Proposal chỉ được đưa vào prepared text khi có exact digest annotation từ operator; identity và semantic preservation vẫn chưa xác thực. Không có cơ chế tự viết lại input để vượt từ chối model.

## Cuộc kiểm có reviewer và executor riêng

Packet local: `evidence/orchestrator_meetings/20261024_local_pipeline_01`, attempt_01. Producer/chair là phiên root; R4a là phiên preflight_reviewer; pentest_executor chạy một lượt; postrun_reviewer thực hiện R4b từ raw. Đây là các phiên agent riêng, cùng model; chưa có human hoặc cross-model review và chưa triển khai runtime sáu identity.

| Phép kiểm hữu hạn | Kết quả |
|---|---|
| R4a freeze | 12 file, exact SHA-256 và size; acceptance có outer process guard |
| Suite | **40/40 ca khớp oracle**, một attempt; **49 lần gọi CLI** trong cap52 |
| Process budget | Outer180giây, case20giây, CLI8giây; outer exit0, không timeout |
| Bảo toàn source | 12/12 file khớp trước/sau chạy |
| R4b | `PASS_REAL_LOCAL_PREPARATION_CLI_ONLY`; rederive từ raw và manifest, không chạy lại subject |
| Provider/model/native dispatch trong suite | 0/0/0 |

Nhóm ca gồm Unicode/nguồn giả quyền, thiếu input, JSON lỗi/duplicate/NaN/type, giới hạn bytes/sources, role bị chặn, traversal/device ID, không ghi đè, proposal pending/accepted/stale, resume và parent tampering, CLI errors và no-newline diff. **40/40 là tỷ lệ case hữu hạn, không phải xác suất an toàn, hiệu quả chống injection hoặc tỷ lệ hoàn thiện sản phẩm.**

| Artifact local | SHA-256 |
|---|---|
| freeze.json | `d60f8224f44bae972dd604a6bfd124bf0d5d7cc7db42de9bf2e0fb20622603eb` |
| plan.json | `0dce560e0effb072bd1f7a4cfeeb985b0b736632dcb04d4ed7ee86dabf1839dd` |
| oracle.json | `e2673d00520b4632063df8d498704de2d711e77496ac6f18f26ac0d65f81b535` |
| runner.py | `b7ccb73835a6998dd4c687f141d512a1fac5ccbda4f39b9a776eae6f406b1a40` |
| r4a-review.md | `a4c104aab89f1585306c883ef12bc649e3ce88ccf6bceec6be5190f7b3c90988` |
| chair-acceptance.json | `426b9f39aa2aecd6c34f1e6a14ed7b1f7be777e798c2412527fbd27a5c72c8e0` |
| execution/executor-receipt.json | `fced402f6016747cb0b400d97d0f8502ebe9f33b1b779f7aab2bf650c114c414` |
| execution/attempt_01/summary.json | `6679c4c8a0e74c961a08215d89d0d693d598c235cb70863af8eb8646cec15895` |
| r4b-verdict.json | `8a7623afe055505f1e9a242c240aa4703495f42661338f22baa7877638be3e73` |
| r4b-review.md | `f871aa622d7c5ec85e3312780296d127ed8a9364f61f0bd71968bacf2a4a7784` |

Public chỉ có code/example/report và digest locators. Raw, runner/oracle, filesystem receipts, path máy và config giữ local; clone public chưa thể tự kiểm lại nguyên suite chỉ từ report. IA verifier chỉ kiểm hash/navigation và không nhập business code.

## Scope và gap giữ mở

Đây là caller mới ở leaf scope `LOCAL_OFFLINE_PREPARATION_ONLY`, không đổi caller đã chọn trong [status v4](../input-support-gates/status-v4.json). Vì vậy tỷ lệ checkpoint lịch sử vẫn66,67/50/0/0; không tự chuyển bằng chứng local mới thành closure sản phẩm. P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF.

Đánh giá R4b **riêng caller local mới**: C1 bound entry→CLI→core, C2 original/revision/digest, C5 structural questions/resume và C6 raw/review có evidence trong scope hữu hạn. C3 mới có local error layers; C4 mới có diff/digest/annotation, nên cả hai PARTIAL. Đây không là chuyển tỷ lệ của worksheet lịch sử. P28 được kiểm trực tiếp prepared text bằng proposal thật; P31 được kiểm câu hỏi/goal trả lời, revision2 và lineage hashes. Identity, semantic preservation và execution authority vẫn false.

Phân loại objective/decision/claim bằng ngôn ngữ tự nhiên, kiểm giữ nghĩa, identity/authority thật, consumer ACK, model refusal/correctness, memory admission và executor enforcement vẫn thiếu. Manifest/hash không là chữ ký, authority hoặc semantic proof. Chưa kiểm filesystem race/concurrent hostile writer; reparse guard là kiểm local tại thời điểm đọc/ghi. Timeout cleanup có guard nhưng chưa bị kích hoạt để kiểm hành vi. Zero-call fields phù hợp code/raw đã review, chưa là syscall/network audit độc lập.

Nhánh native do người dùng chọn được [đọc và đề xuất riêng](native-pilot-research-2026-10-24.md); chưa có target/pair/isolation để chạy. Pilot tương lai cần packet mới theo R4a/R4b và applicability của gate gốc. Những lỗi17/28,23/28 và các suite42/42,39/39 giữ nguyên lịch sử, không cộng vào40ca mới.
