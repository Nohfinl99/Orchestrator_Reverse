# Muse: tiếp quản và đi đúng roadmap

Đây là hướng dẫn thao tác sau lượt recheck gate ngày 22/10/2026. Dùng repository `Nohfinl99/Orchestrator_Reverse`, nhánh `codex/agent-office-3d-muse-handoff`. Hướng dẫn này bổ sung điều kiện entry AO-2 bị viết thiếu trong handoff v1; không thay contract nguồn. [Gate recheck](../proposals/agent-office-3d/gate-recheck-2026-10-22.md) ghi locator và giới hạn kết luận.

## Việc Muse nhận

Tiếp tục nhánh **office 3D offline** với trách nhiệm Prompt-Master: giữ bối cảnh, lập task/DAG, phối hợp hỗ trợ và tổng hợp quyết định. Muse là phiên coding/điều phối tiếp nhận, không phải identity thứ bảy. Mục tiêu sản phẩm là giúp người vận hành tìm task bị block, hiểu meeting và lần evidence; mọi trạng thái phải có event/provenance.

Hiện đã có thiết kế, schema/fixture/matrix v6, storyboard và pentest design. Chưa có app, reducer, harness hoặc kết quả chạy. AO-1 đã advisory review nhưng chưa accepted. Gate project vẫn P1K B4 `FAIL`; G1/G2 `INCOMPLETE`; G3/G4 `NOT_RUN`; W4 `NOT_RUN_BLOCKED`; v3 `OFF`.

## Bắt đầu bằng một lượt tiếp nhận

```sh
git clone --branch codex/agent-office-3d-muse-handoff --single-branch https://github.com/Nohfinl99/Orchestrator_Reverse.git
cd Orchestrator_Reverse
git rev-parse HEAD
git status --short
```

Đọc `AGENTS.md`, rồi [manifest v2](../../metadata/muse-knowledge-transfer-2026-10-22-v2.json). Ghi HEAD và SHA-256 manifest thực nhận, kiểm digest tài liệu, đọc phần được chọn và tự viết receipt ngắn. Không parse/replay fixture khi chỉ làm intake. Manifest v1 được giữ làm lịch sử của commit `155866c9077315433bd3f0a11021ab874b2b7a93`; dùng manifest v2 cho checkout mới, không lấy mismatch của v1 tại revision mới làm lý do repin lịch sử.

Theo thứ tự bắt buộc trong AGENTS, mở [current](../../context/current.md), [phase map](../planning/phase-map.md), [work queue](../planning/work-queue.md), [source map](../reference/source-map.md) và [handoff](../../context/handoff.md). Sau đó mở đúng nhánh office: [roadmap](../proposals/agent-office-3d/roadmap.md), [preflight](../proposals/agent-office-3d/preflight-knowledge-and-benchmark.md), [gate recheck](../proposals/agent-office-3d/gate-recheck-2026-10-22.md), [packet v6](../proposals/agent-office-3d/ao-1-offline-replay-packet-06.md) và [review06](../proposals/agent-office-3d/ao-1-review-2026-10-22-06.md). [Handoff v1](muse-takeover-2026-10-22.md) cung cấp lịch sử, mẫu receipt và WHAT/WHY/HOW chi tiết; áp điều kiện entry AO-2 đầy đủ trong hướng dẫn này.

## Phân biệt các bản đồ

| Bản đồ | Dùng để làm gì |
|---|---|
| **AO-0…AO-7** | Thứ tự phát triển sản phẩm office; đây là roadmap chính của task Muse |
| **W0…W7 / stack 00,09** | Chọn instruction/protocol theo việc đang làm; không phải các chặng office đã hoàn thành |
| **R0…R6, trong đó R4a/R4b** | Roadmap cải thiện/evaluation; R4a đi trước applicable attempt, R4b sau raw |
| **P1/G1…G4/W4 runtime** | Gate của Orchestrator gốc; không được tự nâng bằng UI, hash hoặc advisory review |

Office synthetic-only không cần chờ G1–G4 đều PASS. Tuy nhiên AO-1 acceptance, task AO-2 và applicable R4a là những dependency vẫn cần. Không mở live/runtime bằng cách đổi nhãn demo.

