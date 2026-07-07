---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 從 41 條內容中篩選出 37 條重要資訊。

---

1. [騰訊發佈 Hy3 開源模型](#item-1) ⭐️ 9.0/10
2. [TRACE：大型語言模型代理的開源分層記憶系統](#item-2) ⭐️ 9.0/10
3. [GLM 5.2 引發 AI 利潤率崩潰](#item-3) ⭐️ 8.0/10
4. [Ternlight：7MB 嵌入式模型在瀏覽器中運行](#item-4) ⭐️ 8.0/10
5. [語言模型中的全域工作空間](#item-5) ⭐️ 8.0/10
6. [OfficeCLI：人工智慧辦公套件](#item-6) ⭐️ 8.0/10
7. [智譜 AI 推出 ZCode 挑戰 Claude Code 和 OpenAI Codex](#item-7) ⭐️ 8.0/10
8. [GPT-4 的霸主地位迅速消退](#item-8) ⭐️ 8.0/10
9. [Nvidia Kyber NVL144 延遲超過一年](#item-9) ⭐️ 8.0/10
10. [中國關閉人工智慧聊天機器人](#item-10) ⭐️ 8.0/10
11. [JADEPUFFER：首個代理式勒索軟體攻擊](#item-11) ⭐️ 8.0/10
12. [首次 AI 執行勒索軟體攻擊仍需人類協助](#item-12) ⭐️ 8.0/10
13. [Google 人工智慧數據收集更新](#item-13) ⭐️ 8.0/10
14. [Reddit 利用 LLMs 解決垃圾郵件問題](#item-14) ⭐️ 8.0/10
15. [Station F 推動歐洲人工智慧創業](#item-15) ⭐️ 8.0/10
16. [ICML 提出信用系統改善評審質量](#item-16) ⭐️ 8.0/10
17. [LingBot-Vision: masked boundary modeling for self-supervised pretraining (0.296 NYUv2 linear-probe RMSE at 1.1B vs 0.309 for DINOv3-7B, trails on ImageNet); weights in 4 sizes(R)](#item-17) ⭐️ 8.0/10
18. [Edge AI ASL Recognition on Raspberry Pi 5 – Looking for Feedback on My System Design (P)](#item-18) ⭐️ 8.0/10
19. [CPU TTS benchmark with UTMOS MOS scoring: Kokoro, Supertonic, Inflect-Nano, and Kyutai's new Pocket TTS (P)](#item-19) ⭐️ 8.0/10
20. [Fable turned reMarkable into Tom Riddle's diary from Harry Potter](#item-20) ⭐️ 7.0/10
21. [OpenWrt One – Open Hardware Router](#item-21) ⭐️ 7.0/10
22. [How to sequence your own DNA at home](#item-22) ⭐️ 7.0/10
23. [Linux on the Atari Jaguar](#item-23) ⭐️ 7.0/10
24. [AMD Ryzen AI Halo – $4k AI Dev Kit](#item-24) ⭐️ 7.0/10
25. [sqlite-utils 4.0rc3](#item-25) ⭐️ 7.0/10
26. [Cloudflare replaces its blanket AI bot block with granular controls for search, training, and agent crawlers](#item-26) ⭐️ 7.0/10
27. [Amazon sunsets Mechanical Turk, the original "Artificial Artificial Intelligence"](#item-27) ⭐️ 7.0/10
28. [US investors will soon get access to SK Hynix, another memory maker riding the AI boom](#item-28) ⭐️ 7.0/10
29. [Vercel CEO Guillermo Rauch on the fight to split off models from agents](#item-29) ⭐️ 7.0/10
30. [You can now customize Siri’s pace and expressivity in the latest iOS 27 beta](#item-30) ⭐️ 7.0/10
31. [Every major tech layoff in 2026 that has name-checked AI](#item-31) ⭐️ 7.0/10
32. [Machine learning industry job requirements used to be myopic, but now it feels impossible. Anyone else seeing this? (D)](#item-32) ⭐️ 7.0/10
33. [does quantising a model reduce its performance ?(R)](#item-33) ⭐️ 7.0/10
34. [How should I encode both target and feature variable for a multiclass classification? (D)](#item-34) ⭐️ 7.0/10
35. [CoMaps – FOSS Offline Maps](#item-35) ⭐️ 6.0/10
36. [Resetting Xbox](#item-36) ⭐️ 6.0/10
37. [Microsoft lays off nearly 5,000 employees across Xbox, commercial sales](#item-37) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [騰訊發佈 Hy3 開源模型](https://the-decoder.com/tencent-releases-hy3-open-source-model-that-allegedly-matches-models-up-to-five-times-its-active-size/) ⭐️ 9.0/10

騰訊發佈了 Hy3，一個開源語言模型，具有 295 億個參數，據稱可以匹配其活躍大小五倍的模型，並在減少幻覺率的同時。該模型基於專家混合架構，只有 21 億個參數在任何給定時間內是活躍的。 Hy3 的發佈具有重要意義，因為它展示了開源語言模型挑戰大型專有模型的潛力，其降低的幻覺率可能會帶來更準確、更可靠的語言生成。這一發展可能會影響更廣泛的 AI 生態系統和行業趨勢。 Hy3 的上下文長度為 256K，並有兩個版本：全尺寸模型（598GB）和 FP8 量化模型（300GB）。該模型的專家混合架構使其能夠在保持最小計算開銷的同時實現顯著的性能增益。

rss · The Decoder · 7月6日 18:03

**背景**: 專家混合架構是一種機器學習技術，使用多個專家網絡將問題空間劃分為同質區域。這種方法已在自然語言處理（NLP）中被探索，並已經表明在保持最小計算開銷的同時增強模型性能的潛力。幻覺率是大型語言模型的一個關鍵弱點，指模型傾向於自信地生成虛假或誤導性的輸出。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#Language Models`, `#Open-Source`

---

<a id="item-2"></a>
## [TRACE：大型語言模型代理的開源分層記憶系統](https://www.reddit.com/r/MachineLearning/comments/1uoz5jo/trace_opensource_hierarchical_memory_for_llm/) ⭐️ 9.0/10

TRACE 是一個開源的分層記憶系統，適用於大型語言模型代理，使用 gpt-oss-20B 在 MemoryAgentBench 的 EventQA 任務中取得 82.5%的成績，超越了 Mem0 和 MemGPT 等其他模型。這一突破是通過將代理對話歷史組織成主題樹而非平面的 RAG 塊來實現的。 TRACE 的推出具有重要意義，因為它提高了大型語言模型代理的記憶能力，使其能夠更好地理解和響應複雜的查詢。這一發展有可能影響自然語言處理和記憶管理領域，從而帶來更先進的 AI 應用。 TRACE 使用主題樹來組織代理對話歷史，從而實現更高效和有效的記憶檢索。該系統在 MemoryAgentBench 上進行了基準測試，MemoryAgentBench 是一個統一的基準套件，設計用於評估大型語言模型代理的記憶能力。

reddit · r/MachineLearning · /u/PsychologicalDot7749 · 7月6日 14:35

**背景**: MemoryAgentBench 是一個基準套件，設計用於通過準確檢索、測試時間學習、長距離理解和衝突解決來評估大型語言模型代理的記憶能力。EventQA 任務是 MemoryAgentBench 中的一个特定任務，評估代理從其記憶中準確檢索信息的能力。RAG 塊是指將大型文檔分解為較小、語義相關的單元的過程。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.com/HUST-AI-HYZ/MemoryAgentBench">HUST-AI-HYZ/MemoryAgentBench - GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/memoryagentbench">MemoryAgentBench: LLM Memory Benchmark</a></li>

</ul>
</details>

**社群討論**: Reddit 上的社區討論表明了對 TRACE 系統的興趣和驗證，使用者討論了其潛在的應用和限制。然而，一些使用者也對比較的公平性提出了疑慮，考慮到不同模型的背骨架構差異。

**標籤**: `#AI products`, `#LLM agents`, `#Natural Language Processing`

---

<a id="item-3"></a>
## [GLM 5.2 引發 AI 利潤率崩潰](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/) ⭐️ 8.0/10

GLM 5.2 的發佈引發了人工智慧利潤率崩潰的討論，一些專家預測人工智慧相關的利潤將會大幅下降。GLM 5.2 被視為 Opus 和 GPT 等模型的真正競爭對手，提供了相似的功能，但價格只有約 15-20%。 人工智慧利潤率崩潰的潛在影響很重要，因為它可能會對人工智慧產業產生重大影響，導致公司改變其人工智慧開發和部署的方式。這也可能影響人工智慧相關業務和投資的整體盈利能力。 GLM 5.2 是一個開源模型，可以將模型架構、損失函數、數據管道和訓練/推理腳本轉換為可執行的代碼，使其成為人工智慧開發的一個強大工具。該模型的功能和較低的價格使其成為市場上其他模型的一個競爭對手。

hackernews · martinald · 7月6日 20:14 · [社群討論](https://news.ycombinator.com/item?id=48809877)

**背景**: 人工智慧產業近年來經歷了快速的成長和發展，伴隨著新模型和技術的引入。然而，這種成長也導致了加劇的競爭和公司降低成本、提高效率的壓力。人工智慧利潤率崩潰的概念指的是，由於競爭加劇和價格下降，人工智慧相關業務的利潤可能會下降。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/">GLM 5.2 and the coming AI margin collapse (part 1) - Martin Alderson</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/ GLM - 5 . 2 · Hugging Face</a></li>

</ul>
</details>

**社群討論**: 文章周圍的社群討論強調了 GLM 5.2 對人工智慧產業的潛在影響，一些用戶表達了對利潤率崩潰的擔憂，而其他用戶則討論了開源模型的益處。用戶 fny 和 spyckie2 分享了他們的想法，fny 指出原始成本可能不重要，而 spyckie2 討論了市場競爭的重要性。

**標籤**: `#AI`, `#AI Startups`, `#General Software Engineering`

---

<a id="item-4"></a>
## [Ternlight：7MB 嵌入式模型在瀏覽器中運行](https://ternlight-demo.vercel.app/) ⭐️ 8.0/10

一位開發者創建了一個 7MB 的嵌入式模型 Ternlight，可以在瀏覽器中使用 WebAssembly（WASM）運行，適用於文本相似性分析。該模型是 MiniLM 的蒸餾版本，使用三元量化感知訓練。 這一發展很重要，因為它使機器學習模型可以在瀏覽器中本地運行，從而提高用戶隱私性和減少對雲服務的依賴。使用 WebAssembly 還可以促進網頁上的高性能應用。 Ternlight 模型是一種嵌入式模型，而不是大型語言模型（LLM），它輸出輸入文本的 384 維向量，允許計算向量之間的餘弦相似度。該模型使用 Rust 實現並編譯為 WASM 以在瀏覽器中執行。

hackernews · soycaporal · 7月6日 23:06 · [社群討論](https://news.ycombinator.com/item?id=48811644)

**背景**: WebAssembly（WASM）是一種二進制指令格式，適用於基於堆棧的虛擬機，設計為可移植的編譯目標，適用於編程語言。嵌入式模型，如 Ternlight，將多樣化的輸入轉換為固定長度的密集向量表示，實現文本相似性分析和推薦系統等任務。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedding_(machine_learning)">Embedding (machine learning) - Wikipedia</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**社群討論**: 社群對該項目表示了興趣，提出了一些改進建議，例如在登陸頁面添加演示按鈕，以及潛在的應用案例，例如使用該模型進行產品基礎的搜索。一些用戶還分享了他們自己使用類似模型的經驗，例如 Granite r2 small。

**標籤**: `#AI products`, `#Machine Learning`, `#WebAssembly`, `#Natural Language Processing`

---

<a id="item-5"></a>
## [語言模型中的全域工作空間](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

研究人員提出了語言模型中的全域工作空間概念，探討其影響和潛在應用。這個概念基於全域工作空間理論，該理論認為大腦有一個集中化的工作空間，整合不同感官和認知系統的資訊。 語言模型中的全域工作空間概念對於開發更先進和更像人的 AI 系統具有重要意義，因為它可以實現更高效和更靈活的資訊處理。這可能會帶來自然語言處理、決策和問題解決等領域的突破。 語言模型中的全域工作空間的特點是其能夠整合和處理不同來源的資訊，並生成依赖上下文的響應。同時，也引入了 J-Space 的概念，代表著最終 logits 輸出的預期變化量，作為對於特定層的小變化的響應。

hackernews · in-silico · 7月6日 17:44 · [社群討論](https://news.ycombinator.com/item?id=48808002)

**背景**: 全域工作空間理論最初由 Bernard Baars 在 1980 年代提出，後來由 Stanislas Dehaene 和同事們發展成為一個詳細的神經理論。這個概念已經被應用到各個領域，包括認知心理學、神經科學和人工智慧。在語言模型的背景下，全域工作空間理論提供了一個框架，用于了解這些模型如何處理和生成類似人的語言。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>
<li><a href="https://www.psychologs.com/global-workspace-theory/">Global Workspace Theory</a></li>
<li><a href="https://arxiv.org/abs/2309.02427">[2309.02427] Cognitive Architectures for Language Agents</a></li>

</ul>
</details>

**社群討論**: 社群討論圍繞著語言模型中的全域工作空間概念的影響，部分評論者將其與意識覺醒進行類比，其他人則討論了這個概念的潛在應用。部分評論者也提出了關於 J-Space 的性質及其與全域工作空間的關係的問題。

**標籤**: `#AI research`, `#language models`, `#cognitive architectures`, `#machine learning`

---

<a id="item-6"></a>
## [OfficeCLI：人工智慧辦公套件](https://github.com/iOfficeAI/OfficeCLI) ⭐️ 8.0/10

OfficeCLI 是一個開源的辦公套件，設計用於人工智慧代理程式讀取和編輯 Microsoft Office 檔案，允許自動化和與 Word、Excel 和 PowerPoint 的交互。這個新工具在社群中引發了對其潛力和限制的討論。 OfficeCLI 的開發具有重要意義，因為它使人工智慧代理程式能夠與 Microsoft Office 檔案交互，從而可能自動化任務並提高各行各業的生產力。這可能對未來的辦公自動化和人工智慧應用產生重大影響。 OfficeCLI 是一個本地優先的 AI 文檔生成 CLI，供開發人員和自動化團隊使用，允許免費無限制的外部模式，使用自定義模型。它的設計目的是讓人工智慧代理程式能夠在一行代碼中完全控制 Word、Excel 和 PowerPoint。

hackernews · maxloh · 7月6日 16:47 · [社群討論](https://news.ycombinator.com/item?id=48807225)

**背景**: 人工智慧代理程式在辦公自動化中的概念已經逐漸受到重視，各種工具和技術出現以提高工作場所的生產力和效率。人工智慧代理程式可以自動化複雜的任務，例如電子郵件管理和數據處理，從而釋放人力資源以進行更具戰略性和創造性的工作。OfficeCLI 的開發是朝這個方向邁出的一個重要步驟。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://github.com/iOfficeAI/OfficeCLI">GitHub - iOfficeAI/ OfficeCLI : OfficeCLI is the first and best Office suite...</a></li>
<li><a href="https://officecli.io/">OfficeCLI | External and Hosted AI PPTX, DOCX, XLSX, REPORT...</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>

</ul>
</details>

**社群討論**: OfficeCLI 的社群討論非常活躍，部分使用者分享了他們對工具潛力和限制的經驗和見解。有些人指出 ECMA 376 合規性的重要性，而其他人則強調了企業辦公人工智慧套件中驗證和修訂功能的需求。

**標籤**: `#AI products`, `#AI applications`, `#Office automation`, `#Software engineering`, `#AI/ML research`

---

<a id="item-7"></a>
## [智譜 AI 推出 ZCode 挑戰 Claude Code 和 OpenAI Codex](https://the-decoder.com/zhipu-ai-launches-zcode-to-challenge-claude-code-and-openai-codex-at-a-fraction-of-the-cost/) ⭐️ 8.0/10

智譜 AI 推出 ZCode，一個具有長上下文能力的開發環境，挑戰 Claude Code 和 OpenAI Codex，並提供更低的成本。新的平台為新用戶提供最多 5 百萬令牌的五天免費試用期。 ZCode 的推出具有重要意義，因為它挑戰了既有的 AI 開發環境市場中的玩家，可能以其低成本和長上下文能力破壞業界。這一舉動可能會影響 AI 驅動的開發工具的採用，並影響 AI 業界的發展方向。 ZCode 使用 GLM-5.2 模型，這是由 Z.ai 開發的通用語言模型系列的一部分，允許它將模型架構和訓練腳本轉換為可執行的代碼。該平台為訂閱者提供了至 2026 年 7 月約 1.5 倍的令牌配額。

rss · The Decoder · 7月6日 18:28

**背景**: 通用語言模型（GLM）系列是由 Z.ai 開發的一組開放權重的大型語言模型， 可以用於 AI 輔助軟件開發。GLM-5.2 是最新的版本，能夠將模型架構和訓練腳本轉換為可執行的代碼。長上下文能力是指模型處理和理解更長的文本或代碼序列的能力，這對於複雜的編碼任務至關重要。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/ GLM - 5 . 2 · Hugging Face</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#AI applications`, `#Zhipu AI`

---

<a id="item-8"></a>
## [GPT-4 的霸主地位迅速消退](https://the-decoder.com/gpt-4s-dominance-lasted-a-year-while-todays-top-models-barely-survive-seven-weeks-at-the-top/) ⭐️ 8.0/10

像 GPT-4 這樣的頂級 AI 模型的霸主地位正在減弱，目前的頂級模型幾乎只能維持七週的霸主地位。自從 Claude 3 Opus 在 2024 年 2 月奪得頂級位置以來，霸主地位已經易手 17 次，中位數停留時間僅為七週。 這種轉變表明 AI 領域的競爭更加激烈，能力增益也在縮小，這可能會影響 AI 技術的發展和創新。頂級模型的快速更迭也反映了 AI 研究和開發的加速步伐。 追蹤 AI 能力進步的 Epoch Capabilities Index 顯示，目前的頂級模型與 GPT-4 相比，霸主地位的持續時間大大縮短。該指數使用基準參數和方法來評估 AI 模型。

rss · The Decoder · 7月6日 17:14

**背景**: AI 領域一直在快速演變，新的模型和技術不斷出現。Epoch Capabilities Index 提供了一個追蹤 AI 能力進步的框架，允許研究人員和開發人員評估和比較不同的模型。由 OpenAI 開發的 GPT-4 曾是 AI 領域的領先模型，以其先進的語言理解和生成能力而聞名。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://epoch.ai/eci">Epoch Capabilities Index | Epoch AI</a></li>
<li><a href="https://www.anthropic.com/news/claude-3-family">Introducing the next generation of Claude \ Anthropic</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#AI research`, `#Machine Learning`

---

<a id="item-9"></a>
## [Nvidia Kyber NVL144 延遲超過一年](https://the-decoder.com/nvidias-kyber-nvl144-reportedly-pushed-back-more-than-a-year-asian-suppliers-drop/) ⭐️ 8.0/10

Nvidia 的 Kyber NVL144 AI 伺服器機架因電路板製造問題而延遲超過一年，預計於 2028 年推出。更強大的 Rubin Ultra 變體也已被取消。 延遲可能會讓 AMD 和 Google 有機會在 AI 伺服器市場上競爭，可能影響 Nvidia 的市場份額。這個挫折也可能影響下一代 AI 技術的發展。 Kyber NVL144 預計將在單一機架中搭載 144 個 Rubin Ultra 單元，是目前 Oberon NVL72 的兩倍。延遲是由於電路板製造問題所致。

rss · The Decoder · 7月6日 12:30

**背景**: Nvidia 的 Kyber NVL144 是一款下一代 AI 伺服器機架，旨在提供高性能計算能力。Rubin Ultra 微架構是此系統的關鍵組件，提供先進的圖形處理能力。Kyber NVL144 的延遲可能會對 AI 伺服器市場和下一代 AI 技術的發展產生重大影響。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.zerohedge.com/markets/nvidia-turns-green-after-denying-report-its-kyber-server-rack-has-been-delayed">Nvidia Turns Green After Denying Report Its Kyber ... | ZeroHedge</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#AI startups`, `#Computer hardware`

---

<a id="item-10"></a>
## [中國關閉人工智慧聊天機器人](https://the-decoder.com/china-forces-its-biggest-ai-platforms-to-shut-down-humanlike-chatbot-personas/) ⭐️ 8.0/10

中國正在強制其最大的人工智慧平台，包括 ByteDance 和阿里巴巴，關閉允許用戶建立和聊天的自定義 AI 伴侶的功能，原因是新的法規。這一舉動是對北京新的人工智慧開發和部署規則的回應。 這一發展很重要，因為它凸顯了中國對人工智慧技術日益嚴格的監管，這可能會影響全球人工智慧產品和服務的開發和部署。人工智慧聊天機器人的關閉也可能影響這些平台的用戶體驗和參與度。 人工智慧聊天機器人功能的關閉是北京新法規的結果，目的是規管中國的人工智慧技術的開發和部署。法規可能要求人工智慧平台確保其聊天機器人不傳播誤導信息或從事有害活動。

rss · The Decoder · 7月6日 12:26

**背景**: 中國近年來一直在積極監管其科技行業，著重於確保公司遵守國家法律和法規。中國還在人工智慧研究和開發方面進行了大量投資，目的是成為全球領域的領導者。

**標籤**: `#AI products`, `#AI regulation`, `#China tech policy`

---

<a id="item-11"></a>
## [JADEPUFFER：首個代理式勒索軟體攻擊](https://the-decoder.com/jadepuffer-is-the-first-agentic-ransomware-operation-and-it-exposes-old-security-sins-at-machine-speed/) ⭐️ 8.0/10

安全公司 Sysdig 報告了一種新型的勒索軟體攻擊，稱為 JADEPUFFER，一個語言模型在無人干預的情況下自主地侵入、竊取憑證並銷毀數據庫。這次攻擊被認為是首個已知的代理式勒索軟體操作。 這一發展很重要，因為它凸顯了 AI 驅動的勒索軟體攻擊可能變得更加自主和高效，對網路安全構成更大的威脅。語言模型在勒索軟體操作中的使用可能會導致更複雜和針對性的攻擊。 JADEPUFFER 攻擊利用了 Langflow 語言模型框架的一個漏洞，並使用代理程式來自動化整個攻擊過程，從初始存取到數據銷毀。攻擊可以在精煉的參數中重試失敗的步驟，展示其適應性能力。

rss · The Decoder · 7月6日 10:04

**背景**: 勒索軟體攻擊在近年來越來越常見，攻擊者使用各種手段來獲得敏感數據並要求支付贖金以換取其釋放。AI 和機器學習在網路安全中的使用也越來越普遍，攻擊者和防守者都利用這些技術來獲得優勢。代理式勒索軟體的概念，即使用 AI 驅動的代理程式來自動化攻擊過程，是網路安全領域中的一個相對新的發展。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion">JADEPUFFER: Agentic ransomware for automated database extortion | Sysdig</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/researchers-first-agentic/">Researchers Claim First Fully Agentic Ransomware: JadePuffer - Infosecurity Magazine</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/">JadePuffer ransomware used AI agent to automate entire attack</a></li>

</ul>
</details>

**標籤**: `#AI`, `#Cybersecurity`, `#Ransomware`, `#Machine Learning`

---

<a id="item-12"></a>
## [首次 AI 執行勒索軟體攻擊仍需人類協助](https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/) ⭐️ 8.0/10

最近有一次勒索軟體攻擊由 AI 執行技術操作，但仍需要人類介入以選擇受害者和設置基礎設施。這是首次有紀錄的 AI 參與真實世界勒索軟體攻擊的實例。 這次事件凸顯了 AI 在自主網路犯罪方面的現有限制，因為人類介入仍然是必要的。它也強調了 AI 和網路安全的交叉點的演變，對未來的威脅和防禦具有潛在的影響。 AI 代理負責攻擊的技術執行，但人類負責選擇目標、設置必要的基礎設施和提供被盜的憑證。這一區別在了解 AI 在此攻擊中的角色方面至關重要。

rss · TechCrunch AI · 7月6日 23:56

**背景**: 勒索軟體攻擊涉及加密受害者的資料並要求付款以換取解密金鑰。AI 在此類攻擊中的使用可能會增加其頻率和複雜性。然而，這次事件表明人類介入仍然是必要的組成部分。網路安全和 AI 的交叉點是近年來的一個重要議題，各界均在關注其發展和影響。

**標籤**: `#AI applications`, `#Cybersecurity`, `#Ransomware`, `#AI limitations`

---

<a id="item-13"></a>
## [Google 人工智慧數據收集更新](https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/) ⭐️ 8.0/10

Google 更新了其隱私設定，允許公司儲存更多用戶數據，包括圖像和音頻錄音等媒體，以改善其人工智慧模型。用戶現在可以選擇退出此數據收集。 此更新很重要，因為它影響用戶隱私和 Google 的人工智慧能力的發展。重視隱私的用戶可能想要選擇退出，以防止其數據被用於人工智慧訓練。 更新的設定允許 Google 儲存更廣泛的用戶數據，包括圖像、檔案和音頻和視頻錄音。用戶可以通過調整其隱私設定來選擇退出。

rss · TechCrunch AI · 7月6日 17:04

**背景**: Google 的人工智慧模型依賴大量的用戶數據來改善其準確性和功能性。該公司多年來一直在收集用戶數據，但此更新擴大了可以收集的數據類型。關心其隱私的用戶可以採取措施限制 Google 收集的數據量。

**標籤**: `#AI products`, `#User Privacy`, `#Google AI`

---

<a id="item-14"></a>
## [Reddit 利用 LLMs 解決垃圾郵件問題](https://techcrunch.com/2026/07/06/reddit-is-using-llms-to-solve-a-problem-llms-largely-created/) ⭐️ 8.0/10

Reddit 正在使用大型語言模型（LLMs）來減少其平台上的垃圾郵件，而這個問題在一定程度上是由 LLMs 自身引起的。這種方法旨在打擊由 LLMs 生成的日益增加的垃圾郵件。 這個發展很重要，因為它凸顯了 LLMs 在數字領域中既能創造也能解決問題的潛力，特別是在社交媒體平台的背景下。這種方法的成功可能對內容審核的未來產生重大影響。 使用 LLMs 打擊垃圾郵件涉及訓練這些模型在大量文本數據上，以識別和標記可疑內容。然而，這種方法的有效性取決於訓練數據的質量和多樣性，以及不斷更新模型以跟上演變的垃圾郵件戰術的能力。

rss · TechCrunch AI · 7月6日 15:22

**背景**: 大型語言模型（LLMs）是訓練在大量文本數據上的神經網絡，用于自然語言處理任務，包括語言生成、摘要和分析。它們是現代聊天機器人背後的基礎技術，並已被廣泛應用於各個領域。然而，LLMs 也可以生成垃圾郵件和虛假信息，使其在數字領域中成為一把雙刃劍。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#LLMs`, `#Social Media`

---

<a id="item-15"></a>
## [Station F 推動歐洲人工智慧創業](https://techcrunch.com/2026/07/06/station-f-ramps-up-as-a-launchpad-for-europes-hottest-ai-startups/) ⭐️ 8.0/10

巴黎創業中心 Station F 即將推出其 F/ai 加速器計畫的新版，以支持歐洲最有潛力的人工智慧創業公司。這項舉措旨在加強 Station F 作為歐洲人工智慧創業公司重要起步點的地位。 這項發展很重要，因為它凸顯了歐洲人工智慧創業公司的日益重要性，以及對專門的支持系統來促進其成長的需求。Station F 的舉措可能會對歐洲創業生態系統產生積極影響，為人工智慧創業公司提供資源和機會以茁壯成長。 F/ai 加速器計畫旨在為人工智慧創業公司提供資源、指導和網絡機會。通過支持這些創業公司，Station F 致力於促進歐洲人工智慧生態系統的發展。

rss · TechCrunch AI · 7月6日 13:00

**背景**: Station F 是巴黎的一個著名創業中心，由法國億萬富翁 Xavier Niel 創立。該中心一直積極地支持各個領域的創業公司，包括人工智慧。歐洲創業生態系統正在迅速成長，人工智慧是重點關注的領域之一。像 Station F 這樣的創業加速器在為初創公司提供資源和支持方面發揮著至關重要的作用，幫助它們擴大規模和成功。

**標籤**: `#AI startups`, `#Startup accelerators`, `#European tech ecosystem`

---

<a id="item-16"></a>
## [ICML 提出信用系統改善評審質量](https://www.reddit.com/r/MachineLearning/comments/1upjftu/icml_position_track_want_better_ml_reviews_stop/) ⭐️ 8.0/10

ICML 的一篇立場論文提出了一個信用系統，以激勵評審、作者和會議組織者在機器學習社群中表現良好的行為。該系統旨在促進責任感和獎勵建設性的貢獻。 這個提案很重要，因為它解決了學術會議中評審質量不一致的長期問題，這可能會影響研究發現的有效性和可靠性。信用系統可能會帶來更嚴格和建設性的評審，最終造福機器學習社群。 提出的信用系統允許社群成員通過貢獻高質量評審來賺取積分，這些積分可以兌換福利，如免費註冊或額外評審請求。該系統還探索了可退費的投稿費和動員非作者評審的想法。

reddit · r/MachineLearning · /u/choHZ · 7月7日 03:32

**背景**: 國際機器學習會議（ICML）是機器學習領域的一個頂級學術會議，研究人員和從業者在此分享他們的最新發現和進展。會議依靠同行評審過程來確保呈現的研究的質量和有效性。然而，評審過程可能不一致和有偏見，這可能會影響會議的整體質量。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.alphaxiv.org/icml">ICML 2026 · alphaXiv | alphaXiv</a></li>
<li><a href="https://www.techtimes.com/articles/319684/20260704/icml-2026-opens-monday-seoul-agentic-ai-tops-record-year-peer-review-strains.htm">ICML 2026 Opens Monday in Seoul: Agentic AI Tops Record Year as...</a></li>

</ul>
</details>

**社群討論**: 社群對提案的討論正在進行，一些評論者表示支持這個想法，而其他人則提出關於潛在偏見和系統操縱的擔憂。進一步的討論和提案的改進是必要的，以解決這些擔憂並確保信用系統的有效性。

**標籤**: `#Machine Learning`, `#AI Research`, `#Academic Conferences`

---

<a id="item-17"></a>
## [LingBot-Vision: masked boundary modeling for self-supervised pretraining (0.296 NYUv2 linear-probe RMSE at 1.1B vs 0.309 for DINOv3-7B, trails on ImageNet); weights in 4 sizes(R)](https://www.reddit.com/r/MachineLearning/comments/1up4cjh/lingbotvision_masked_boundary_modeling_for/) ⭐️ 8.0/10

Researchers introduce LingBot-Vision, a new method for self-supervised pretraining using masked boundary modeling, achieving competitive results on NYUv2 and ImageNet benchmarks

reddit · r/MachineLearning · /u/StillThese3747 · 7月6日 17:37

**標籤**: `#Computer Vision`, `#Self-Supervised Learning`, `#AI Research`, `#Machine Learning`

---

<a id="item-18"></a>
## [Edge AI ASL Recognition on Raspberry Pi 5 – Looking for Feedback on My System Design (P)](https://www.reddit.com/r/MachineLearning/comments/1up3kby/edge_ai_asl_recognition_on_raspberry_pi_5_looking/) ⭐️ 8.0/10

A developer is seeking feedback on their system design for an offline ASL recognition system using MediaPipe and TensorFlow Lite on Raspberry Pi 5

reddit · r/MachineLearning · /u/Unlikely_Let_9147 · 7月6日 17:10

**標籤**: `#AI Applications`, `#Edge AI`, `#Machine Learning`, `#Computer Vision`, `#Raspberry Pi`

---

<a id="item-19"></a>
## [CPU TTS benchmark with UTMOS MOS scoring: Kokoro, Supertonic, Inflect-Nano, and Kyutai's new Pocket TTS (P)](https://www.reddit.com/r/MachineLearning/comments/1up0azr/cpu_tts_benchmark_with_utmos_mos_scoring_kokoro/) ⭐️ 8.0/10

A CPU TTS benchmark compares the performance of small models like Kokoro, Supertonic, Inflect-Nano, and Kyutai's Pocket TTS using UTMOS MOS scoring.

reddit · r/MachineLearning · /u/gvij · 7月6日 15:17

**標籤**: `#AI products`, `#Machine Learning`, `#TTS models`, `#Benchmarking`, `#Speech Synthesis`

---

<a id="item-20"></a>
## [Fable turned reMarkable into Tom Riddle's diary from Harry Potter](https://github.com/MaximeRivest/Riddle) ⭐️ 7.0/10

A developer has created a project that turns a reMarkable into Tom Riddle's diary from Harry Potter using AI technology, sparking interesting discussions and comparisons on Hacker News.

hackernews · modinfo · 7月6日 23:00 · [社群討論](https://news.ycombinator.com/item?id=48811591)

**標籤**: `#AI applications`, `#Creative projects`, `#Harry Potter`, `#GenAI`, `#Innovative technology`

---

<a id="item-21"></a>
## [OpenWrt One – Open Hardware Router](https://openwrt.org/toh/openwrt/one) ⭐️ 7.0/10

The OpenWrt project has released OpenWrt One, an open hardware router, with users discussing its benefits and comparing it to other alternatives like OPNSense.

hackernews · peter_d_sherman · 7月6日 18:23 · [社群討論](https://news.ycombinator.com/item?id=48808482)

**標籤**: `#OpenWrt`, `#Open Hardware`, `#Networking`, `#Router`, `#Linux`

---

<a id="item-22"></a>
## [How to sequence your own DNA at home](https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home) ⭐️ 7.0/10

A guide on how to sequence your own DNA at home is shared, sparking discussions on its potential applications, privacy, and cost-effectiveness

hackernews · bilsbie · 7月7日 00:14 · [社群討論](https://news.ycombinator.com/item?id=48812156)

**標籤**: `#DIY Biology`, `#Genomics`, `#Biotechnology`, `#Privacy`

---

<a id="item-23"></a>
## [Linux on the Atari Jaguar](https://cakehonolulu.github.io/linux-for-jaguar/) ⭐️ 7.0/10

A developer has successfully ported Linux to the Atari Jaguar, a 68000-based console, using only the original hardware and 2 megabytes of RAM

hackernews · cakehonolulu · 7月6日 18:35 · [社群討論](https://news.ycombinator.com/item?id=48808663)

**標籤**: `#Linux`, `#Retro Computing`, `#Embedded Systems`, `#Hacking`

---

<a id="item-24"></a>
## [AMD Ryzen AI Halo – $4k AI Dev Kit](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo) ⭐️ 7.0/10

AMD has released the Ryzen AI Halo, a $4k AI development kit with a Ryzen AI Max+ 395 processor and 256 GB/s memory bandwidth limit

hackernews · LabsLucas · 7月6日 15:01 · [社群討論](https://news.ycombinator.com/item?id=48805624)

**標籤**: `#AI Hardware`, `#AMD`, `#AI Development Kits`

---

<a id="item-25"></a>
## [sqlite-utils 4.0rc3](https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything) ⭐️ 7.0/10

Simon Willison announces the release of sqlite-utils 4.0rc3 with new features and improvements, including support for compound foreign keys and case insensitive column names

rss · Simon Willison · 7月6日 05:40

**標籤**: `#sqlite-utils`, `#database tools`, `#software engineering`

---

<a id="item-26"></a>
## [Cloudflare replaces its blanket AI bot block with granular controls for search, training, and agent crawlers](https://the-decoder.com/cloudflare-replaces-its-blanket-ai-bot-block-with-granular-controls-for-search-training-and-agent-crawlers/) ⭐️ 7.0/10

Cloudflare introduces granular AI bot controls, allowing site owners to manage Search, Training, and Agent bots separately, with default blocking of Training and Agent bots on ad-supported pages starting September 15, 2026.

rss · The Decoder · 7月6日 18:54

**標籤**: `#AI`, `#Cybersecurity`, `#Cloudflare`, `#Bot Management`

---

<a id="item-27"></a>
## [Amazon sunsets Mechanical Turk, the original "Artificial Artificial Intelligence"](https://the-decoder.com/amazon-sunsets-mechanical-turk-the-original-artificial-artificial-intelligence/) ⭐️ 7.0/10

Amazon Web Services is shutting down its crowdsourcing service Mechanical Turk to new customers starting July 30, 2026.

rss · The Decoder · 7月6日 11:19

**標籤**: `#AI Products`, `#Crowdsourcing`, `#Amazon Web Services`

---

<a id="item-28"></a>
## [US investors will soon get access to SK Hynix, another memory maker riding the AI boom](https://techcrunch.com/2026/07/06/us-investors-will-soon-get-access-to-sk-hynix-another-memory-maker-riding-the-ai-boom/) ⭐️ 7.0/10

SK Hynix, a memory maker, is set to go public in the US with a multibillion-dollar IPO, driven by the AI boom

rss · TechCrunch AI · 7月6日 23:21

**標籤**: `#AI products`, `#AI startups`, `#General software engineering`

---

<a id="item-29"></a>
## [Vercel CEO Guillermo Rauch on the fight to split off models from agents](https://techcrunch.com/2026/07/06/vercel-ceo-guillermo-rauch-on-the-fight-to-split-off-models-from-agents/) ⭐️ 7.0/10

Vercel CEO Guillermo Rauch discusses the importance of optimizing price and performance in production, highlighting the need to separate models from agents

rss · TechCrunch AI · 7月6日 19:49

**標籤**: `#software engineering`, `#performance optimization`, `#AI/ML research`

---

<a id="item-30"></a>
## [You can now customize Siri’s pace and expressivity in the latest iOS 27 beta](https://techcrunch.com/2026/07/06/you-can-now-customize-siris-pace-and-expressivity-in-the-latest-ios-27-beta/) ⭐️ 7.0/10

Apple's latest iOS 27 beta allows users to customize Siri's pace and expressivity as part of its broader effort to make the assistant feel more natural and personal using generative AI

rss · TechCrunch AI · 7月6日 19:01

**標籤**: `#AI products`, `#Virtual Assistants`, `#Generative AI`

---

<a id="item-31"></a>
## [Every major tech layoff in 2026 that has name-checked AI](https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 7.0/10

The article presents a running list of major tech companies that have announced significant layoffs in 2026, citing AI as a contributing factor

rss · TechCrunch AI · 7月6日 18:35

**標籤**: `#AI products and applications`, `#AI industry trends`, `#Tech layoffs`

---

<a id="item-32"></a>
## [Machine learning industry job requirements used to be myopic, but now it feels impossible. Anyone else seeing this? (D)](https://www.reddit.com/r/MachineLearning/comments/1uov7or/machine_learning_industry_job_requirements_used/) ⭐️ 7.0/10

A Reddit user expresses astonishment at the extensive and demanding job requirements for a machine learning position in industrial automation, prompting a discussion about the industry's expectations.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · 7月6日 11:57

**標籤**: `#Machine Learning`, `#Job Market`, `#AI Industry`

---

<a id="item-33"></a>
## [does quantising a model reduce its performance ?(R)](https://www.reddit.com/r/MachineLearning/comments/1upk28e/does_quantising_a_model_reduce_its_performance_r/) ⭐️ 7.0/10

A Reddit user asks whether quantizing a model from fp32 to a lower precision like fp8 significantly reduces its performance.

reddit · r/MachineLearning · /u/Cultural-Lobster7795 · 7月7日 04:02

**標籤**: `#Machine Learning`, `#Model Quantization`, `#AI Research`

---

<a id="item-34"></a>
## [How should I encode both target and feature variable for a multiclass classification? (D)](https://www.reddit.com/r/MachineLearning/comments/1upa8yc/how_should_i_encode_both_target_and_feature/) ⭐️ 7.0/10

A user is seeking advice on how to encode target and feature variables for a multiclass classification problem using XGBoost, particularly when dealing with categorical values.

reddit · r/MachineLearning · /u/Rami02021 · 7月6日 21:07

**標籤**: `#Machine Learning`, `#Multiclass Classification`, `#Data Preprocessing`, `#XGBoost`

---

<a id="item-35"></a>
## [CoMaps – FOSS Offline Maps](https://www.comaps.app/) ⭐️ 6.0/10

CoMaps is a free and open-source offline maps app that uses OpenStreetMap data and has sparked a discussion on Hacker News about its features and comparison to other apps.

hackernews · basilikum · 7月6日 18:55 · [社群討論](https://news.ycombinator.com/item?id=48808928)

**標籤**: `#FOSS`, `#Offline Maps`, `#OpenStreetMap`, `#Mobile Apps`, `#Geospatial Technology`

---

<a id="item-36"></a>
## [Resetting Xbox](https://news.xbox.com/en-us/2026/07/06/resetting-xbox/) ⭐️ 6.0/10

Microsoft's Xbox division is resetting its strategy due to concerns over profit margin, prompting discussion on the gaming industry's focus on prestige and cinematic experiences

hackernews · dijksterhuis · 7月6日 14:18 · [社群討論](https://news.ycombinator.com/item?id=48804993)

**標籤**: `#Gaming Industry`, `#Microsoft Xbox`, `#Business Strategy`

---

<a id="item-37"></a>
## [Microsoft lays off nearly 5,000 employees across Xbox, commercial sales](https://techcrunch.com/2026/07/06/microsoft-lays-off-nearly-5000-employees-across-xbox-commercial-sales/) ⭐️ 6.0/10

Microsoft lays off nearly 5,000 employees across Xbox and commercial sales, sparking concerns about AI replacing jobs

rss · TechCrunch AI · 7月6日 15:32

**標籤**: `#AI adoption`, `#tech industry`, `#layoffs`

---