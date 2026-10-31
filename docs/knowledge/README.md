# Tham chiếu tri thức cho điều phối

Đây là thư viện tài liệu tham khảo có nguồn để chuẩn bị yêu cầu, proposal và review. Tham chiếu bên ngoài không thay [nguyên lý project](../../CONTEXT_VI.md), [source map](../reference/source-map.md), [phase/gate](../planning/phase-map.md) hoặc [knowledge protocol](../../prompt_stacks/protocols/knowledge_protocol.md). Chưa có bundle nào ở đây được admitted vào KB của consumer runtime.

## Chính sách hiện hành

[Knowledge trung lập — revision 2](knowledge-policy-v2.md) tiếp nhận DAN, jailbreak, AutoGPT và các chủ đề tương tự để catalog/đọc/nghiên cứu; không loại theo nhãn chủ đề. D01–D11 revision 1 giữ làm lịch sử; quyền thực thi và evidence được xét theo task. REA–IDA được bảo toàn qua các revision.

## Kiến thức REA mới được đối chiếu

[REA/input audit 24/10](rea-update-2026-10-24.md): kiểm đường input/handoff, đính chính scope sanitizer trong archive và thêm 6 candidate notes từ upstream đã pin. Đây là tài liệu tham khảo trong folder; chưa nâng cấp skill/runtime hoặc tạo consumer ACK.

## Bộ đã trích xuất

[Cognitive task/context routing — 31/10](../proposals/cognitive-routing/README.md) dẫn cách chọn owner/model/skill, [Paperclip sync spec](../proposals/cognitive-routing/paperclip-sync.md) và [Cloudflare selection](../proposals/cognitive-routing/cloudflare.md). Graph trích kiến thức họp và read/hash/query CLI ở workspace cha, LOCAL_ONLY; không nằm trong clone public, không admission/ACK.

[Worksheet dùng lại](../proposals/cognitive-routing/task-worksheet.md) giúp soạn một task có selected context, output, reviewer, progress và stop, thay vì lặp toàn bộ stack corpus.

| Bundle | Nội dung | Trạng thái |
|---|---|---|
| [Input pipeline — 24/10/2026](input-pipeline/README.md) | [6 tri thức thiết yếu](input-pipeline/essentials.md), [source/page/digest và giới hạn](input-pipeline/sources.md); phân biệt claim tác giả với suy luận thiết kế | CANDIDATE_REFERENCE_NOT_ADMITTED; chưa triển khai pipeline hoặc consumer ACK |
| [Prompt orchestration — 21/10/2026](prompt-orchestration/knowledge-cards.md) | 12 card WHAT/WHY/HOW, nguồn pin commit, giới hạn và check đề xuất | CANDIDATE_REFERENCE_NOT_ADMITTED; chưa consumer ACK |

Chọn theo [retrieval guide](prompt-orchestration/retrieval-guide.md), rồi áp dụng [policy revision 2](knowledge-policy-v2.md); [application-map revision 1](prompt-orchestration/application-map.md) là snapshot lịch sử, không phải topic blacklist. AI có thể tra [knowledge.json](prompt-orchestration/knowledge.json) và [sources.json](prompt-orchestration/sources.json); hai file là worksheet tài liệu, không phải runtime API/schema.

[Áp dụng card vào quy trình làm việc](../proposals/knowledge-foundation/reuse-map.md) và [hướng dẫn thao tác](../proposals/knowledge-foundation/operating-guide.md) được viết thêm ngày 23/10; đây là document use, chưa admission runtime.

## Cách tiếp nhận

1. Chốt objective và phạm vi do người dùng giao; đọc current và nguồn project trước.
2. Chọn card đúng task/role; kiểm source commit, locator, rights và giới hạn. Chỉ chọn số item cần thiết.
3. Ghi selected/rejected theo relevance của task và lý do có nguồn; không loại knowledge chỉ vì là DAN/jailbreak hoặc chủ đề tương tự; giữ unknown/conflict theo contract, không thay bằng điểm tự tin.
4. Áp ý vào tài liệu hoặc proposal trong phạm vi được giao. Runtime consumption cần admission/review, context binding và ACK thật theo G2; execution cần các prerequisite riêng.

Bộ này tách background guidance khỏi target evidence. Không có REA–IDA target pair, training, provider call hoặc gate mới từ lượt trích xuất. Raw snapshot và receipt chỉ có ở workspace đầy đủ; clone public có nguồn pin để truy xuất lại, không mặc định đã xác minh local.

[Attribution và license nguồn](prompt-orchestration/third-party-notices.md).