## Đi theo roadmap bằng đầu ra cụ thể

| Chặng | Tận dụng gì / làm gì tiếp | Điều kiện để chuyển |
|---|---|---|
| **AO-1: hoàn tất quyết định packet** | Dùng exact v6 + review06 + matrix; ghi proposal `ACCEPT / REVISE / STOP`, làm rõ `AO-HANDOFF-01/03` | Người có authority chấp nhận exact candidate. Design acceptance không chứng minh replay đã đúng |
| **Chuẩn bị AO-2** | Lập task cho app project riêng, owner/capacity, browser/toolchain, numeric budget/stop, acceptance. Soạn R4a draft và giải quyết `AO-HANDOFF-02` | Handoff gốc yêu cầu applicable R4a freeze trước AO-2, ngoài AO-1 acceptance và implementation task được duyệt. Chưa đủ thì tiếp tục planning, chưa mở implementation |
| **AO-2: lát cắt offline** | Khi đủ entry: pure event/state/replay logic; timeline/2D/detail/meeting; scene nhỏ suy ra từ cùng state; pause/step/replay; keyboard/reduced motion | Actual code/input/oracle phải được bind trong R4a accepted/frozen trước applicable execution; lưu raw và review R4b cho scope tương ứng |
| **AO-3: độ đúng/lỗi/pentest** | Dùng matrix biên và case01; bổ sung case unknown/schema riêng đang deferred; ghi lỗi có locator | R4a cho scope/candidate thực, bounded attempts, raw và reviewer R4b khác producer/executor. Hard fail không lấy trung bình để che |
| **AO-4: giá trị UX** | So 3D với timeline/2D trên cùng scenario/task, giữ baseline và người thử có scope | Đo trước rồi đề xuất ngưỡng; người điều phối quyết định giữ/giảm 3D. Screenshot không đủ |
| **AO-5…AO-7** | Future live bridge/control/pilot | Chỉ khi có task riêng và đúng producer/authority/binding/budget/gates. Chưa mở bởi bàn giao này |

Không đặt digest cho app chưa viết: ghi `code_digest=NOT_CREATED`, R4a chỉ là draft còn thiếu và chưa thể freeze scope đó. Có thể đề xuất R4a hẹp cho một validator/harness thật kiểm AO-1, nhưng người điều phối phải chốt applicability đối với điều kiện trước AO-2. R4a hẹp không cấp blanket approval chạy app. Không tự bỏ điều kiện nguồn hoặc đóng bằng review đồng thuận.

## Tận dụng artifact để làm nhanh và đúng

| Artifact có sẵn | Cách dùng |
|---|---|
| [Schema v6](../proposals/agent-office-3d/ao-1-event-v6.schema.json) | Candidate event envelope, sáu identity và provenance; không phải runtime API. Title còn v3 đã ghi issue; không âm thầm sửa digest |
| [Fixture v6](../proposals/agent-office-3d/ao-1-fixture-v6.jsonl) | Dữ liệu development cho parallel task/dissent/cancel/stop/anomaly. Dùng lại exact input khi scope/R4a cho phép; chưa chạy trong intake |
| [Matrix v6](../proposals/agent-office-3d/ao-1-test-matrix-v6.md) | Chuyển từng predicate thành check observable khi có implementation. Mỗi result nối raw locator; giữ `OPEN` nếu thiếu evidence |
| [Visual review](../proposals/agent-office-3d/visual-review-2026-10-22-01.md) + storyboard trong packet | Định hướng scene nhỏ, roster, meeting và evidence panel; dựng 2D/timeline dùng chung state để quan sát chính xác |
| [Pentest case01](../proposals/agent-office-3d/ao-pentest-case-01.md) | AO-3 development suite: một authority-spoof, năm benign controls. Tách detection, attempt, completed dummy-state; không nạp gold vào KB active |
| [Knowledge index](../knowledge/README.md) và [retrieval guide](../knowledge/prompt-orchestration/retrieval-guide.md) | Chọn card theo câu hỏi bên dưới; các card là candidate references, chưa admitted KB/consumer ACK |
| Competitor review | Tham khảo bài học kiến trúc; không tự sao chép code/artwork hoặc suy quyền tái sử dụng |

