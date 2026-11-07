# Roadmap sửa luồng điều phối — 06/11/2026

Revision 1. Phạm vi hiện tại: thiết kế và sửa workflow phiên, review độc lập; implementation/dispatch và benchmark runtime chưa thực hiện. Đây là nhánh sửa luồng, không đổi định danh R0–R6, W0–W7 hoặc G1–G4.

## Mục tiêu gốc và căn cứ

Người dùng yêu cầu dùng model lớn để làm roadmap/review kết quả cuối, model thấp hơn đọc và tổng hợp bằng chứng; Orchestrator giữ input để tránh làm lệch yêu cầu gây reject; giải quyết việc REA/IDA không được dùng, review thiếu trật tự và các agent thiếu bước thống nhất. Bản nguyên văn của yêu cầu và biên bản/review phiên này nằm ở workspace cha `evidence/orchestrator_meetings/20261106_orchestration_repair_01/` (LOCAL_ONLY_NOT_DISTRIBUTED).

Các vấn đề người dùng phản ánh là đầu vào cần điều tra. Chưa có trace prompt/provider của các lần reject được chỉ định trong task này để kết luận nguyên nhân. Không sửa ý định, thêm quyền hay thay từ để né quyết định của model. Phân biệt reject do prompt đổi nghĩa, lỗi contract, thiếu tool/prerequisite và quyết định thực của provider; chỉ gán nguyên nhân khi có evidence tại boundary tương ứng.

Nguồn đã đối chiếu:

- [Task execution](../operations/task-execution.md) và [cognitive routing](../proposals/cognitive-routing/README.md): đã có hướng dẫn giữ mục tiêu/model nhỏ hỗ trợ/model cao review; đây là procedure, chưa router runtime.
- [Local session controller](../operations/local-session-controller.md), `orchestrator_session/core.py` các hàm `create`, `prepare_work`, `report`: giữ original bytes và binding; không dispatch, không kiểm tự động việc prompt giữ nghĩa, không xác thực reviewer.
- [Input CLI](../guides/local-input-pipeline.md), `orchestrator_pipeline/core.py` hàm `prepare`: proposal có unified diff/bundle digest; annotation accept không xác thực danh tính, giữ nghĩa hoặc quyền thực thi. Kết quả `PREPARED_NOT_DISPATCHED` ghi model/tool/native calls bằng 0. Không viết lại phần custody/diff đã có.
- [Kiến trúc](../architecture/system.md), mục bảo toàn REA–IDA và routing/state: invariant, applicability và không ép consensus đã có; roadmap nối các yêu cầu này vào caller thực, không tạo nguyên lý mới. Với non-target, giữ field pair/status theo contract gốc (`null`/`NOT_RUN`), applicability ghi riêng.
- [Input finding INPUT-01](../reference/open-questions.md) và [REA update](../knowledge/rea-update-2026-10-24.md): scope sanitizer lịch sử không đủ chứng minh active request bị rewrite hoặc nguyên nhân reject. Giữ archive nguyên byte.
- [Native local](../proposals/input-pipeline/local-native-2026-10-24.md): đã có direct IDA static inventory trong scope lịch sử; REA–IDA pair/ACK chưa established. “Chưa dùng pair” khác với “chưa từng chạy IDA”.
- [Loop guard](../operations/local-loop-guard.md): local opt-in, không runtime broker. Tiếp tục dùng receipt hợp lệ sau revalidation; không reset M0–M4 để viết lại từ đầu.

## Luồng áp dụng ngay trong phiên

`original → evidence → roadmap/task DAG → chốt kế hoạch → producer → review đúng revision → chốt kết quả → handoff`

Prompt-Master điều phối và giữ mục tiêu. Evidence-Synthesizer gom evidence/review; owner chuyên môn chọn trong [sáu identity](../architecture/agents.md). Tên model hoặc tên phiên không là identity thứ bảy. Model thấp hơn đọc nguồn, trích locator, phân loại claim/unknown và trả evidence packet; model lớn phân rã, giải quyết logic khó, review roadmap và final. Ghi model thực được yêu cầu và nguồn quan sát; nếu host không trả attestation thì không gọi đó là danh tính đã xác thực.

