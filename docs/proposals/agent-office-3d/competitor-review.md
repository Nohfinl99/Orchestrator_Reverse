# Khảo sát mã nguồn: văn phòng agent và phòng họp

**Phạm vi:** đọc README và các file nguồn được dẫn cụ thể ở revision/commit bên dưới vào ngày 22/10/2026. Đây là khảo sát tĩnh có chọn lọc, không checkout/chạy các repo, không xác minh toàn bộ tính năng hoặc claim sản phẩm.

## Nguồn đã xem

| Dự án | Revision đã xem | Observation từ nguồn | Ý nghĩa cho hồ sơ |
|---|---|---|---|
| [Atlassian Roving Office](https://github.com/atlassian-labs/roving-office/tree/f3c51c85d04c13ae32a4b929c7488847980c3851) | `f3c51c85d04c13ae32a4b929c7488847980c3851` | [README](https://github.com/atlassian-labs/roving-office/blob/f3c51c85d04c13ae32a4b929c7488847980c3851/README.md) mô tả phòng soft-3D, agent-session thành nhân vật và adapter cho nhiều harness. [AOP](https://github.com/atlassian-labs/roving-office/blob/f3c51c85d04c13ae32a4b929c7488847980c3851/docs/developer/protocol/aop-spec.md) định nghĩa luồng harness → adapter → ingest → SSE → browser; [AopSource](https://github.com/atlassian-labs/roving-office/blob/f3c51c85d04c13ae32a4b929c7488847980c3851/src/data/AopSource.js) hydrate snapshot rồi nghe stream và giảm event thành stage directions. | Bằng chứng tốt cho lớp quan sát và event adapter trung lập. AOP hiện là feed hoạt động vào office; không có meeting command hoặc điều phối task/DAG trong event contract đã đọc. README nói demo mặc định dùng agent mô phỏng. |
| [ClawProwl](https://github.com/clawprowl/clawprowl/tree/866351cc5143baf9c78a6003b7848319da459055) | `866351cc5143baf9c78a6003b7848319da459055` | [Types](https://github.com/clawprowl/clawprowl/blob/866351cc5143baf9c78a6003b7848319da459055/src/gateway/types.ts) có `AgentZone` gồm `meeting`, status và movement. [meeting-manager](https://github.com/clawprowl/clawprowl/blob/866351cc5143baf9c78a6003b7848319da459055/src/store/meeting-manager.ts) gom agent theo collaboration link/session key và đưa họ tới meeting zone; [office-store](https://github.com/clawprowl/clawprowl/blob/866351cc5143baf9c78a6003b7848319da459055/src/store/office-store.ts) cập nhật vị trí animation. | Chứng minh có thể hiện meeting zone và chuyển động theo sự kiện cộng tác. Logic được đọc ở đây là gom nhóm/hiển thị, không chứng minh có tranh luận theo lượt hoặc quyết định điều phối trong phòng. Gateway bên ngoài cung cấp event/control. |
| [Hermes Virtual Office](https://github.com/JuniorXcoder/hermes-virtual-office/tree/1d23350d7df734b551bea52167d02aeaf23158e2) | `1d23350d7df734b551bea52167d02aeaf23158e2` | [README](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/README.md) mô tả 3D office và phòng họp. Đọc [meeting-a2a.ts](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/lib/hermes/meeting-a2a.ts), [meeting.ts](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/lib/hermes/meeting.ts) và [MeetingPanel.tsx](https://github.com/JuniorXcoder/hermes-virtual-office/blob/1d23350d7df734b551bea52167d02aeaf23158e2/src/components/MeetingPanel.tsx): code tách mode `simulasi` với `a2a`, giới hạn participants/turns, từ chối participant chưa served, lưu archive, cho mở transcript và follow-up; lỗi A2A được ghi là failed thay vì thay bằng lời bịa. | Gần nhất với yêu cầu có cuộc họp thật, transcript và minutes. Không nên định vị sản phẩm chỉ bằng “3D + debate + minutes”. Tích hợp gắn với Hermes CLI/A2A của repo đó; không chứng minh tương thích với Orchestrator hoặc REA–IDA. Protocol docs còn chứa đoạn cũ đã được ghi rõ là lỗi thời, nên ưu tiên code ở revision đã pin. |
| [Agent Office](https://github.com/AgentSystemLabs/agent-office/tree/852e2ab28c4f3f31bffdf4b20353bd119c9d3270) | `852e2ab28c4f3f31bffdf4b20353bd119c9d3270` | Chỉ xem README: repo mô tả workers nhiều harness, terminal, task/PR board và agent có thể quản lý agent khác. | Nguồn discovery cho nhóm sản phẩm 3D/control. Chưa đọc code meeting nên không dùng làm bằng chứng tính năng meeting hoặc sản phẩm hoạt động. |

## Hướng khác biệt nên theo đuổi

“Có văn phòng 3D”, “có agent đi vào phòng họp”, “có chat/transcript” và “có minutes” đã xuất hiện trong dự án khác. Đây không phải lợi thế đủ để định vị sản phẩm.

Hermes Virtual Office README còn mô tả approval, evidence và independent verification. Vì thế không thể coi những từ “có evidence” hoặc “có transcript” là điểm khác biệt độc quyền; phần implementation đó chưa được audit sâu trong khảo sát này. Đề xuất định vị Orchestrator là **phòng họp kỹ thuật nối chặt với REA–IDA và các gate của project**:

1. Mỗi lệnh và phân công gắn với task/DAG node, owner đã đăng ký, điều kiện và receipt.
2. Mỗi ý kiến có dạng claim, locator/evidence ref, mức chưa chắc chắn và phản biện liên quan; người dùng bấm avatar để mở phần đã được phép công bố.
3. Synthesis tách rõ điểm đồng thuận, ý kiến thiểu số, conflict chưa giải quyết, thiếu evidence và quyết định cuối.
4. Kết luận không tự cập nhật trạng thái chỉ vì đa số đồng ý. Chỉ acceptance/gate hợp lệ mới chuyển task; nếu chưa đủ điều kiện thì hiển thị `WAIT_INPUT`, `BLOCKED`, `CONFLICT` hoặc `NOT_RUN` đúng nghĩa.
5. Giữ target/component/slice/IDA-state binding, nguồn/revision, provenance và ACK của từng consumer qua meeting, handoff, checkpoint và gate. Đây là lợi thế tiềm năng cụ thể từ project gốc; chưa phải feature đã triển khai hoặc market-validated.

## Giới hạn claim

- Phân tích trên là đọc tĩnh các nguồn ở revision cụ thể, không chạy demo, không benchmark, không kiểm tra độ ổn định/hiệu năng và không xác nhận các claim vận hành do README của repo tự nêu.
- Không sao chép code, schema, prompt, artwork hoặc thương hiệu từ repo bên ngoài vào hồ sơ này.
- Việc Roving Office có license code hay một repo có license không tự cấp quyền dùng mọi artwork, trademark, model hoặc nội dung phụ thuộc.
- Tham khảo này là nguồn product/architecture cho proposal, không là evidence target, quyền dispatch, consumer ACK hoặc KB admission của Orchestrator.

