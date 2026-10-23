# Input support theo checkpoint — 24/10/2026

Baseline `82242c9f492fc20b636fb7504ade0fb4409962cb`. Người dùng yêu cầu điều phối theo gate có % và evidence, không mặc định phát biểu người dùng đúng, hỏi 2–3 câu nếu mục tiêu chưa rõ, chỉ xác nhận xong sau verify, chọn model/độ sâu theo tác vụ. Các trả lời bổ sung chốt packet offline trước, benchmark có raw hoặc pentest evidence và giao coordinator chọn model phù hợp cho run tương lai.

## Thay đổi

- [Bốn checkpoint đề xuất](../proposals/input-support-gates/README.md), mỗi checkpoint 6 tiêu chí cố định; status là worksheet chờ user quyết định, không thay G1–G4.
- [Packet](../proposals/input-support-gates/packet.md) chọn một archived generated-prompt builder để source-map; scope/budget 0 provider/target/fixture/training calls mới. Không đưa sanitizer vào user input hoặc thay parser Stage1.
- [Benchmark plan](../proposals/input-support-gates/benchmark-plan.md) dùng 6 source-grounded seed case local chờ review; expected labels không đưa vào active KB. Historical verifier suite là tooling synthetic đã chạy, AO pentest là design NOT_RUN.
- AGENTS/session workflow cập nhật cách xét claim, ambiguity, verification, model profile và report theo tiêu chí. Public entry/context/queue/handoff/navigation dẫn đúng nhánh.

## Evidence và status

Readback script local chỉ đọc/hash: 13/13 source captures khớp SHA/size; phiên bản local/main/release được đối chiếu; capability metadata snapshot có 207 advertised tool names và 9 selected routes được kiểm membership. Historical 10/10 case receipt khớp raw stdout/stderr/exit, frozen plan/candidate pins và oracle; không rerun suite. Đây không phải model/pentest run mới hay independent review của lượt này.

[Status revision 1](../proposals/input-support-gates/status.json): INPUT-A 3/6 (50%), KNOWLEDGE-B 3/6 (50%), IMPLEMENTATION-C 0/6 (NOT_IMPLEMENTED/NOT_RUN), EVALUATION-D 0/6 (NOT_RUN). Tỷ lệ là criterion coverage, không phải quality score hoặc xác suất thành công. Chưa checkpoint nào accepted; user chưa chốt thresholds, oracle còn chờ independent review và chưa có raw model-refusal benchmark.

Raw/source pins/seed oracle/verification ở workspace `evidence/orchestrator_meetings/20261024_input_support_gates_01` (LOCAL_ONLY). Verification của public package chỉ dùng IA/read/hash/link/preservation và diff check; output cụ thể ở receipt phiên. Phần này chưa chứng minh implementation/pilot/training; không có provider/model/REA invocation mới.

Giữ original REA–IDA principles, identity, phase/gate, mười stack/protocol, archive/raw/frozen history và preservation pins. P1K B4 FAIL; G1/G2 INCOMPLETE; G3/G4 NOT_RUN; W4 NOT_RUN_BLOCKED; v3 OFF. Next decision: nhận/chỉnh bộ checkpoint và scope source-comprehension benchmark; next work: review oracle/consumer admission trước implementation và applicable frozen R4a trước execution.
