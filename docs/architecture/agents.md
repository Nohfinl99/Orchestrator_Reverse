# Sáu identity và trách nhiệm

View dẫn xuất từ [CONTEXT_VI.md](../../CONTEXT_VI.md), [kiến trúc gốc](system.md) và [source map](../reference/source-map.md). Mục này giúp chọn nguồn/owner; không đăng ký agent, sửa tool allowlist hoặc chứng minh dispatch đang hoạt động.

| Identity hiện hữu | Khi phù hợp | Đầu ra và handoff |
|---|---|---|
| Prompt-Master | Intake, goal/scope, atomic DAG, routing và prompt | Task/prompt theo dependency, owner và gate; function Orchestrator không là identity thứ bảy |
| Triage-Sentinel | Recon cấu trúc tĩnh trong scope được giao | Triage evidence về controller rồi Decomp; Stage1 được kiểm hiện là parser trực tiếp |
| Decomp-Analyst | Phân tích sâu disassembly/decompiler trong state đã bind | Claim/proposal có locator; Crypto chỉ khi evidence thích hợp |
| Crypto-Logic-Specialist | Nhánh algorithm có điều kiện | Hypothesis/claim và phản chứng; không append mặc định vào mọi task |
| Evidence-Synthesizer | Provenance/support/conflict, review và handoff | Report/receipt hoặc findings chưa đóng; không tự cấp quyền mutation |
| Product-Evolution-Architect | Goal product rõ và evidence được chấp nhận | Gap/feature/acceptance proposal; executable dispatch trong fixed SOP còn chưa map |

Debate là review service có điều kiện. HITL là human approval/executor theo quyền thực. Các phiên reviewer tài liệu không tự là agent được deploy; A0–A7 là coverage proposal, không phải alias dùng để dispatch.

Owner trách nhiệm của tài liệu: Prompt-Master phụ trách stack 00/01/02/05/07/08; Evidence-Synthesizer phụ trách 03/04/06/09. Đây không phải record giao việc hoặc bằng chứng consumer invocation. Target consumer nào tham gia đều cần scope/binding và ACK riêng theo contract.

Các gap context/authority/pair/KB/admission, conditional Crypto và Product dispatch được giữ tại [open questions](../reference/open-questions.md). Training một role không tự thay parser hay enforcement của role đó.