Mỗi handoff có original hoặc locator/digest truy cập được, objective dẫn xuất tách riêng, scope, revision, dependencies, output, acceptance, tool thật và stop. Tóm tắt chỉ bổ sung context; không thay original. Khi cần prompt dẫn xuất, giữ diff và mapping từng yêu cầu sang task/criterion. Không thêm mục tiêu, quyền hoặc loại bỏ thuật ngữ làm thay đổi nghĩa. Câu mơ hồ ảnh hưởng hành động thì hỏi đúng phần đó; phần rõ và độc lập tiếp tục.

### Hai điểm thống nhất

Trước producer: reviewer kiểm kế hoạch theo original; coordinator ghi kế hoạch được chọn, finding đã giải quyết, bất đồng/gap còn mở, nhánh được đi tiếp và nhánh chờ. Sau producer: reviewer đọc exact artifact/revision và sources; coordinator ghi disposition từng finding và từng criterion, rồi chốt kết quả. Không dispatch bước phụ thuộc chỉ vì đã có buổi họp.

Decision record tối thiểu: decision ID; original/task/candidate revision hoặc digest; producer/reviewer/model và nguồn quan sát; criterion/finding; evidence locator; ý kiến/objection; disposition và lý do; owner; next/stop/reopen. Phiên chưa có artifact thì review thiết kế, không review execution. Thay artifact sau review thì review lại phần bị ảnh hưởng và dependency.

Thống nhất là có một quyết định và next action chung được ghi nhận, không phải mọi agent bắt buộc đồng ý. Bất đồng có căn cứ được giữ; finding ảnh hưởng tiêu chí bắt buộc chưa xử lý thì `REVISE_NOT_ACCEPTED` hoặc chặn đúng nhánh. Coordinator có thể quyết định phần trong scope với lý do/evidence, không thể biến phản đối còn đúng thành PASS. Tối đa hai vòng document review mỗi task/candidate; không đổi tên hoặc thêm agent để reset cap. Hết cap ghi owner/điều kiện mở lại và tiếp tục nhánh độc lập.

## Các bước và tiêu chí nghiệm thu

Các mã OR dưới đây chỉ là work-item của roadmap này. Trạng thái baseline: OR-0/OR-1 là việc tài liệu đang review; OR-2–OR-6 chưa triển khai/chạy trong phiên này.

