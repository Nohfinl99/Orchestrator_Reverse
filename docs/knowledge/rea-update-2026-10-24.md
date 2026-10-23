# REA và input/handoff — knowledge candidate 24/10/2026

Trạng thái: CANDIDATE_REFERENCE_NOT_ADMITTED, static/source review, chưa consumer ACK. Đây là ghi nhận mới trong folder; không nâng cấp package/skill/MCP hoặc chứng minh runtime đã dùng các kiến thức này. Policy [trung lập revision 2](knowledge-policy-v2.md) vẫn áp dụng.

## Input có bị viết lại không?

Kiểm source local cho thấy ba đường khác nhau:

| Nguồn workspace-relative, LOCAL_ONLY | Observation tĩnh | Giới hạn |
|---|---|---|
| `src/candidates/prompt_contract.py:175–230` | Ghép task/role/policy và evidence refs; `PREPARED_NOT_DISPATCHED`, dispatch chưa implemented | Không thấy bộ tự viết lại input để né model refusal trong candidate này. |
| `archive/RE-Decom/01_control_plane/prompt_master.py:430–433,534–537` | `task_message` được đưa vào prompt; `sanitized_user_prompt = raw_user_prompt`, comment ghi no sanitization | Tên biến/import sanitizer không chứng minh sanitizer được gọi tại builder này; code có chunking evidence theo budget được gắn nhãn. |
| `archive/RE-Decom/01_control_plane/rea_ledger.py:28–55,92–94,292–317` | Có `AntiRefusalSanitizer`; tạo handoff gọi sanitizer trên summary; một method khác trả projection của source facts | Đây là thành phần có mục đích anti-refusal được ghi trong source. Chưa chạy, chưa đo hiệu quả và không chứng minh mọi user input đi qua nó. |
| `archive/RE-Decom/01_control_plane/orchestrator.py:751,811,867` | Có call site tạo handoff trong pipeline source | Chưa xác thực pipeline/session live hiện đang dùng source đó. |

Trong phần đã đọc, formatter dùng raw `source_facts`; ledger lưu facts như dữ liệu nguồn. Chưa thấy caller của `get_academically_framed_facts` trong các file Python dưới `archive/RE-Decom/01_control_plane` được tìm bằng symbol search. Đây là kết quả tìm giới hạn, không phải kết luận toàn workspace không có caller.

Đính chính phạm vi nhận định trước: “chưa thấy code né refusal” chỉ phù hợp candidate/builder được xét; không phù hợp nếu áp cho toàn archive vì sanitizer/handoff component có tồn tại. Không có bằng chứng cho lời hứa “refusal-proof” trong docstring. Không sửa hoặc chạy sanitizer để kiểm giả định đó.

Loader lịch sử ở `prompt_master.py:135–152,470–484` đọc fewshot JSON và gắn nhãn KNOWLEDGE_BASE_REFERENCE, khác target evidence. Vault local được kiểm kê có nhóm anti-debug, crypto S-box, decomp structure và unpacking. Sự hiện diện/loader không chứng minh rights/admission/consumer ACK hoặc model đã nhận. DAN trong policy mới là chủ đề được phép catalog/nghiên cứu; policy không đồng nghĩa corpus DAN đã được ingest.

## Đối chiếu REA upstream

