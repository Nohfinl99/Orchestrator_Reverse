# Biên bản điều phối bốn checkpoint theo giai đoạn sản phẩm

Ngày 24/10/2026. Chỉ thị mới: cải thiện cách chuẩn bị và điều phối; vấn đề chưa giải quyết hoặc cần sản phẩm thật được giữ chờ, cải tiến dần khi có sản phẩm. Đây là quyết định quản lý công việc, không phải chấp nhận threshold hay đóng checkpoint.

## Phiên họp và căn cứ

Chair/producer `/root` tổng hợp ba phiên thật: `/root/preflight_reviewer` xem A/B; `/root/pentest_executor` tư vấn implementation C trong phiên này, **không thực thi**; `/root/postrun_reviewer` xem D và tính nhất quán của báo cáo. Các phiên cùng model kế thừa, không phải human/cross-model review hoặc sáu identity runtime đã deploy. Owner ở bảng dưới là trách nhiệm tương lai theo [sáu identity hiện hữu](../../architecture/agents.md), không phải receipt dispatch.

Căn cứ: [24 tiêu chí gốc](README.md), [status v3](status-v3.json), [repair và R4b](repair-2026-10-24.md), [packet lịch sử](packet.md), [benchmark plan](benchmark-plan.md) và [W4 readiness](../../planning/w4-readiness-plan.md). Chỉ đọc các phần phục vụ objective này; không tuyên bố audit lại toàn bộ archive. Advisory/review local ở `evidence/orchestrator_meetings/20261024_checkpoint_deferral_01`.

## Cải thiện ngay trong lượt này

1. Lập sổ chờ bên dưới cho đủ 18 tiêu chí chưa đóng: mỗi tiêu chí có owner, điều kiện mở lại và bằng chứng cần nhận. Các tiêu chí đã verify giữ scope lịch sử, không mặc định còn fresh cho sản phẩm tương lai.
2. Chuẩn bị [mẫu packet pilot sản phẩm](product-pilot-template.json): caller/source pin, original input/digest, diff đề xuất, taxonomy, knowledge/ACK, profile/budget, R4a/raw/R4b và rollback. Trường chưa có để `null`; mẫu **không dispatch được**, chưa là implementation hoặc schema validator.
3. Đổi next action từ cố đóng toàn bộ checkpoint sang pilot nhỏ: một objective, một caller, một consumer, đúng dependency. Phần cần sản phẩm chờ sản phẩm; phần chờ quyết định/review được ghi riêng, không ép anh quyết định trong cuộc họp này.

Không chạy suite, provider, model, REA/IDA, target, sanitizer, training hoặc W4 trong lượt lập kế hoạch này. Kết quả42/42 là lịch sử của packet sửa trước, không có thêm ca test mới. Không sửa source, raw hoặc oracle đã freeze.

## Hai loại trạng thái phải đọc riêng

- **Evidence:** giữ nguyên VERIFIED/PARTIAL/PENDING/NOT_RUN trong status v3. Mẫu số luôn sáu tiêu chí mỗi checkpoint.
- **Công việc:** `DEFERRED_DECISION` chờ quyết định theo scope; `DEFERRED_DEPENDENCY` chờ nguồn/review hoặc prerequisite; `DEFERRED_PRODUCT` chờ caller/consumer/runtime sản phẩm cụ thể. Các nhãn này không đổi PASS/FAIL, không tự unblock và không xóa backlog.

| Checkpoint | Tiêu chí đã verify | Phần giữ chờ |
|---|---|---|
| INPUT-A | 3/6 — 50% | Adjudicate seed riêng, chọn mục đích đánh giá, nhận criteria/threshold |
| KNOWLEDGE-B | 3/6 — 50% | Review bundle/use, ACK thật và admission |
| IMPLEMENTATION-C | 0/6 — 0% | Pipeline đúng caller; C6 mới có bằng chứng component hữu hạn |
| EVALUATION-D | 0/6 — 0% | Benchmark model/REA thật đúng profile và prerequisite |

Không cộng trung bình thành tiến độ toàn sản phẩm. Sáu tiêu chí đã verify là A1/A2/A4/B1/B2/B3;18 tiêu chí còn lại dưới đây không được tính điểm. 0% ở C/D không có nghĩa toàn bộ code đã chạy đều FAIL.

## Sổ chờ và điều kiện mở lại

