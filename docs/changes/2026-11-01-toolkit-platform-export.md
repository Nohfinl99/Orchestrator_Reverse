# Toolkit và gói GPT/Gemini — 01/11/2026

## Nội dung

Thêm năm workflow nguyên bản tại [plugins/orchestrator-toolkit](../../plugins/orchestrator-toolkit/README.md): CUA, Strix, D810-ng, MicroSMT và OLLVM research. Chọn theo mục tiêu, chỉ mở skill/reference liên quan. [Task execution](../operations/task-execution.md) giữ yêu cầu gốc, phân rã, handoff và nghiệm thu; Orchestrator điều phối/review chính, worker model nhỏ làm phần hẹp khi host hỗ trợ.

[Hướng dẫn nền tảng](../operations/toolkit.md) phân biệt local discovery, export và account import. `scripts/export_toolkit.py` tạo ZIP plugin, năm ZIP skill, sáu file Instructions/Knowledge và manifest ngoài repo. Gói không chứa upstream code/runtime. Các digest trong reference là snapshot lịch sử; local evidence không đưa lên public.

## IA và bảo toàn

- Nguồn toolkit: `plugins/`; workflow/nghiệm thu và portability: `docs/operations/`; record lượt sửa: `docs/changes/`; exporter: `scripts/`; navigation/inventory: `metadata/`.
- Thêm GEMINI.md làm điểm vào cho Gemini CLI; README/AGENTS/operations dẫn tới đúng nhánh.
- Không đổi mười stack, mười protocol, nguyên lý, sáu identity, phase/gate hoặc lịch sử FAIL. Không di chuyển đường dẫn contract cũ để làm đẹp folder. Skill bytes được giữ qua Git bằng thuộc tính `-text` riêng cho toolkit; original preservation pins giữ nguyên.

## Kiểm local và giới hạn

Tám nhóm kiểm packaging/discovery/preservation đã chạy local: manifest khớp nguồn và exports; sáu ZIP/21 member khớp bytes; sáu file Knowledge; rebuild xác định; mười skill/reference khớp ba bản nguồn/public/local discovery; 33 baseline files bảo toàn; từ chối output trong repo, schema sai và reference thoát gói. Đây là kiểm bytes/format, không chứng minh chất lượng phân tích hoặc tool runtime.

Local workspace có năm thư mục skill tại `.agents/skills` để Codex/Gemini CLI discovery; chưa kiểm host activation hoặc Gemini CLI execution. Account GPT/Gemini web chưa được nhập, theo yêu cầu người dùng chỉ xuất gói trong phiên này. Không bật API trả phí, scanner, native/provider hay W4. Full external schema validation và account scan/import diagnostics vẫn cần kiểm tại host; không suy từ export thành install.

Biên bản local: `evidence/orchestrator_meetings/20261101_platform_sync_01/` ở workspace cha, không phân phối trong public clone. IA verifier của public kiểm navigation/inventory/preservation riêng; không đóng G1–G4/W4.