| Bước | Dependency / owner | Output và điều kiện hoàn thành |
|---|---|---|
| OR-0 Evidence baseline | Độc lập; Evidence-Synthesizer, model nhỏ | Locator/revision, observation/inference/user report tách riêng; những gì đã đọc và chỉ kiểm kê; known/gap. Model lớn kiểm lại claim trọng yếu với source |
| OR-1 Roadmap + quyết định kế hoạch | OR-0; Prompt-Master, model lớn; reviewer độc lập | Đủ bốn vấn đề, dependency/acceptance/owner; ghi finding/disposition và quyết định chung. Đóng tài liệu không tính runtime đã sửa |
| OR-2 Bind một caller gửi prompt thật | OR-1; Prompt-Master chọn owner source phù hợp | Chọn call site/consumer cụ thể, exact revision, original→task→prompt trace, phạm vi thay đổi, output contract và numeric calls/cost/time/retry budget trước attempt. Không tạo broker song song hoặc ngầm thay Stage1 parser. Prerequisite B4/compatibility nếu áp dụng thì giữ blocked đúng nhánh |
| OR-3 Giữ input tại boundary | OR-2; producer source được giao; Evidence-Synthesizer review | Original bytes/digest được reuse; derived instruction tách riêng; mapping/diff trước send; actual outbound payload capture trong quyền/phạm vi đã giao. Bảo toàn ý nghĩa kiểm độc lập, không suy từ hash. Rejection giữ raw response/reason và causal classification có evidence; UNKNOWN nếu không đủ |
| OR-4 REA/IDA theo applicability | OR-1; Triage-Sentinel → Decomp-Analyst | Với native task: target/component/slice digest, REA workflow/ledger + IDA/IDB state/version/transport và receipts liên kết đúng state; review pair/ACK/prerequisite trước phần phụ thuộc. Với managed/Electron/browser/firmware artifact: chọn REA workflow đúng loại, IDA khi có native state cần phân tích; phần không áp dụng ghi rõ theo contract, không miễn pair cho target consumer vốn yêu cầu pair. Crypto chỉ khi evidence cần. Với source/docs: ghi lý do không áp dụng, không gọi RE tools để đủ số. Direct IDA giữ nhãn standalone khi pair chưa chứng minh |
| OR-5 Review và quyết định trong caller | OR-2; Prompt-Master + Evidence-Synthesizer | Gắn plan decision trước execution và final decision sau review exact output; invalidation khi revision đổi; finding unresolved chặn đúng downstream; evidence và reviewer origin có provenance, không tin label caller tự khai. Reuse helper M0–M4 theo giới hạn đã công bố |
| OR-6 Pilot end-to-end | OR-3/OR-5; OR-4 nếu task artifact/target áp dụng; producer/reviewer tách biệt | Packet có expected outcome tách output, target/profile/quyền/tool/budget thật và prerequisite đúng scope. Reviewer freeze oracle/criteria/threshold/exclusions trước run, applicable R4a trước attempt; R4b kiểm raw và exact result sau run theo [evaluation plan](../proposals/input-pipeline/evaluation-plan.md). Trace nối original→outbound→response→artifact→review→decision; báo criterion đạt/chưa đạt/chưa chạy, không chỉ đếm test xanh. Đổi oracle thì revision/attempt mới, giữ kết quả FAIL cũ |

OR-3 và OR-5 có thể thiết kế song song sau OR-2. OR-4 không chặn nhánh source/docs độc lập. Thiếu pair, provider hay tool chỉ chặn nhánh phụ thuộc; không biến toàn yêu cầu thành từ chối. Không khẳng định mọi reject sẽ hết: đo trên bộ ca và trace đã freeze/review, báo n/N giữ nghĩa theo oracle, sai nghĩa đã phát hiện, reject/block có căn cứ và trường hợp unresolved. Semantic review vẫn có blind spots; không ngoại suy thành bảo đảm cho mọi input.

### Bộ tình huống đề xuất cho OR-6

Chưa phải suite đã chạy. Reviewer giữ expected outcome độc lập với worker output:

1. Yêu cầu có thuật ngữ dễ bị sửa nghĩa: original giữ byte, derived mapping đủ và không thêm quyền.
2. Yêu cầu nhiều nhánh, một nhánh thiếu tool: tiếp tục phần độc lập, gap cụ thể và next action.
3. Native artifact: REA evidence và IDA state được bind đúng; standalone IDA không được báo pair PASS.
4. Source/docs bình thường: chọn owner thích hợp và giải thích applicability; không ép REA/IDA execution.
5. Reviewer bất đồng: lưu objection/disposition, dừng đúng nhánh khi criterion bắt buộc chưa đạt.
6. Artifact đổi sau review hoặc worker tự gán PASS: review cũ bị stale; không nhận hoàn tất từ label.
7. Cùng failure không evidence mới: stop/reopen theo cap; không họp/retry vô hạn.
8. Rejection tại provider hoặc lỗi contract: giữ response/error gốc, không đổi ý người dùng để thử né; nguyên nhân chưa chứng minh ghi UNKNOWN.

## Việc tiếp theo và giới hạn

Next atomic task: OR-2, đọc projection/caller hiện có để chọn đúng một send boundary và soạn packet triển khai; chưa có caller/profile/target cụ thể được bind từ yêu cầu hiện tại. Evidence local phiên này phải ghi quyết định và kết quả review thực trước khi báo OR-1 xong. Không dùng roadmap này làm receipt triển khai hoặc mở lại mọi product pilot đã defer.

Giữ P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Gate chỉ đổi bằng evidence và quy trình đúng scope. Archive, source pins lịch sử, mười stack và mười protocol giữ nguyên.
