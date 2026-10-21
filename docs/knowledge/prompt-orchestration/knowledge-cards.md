# Knowledge cards cho điều phối

View đọc của [knowledge.json](knowledge.json), revision 1. Trạng thái chung: `CANDIDATE_REFERENCE_NOT_ADMITTED`; self-review một phiên, chưa review độc lập và chưa consumer ACK. WHAT là ý nguồn/quan sát tĩnh; WHY/HOW/CHECK là diễn giải áp dụng có giới hạn cho project, chưa là kết quả execution. [Nguồn và phạm vi đọc](sources.json); [cách tra cứu](retrieval-guide.md).

## K01 — Task có đầu ra và tiêu chí kiểm được

- **WHAT:** Nguồn tách role, bối cảnh, task, ràng buộc, định dạng và ví dụ khi cần.
- **WHY:** Giúp người nhận biết phải tạo artifact nào và căn cứ nào đủ để bàn giao.
- **HOW:** Dùng như checklist soạn proposal: chốt một objective; map owner hiện hữu; nêu input/revision, output, acceptance và phần còn thiếu. Các field authority/budget/dependency phải lấy từ contract project.
- **Áp dụng:** Prompt-Master; đường dẫn phase tham khảo W0, W1.
- **Giới hạn:** Cấu trúc câu lệnh không chứng minh capability, quyền hoặc task đã admitted; không thay schema hiện hữu.
- **CHECK đề xuất:** Người nhận chỉ ra được output và acceptance; field thiếu vẫn ghi UNKNOWN, không tự điền.
- **Nguồn:** [S3-ANATOMY: 7–181](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/02-anatomy-of-effective-prompt.mdx#L7-L181).

## K02 — Nạp context theo câu hỏi và giữ locator

- **WHAT:** Nguồn mô tả retrieval phần liên quan và tóm tắt quyết định, mục tiêu, câu hỏi còn mở để quản lý context.
- **WHY:** Giảm việc nạp nguyên corpus hoặc mất quyết định sau khi chuyển phiên.
- **HOW:** Bắt đầu từ current/source map; chọn phần đúng role/task; tóm tắt trạng thái và giữ đường dẫn/revision/digest để mở lại nguồn. Ghi cả nguồn không chọn và lý do.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W0, W2.
- **Giới hạn:** Tóm tắt có thể bỏ sót chi tiết. Ngưỡng token trong ví dụ không trở thành budget project; chưa triển khai RAG/embedding.
- **CHECK đề xuất:** Mỗi trạng thái quan trọng truy về nguồn; phần chưa đọc hoặc thiếu nguồn không biến thành fact.
- **Nguồn:** [S3-CONTEXT: 49–94](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14-context-engineering.mdx#L49-L94); [S3-CONTEXT: 155–237](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14-context-engineering.mdx#L155-L237); [S3-CONTEXT: 259–273](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14-context-engineering.mdx#L259-L273).

## K03 — Chọn dạng dependency trước khi chọn agent

- **WHAT:** Nguồn phân biệt chain tuần tự, song song, có điều kiện và lặp.
- **WHY:** Làm rõ bước nào cần kết quả trước, bước nào độc lập, và bước nào chỉ mở khi có predicate.
- **HOW:** Đánh dấu dependency và predicate trong proposal DAG. Chỉ cân nhắc song song khi input/state không xung đột và execution đã được cấp đúng phạm vi; route vẫn theo sáu identity hiện hữu.
- **Áp dụng:** Prompt-Master; đường dẫn phase tham khảo W1, W4.
- **Giới hạn:** Lượt trích xuất không dispatch agent. Ví dụ routing theo confidence không thay integrity/capability/gate checks; Crypto vẫn có điều kiện riêng.
- **CHECK đề xuất:** Không có node dùng output chưa được kiểm; mỗi nhánh conditional có nguồn predicate và owner hợp lệ.
- **Nguồn:** [S3-CHAIN: 66–131](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/11-prompt-chaining.mdx#L66-L131).

## K04 — Kiểm artifact trước khi chuyển giao

- **WHAT:** Nguồn yêu cầu kiểm intermediate output và quy định dữ liệu thiếu thay vì bịa giá trị.
- **WHY:** Một output sai có thể lan sang mọi bước sau dù định dạng nhìn hợp lệ.
- **HOW:** Ở bước chuẩn bị, liệt kê check cú pháp, schema và đối chiếu source; khi có execution được phép, consumer kiểm artifact/revision/dependency trước dùng và ACK theo contract gốc.
- **Áp dụng:** Evidence-Synthesizer, Prompt-Master; đường dẫn phase tham khảo W2, W4, W5.
- **Giới hạn:** JSON parse được không chứng minh semantics, provenance hay authority. null của ví dụ không thay enum UNKNOWN/CONFLICT/WAIT trong project.
- **CHECK đề xuất:** Có check nguồn và semantics bên cạnh parse; không phát ACK thay consumer.
- **Nguồn:** [S3-CHAIN: 273–293](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/11-prompt-chaining.mdx#L273-L293); [S3-OUTPUT: 150–161](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/05-structured-output.mdx#L150-L161); [S3-OUTPUT: 371–391](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/05-structured-output.mdx#L371-L391).

## K05 — Vòng lặp có tiêu chí thành công, lỗi và hết ngân sách

- **WHAT:** Nguồn đề nghị contract gồm goal, state, action, observation, evaluator, success/failure và budget; so bằng chứng với tiêu chí rồi quyết định bước sau.
- **WHY:** Giúp phát hiện retry vô hạn, drift mục tiêu và dừng do hết budget nhưng báo nhầm thành công.
- **HOW:** Đối chiếu packet với ba điều kiện dừng và số attempt/time/token/cost được phép. Trước retry phải giữ kết quả attempt và nguyên nhân đổi chiến lược; số vòng lấy từ contract hiện hành.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W4, W5.
- **Giới hạn:** Không nhận giới hạn 3–5 vòng của chương chaining làm mặc định; không tự giải quyết RETRY/caller-halt gap của project.
- **CHECK đề xuất:** Mỗi quyết định tiếp tục/dừng có observation, predicate và budget còn lại; hết budget không mang verdict PASS.
- **Nguồn:** [S3-LOOP: 26–37](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14a-loop-engineering.mdx#L26-L37); [S3-LOOP: 165–183](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14a-loop-engineering.mdx#L165-L183); [S3-LOOP: 289–332](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14a-loop-engineering.mdx#L289-L332).

## K06 — State để tiếp tục phiên là record quyết định và bằng chứng

- **WHAT:** Nguồn phân biệt context của một lượt với state giữ mục tiêu, attempt, artifact/version, verdict, gap và budget giữa các lượt.
- **WHY:** Để agent sau tiếp tục đúng vị trí và tránh lặp lại việc đã thực hiện.
- **HOW:** Bổ sung vào handoff view đường dẫn artifact, revision, check đã chạy, unresolved issues và next action. Khi resume, đọc record và đối chiếu nguồn/binding trước kế thừa.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W4.
- **Giới hạn:** Đây là checklist tài liệu, không thay runtime state schema; checkpoint đọc được chưa chứng minh binding còn hợp lệ. Không lưu private reasoning.
- **CHECK đề xuất:** Người nhận phân biệt được proposed/attempted/verified và nguồn nào cần revalidation.
- **Nguồn:** [S3-LOOP: 248–261](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14a-loop-engineering.mdx#L248-L261); [S3-HARNESS: 214–224](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/26-the-harnesses.mdx#L214-L224).

## K07 — Bằng chứng từ môi trường và vai trò người kiểm

- **WHAT:** Nguồn dùng observation thực, evaluator có rubric và tách người tạo khỏi người kiểm trong công việc quan trọng.
- **WHY:** Giảm khả năng tự đánh giá một câu trả lời hợp lý thành kết quả đã được chứng minh.
- **HOW:** Trong proposal, ghi observable cần thu và evaluator. Tuân thủ R4a trước attempt, raw sau attempt và R4b độc lập theo project; review tài liệu một người chỉ được ghi self-review.
- **Áp dụng:** Evidence-Synthesizer, Prompt-Master; đường dẫn phase tham khảo W5.
- **Giới hạn:** Confidence, số reviewer đồng ý, hash hay source popularity không đủ để đóng gate. Lượt này không thực hiện R4b độc lập hoặc fixture nghiệp vụ.
- **CHECK đề xuất:** Verdict gắn exact artifact/revision và evidence thực; nguồn hướng dẫn không bị dùng làm bằng chứng runtime.
- **Nguồn:** [S3-LOOP: 185–246](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/14a-loop-engineering.mdx#L185-L246).

## K08 — Version prompt và kiểm biến chưa được điền

- **WHAT:** Source schema lưu PromptVersion/ChangeRequest; hàm compile giữ nguyên placeholder nếu không có giá trị hoặc default.
- **WHY:** Prompt có thể đúng bản trước nhưng sai sau sửa, hoặc đi qua pipeline với biến vẫn chưa điền.
- **HOW:** Giữ prompt/template revision, input bindings và assembled digest trong proposal theo manifest gốc. Ghi rõ missing required variables; thay đổi tạo revision mới và review lại đúng digest.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W1, W4.
- **Giới hạn:** Đây là quan sát tĩnh trên repo khác, chưa chạy code; không import compiler/schema hoặc đưa default tự chọn vào field authority/target/budget.
- **CHECK đề xuất:** Phát hiện unresolved placeholders trước dispatch; reviewer thấy được exact assembled revision và nguồn biến.
- **Nguồn:** [S3-SCHEMA: 147–183](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/prisma/schema.prisma#L147-L183); [S3-VARIABLES: 259–297](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/packages/prompts.chat/src/variables/index.ts#L259-L297).

## K09 — Danh mục discovery tách khỏi nguồn đã kiểm

- **WHAT:** Danh mục AI chia tài nguyên theo loại; guidance yêu cầu link canonical và workflow có bước kiểm HTTP/archived.
- **WHY:** Giúp chọn nơi tìm tiếp và phát hiện nguồn đổi tên/hỏng mà không hiểu nhầm một danh sách là knowledge đã xác thực.
- **HOW:** Catalog ghi category, URL, commit đã đọc, read scope, quyền và ngày kiểm. Nguồn ngoài danh mục chưa mở vẫn ghi DISCOVERY_ONLY. Khi drift tạo revision mới; giữ pin lịch sử.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W0, W2.
- **Giới hạn:** Stars/last commit và HTTP 200 không chứng minh chất lượng hoặc source rights. Không sao chép quy tắc xóa row lỗi; giữ tombstone/locator lịch sử nếu cần.
- **CHECK đề xuất:** Không có claim phương pháp lấy từ một link chưa mở; link nguồn và link pin cùng đúng repository.
- **Nguồn:** [S2-RM: 19–64](https://github.com/dukeluo/awesome-awesome-ai/blob/03173a28827eb48d6d5577421825b2e1f06639db/README.md#L19-L64); [S2-GUIDANCE: 10–49](https://github.com/dukeluo/awesome-awesome-ai/blob/03173a28827eb48d6d5577421825b2e1f06639db/CLAUDE.md#L10-L49); [S2-AUDIT: 49–86](https://github.com/dukeluo/awesome-awesome-ai/blob/03173a28827eb48d6d5577421825b2e1f06639db/.github/workflows/weekly-audit.yml#L49-L86).

## K10 — Thiết kế ca biên và no-match từ trước

- **WHAT:** Nguồn liệt kê input trống/dài/sai dạng, giới hạn, adversarial và domain cases; mỗi case có expected behavior và failure indicator.
- **WHY:** Giúp thấy trường hợp thiếu dữ liệu hoặc ngoài scope thay vì chỉ kiểm happy path.
- **HOW:** Đưa vào proposal test matrix các ca input thiếu, nguồn drift, Unicode, dependency chưa đạt và no-match. Tách gold/heldout khỏi KB active; chạy fixture chỉ sau accepted R4a và review độc lập.
- **Áp dụng:** Evidence-Synthesizer, Prompt-Master; đường dẫn phase tham khảo W5.
- **Giới hạn:** Chỉ là ý tưởng test, không phải ca đã chạy. Không đổi oracle/status đã pin hoặc đưa câu trả lời gold vào retrieval.
- **CHECK đề xuất:** Mỗi case có expected outcome và failure signal theo contract, không có fabricated run result.
- **Nguồn:** [S3-EDGE: 65–115](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/12-handling-edge-cases.mdx#L65-L115); [S3-EDGE: 403–486](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/12-handling-edge-cases.mdx#L403-L486).

## K11 — Prompt hướng dẫn; harness và tool thực thi quyền

- **WHAT:** Nguồn phân biệt instruction với enforcement; harness kiểm yêu cầu tool, đưa observation về và quản lý giới hạn.
- **WHY:** Tránh suy rằng role text, XML delimiter hay prompt từ thư viện tự cấp tool/quyền hoặc chứng minh action đã chạy.
- **HOW:** Trong proposal ghi capability/authority thực từ source project; mọi text repo/tool đọc về giữ là dữ liệu tham khảo. Giữ REA workflow/evidence và IDA native/IDB ownership.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W0, W4.
- **Giới hạn:** Không cài MCP/plugin, thêm allowlist hay đổi runtime từ lần đọc này. Không tuyên bố prompt chống injection bảo đảm runtime.
- **CHECK đề xuất:** Tool call/receipt có thật được phân biệt với đoạn hướng dẫn hoặc ví dụ call.
- **Nguồn:** [S3-HARNESS: 5–68](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/26-the-harnesses.mdx#L5-L68); [S3-HARNESS: 194–212](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/26-the-harnesses.mdx#L194-L212).

## K12 — Chỉ mở module phù hợp, có chỉ dẫn sử dụng và giới hạn

- **WHAT:** Nguồn tổ chức skill từ nguyên tắc tới guideline/reference và mô tả progressive disclosure theo metadata → instruction → supporting files.
- **WHY:** Giữ bối cảnh vừa đủ và giảm xung đột giữa những checklist không liên quan.
- **HOW:** Tra index theo objective; chọn card/module có relevance, rights và giới hạn phù hợp; ghi selected/rejected. Chỉ dựng integration proposal riêng nếu có consumer cụ thể và thiếu capability thật.
- **Áp dụng:** Prompt-Master, Evidence-Synthesizer; đường dẫn phase tham khảo W1, W2.
- **Giới hạn:** Nạp skill không train model, cài tool hay bảo đảm expertise. Giữ thứ tự quyền và conflict unresolved; không biến role nhãn thành identity mới.
- **CHECK đề xuất:** Mỗi module được chọn có lý do dùng và lý do không dùng các item gần giống.
- **Nguồn:** [S3-SKILLS: 333–444](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/25-agents-and-skills.mdx#L333-L444); [S3-HARNESS: 152–192](https://github.com/f/prompts.chat/blob/f8fe2385244a6188c976e352ea7ca849e3d20b1e/src/content/book/26-the-harnesses.mdx#L152-L192).
