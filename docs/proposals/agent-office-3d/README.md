# Hồ sơ IA: văn phòng 3D cho Orchestrator

| Trường | Giá trị |
|---|---|
| Profile ID | `AGENT_OFFICE_3D_PROFILE_01` |
| Revision | `1` |
| Ngày lập | 22/10/2026 |
| Trạng thái | `PROFILE_CREATED / PROPOSAL_ONLY / OFFLINE_FIRST` |
| Phạm vi | Hồ sơ sản phẩm, kiến trúc đề xuất, khảo sát nguồn và tiêu chí kiểm chứng |
| Execution | `NOT_RUN` — chưa có UI, event bridge hay runtime mới |

## Mục tiêu sản phẩm

Tạo một văn phòng 3D để người điều phối quan sát lệnh, luồng giao việc, trạng thái agent và cuộc họp trong thời gian thực. Người dùng có thể bấm vào nhân vật hoặc sự kiện để xem đầu ra có cấu trúc, căn cứ, ý kiến phản biện và quyết định liên quan.

Phòng 3D là cách nhìn vào trạng thái điều phối. Orchestrator và event log có thẩm quyền mới quyết định ai được giao việc, ai đang họp, việc nào bị chặn và quyết định nào cập nhật DAG. Chuyển động của avatar không thay cho receipt hoặc bằng chứng agent đã thực sự nhận lệnh.

## Ranh giới của hồ sơ

- Bước đầu là **bảng offline phát lại dữ liệu giả lập**, gắn nhãn `SIMULATED`; không gọi model, provider, target, REA, IDA hoặc training.
- Giữ sáu identity hiện có. Orchestrator tiếp tục là trách nhiệm điều phối, không phải identity thứ bảy. Debate/HITL vẫn theo định nghĩa hiện hành.
- Tách trạng thái công việc, vị trí trong phòng và tình trạng kết nối.
- Mỗi contribution, phản biện, synthesis và quyết định phải nối được về meeting/task/event ID và căn cứ được phép hiển thị.
- Không lưu hoặc trình bày chain-of-thought riêng tư. Hiển thị câu trả lời có cấu trúc, nguồn, artifact, điểm bất đồng và quyết định.
- Không sao chép code, thương hiệu hoặc artwork từ dự án tham khảo. Chỉ dùng các repo công khai làm căn cứ khảo sát kiến trúc/tính năng; kiểm tra quyền riêng trước khi tái sử dụng tài sản.

## Cách đọc hồ sơ

