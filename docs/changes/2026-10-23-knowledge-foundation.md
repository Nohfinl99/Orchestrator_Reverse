# Cải tiến nền tảng từ knowledge hiện hữu — 23/10/2026

Người dùng yêu cầu chọn phần hữu ích trong GitHub Orchestrator_Reverse, tận dụng vào folder, cải tiến từ nền tảng, viết biên bản đề xuất và upload lại GitHub. Baseline checkout `a69d9c030b7533df4779bfa198025abec13a42e0`; GitHub main `1f9445f8d8c9ef13fd51c499c9df8003e1f9a9f1`. Nhánh xuất bản mới dựa trên checkout này, do đó chứa cả hai commit office/Muse đã có trên remote ngoài main; chưa có quyết định merge vào main từ lượt này.

## Thay đổi có thể review

- [Biên bản/đề xuất](../proposals/knowledge-foundation/README.md) ghi bài toán, quyết định tư vấn, roadmap và scope của bản đầu.
- [Reuse map](../proposals/knowledge-foundation/reuse-map.md) nối K01–K12 với artifact mới; giữ D01–D11 và attribution, không nhân bản corpus hoặc copy S1 templates.
- [Operating guide](../proposals/knowledge-foundation/operating-guide.md), [worksheet](../proposals/knowledge-foundation/packet-template.md) và [progress](../proposals/knowledge-foundation/progress.md) giúp điều phối từ task đến handoff; đây là tài liệu dùng soạn proposal/review, chưa runtime schema hoặc enforcement mới.
- [Source pins](../../metadata/knowledge-foundation-source-pins.json) bind 11 nguồn public. Git blob của knowledge-cards local khớp file được GitHub connector trả tại main đã pin.
- Cập nhật entry/context/handoff/queue/navigation; sửa KB-03 từ link thoát root thành locator LOCAL_ONLY và tóm tắt public; ghi gap applicability/validator tại FOUNDATION-01.
- Entry START_HERE của workspace cha dẫn vào bản mới; file cha không thuộc commit/public package.

## Kiểm và giới hạn

Lượt này chỉ có producer/self-reviewer, không có roster nhiều agent hoặc acceptance độc lập. Kiểm publication dùng verifier IA read/hash/link/preservation và review Git diff; raw receipt giữ local. Không chạy fixture nghiệp vụ, target, provider, model training hoặc W4. Phiên sau dùng commit/remote và receipt thực tế để xác định publication/check outcome, không suy từ việc trang này tồn tại.

Giữ nguyên mười stack, mười protocol, original principles, phase IDs và preservation manifest; không sửa archive/raw hoặc repin frozen evidence. Các manifest Muse cũ tiếp tục bind revision lịch sử của chúng; source pins mới không thay thế chúng.

P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Bản đầu hoàn thiện lớp hướng dẫn tài liệu; consumer compatibility, trusted validation bindings, rights/ACK và authentic target pair tiếp tục theo prerequisite hiện hữu.
