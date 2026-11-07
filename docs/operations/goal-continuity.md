# Giữ mục tiêu qua điều phối và review

Áp dụng trong phiên Orchestrator. Đây là quy tắc cho người/agent và phần hiển thị của CLI local, chưa là broker enforcement hay bộ kiểm nghĩa tự động. [Ca review và roadmap](../planning/orchestration-repair-2026-11-06.md) dẫn nguồn local. Không đổi sáu identity, phase, gate hoặc các protocol đã freeze.

## Original là căn cứ xuyên suốt

Giữ nguyên yêu cầu gốc và các quyết định user sau đó, tách khỏi objective của bước. Trước handoff, ghi frame ngắn:

| Trường | Nội dung phải có |
|---|---|
| Original | Nguyên văn hoặc locator đọc được + revision/digest khi có file; không chỉ tóm tắt |
| Active goal | Mục tiêu hiện hành theo original cùng các chỉ thị/làm rõ mới nhất của user; exact decision/message locator, phần kế thừa và phần được user sửa |
| Kết quả user cần | Các outcome/criterion theo original; phân biệt cách diễn giải của coordinator với câu user nói |
| Bước đang giao | Làm phần nào, phục vụ outcome nào; output/acceptance của bước không thay acceptance toàn việc |
| Đã loại/bỏ/chưa nhận | Nhánh cụ thể, reason/source, trạng thái chưa làm; không xóa khỏi mục tiêu theo dõi |
| Alternative | Mô tả thay đổi outcome; pending hay được user chọn, exact message/decision locator và phạm vi lựa chọn |
| Goal còn lại | Đã làm/chưa làm, next/stop và điều kiện mở lại; không tự dispatch nếu nhánh bị dừng |

Nếu original không có trong handoff, worker/reviewer tìm qua locator trước. Không truy cập được thì báo `ORIGINAL_NOT_AVAILABLE`, chỉ review được phần local; không cấp goal-level acceptance. Có context chung không tự chứng minh đã đọc/đối chiếu original.

## Từ chối, blocker và thay đổi mục tiêu

Từ chối một nhánh là disposition của nhánh đó. Nêu rõ phần không làm, căn cứ và ảnh hưởng tới mục tiêu; giữ original cùng trạng thái chưa giải quyết. Không tự chuyển thành một bài toán khác rồi mô tả đó là đã đáp ứng yêu cầu. Không đổi từ, giấu mục đích hoặc chia agent để vượt một giới hạn thực sự áp dụng.

Một alternative có outcome khác phải được ghi rõ là proposal riêng. Chỉ thực hiện phần đó khi chỉ thị user hiện có thực sự bao phủ nó; nếu chưa có thì giữ pending và có thể hỏi một câu lựa chọn trọng yếu. User chọn làm alternative hoặc một nhánh phụ không tự nghĩa là user rút/thay mục tiêu gốc. Chỉ ghi original được thay/rút khi có quyết định user rõ về việc đó. Dù được rút/thay, original không được đánh dấu đã đạt.

User có thể làm rõ hoặc sửa phạm vi bằng ngôn ngữ tự nhiên; không cần mẫu câu hay quyết định theo một schema. Chỉ thị mới rõ ràng xác định scope đang làm phải được áp dụng, giữ yêu cầu trước làm lịch sử và ghi quan hệ thay đổi. Không tiếp tục gán mục đích cũ cho mọi yêu cầu sau khi user đã làm rõ; cũng không xóa context liên quan khi đánh giá hành động cụ thể. Phân biệt user nói rõ “chỉ làm X, không làm Y” với việc chỉ đồng ý một bước X trong dự án còn Y. Nếu chưa rõ quan hệ và nó ảnh hưởng hành động, hỏi đúng phần đó, không tự chọn thay user.

Handoff và review đối chiếu **active goal**, không bắt output đạt một mục tiêu lịch sử đã được user sửa. Nếu lượt làm rõ thất bại trước khi assistant trả lời, ghi failure đúng actor/message, không suy user chưa làm rõ hoặc đã có agent thực thi; khi tiếp tục phải đọc chỉ thị mới cùng context liên quan.

Không hỏi lại cho việc diễn đạt tương đương, chia task, chọn công cụ hay phần việc đã được chỉ thị hiện tại bao phủ. Kiểm thay đổi **outcome**, không bắt user phê duyệt từng câu chữ. Diễn đạt lại phải giữ ràng buộc và mục đích, không giả rằng diff/hash chứng minh cùng nghĩa.