| ID | Trạng thái công việc / owner | Mở lại khi có gì | Bằng chứng để xét đóng |
|---|---|---|---|
| A3 | DEFERRED_DEPENDENCY — Evidence-Synthesizer | Objective/set đọc nguồn được chọn, reviewer khác producer sẵn sàng | Adjudication từng seed S01–S06 với locator/digest/uncertainty và freeze; review42ca khác không thay thế |
| A5 | DEFERRED_DECISION — Prompt-Master | Chọn mục đích đánh giá cho use case | Quyết định source-only rõ scope, hoặc raw input/refusal với ground truth về phạm vi hỗ trợ; không bắt buộc model run nếu đã chọn source-only |
| A6 | DEFERRED_DECISION — Prompt-Master | Anh nhận/revise criteria/threshold theo scope cụ thể | Decision có revision; giao chuẩn bị hay trì hoãn không tự là nhận ngưỡng |
| B4 | DEFERRED_PRODUCT — Evidence-Synthesizer | Chọn bundle, consumer, mục đích và đường dữ liệu | Rights/source locators và applicability review; UNKNOWN giữ pending, không loại theo nhãn DAN/chủ đề |
| B5 | DEFERRED_PRODUCT — Prompt-Master | Có consumer thật với context và bundle cụ thể | ACK thật bind identity/context/bundle digest/revision/use/invalidation; không lấy caller flag làm ACK |
| B6 | DEFERRED_PRODUCT — Evidence-Synthesizer | Có bundle/consumer packet cùng evidence B4/B5 | Admission review độc lập đúng scope; R4b component không thay KB admission |
| C1 | DEFERRED_PRODUCT — Prompt-Master | Có một caller được chọn và dependency compatibility đủ | Source map/call path/revision và raw tích hợp; archived builder chưa là active caller |
| C2 | DEFERRED_PRODUCT — Prompt-Master | Thiết kế lưu input ở boundary của caller đã chọn | Original bytes/locator, revision/digest và các lần sửa có lineage; không ghi đè raw |
| C3 | DEFERRED_PRODUCT — Prompt-Master | Caller/provider/tool boundary đã xác định | Raw chứng minh taxonomy đúng layer; không gộp mọi lỗi thành model refusal |
| C4 | DEFERRED_PRODUCT — Prompt-Master | Có input và cách đề xuất sửa trong flow thật | Diff hiển thị, original giữ nguyên, kiểm intent/scope/locators; không che ý định để né reject |
| C5 | DEFERRED_PRODUCT — Prompt-Master | Có flow ambiguity của use case | Case ambiguity hỏi tối đa2–3 câu trọng yếu; case rõ không hỏi thừa; không bịa facts/authority |
| C6 | DEFERRED_PRODUCT — Evidence-Synthesizer | Có revision pipeline và cases cho C1–C5 | Fresh applicable R4a, positive/negative raw, R4b khác producer/executor;42/42 component chỉ là partial |
| D1 | DEFERRED_PRODUCT — Prompt-Master | Sản phẩm cần benchmark cụ thể | Exact model/provider/version hoặc profile REA phù hợp, data policy và numeric cap; không chọn theo tên model chung chung |
| D2 | DEFERRED_PRODUCT — Evidence-Synthesizer | Có objective/profile và bộ case đúng use case | Input/oracle adjudicate, exact revision freeze và applicable R4a trước run |
| D3 | DEFERRED_PRODUCT — Triage-Sentinel | Environment/action của pilot được chọn | Capability/authority/gate evidence; target binding và applicable REA–IDA pair nếu target-dependent; non-target ghi lý do N/A |
| D4 | DEFERRED_PRODUCT — role executor theo task | D1–D3 và prerequisite liên quan đủ | Attempt thật có raw/stdout/stderr/exit/timestamps/budget; không tái dùng receipt lịch sử |
| D5 | DEFERRED_PRODUCT — Evidence-Synthesizer | Có capture đúng accepted freeze | R4b reviewer khác producer/executor, tái tính metrics từ raw; không dựa tự chấm |
| D6 | DEFERRED_PRODUCT — Prompt-Master, anh quyết định | Có metrics được chốt trước run và R4b | Đối chiếu ngưỡng đã nhận, continuation/rollback decision và revision rõ |

Finding bổ sung giữ chờ: checker chưa validate mọi dạng JSON hợp lệ nhưng sai shape, chưa kiểm đủ lỗi ghi receipt/timeout. Trạng thái `DEFERRED_DEPENDENCY`, owner trách nhiệm Prompt-Master điều phối và Evidence-Synthesizer review. Mở lại khi checker được chọn làm interface thật hoặc có task hardening offline riêng với oracle/budget/R4a mới. Không sửa tiếp candidate đã freeze chỉ để tăng số case.

## Lộ trình mở lại khi bắt đầu sản phẩm

1. **Chọn lát cắt nhỏ.** Product-Evolution-Architect chuẩn bị objective/người dùng/giá trị/acceptance proposal; Prompt-Master bind đúng một caller và consumer từ source hiện hữu. Đây là vai trò đề xuất, chưa có runtime Product dispatch binding được xác nhận.
2. **Kiểm dependency.** Rà source drift, B4 oracle/compatibility và các gate gốc áp dụng, bundle/use/rights/context/ACK. Không lấy sự tồn tại của sản phẩm làm đủ điều kiện. Thiếu gì giữ đúng mục đó chờ; không tự mở W4/v3.
3. **Làm pilot theo packet mới.** Lưu original input, revision/diff, taxonomy và ambiguity flow; chọn model theo khả năng/độ khó tại thời điểm chạy nếu cần. Chốt data/budget/case/oracle/metrics và applicable R4a trước bất kỳ execution mới. Không cần target/native pair cho việc chỉ đọc source nếu có lý do applicability được review.
4. **Đo và sửa từng lỗi có bằng chứng.** Executor đúng task tạo raw; reviewer độc lập làm R4b. Fail thì giữ capture, sửa revision mới rồi review lại; stop khi thiếu quyền/prerequisite, drift hoặc hết budget. Rollback về revision đã pin theo packet; không rollback bằng xóa FAIL.
5. **Chỉ xét tiêu chí liên quan.** Có thể tiến một tiêu chí sau khi đủ bằng chứng; anh quyết định nhận checkpoint/threshold. Knowledge REA–IDA và nguyên tắc trung lập giữ qua mọi vòng; không suy đã nạp/training từ việc viết thêm tài liệu.

Đây là hàng đợi có điều kiện, không phải lịch tự chạy hoặc automation. Phiên tiếp theo chỉ mở mục tương ứng khi được giao giai đoạn sản phẩm/nhánh offline và kiểm đủ điều kiện. Không báo nhắc theo thời gian hoặc chạy lại42ca chỉ vì chưa có sản phẩm.

## Quyết định và giới hạn

Giữ P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Không đồng nhất checkpoint **KNOWLEDGE-B/B4** với gate lịch sử **P1K B4**. Giữ sáu identity và mọi source/evidence/FAIL cũ. Cuộc họp hoàn thành bản kế hoạch và mẫu bàn giao; không tuyên bố đã giải quyết các tiêu chí đang chờ.