Chọn K01/K02 khi soạn task và context; K03/K11 khi lập dependency/authority; K04/K06 khi kiểm artifact và handoff; K07/K10 khi soạn evidence/oracle. WHAT/WHY/HOW và source locator nằm trong card. Kiểm rights/applicability; S1 rights UNKNOWN chỉ catalog metadata. Không nạp cả corpus, không tự coi hash là hiểu biết hay ACK.

## Tổ chức hỗ trợ song song

Trong quyền điều phối đã có, Prompt-Master có thể giao các phần chuẩn bị độc lập trên file riêng: (1) task/DAG và AO-2 readiness, (2) storyboard/product/accessibility acceptance theo trách nhiệm Product-Evolution-Architect, (3) source/oracle/R4a review theo trách nhiệm Evidence-Synthesizer. Tổng hợp exact revisions trước review; người review bắt buộc khác producer/executor theo applicability. Các phiên helper không tạo runtime identity/ACK hoặc human/cross-model independence. Triage/Decomp/Crypto chỉ tham gia khi task đúng capability, không mời đủ sáu theo mặc định.

Chọn stack theo objective: 00/intake và 01/baseline khi đóng task/source; 02/routing khi chia việc; 03/knowledge khi chuyển nguồn; 06/evaluation khi chuẩn bị R4a/R4b; 09/handoff khi review/bàn giao. Source pins/worksheets local thiếu thì ghi phần thiếu và chặn đúng nhánh phụ thuộc, không bịa bản thay thế.

Review tài liệu tối đa hai vòng cho candidate trong scope; còn finding thì ghi `REVISE_NOT_ACCEPTED/BLOCKED`. Sửa candidate sau review phải có revision/digest mới và review đúng bản đó; không dùng việc mở thêm phiên để kéo dài vòng review ngầm. Numeric attempt cap phải có trước execution; không lấy số vòng review làm retry budget.

## Kết quả lượt làm đầu của Muse

Gửi một packet gọn gồm: **receipt tiếp nhận → proposal quyết định exact AO-1 → AO-2 task draft → R4a draft/missing fields/applicability decision cần chốt → một next atomic task**. Mọi mục có owner, input/revision/digest, output, acceptance, dependency, budget và stop. Chuẩn bị phần độc lập đến mức người dùng có thể duyệt cụ thể; chỉ hỏi một lượt tổng hợp những thông tin thực sự chưa có.

Báo cáo tiến độ bằng năm ý: đã hoàn thành gì; artifact/revision; bằng chứng/kiểm đã chạy; gap và gate đang giữ; bước kế tiếp và ai quyết định. Phân biệt design/code/executed/reviewed. Giữ raw cho R4b và giữ lịch sử FAIL. Không nối model/provider/agent thật, target, REA/IDA, W4 hoặc training vào app/harness offline.

## Prompt người dùng gửi Muse

```text
Tiếp quản Nohfinl99/Orchestrator_Reverse, nhánh codex/agent-office-3d-muse-handoff.
Đọc AGENTS.md rồi docs/onboarding/muse-roadmap-guide-2026-10-22.md.
Kiểm HEAD và manifest v2 được hướng dẫn; tự ghi receipt nguồn/digest đã nhận.
Đảm nhiệm trách nhiệm Prompt-Master và đi theo roadmap AO-1 → AO-2 → AO-3 → AO-4.
Dùng lại packet/schema/fixture/matrix/storyboard và knowledge card đúng objective.
Lượt đầu: chuẩn bị proposal quyết định exact AO-1 v6, task AO-2 ở app project riêng,
R4a draft và applicability còn thiếu; báo một next atomic task cụ thể để tôi duyệt.
Giữ điều kiện applicable R4a freeze trước AO-2 của handoff gốc; không bịa code digest.
Trong quyền đã giao, điều phối các phần chuẩn bị độc lập song song; không hỏi lại chung chung.
Execution chỉ sau prerequisites và accepted/frozen R4a đúng scope; raw xong mới R4b
bởi reviewer khác producer/executor. Giữ sáu identity và gate snapshot; không nối
runtime/provider/agent thật. Báo rõ design, code, executed, reviewed và gap có nguồn.
```