Blocker chỉ áp cho câu hỏi/nhánh có dependency tương ứng. Ví dụ thiếu symbol để xác minh một backtrace không tự chứng minh mọi static question đều bị chặn. Kiểm tool/capability thật trước báo thiếu; ghi riêng NOT_CHECKED, UNAVAILABLE, ERROR hoặc NOT_APPLICABLE. REA giữ workflow/evidence/ledger; IDA giữ native/decompiler/IDB state. Không bắt gọi engine cho mọi task và không dùng receipt của ca khác để nhận đã làm ca này.

## Câu hỏi bắt buộc của từng trách nhiệm

Đây là checklist trách nhiệm, không yêu cầu khởi động đủ sáu agent hoặc dựng lời đối thoại không xảy ra.

| Identity | Câu chất vấn và hành động |
|---|---|
| Prompt-Master | Tôi đang giao đúng kết quả user cần hay kết quả dễ hơn? Mọi phần cắt bỏ có disposition chưa? Ai chọn alternative và chọn ở phạm vi nào? Giữ original, branch mapping và user decision trong handoff |
| Triage-Sentinel | Tôi đã kiểm capability/input thật hay suy từ tên tool? Blocker này chỉ ảnh hưởng câu hỏi nào? Trả evidence/locator, không nâng inventory thành phân tích hoàn tất |
| Decomp-Analyst | Claim về luồng cần state/image/function nào? Tôi đang trả lời câu hỏi gốc hay câu crash khác? Ghi phần chưa chạy, pair/state/ACK áp dụng và giới hạn từng claim |
| Crypto-Logic-Specialist | Có câu hỏi algorithm phù hợp không? Nếu không, ghi N/A; không gọi review Crypto để đủ số hoặc làm lý do chặn toàn task |
| Evidence-Synthesizer | Output đúng với original nào? Criterion có bị thay bằng criterion của nhánh phụ không? Review source/trace và phản chứng; ghi local acceptance riêng, giữ goal chưa đạt rõ ràng |
| Product-Evolution-Architect | Alternative có thay outcome/success criterion không? Có quyết định user đúng phạm vi không? Proposal hữu ích không thay quyền chọn mục tiêu của user; product role chỉ khi thực sự applicable |

## Hai quyết định và kết quả cuối

Chốt kế hoạch trước bước phụ thuộc: mapping đủ original→branch→criterion, tool applicability và alternative decisions. Chốt sau review: đối chiếu original, artifact đúng revision và từng criterion; record finding, dissent, disposition có lý do và next/stop. Giữ cap hai vòng document review; không họp lại chỉ để có câu đồng ý.

Mapping phải có original→user revisions→active goal→branch→criterion. Tách criterion còn áp dụng khỏi criterion lịch sử được user sửa/rút; không bắt review viên tự suy quan hệ này từ context chung.

Kết quả phải tách:

- **Bước/alternative:** đã làm và review những gì, theo criterion nào.
- **Mục tiêu gốc:** đã đạt phần nào, chưa đạt/từ chối/chờ gì; được user rút/thay nếu có source rõ.

`PASS_FOR_DOCUMENT`, test xanh, thống nhất agent hoặc user đồng ý bước tiếp theo không tự là original goal DONE. Nếu goal chưa đạt thì nêu ngay, không chỉ để trong phụ lục. Không xóa lịch sử refusal hoặc FAIL khi tạo scope mới.

## CLI local và giới hạn

`session_task check/report` hiển thị `goal_review`: original được giữ ở đâu, digest/encoding, objective/scope/acceptance/provenance do caller khai, alignment chưa xác minh và original resolution chưa established. Root phải mở original và đối chiếu; CLI không hiểu nghĩa, xác thực user decision hoặc quyết định refusal có đúng hay không. Các criterion hiển thị là của request caller đã pin, chưa chứng minh là đủ criterion gốc của user.

Sửa hiển thị này giúp review trên CLI đang có; nó không ép host assistant dùng CLI và không ngăn một root bỏ qua quy tắc. Bằng chứng mạnh hơn phải đến từ kiểm handoff/trace thật và pilot đúng scope. Không nhận là đã loại trừ mọi drift, giảm refusal hoặc nối runtime từ thay đổi này.