1. [Khảo sát sản phẩm và mã nguồn tương tự](competitor-review.md)
2. [Kiến trúc trải nghiệm và luồng cuộc họp](architecture.md)
3. [Biên bản review, phản biện, ma trận áp dụng và thẻ IDEA](meeting-review-2026-10-22-01.md)
4. [Roadmap sản phẩm theo phase và acceptance](roadmap.md)
5. [Biên bản họp review tính khả thi roadmap](roadmap-review-2026-10-22-01.md)
6. [Runbook điều phối task theo roadmap](execution-runbook.md)
7. [Mục tiêu offline có thể kiểm chứng](verification-plan.md)
8. [Knowledge và bộ công cụ đề xuất](knowledge-and-tools.md)
9. [Bàn giao, trạng thái và bước kế tiếp](handoff.md)
10. [Gói chuẩn bị stack/gate/benchmark trước triển khai](preflight-knowledge-and-benchmark.md)
11. [Biên bản họp tiền triển khai](preflight-meeting-2026-10-22-01.md)
12. [Review hướng hình ảnh và đề xuất khởi động prototype](visual-review-2026-10-22-01.md)
13. [AI_Judges review và phòng ban liên kết](ai-judges-review-2026-10-22-01.md)
14. [Handoff/prompt sang context triển khai](context-handoff-implementation-2026-10-22.md)
15. [AO-1 offline replay packet candidate](ao-1-offline-replay-packet-01.md) cùng [event schema](ao-1-event.schema.json) và [synthetic fixture](ao-1-fixture.jsonl)
16. [AO-1 advisory review report](ao-1-review-2026-10-22-01.md): `REVISE_NOT_ACCEPTED`, chưa chạy fixture/benchmark
17. [Điều phối hỗ trợ sửa AO-1](ao-1-agent-support-coordination-2026-10-22.md): phương án candidate 2 chờ anh duyệt
18. AO-1 candidate revision 2: [packet](ao-1-offline-replay-packet-02.md), [schema](ao-1-event-v2.schema.json), [fixture](ao-1-fixture-v2.jsonl), [test/review matrix](ao-1-test-matrix-v2.md); vẫn `NOT_ACCEPTED / NOT_RUN`
19. [AO-1 review report 02](ao-1-review-2026-10-22-02.md): candidate 2 `REVISE / NOT_ACCEPTED`
20. AO-1 candidate revision 3: [packet](ao-1-offline-replay-packet-03.md), [schema](ao-1-event-v3.schema.json), [fixture](ao-1-fixture-v3.jsonl), [test/review matrix](ao-1-test-matrix-v3.md); advisory review yêu cầu sửa, `NOT_ACCEPTED / NOT_RUN`
21. [AO-1 review report 03](ao-1-review-2026-10-22-03.md): candidate 3 cần làm rõ budget stop; ghi nhận review handling lapse
22. AO-1 candidate revision 4: [packet](ao-1-offline-replay-packet-04.md), [schema](ao-1-event-v4.schema.json), [fixture](ao-1-fixture-v4.jsonl), [test/review matrix](ao-1-test-matrix-v4.md); advisory review yêu cầu sửa, `NOT_ACCEPTED / NOT_RUN`
23. [AO-1 review report 04](ao-1-review-2026-10-22-04.md): candidate 4 `REVISE / NOT_ACCEPTED`
24. AO-1 candidate revision 5: [packet](ao-1-offline-replay-packet-05.md), [schema](ao-1-event-v5.schema.json), [fixture](ao-1-fixture-v5.jsonl), [test/review matrix](ao-1-test-matrix-v5.md); chờ independent review, `NOT_RUN`
25. [AO-1 review report 05](ao-1-review-2026-10-22-05.md): candidate 5 `REVISE / NOT_ACCEPTED`
26. AO-1 candidate revision 6: [packet](ao-1-offline-replay-packet-06.md), [schema](ao-1-event-v6.schema.json), [fixture](ao-1-fixture-v6.jsonl), [test/review matrix](ao-1-test-matrix-v6.md); advisory review không còn finding trọng yếu, chờ anh quyết định, `NOT_RUN`
27. [AO-1 review report 06](ao-1-review-2026-10-22-06.md): candidate 6 chờ coordinator decision; chưa phải R4a hay test result
28. [AO-3 offline pentest case 01](ao-pentest-case-01.md) và [JSONL cases](ao-pentest-case-01.jsonl): authority-spoof case cùng năm benign controls; advisory reviewed, chờ coordinator decision, `NOT_RUN`
29. [Muse takeover](../../onboarding/muse-takeover-2026-10-22.md): điểm tiếp nhận mới, current candidate pointers, Prompt-Master knowledge transfer và source/digest manifest; publication không thay acceptance.
30. [Gate recheck](gate-recheck-2026-10-22.md) và [Muse roadmap guide](../../onboarding/muse-roadmap-guide-2026-10-22.md): điểm vào sau recheck, điều kiện pre-AO2/R4a và cách tận dụng artifact/knowledge; dùng manifest v2, không đổi gate.

## Kết luận hiện tại

**Khả thi ở mức giao diện 3D và mô phỏng offline.** Các repo đã có minh chứng cho 3D, event streaming, animation theo trạng thái, khu họp, giao tiếp A2A và tổng hợp biên bản. Ý tưởng không còn khác biệt nếu chỉ dừng ở văn phòng 3D hoặc cuộc họp agent. Điểm sản phẩm nên theo đuổi là cuộc họp có nguồn gốc kiểm toán: lệnh điều phối → participant thật/giả lập được gắn nhãn rõ → ý kiến có căn cứ → bất đồng còn mở → quyết định → thay đổi task/DAG có receipt.

**Khả năng tích hợp vào Orchestrator hiện tại:** chưa có runtime để điều phối thật. Các trang kiến trúc của project xác định đây là mô hình đích; prompt stack chưa được nối vào runtime và candidate router ghi `dispatch_status=NOT_IMPLEMENTED`. Do đó hồ sơ này không tuyên bố có cuộc họp agent thật hoặc thay đổi gate.

**Mức sẵn sàng:** kỹ thuật dựng 3D và replay offline là khả thi; product-market fit, nhóm người dùng ưu tiên và lợi thế cạnh tranh vẫn `NOT_VALIDATED`. Đặc biệt, Hermes Virtual Office còn mô tả approval/evidence/independent verification trong README, nên cần định vị sâu theo binding REA–IDA, source revision, conflict resolution và gate/ACK semantics của Orchestrator; chưa audit toàn bộ feature implementation của đối thủ.

