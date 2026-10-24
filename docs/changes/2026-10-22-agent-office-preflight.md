# Chuẩn bị stack, gate và benchmark văn phòng 3D — 22/10/2026

## Objective

Tổ chức review trước triển khai, quyết định stack/protocol áp dụng theo objective, làm rõ acceptance/gate correctness, số vòng họp/review và thiết kế benchmark cho văn phòng agent 3D.

## Thay đổi

- Thêm `preflight-knowledge-and-benchmark.md`: mapping stack 00–09 theo applicability; gate applicability cho offline vs runtime; acceptance invariants; benchmark offline, UI, UX và runtime; R4a/R4b; knowledge cards candidate; toolchain candidate.
- Thêm `preflight-meeting-2026-10-22-01.md`: agenda, debate positions, adjudication, unresolved status và nguồn local đã đọc.
- Cập nhật profile index, navigation, handoff và work queue để trỏ tới preflight và giữ benchmark `NOT_RUN`.
- Kết luận meeting: tiếp tục AO-1 packet sau khi được giao/review; chưa code/test/benchmark. Office AO acceptance không thay G1–G4; G4 status discrepancy giữ theo source scopes.

## Nguồn đã đọc

- `START_HERE.md`, `docs/ia/workspace-map.md`, `Orchestrator_Reverse/AGENTS.md`.
- `Orchestrator_Reverse/context/current.md`, `docs/planning/phase-map.md`, `work-queue.md`, `w4-readiness-plan.md`.
- Stack: `00_bootstrap.md`, `01_W0_context_baseline.md`, `02_W1_masters_prompts.md`, `03_W2_knowledge_transfer.md`, `04_W3_REA_IDA.md`, `05_W4_integration.md`, `06_W5_evaluation.md`, `07_W6_pilot_release.md`, `09_review_gate_handoff.md`.
- Protocol: intake, baseline, routing, knowledge, pair, state, evaluation, pilot, handoff; plus `docs/reference/validation-status.md`, `docs/knowledge/README.md`, `retrieval-guide.md` và office roadmap/verification plan.
- Ba reviewer advisory: stack/gate audit; benchmark design; orchestration-round design. Không sửa code, không chạy test/fixture/provider/target/runtime.

## Kiểm tra

`python -I -B scripts/verify_ia.py` chỉ kiểm navigation/tài liệu/public inventory. Không có benchmark hoặc gate execution mới.
