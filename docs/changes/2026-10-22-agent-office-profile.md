# Profile IA văn phòng agent 3D — 22/10/2026

## Objective và phạm vi

Tổ chức proposal sản phẩm về phòng làm việc 3D cho sáu identity Orchestrator hiện có; khảo sát mã nguồn tương tự; thiết kế luồng họp, trạng thái, dissent/synthesis; chuẩn bị mục tiêu và bộ công cụ kiểm chứng bắt đầu bằng bảng offline.

Phạm vi là hồ sơ IA/product proposal. Không implementation, không dispatch runtime, không provider/target/REA–IDA, không training và không thay gate.

## Thay đổi

- Tạo `docs/proposals/agent-office-3d/` với profile, source review, interaction architecture, offline verification plan, knowledge/tool map và handoff.
- Ghi rõ project differentiator còn là proposal: meeting có thể truy nguyên tới task/DAG, evidence, disagreement và quyết định, không chỉ là 3D office.
- Thêm route điều hướng, mục lục và work-queue row; ghi PRODUCT-01 trong sổ open questions.
- Kế thừa sáu identity, REA–IDA principle, phase/gate/status nguyên trạng.

## Nguồn đã đọc

### Workspace/project

- `START_HERE.md`, `docs/ia/workspace-map.md`, `Orchestrator_Reverse/AGENTS.md`
- `Orchestrator_Reverse/context/current.md`, `context/handoff.md`, `CONTEXT_VI.md`
- `docs/architecture/system.md`, `agents.md`, `information-architecture.md`
- `docs/planning/phase-map.md`, `work-queue.md`, `w4-readiness-plan.md`
- `docs/knowledge/README.md`, `retrieval-guide.md`, `application-map.md`, `knowledge-cards.md`
- `docs/reference/source-map.md`, `open-questions.md`; `src/README.md`; `docs/onboarding/session-workflow.md`
- Consumer proposal/admission checklist: `evidence/agent_alignment/20261021_01/next_atomic_task.json`, `evidence/orchestrator_meetings/20261021_logic_audit_01/candidate/proposal_admission.json`

### GitHub source review

- Atlassian Roving Office `f3c51c85d04c13ae32a4b929c7488847980c3851`: README, AOP protocol, `src/data/AopSource.js`; AgentManager behavior referenced by protocol.
- ClawProwl `866351cc5143baf9c78a6003b7848319da459055`: README, `src/gateway/types.ts`, `src/store/meeting-manager.ts`, `src/store/office-store.ts`, gateway adapter/types.
- Hermes Virtual Office `1d23350d7df734b551bea52167d02aeaf23158e2`: README, `src/lib/hermes/meeting-a2a.ts`, `src/lib/hermes/meeting.ts`, `src/components/MeetingPanel.tsx`, `docs/MEETING-PROTOCOL.md` (protocol document contains stale sections explicitly corrected in that file; profile behavior claims prefer code paths).
- Agent Office `852e2ab28c4f3f31bffdf4b20353bd119c9d3270`: README only; no meeting implementation claim based on code.

## Đã verify / chưa verify

- **Static IA:** local links, content inventory, navigation và preservation checks chạy sau khi sửa; kết quả ở dưới.
- **Source review:** selected files/revisions đọc tĩnh; không checkout/chạy repo, không benchmark và không independent demo/runtime verification.
- **Offline UI:** chưa implement; toàn bộ V0–V4 acceptance còn proposed/not run.
- **Runtime/gates:** P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 runtime `NOT_RUN_BLOCKED`; v3 `OFF` — giữ nguyên.

## Cách kiểm tra

```powershell
python -I -B scripts/verify_ia.py
```

Verifier chỉ kiểm lớp tài liệu. Nó không chứng minh UI, agent meeting, realtime bridge hoặc product-market fit.

