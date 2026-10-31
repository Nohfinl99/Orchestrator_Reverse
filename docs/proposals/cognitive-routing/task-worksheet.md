# Worksheet dùng lại cho một cognitive task

Đây là mẫu soạn yêu cầu cho [CT guide](README.md), không phải schema/API, approval hoặc dispatch command. Chỉ điền một mục tiêu/owner; source/protocol gốc quyết định semantics. Trường chưa có giữ UNKNOWN/null và chặn đúng nhánh phụ thuộc.

```text
Task/revision/attempt:
Original request ref/digest:
Objective / CT ID / expected output:
Owner responsibility (một trong sáu identity hiện hữu):
Executor session/model thực tế / reviewer khác producer:

Inputs được chọn:
  path + revision + expected digest + range + relevance
Source/graph query bị bỏ và lý do / ảnh hưởng dependency:
Context/dependency revision / authority receipt refs:
Knowledge applicability/rights/admission/consumer ACK:
Target applicability / pair refs hoặc lý do NON_TARGET_PREPARATION:
Protocol sections thực sự cần đọc / skill được chọn và lý do:
Budget: context đơn vị gì / task calls-cost-time-retry nếu applicable:

Thao tác nhận thức chính:
  CT-01: xác định ambiguity làm thay đổi output; phân rã dependency.
  CT-02: tìm proposition; giữ condition/exception; gộp trùng nghĩa có nguồn.
  CT-03: theo entry → state/data flow → observation; tách hypothesis/unknown.
  CT-04: nêu invariant; so phương án theo acceptance; tạo diff nhỏ đúng roadmap.
  CT-05: cố bác bỏ claim; kiểm control mạnh nhất và counterexample; chỉ kết luận theo evidence.
  CT-06: so revisions; kiểm delta/ACK; chọn next, wait hoặc stop có lý do.
  Chỉ chọn nhánh phù hợp, không chạy toàn danh sách.

Output artifact path/revision/digest + nguồn từng claim:
Acceptance predicates và checks applicable trước khi thực hiện:
Reviewer decision / exact reviewed digest / objections còn mở:
Delta so với attempt trước / evidence của progress:
Failure signature / budget còn / STOP hoặc reopen trigger:
Next atomic task đề xuất / owner / missing prerequisites:
```

Khi bàn giao cho Luna, chỉ gửi task con và selected input refs/đoạn cần thiết, không mặc định toàn lịch sử hoặc quyền của chair. Model cao đọc lại source quyết định và exact output digest; nhận summary từ Luna không thay review. Không yêu cầu private reasoning; ghi decision facts, alternatives đã xét và locator kiểm được.

Nếu không có delta hoặc thiếu prerequisite, không lặp cùng prompt. Review cap và runtime cap theo guide/protocol tương ứng; trạng thái `PROPOSED` không tự chuyển `READY` từ việc điền worksheet.