Nguồn trực tiếp kiểm ngày 24/10: [npm metadata](https://registry.npmjs.org/rea-agents/latest), [release 6.7.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.7.0), [main đã pin](https://github.com/morluto/rea/commit/5d2c8c2b78d2552da0e13a11d3e2678efb69810d). npm latest và GitHub latest đều là 6.7.0, phát hành 18/10/2026. Main có thay đổi sau release nhưng package.json vẫn ghi 6.7.0; cùng số package version không chứng minh cùng source.

Skill local tại `C:/Users/Admin/.agents/skills/reverse-engineer-anything/SKILL.md` ghi metadata version 42; skill của release 6.7.0 cũng ghi 42. [Skill main đã pin](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/.agents/skills/reverse-engineer-anything/SKILL.md) ghi version 45. Các số 42/45 là revision skill, không là package version. Phiên hiện quảng bá 207 REA tools; số này không tự xác định npm runtime build. Không tìm được `rea` qua PATH ở lượt kiểm; chưa xác định package runtime đang chạy.

## Kiến thức mới có thể dùng cho proposal

| ID | WHAT / WHY / HOW | Source và giới hạn |
|---|---|---|
| REA-U01 | Phân biệt host deadline, server deadline và công việc còn chạy; trước retry xét operation có thể đã thay state. Dùng cho thiết kế bounded retry của Orchestrator. | [Recovery guide](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md). Chưa thay retry contract/runtime của project. |
| REA-U02 | PyInstaller CArchive là lớp app cần inventory, không chỉ phân tích native bootloader. Chọn artifact route trước deep native analysis. | [Python packages](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/docs/python-packaged-applications.md). Inventory/extraction không bằng decompile Python hoặc execute app. |
| REA-U03 | APK signer/certificate/digest observations hỗ trợ identity và integrity; không tự là trust verdict. Dùng khi thiết kế provenance checks. | [APK signing](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/docs/apk-signature.md). Không gọi tool hoặc đánh giá APK thật trong lượt này. |
| REA-U04 | GGUF/safetensors metadata có thể đọc như artifact mà không inference. Dùng để phân biệt model declaration với khả năng model đã chứng minh. | [Model artifacts](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/docs/model-artifacts.md). Header/tensor metadata không chứng minh hành vi hoặc chất lượng model. |
| REA-U05 | IL2CPP metadata có thể cho name/owner/string và index có nguồn trước khi ghép native observations. Giữ metadata và native identity riêng. | [IL2CPP](https://github.com/morluto/rea/blob/5d2c8c2b78d2552da0e13a11d3e2678efb69810d/docs/il2cpp-metadata.md). Không suy đúng build hoặc runtime behavior từ tên file. |
| REA-U06 | Main commit nêu thay đổi CLI row-oriented export sang JSON Lines. Adapter dùng output CLI cần review format tương ứng revision. | [Commit đã pin](https://github.com/morluto/rea/commit/5d2c8c2b78d2552da0e13a11d3e2678efb69810d). Chỉ đọc metadata commit, chưa review implementation/export suite; không khẳng định npm 6.7.0 có cùng behavior. |

U02–U05 là route mới được mô tả trong skill main so với skill local đã đọc. Các tool mới tương ứng không được quảng bá trong phiên hiện tại. Không dùng tài liệu main để giả lập capability; muốn sử dụng cần kiểm schema/provider thực trong task cụ thể. Raw snapshots/diff và source SHA-256 được giữ ở workspace `evidence/upstream_review/20261024_rea_input_audit_01` (LOCAL_ONLY_NOT_DISTRIBUTED). Đã đọc opening sections/selected headings ở các guide, không audit toàn implementation hoặc mọi guide upstream.

## Cách điều phối input nên đề xuất

Nếu cần làm rõ một yêu cầu hợp lệ để model hiểu đúng: giữ original input và digest, tạo bản diễn đạt có mục tiêu/scope/nguồn/quyền quan sát được, hiển thị diff cùng lý do thay đổi, kiểm giữ nguyên ý định và thuật ngữ/locator/raw evidence. Ghi rõ rejection đến từ packet integrity, thiếu authority/capability, tool/provider error hay model refusal; không gộp mọi lỗi thành “AI reject”. Thiếu quyết định trọng yếu thì hỏi phần đó. Không đổi nhãn hoặc giấu ý định để che nguyên nhân từ chối; thay wording không bảo đảm model chấp nhận.

Đây là proposal về tính minh bạch và kiểm giữ nghĩa, chưa có adapter rewrite/audit được triển khai hoặc test. Không sửa archive/raw, không chạy fixture; REA–IDA và mọi gate kế thừa giữ nguyên.
