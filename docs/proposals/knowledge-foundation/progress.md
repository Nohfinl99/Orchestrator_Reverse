# Tiến trình cải tiến nền tảng — revision 1

Ngày 23/10/2026, baseline `a69d9c030b7533df4779bfa198025abec13a42e0`. Scope đang thực hiện: lấy các thực hành hữu ích đã trích xuất trong repo, đưa vào hướng dẫn và worksheet dùng từ folder, xuất bản để review. Chỉ có producer/self-reviewer của phiên này; không khai cuộc họp nhiều agent hoặc acceptance độc lập.

| Việc | Tiến độ | Bằng chứng/giới hạn |
|---|---|---|
| Đọc lại GitHub knowledge tại main đã pin | Hoàn tất đọc card qua GitHub connector | Đối chiếu Git blob với bản local; không audit lại toàn upstream |
| Chọn ý hữu ích và giới hạn áp dụng | Đã viết | [Reuse map](reuse-map.md), rights/D01–D11 giữ theo nguồn gốc |
| Biên bản đề xuất viết lại từ nền tảng | Đã viết | [Proposal](README.md), runtime steps còn là đề xuất |
| Hướng dẫn thao tác và worksheet | Đã viết | [Guide](operating-guide.md), [packet template](packet-template.md); document use, chưa admission runtime |
| Public entry và link KB-03 | Đã cập nhật | Điểm vào mới; tóm tắt public thay link thoát root tới evidence local |
| Inventory/navigation/preservation check | PASS_IA_DOCUMENT_CHECKS tại working tree và staged export | 132 files, 438 links, 33 byte-preserved files, 10 stacks/10 protocols; chỉ kiểm tài liệu |
| Git publication | Nhánh `codex/knowledge-foundation-revision` | Commit/remote và phản hồi push quyết định đã xuất bản; trang này không tự là receipt upload |
| Integration/consumer ACK/target pair | Chưa triển khai hoặc nghiệm thu | Theo source-map/W4 readiness; G1/G2/G3 chưa đủ |

## Next atomic task

Hoàn thiện `SELECTED_TRIAGE_CONSUMER_ADAPTER_COMPATIBILITY_PROPOSAL_01` từ projection đã có trong workspace. Scope: một generated-prompt consumer/call site và mapping context/authority/pair/knowledge/ACK, validator/receipt producer, applicability và missing fields. Output là compatibility packet source-bound; review bởi phiên khác producer khi được bố trí. Budget tài liệu đề xuất: tối đa 12 input files được liệt kê trước, 1 candidate, 2 vòng sửa, 0 fixture/provider/target calls.

Chưa chọn source/call site/reviewer cụ thể cho task sau nên giữ PROPOSED_NOT_DISPATCHED. Correction B4 là nhánh riêng trước implementation caller phụ thuộc. Chỉ có clone public thì dependent raw/caller sources vẫn LOCAL_ONLY. Không bịa source pins hoặc consumer ACK.

Gate: P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Ghi nhận document improvement không đóng các gate này. Lịch sử trước đó và manifests đã freeze giữ nguyên.

## Cập nhật knowledge trung lập — revision 2

Đã thêm [policy hiện hành](../../knowledge/knowledge-policy-v2.md), diễn giải lại D01–D11 theo hướng không cấm chủ đề và cập nhật entry/handoff. DAN và các chủ đề tương tự được catalog/đọc/nghiên cứu theo objective; chưa ingest corpus mới. Bảo toàn REA–IDA qua revision và mọi nguồn/frozen history. Publication theo commit/remote của PR #2.
