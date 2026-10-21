# Fine-tuning theo vai trò

Fine-tuning là cách thay đổi trọng số model. Nó khác với việc sửa prompt, retrieval, tool routing hoặc validator. Bắt đầu bằng thay đổi nhỏ nhất có thể xử lý lỗi đo được. Không train để thay quyền broker, HITL, integrity checks, state validation hay gate.

## Khi nào cân nhắc

Chỉ mở pilot khi có lỗi lặp theo một role sau khi đã cố định prompt, knowledge, tools và contract; source/data rights được xác nhận; chuyên gia duyệt ground truth; train/dev/heldout split được đóng; metric và hard-fail được khóa trước evaluation. Nếu vấn đề là routing, parser, schema, stale evidence, pair hoặc ACK, sửa/cung cấp enforcement ở orchestration thay vì hy vọng training khắc phục.

Một base model có thể phục vụ nhiều role với system instructions riêng. Adapter riêng từng role là tuỳ chọn nếu đánh giá cho thấy cần. Bắt đầu bằng một role có input/output hẹp; không train sáu model cùng lúc hoặc suy kết quả của pilot lên các role khác.

## Dataset theo identity

| Role | Behavior mục tiêu | Negative/unknown examples |
|---|---|---|
| Prompt-Master | Biến goal đã làm rõ thành atomic DAG, owner, dependencies và gate. | Ambiguous scope, thiếu prerequisite, owner conflict hoặc continue cần revalidate context. |
| Triage-Sentinel | Trích metadata tĩnh thành output có schema và nguồn. | Truncated/unsupported header; entropy cao đơn lẻ không đủ kết luận packer. |
| Decomp-Analyst | Lập luận từ disassembly/decompiler/CFG và binding state. | Stale IDB, wrong slice, thiếu xref; proposal không được mô tả như applied change. |
| Crypto-Logic-Specialist | Nêu algorithm hypothesis chỉ khi constants và control/data flow cùng support. | Benign lookup/checksum tương tự; fragment không phân biệt được thì unknown. |
| Evidence-Synthesizer | Nối claim với provenance, tìm conflict/stale receipt và báo thiếu bằng chứng. | Missing receipt, rights/ACK unknown, competing intact evidence. |
| Product-Evolution-Architect | Dựa trên observation đã được chấp nhận để viết feature gap và acceptance criteria đo được. | Feature chưa quan sát, offline/compatibility/performance chưa đo. |

Mỗi mẫu cần role/version, prompt/context như khi dùng thật, evidence/source digest và locator, desired output, rights/applicability, người duyệt, lý do nhãn và group ID để giữ các mẫu liên quan trong cùng split. Không đưa private chain of thought, credential, unreviewed model output hoặc target evidence không được phép dùng vào corpus.

## Chia dữ liệu và đánh giá

Phân nhóm theo project, binary, binary family, build/version và derived lineage trước khi chia train/dev/sealed test. Tránh để các function gần nhau từ cùng binary xuất hiện ở cả train lẫn test. Đưa gold, heldout critiques và nhãn evaluator khỏi active retrieval/index. Lưu digest manifest cho dataset và từng split. Cỡ mẫu và ngưỡng không lấy theo con số tùy ý; xác định từ requirement, mức rủi ro và precision cần đạt.

Đóng evaluation trước khi xem kết quả: cùng input, context, tool version, budget và rubric cho baseline/candidate; metric riêng theo role; reviewer ground truth độc lập; report numerator/denominator, abstention, hard failures, regressions và chi phí/latency nếu đo được. Với mọi fixture, packet R4a phải được review và freeze trước attempt; R4b dùng raw output sau attempt. Không dùng heldout để tune hyperparameters.

## Phương án kỹ thuật

Nếu nhà cung cấp hỗ trợ đúng model/account và data policy, có thể dùng supervised fine-tuning cho format/instruction patterns với ví dụ được người có chuyên môn duyệt. Nếu dùng model có trọng số mở, PEFT LoRA có thể lưu adapter riêng trên base model; giữ đúng base weights, tokenizer, chat template, config và license. TRL SFTTrainer là một lựa chọn framework, không phải bảo đảm phần cứng hoặc chất lượng cho một model cụ thể. Cần đo VRAM, thời lượng, lưu trữ và tương thích trước khi chọn.

Khi kiểm ngày21/10/2026, [OpenAI Fine-tuning guide](https://developers.openai.com/api/docs/guides/supervised-fine-tuning) nói platform không mở cho organization mới; khách hàng hiện hữu đủ điều kiện có hạn tạo job muộn nhất 06/01/2027, có thể sớm hơn nếu base model dừng trước. Eligibility của tài khoản/model cụ thể phải được xác minh trực tiếp lúc lập kế hoạch. Không coi các tên model lịch sử trong cấu hình cũ là lựa chọn hiện hành.

Tài liệu tham khảo phương án open-weight: [Hugging Face PEFT LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) và [TRL SFTTrainer](https://huggingface.co/docs/trl/main/en/sft_trainer). Chốt license, phiên bản, chat template và base-model support trước khi chạy.

## Thứ tự pilot

1. Chọn một role và lỗi lặp có source evidence.
2. Kiểm prompt/retrieval/tool/contract fixes trước training.
3. Duyệt ví dụ, quyền sử dụng, ground truth và grouped splits.
4. Freeze candidate, baseline, eval packet, budget và stop criteria.
5. Chạy một thí nghiệm authorized; lưu model/data/config digests và raw metrics.
6. Reviewer độc lập đánh heldout; hard failure không được bù bằng semantic score.
7. Chỉ tích hợp adapter/model vào đúng role khi đạt threshold đã khóa, có version và rollback.

Training không tự làm thay đổi output parser hiện có. Chọn consumer thật trước: một Stage1 parser chạy trực tiếp sẽ không đổi chỉ vì huấn luyện model Triage riêng. Capability, broker scope, approval, REA evidence, IDA state, freshness và consumer ACK vẫn phải được kiểm ngoài model.
