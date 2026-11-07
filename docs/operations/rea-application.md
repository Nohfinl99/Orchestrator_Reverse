# Áp dụng đúng REA trong Orchestrator

Đối chiếu ngày 07/11/2026: [morluto/rea](https://github.com/morluto/rea), skill local `reverse-engineer-anything` revision 49 và tool schemas host đang cung cấp. Skill revision, package version, GitHub main và khả năng provider là các thông tin riêng. Đây là hướng dẫn áp dụng; không nâng gate hoặc thay contract project.

## REA, IDA và Orchestrator

REA cung cấp MCP/CLI để agent điều tra artifact và hành vi, trả findings kèm Evidence. Agent dùng kết quả để hỏi tiếp, giải thích hoặc kiểm một reconstruction. Phạm vi có native, packaged/managed/JavaScript và runtime workflows; không chỉ ghi ledger. [README upstream](https://github.com/morluto/rea#how-rea-works).

IDA là một provider native được REA tích hợp, bên cạnh các provider khác. Dùng IDA qua REA cần registration và profile phù hợp; mở original binary, đối chiếu input identity. Có IDA local không chứng minh REA–IDA đã connected. [IDA provider](https://github.com/morluto/rea/blob/main/docs/ida-provider.md).

Orchestrator chọn câu hỏi, owner, dependency và nghiệm thu. Contract REA–IDA của [project](../architecture/system.md) vẫn áp dụng ở các boundary được quy định. Đó là yêu cầu project, không phải khẳng định mọi upstream REA tool cần IDA. Không tự miễn pair cho consumer vốn yêu cầu pair; xét đúng applicability/acquisition scope, giữ gap nếu chưa map.

## Chọn thao tác theo câu hỏi

| Câu hỏi/đầu vào | Thao tác phù hợp khi host quảng bá | Phần chưa được chứng minh |
|---|---|---|
| Package/IPA chứa gì? | `open_binary` → `inspect_artifact` | Inventory không chứng minh hành vi hoặc đã decompile |
| `.ips` ghi nhận gì? | `inspect_apple_ips` với path riêng | Parser không tự symbol hóa, join IDB/dSYM hoặc tìm nguyên nhân; [IPS guide](https://github.com/morluto/rea/blob/main/docs/apple-ips.md) |
| Một hàm native làm gì? | Mở đúng executable/provider → tìm function → pseudocode/assembly/dossier phù hợp | Chỉ dùng facets provider thật sự hỗ trợ; IDA không có mọi công cụ của provider khác |
| Feature đi qua module nào? | Route đúng loại artifact, trace từ seed có evidence | Không suy feature từ một filename/string |
| Hành vi thực thi thế nào? | Workflow runtime đúng host/target khi task yêu cầu và có capability | Static evidence không là runtime observation |
| Source repository đầy đủ được tổ chức ra sao? | Công cụ source thông thường | Không ép mở provider hoặc chạy readiness cho source maintenance |

Không tự chọn target từ report cũ. Với điều tra đã có target trong context, reuse identity/state phù hợp thay hỏi lại hoặc mở trùng. Dùng schema host thật, không đoán từ tài liệu main. Không chạy setup/doctor mặc định mỗi vòng.

## Giữ qua vòng: ba lớp khác nhau

1. **Evidence:** giữ complete record/parent, ID, input identity, coverage, limitations và unknowns. Summary/page chỉ là view. Export bundle để chuyển process/agent; import kiểm record integrity, không tạo quan sát độc lập mới. [MCP Evidence contract](https://github.com/morluto/rea/blob/main/docs/mcp-contracts.md#tool-results).
2. **Analysis snapshot:** cache kết quả query có binding tương ứng; không là bản sao toàn bộ database. Mỗi CLI invocation là process riêng. Reuse cần target/provider/parameters/profile phù hợp. [CLI snapshots](https://github.com/morluto/rea/blob/main/docs/cli.md#save-and-reuse-analysis-snapshots).
3. **IDA/IDB state:** kết quả live và lifecycle tùy attached/headless profile; không suy DB freshness từ hash executable hoặc bundle import. [IDA lifecycle](https://github.com/morluto/rea/blob/main/docs/ida-provider.md).

Với attached IDA, REA không replay kết quả live từ snapshot; close giải phóng kết nối/proxy, không tự save/close GUI IDB. Headless quản lý DB/workspace riêng theo profile, không coi đó là GUI state được giữ. Khi resume phải biết mình đang kế thừa mode/state nào.

Không đồng nhất giữ tool session với giữ nguyên context model. Khi đổi process/agent hoặc kết thúc điều tra, lưu bundle/locators cần chuyển; ghi provider/session/state áp dụng. Không gọi lại engine chỉ để lặp kết quả đã giữ và kiểm còn phù hợp. State đổi thì revalidate/invalidate downstream theo contract project.

## Một vòng điều phối cụ thể

Giữ active goal theo [goal continuity](goal-continuity.md), lập checklist câu hỏi và evidence cần có. Chọn route; lấy overview vừa đủ; phân tích tập trung theo gap; giao nhánh độc lập với original/user revisions, target identity, Evidence và output/criterion; review theo checklist ban đầu rồi cập nhật answered/partial/unresolved. Evidence và tool capabilities phải có source, không chỉ role label.

Upstream có guided investigation prompts; render chỉ tạo hướng dẫn, không tự gọi tool hoặc chạy phân tích. Dùng qua host chỉ khi capability tương ứng được quảng bá; nếu không, thực hiện workflow đọc được bằng các tool thật. [Guided workflows](https://github.com/morluto/rea/blob/main/docs/mcp-prompts.md).

Diễn đạt kỹ thuật là chuyển câu hỏi thành thao tác có kiểm chứng, giữ mục đích và outcome. Nó không tự thay goal sang crash, không là cơ chế bảo đảm tránh model/platform reject. Phân loại refusal/flag/tool error bằng phản hồi thật; không gán lỗi REA khi chưa có lỗi REA.

## Khác revision cần lưu ý

Reference local về native nói close xóa session records; MCP docs main đọc 07/11 mô tả target retirement xóa replay state nhưng giữ investigation Evidence/Unknown history trên connection đó. Không coi mô tả main là behavior của server chưa kiểm version; portable export vẫn là cách chuyển dữ liệu chắc chắn giữa process. Không sửa skill cài đặt hoặc repin nguồn cũ trong task này.

Hồ sơ phạm vi đọc, metadata host và source tension ở workspace cha `evidence/upstream_review/20261107_rea_application_01/` (LOCAL_ONLY). Không chạy target/provider/setup trong lượt đọc này; quảng bá tool không chứng minh engine ready hoặc pair/ACK đã established.
