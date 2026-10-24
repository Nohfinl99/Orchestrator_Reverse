# Dùng CLI chuẩn bị input offline

Caller thực: `scripts/prepare_input.py` → `orchestrator_pipeline.cli.main` → `core.prepare`. Chỉ chuẩn bị artifact cho **Prompt-Master / INTAKE_AND_PLAN**; không gọi model, REA, IDA hoặc target. [Report kiểm](../proposals/input-pipeline/local-runtime-2026-10-24.md) ghi phạm vi, raw digest và giới hạn.

## Chạy từ repository root

Python **3.12.14** được ghi trong executor receipt local của [report](../proposals/input-pipeline/local-runtime-2026-10-24.md), chỉ cần thư viện chuẩn; chưa lập compatibility matrix các version khác. Chọn `--output-root` ngoài public repo và run ID mới cho mỗi lượt:

```powershell
python -I -B scripts/prepare_input.py --input examples/input-pipeline/request.json --output-root ../local-runs --run-id intake-001
```

Đọc JSON trên stdout và `receipt.json`/`manifest.json` trong output; không suy kết quả từ exit code một mình. Các file tạo bằng exclusive write và kiểm readback/hash; run ID có sẵn không bị ghi đè. Lỗi acquisition có thể chưa giữ được original; receipt ghi tình trạng thực.

| Exit | Trạng thái | Cách xử lý |
|---:|---|---|
| 0 | `PREPARED_NOT_DISPATCHED` | Kiểm `prompt.json`; chưa có execution authority |
| 3 | `WAIT_INPUT` | Trả lời tối đa 3 câu trong `questions.json`; tạo request revision kế tiếp và resume |
| 4 | `REVIEW_REQUIRED` | Review proposal/diff/bundle digest; chưa có prepared prompt |
| 2 | Invalid, blocked hoặc lỗi storage | Đọc code/error/receipt; không retry tự động hoặc nhận runtime đã sẵn sàng |

## Request và nguồn

Xem [request mẫu](../../examples/input-pipeline/request.json). Schema `orchestrator.input-request.v1` có `task_id`, `revision`, nguyên văn `text`, `goal`, `scope`, `task_kind`, `output_contract`; `sources` và `unresolved_fields` tùy chọn. Nguồn có `source_id`, `kind` (document/rag/tool/memory), `locator`, `text`; giữ là untrusted data trong prepared artifact. Input phải là UTF-8 JSON, không duplicate keys/NaN/field ngoài schema. Task/run ID chỉ dùng chữ/số ASCII, `_`, `-`, dài 1–64; chặn tên device Windows.

Giới hạn: request/proposal ≤64 KiB mỗi file, tối đa16 nguồn, output budget1 MiB/run. Original bytes được lưu trước parse trong acquisition cap. Thiếu goal/output/scope/task-kind hoặc `unresolved_fields` tạo câu hỏi hữu hạn. Đây là phát hiện thiếu field/khai báo của operator, chưa hiểu ambiguity bằng ngôn ngữ tự nhiên.

Năm task kind khác có mapping sáu identity nhưng trả `RUNTIME_PREREQUISITES_UNBOUND`; chúng không nhận prompt để dispatch. Không khai task là intake để thực hiện hành động native/model.

## Resume và proposal

Request đầu có revision1. `--resume-from intake-001` trỏ parent trong cùng output-root; parent phải WAIT_INPUT/REVIEW_REQUIRED, cùng task ID và manifest hợp lệ. Request thay đổi cần tăng revision; lineage ghi các material field thay đổi. Đây là integrity local, chưa có signed authority hoặc khóa chống sửa đồng thời.

`--proposal-file <UTF8-text-file>` tạo proposal và unified diff từ `text` gốc. CLI không tự viết lại input. Đọc proposal/diff trước khi dùng `--accept-proposal-digest <exact-bundle-sha256>` với run ID mới và parent phù hợp. Digest bind task, original, proposed text và diff; đổi proposal làm acceptance cũ không khớp. Flag chỉ là annotation do operator cung cấp: `identity_verified:false`, `semantic_preservation_verified:false`, `execution_authorized:false`. Nó không thay human authentication, kiểm giữ nghĩa hoặc quyền executor.

Không dùng output-root chia sẻ với tác nhân có quyền sửa đồng thời. Reparse/symlink ancestor bị chặn tại thời điểm kiểm; chưa chứng minh an toàn trước filesystem race hoặc chống sửa bởi người có quyền trên host. Artifact local không có chữ ký và không phải sandbox.

[Trạng thái máy đọc](../../context/local-pipeline-state.json) · [Nghiên cứu native pilot](../proposals/input-pipeline/native-pilot-research-2026-10-24.md) · [Nguyên lý](../../CONTEXT_VI.md)
