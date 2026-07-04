---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 從 31 條內容中篩選出 22 條重要資訊。

---

1. [對比解碼差異法恢復微調數據](#item-1) ⭐️ 9.0/10
2. [GLM5.2 在 AMD MI355X 上達到 2626 tok/s/node](#item-2) ⭐️ 8.0/10
3. [在本地運行最先進的 LLM](#item-3) ⭐️ 8.0/10
4. [歐洲議會成員被 Pegasus 間諜軟體入侵](#item-4) ⭐️ 8.0/10
5. [開源人工智慧缺口地圖發佈](#item-5) ⭐️ 8.0/10
6. [微軟進入 AI 超級應用競爭](#item-6) ⭐️ 8.0/10
7. [AI 模型推動安全漏洞報告激增](#item-7) ⭐️ 8.0/10
8. [英國人工智慧安全研究所發現 AI 評估標準存在缺陷](#item-8) ⭐️ 8.0/10
9. [GPT and Claude failed Bridgewater's finance tests because the right answers were never public](#item-9) ⭐️ 8.0/10
10. [Chinese AI video maker Kling raises $2 billion as it gears up for Hong Kong IPO](#item-10) ⭐️ 8.0/10
11. [H64LM: A 249M-parameter Mixture-of-Experts Transformer built from scratch in PyTorch (P)](#item-11) ⭐️ 8.0/10
12. [What does "Safe AI" look like? (D)](#item-12) ⭐️ 8.0/10
13. [Leanstral 1.5: Proof abundance for all](#item-13) ⭐️ 7.0/10
14. [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](#item-14) ⭐️ 7.0/10
15. [SearXNG: A free internet metasearch engine](#item-15) ⭐️ 7.0/10
16. [Costco is the anti-Amazon](#item-16) ⭐️ 7.0/10
17. [Quoting Josh W. Comeau](#item-17) ⭐️ 7.0/10
18. [Fable's judgement](#item-18) ⭐️ 7.0/10
19. [Claude Code's complicated China problem involves bans on both sides of the Pacific](#item-19) ⭐️ 7.0/10
20. [Meta's AI agent push is moving slower than Zuckerberg planned](#item-20) ⭐️ 7.0/10
21. [Factories are just rooms](#item-21) ⭐️ 6.0/10
22. [Tesla caps employee AI spending at $200 per week](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [對比解碼差異法恢復微調數據](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

研究人員提出了一種新的方法，稱為對比解碼差異法（CDD），可以從 logits 中恢復微調數據，而無需權重存取。這一突破在多個模型家族中實現了高的逐字恢復率。 這一發展很重要，因為它推進了模型差異分析領域，允許在無需完整模型存取的情況下恢復微調數據。它對於了解和分析模型及其訓練數據的差異具有重要意義。 CDD 通過直接對比基礎模型和微調模型的 logits，實現了 19/20 個生物體 x 模型對中的 4+/5 逐字恢復率，跨越四個模型家族。這一方法超越了需要完整權重存取的激活差異鏡頭（ADL）方法。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差異分析是指識別、分析和解釋計算模型之間的差異。它涉及了解模型之間的結構和行為變化。激活差異鏡頭（ADL）是一種方法，用于診斷和解釋 LLM 中狹義微調的影響，通過分析模型預微調和後微調之間的隱藏激活差異。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/nlp/contrastive-decoding-in-natural-language-processing/">Contrastive Decoding in Natural Language Processing - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2309.09117">[2309.09117] Contrastive Decoding Improves Reasoning in Large Language Models</a></li>

</ul>
</details>

**社群討論**: Reddit 上的社群討論表明了高程度的興趣和參與，使用者探討這一突破對模型透明度和數據隱私的影響。

**標籤**: `#Machine Learning`, `#Model Diffing`, `#AI Research`, `#LLMs`

---

<a id="item-2"></a>
## [GLM5.2 在 AMD MI355X 上達到 2626 tok/s/node](https://www.wafer.ai/blog/glm52-amd) ⭐️ 8.0/10

GLM5.2 在 AMD MI355X 上實現了 2626 個令牌每秒每節點的性能，超越了 Blackwell 並且成本降低了 2 倍以上。這一突破是由量化和優化技術的進步所實現的。 這一成就很重要，因為它展示了 AMD MI355X 在 AI 硬體市場的競爭力，可能會打破 Nvidia 產品的壟斷地位。同時，它也強調了量化在實現高效和成本有效的 AI 模型部署中的重要性。 這一性能是通過將模型的參數和激活量化到 FP4 來實現的，從而減少了模型的精度，導致推理時間更快，內存使用量更低。然而，一些社群成員對量化可能導致的準確度損失提出了一些疑慮。

hackernews · latchkey · 7月3日 21:49 · [社群討論](https://news.ycombinator.com/item?id=48780417)

**背景**: GLM5.2 是由 Z.ai 開發的一個大型語言模型，Z.ai 是一家專門從事人工智慧的中國科技公司。AMD MI355X 是一款為高性能計算和 AI 工作負載設計的數據中心 GPU。量化是一種用於減少機器學習模型精度的技術，從而實現更快的推理時間和更低的內存使用量。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html">AMD Instinct™ MI355X GPUs</a></li>

</ul>
</details>

**社群討論**: 社群成員討論了考慮每瓦性能和準確度與效率之間的潛在權衡的重要性。一些成員也對量化方法的缺乏透明度和更標準化的基準測試的需求提出了一些疑慮。

**標籤**: `#AI Benchmarks`, `#AMD`, `#Nvidia`, `#AI Hardware`, `#Machine Learning`

---

<a id="item-3"></a>
## [在本地運行最先進的 LLM](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 創建了一份在本地運行最先進的 LLM 的指南，引發了 Hacker News 上關於本地 LLM 設置的成本、優點和限制的討論。該指南提供了在本地運行最先進 LLM 的硬件和軟件要求的詳細概覽。 這份指南很重要，因為它強調了在本地運行 LLM 的成本、質量和安全性之間的權衡，並為開發人員和研究人員提供了一個基礎來探索本地 LLM 設置的可能性。Hacker News 上的討論也揭示了本地 LLM 的限制和潛在風險，例如高成本和潛在的安全漏洞。 指南建議一個 4 萬美元的預算來搭建一個高端設置，包括 4 個每個成本 12,000 美元的 GPU，並建議使用量化和技術來優化性能。然而，社群成員指出，實際成本可能更高，本地設置通常依賴量化和技術，這可能會影響模型質量。

hackernews · livestyle · 7月3日 15:03 · [社群討論](https://news.ycombinator.com/item?id=48775921)

**背景**: 大型語言模型（LLM）是訓練在大量文本數據上的神經網絡，用于自然語言處理任務，是現代聊天機器人背後的基礎技術。最先進的 LLM 是該領域中最先進的模型，能夠生成、摘要、翻譯和分析文本在許多情境中。然而，訓練和運行這些模型需要大量的計算資源和專業知識。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://medium.com/@paul.k.pallaghy/we-dont-understand-exactly-how-llms-work-but-there-is-progress-a1e1a2532e38">We don’t understand *exactly* how LLMs work. But there is... | Medium</a></li>

</ul>
</details>

**社群討論**: Hacker News 上的社群討論強調了在本地運行 LLM 的顧慮和限制，包括高成本、潛在的安全漏洞，以及成本、質量和安全性之間的權衡。有些成員建議替代方法，例如使用雲服務或通過量化和技術優化模型性能。

**標籤**: `#AI products`, `#LLMs`, `#Software Engineering`, `#Machine Learning`

---

<a id="item-4"></a>
## [歐洲議會成員被 Pegasus 間諜軟體入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

歐洲議會調查間諜軟體的委員會成員被發現遭到 Pegasus 間諜軟體入侵，引發了對政府監控和網路安全的關注。入侵發生在 2022 年 10 月 21 日左右和 2023 年 3 月 6 日和 7 日。 此事件引起關注，因為它提高了對政府官員在網路攻擊中的脆弱性和敏感信息被泄露的可能性。同時也強調了加強網路安全措施以防禦此類威脅的必要性。 Pegasus 間諜軟體可以讀取短信、竊聽電話、收集密碼、追蹤位置、存取目標設備的麥克風和相機，並從應用程式中收集信息。入侵行為是由 Citizen Lab 檢測到的，該實驗室對受影響的 iPhone 進行了法醫分析。

hackernews · ledoge · 7月3日 20:38 · [社群討論](https://news.ycombinator.com/item?id=48779683)

**背景**: Pegasus 是一款由以色列網路情報公司 NSO Group 開發的商業間諜軟體。它設計為在 iOS 和 Android 手機上進行隱秘和遠程安裝。Pegasus 授權的銷售必須得到以色列國防部的批准。Pegasus 已被各國政府用於監控記者、律師、政治異見人士和人權活動家。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>

</ul>
</details>

**社群討論**: 社群成員討論了此事件，一些人表達了對敏感信息被泄露的擔憂，其他人指出這不是一個孤立的事件，因為其他國家，如希臘和波蘭，也有類似的案例被報導。

**標籤**: `#cybersecurity`, `#espionage`, `#government surveillance`, `#Pegasus spyware`, `#European Parliament`

---

<a id="item-5"></a>
## [開源人工智慧缺口地圖發佈](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

非營利組織 Current AI 發佈了開源人工智慧缺口地圖，該地圖深入索引了開源人工智慧的當前狀態，涵蓋 14 個類別的 421 個產品。該地圖得到了大量資金的支持，目前已經承諾了 4 億美元的資金。 開源人工智慧缺口地圖的重要性在於它提供了開源人工智慧當前狀態的全面概覽，幫助研究人員、開發人員和組織識別領域中的空白和機遇。這一倡議有可能加速開源人工智慧的發展，促進利益相關者之間的合作。 缺口地圖 v0.1 詳細介紹了 421 個產品，包括 266 個軟體工具和庫，85 個模型，50 個數據集和 20 個硬體項目，由 228 個組織生產。底層數據以 MIT 許可證發佈，並可在 GitHub 上獲得。

rss · Simon Willison · 7月3日 22:04

**背景**: 缺口地圖的概念並不新鮮，已經在各個領域中用於識別空白和機遇。在開源人工智慧的背景下，缺口地圖可以幫助識別需要更多研究和開發的領域。Current AI 是一個於 2025 年成立的非營利組織，目標是為人工智慧建立一個公共選項。

**標籤**: `#AI products`, `#open-source AI`, `#AI applications`

---

<a id="item-6"></a>
## [微軟進入 AI 超級應用競爭](https://the-decoder.com/microsoft-follows-anthropic-and-openai-into-the-ai-super-app-race-with-overhauled-copilot-and-autopilot-agents/) ⭐️ 8.0/10

微軟正在改版其 Copilot 應用程序，並推出新的 AutoPilot 代理，以在 AI 超級應用領域與 Anthropic 和 OpenAI 競爭。更新的 Copilot 應用程序將合併消費者和企業版本為單一應用程序，很少使用的功能將被刪除，新的 AI 代理將在後台處理任務，需額外付費。 這一發展很重要，因為它表明微軟致力於 AI 超級應用領域，在這裡它將與 Anthropic 和 OpenAI 等主要玩家競爭。AutoPilot 代理的推出和 Copilot 的改版可能會影響用戶與 AI 驅動的工具和服務的交互方式。 更新的 Copilot 應用程序將具有新的 AI 代理，稱為 AutoPilot，它們將在後台處理任務，需額外付費。該應用程序還將刪除很少使用的功能，如 Copilot Podcasts，簡化用戶體驗。

rss · The Decoder · 7月3日 19:24

**背景**: AI 超級應用領域近年來取得了顯著的成長，公司如 Anthropic 和 OpenAI 開發了大型語言模型和 AI 驅動的工具。微軟以其更新的 Copilot 應用程序和 AutoPilot 代理進入這個領域，標誌著業界的一個值得注意的發展。Anthropic 由前 OpenAI 成員創立，開發了一系列名為 Claude 的大型語言模型，並注重 AI 安全。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_AI">Anthropic AI</a></li>
<li><a href="https://help.clickup.com/hc/en-us/articles/37045015737111-What-are-Autopilot-Agents">What are Autopilot Agents ? – ClickUp Help</a></li>

</ul>
</details>

**標籤**: `#AI products`, `#AI applications`, `#Microsoft`

---

<a id="item-7"></a>
## [AI 模型推動安全漏洞報告激增](https://the-decoder.com/security-vulnerability-reports-have-exploded-since-ai-models-started-hunting-for-bugs/) ⭐️ 8.0/10

自從引入了設計用於尋找漏洞的 AI 模型後，安全漏洞報告數量急劇增加，2026 年 6 月份報告了 1,500 個高風險和關鍵的 CVE，創下了新的記錄。這一波報告潮與 AI 驅動的漏洞狩獵程序的推出相吻合。 AI 驅動的漏洞狩獵程序導致安全漏洞報告數量的大幅增加，對網絡安全和 AI 應用領域產生了顯著影響。這一發展可能會帶來更好的安全措施和更高效的漏洞檢測。 2026 年 6 月份報告的 1,500 個高風險和關鍵的 CVE 是之前月度記錄的 3.5 倍以上。AI 驅動的漏洞狩獵程序旨在自動識別和報告軟件和硬件中的漏洞。

rss · The Decoder · 7月3日 16:49

**背景**: 共同漏洞和暴露（CVE）是一個全球標準，用于識別和編目軟件和硬件中的網絡安全漏洞和暴露。使用 AI 模型來尋找漏洞是在網絡安全領域的一個相對新的發展。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://www.rapid7.com/fundamentals/common-vulnerabilities-and-exposures-cve/">What are CVEs? | Common Vulnerabilities and Exposures Guide - Rapid7</a></li>

</ul>
</details>

**標籤**: `#AI applications`, `#Cybersecurity`, `#Bug detection`, `#AI-powered tools`, `#Security vulnerability reports`

---

<a id="item-8"></a>
## [英國人工智慧安全研究所發現 AI 評估標準存在缺陷](https://the-decoder.com/uks-ai-security-institute-finds-standard-benchmarks-systematically-underestimate-what-ai-agents-can-actually-do/) ⭐️ 8.0/10

英國人工智慧安全研究所發現，標準的 AI 評估標準因為計算資源預算有限，而低估了 AI 代理的能力。這種低估導致了對人工智慧研究和開發實際進展的重大誤判。 這個發現很重要，因為它強調了需要重新評估人工智慧研究中的現有評估方法，這可能會影響更先進的 AI 模型的開發。AI 能力的低估也可能對人工智慧安全和更強大的 AI 系統所帶來的潛在風險產生影響。 研究發現，將 token 預算增加十倍，軟體工程任務的成功率就會增加 25%，而新模型能夠獲得最大的益處。人工智慧研究的前沿實際進展比之前的測量結果所顯示的要-steep 60%。

rss · The Decoder · 7月3日 16:14

**背景**: 人工智慧評估標準用於評估 AI 模型的性能，而計算資源預算是這些評估中的關鍵因素。然而，使用固定計算資源預算可能會限制 AI 模型展示其全部能力的能力。Token 預算的概念也很相關，因為它指的是在人工智慧系統中將 token 視為稀缺資源的做法。

<details><summary>參考連結</summary>
<ul>
<li><a href="https://medium.com/@vasanthancomrads/token-budgeting-architecture-for-large-ai-apps-8c2ba5cd9c82">Token Budgeting Architecture for Large AI Apps | Medium</a></li>
<li><a href="https://gentic.news/article/aisi-fixed-compute-budgets">AISI: Fixed compute budgets underestimate AI … | gentic.news</a></li>

</ul>
</details>

**標籤**: `#AI Research`, `#AI Benchmarks`, `#AI Security`, `#Machine Learning`, `#Software Engineering`

---

<a id="item-9"></a>
## [GPT and Claude failed Bridgewater's finance tests because the right answers were never public](https://the-decoder.com/gpt-and-claude-failed-bridgewaters-finance-tests-because-the-right-answers-were-never-public/) ⭐️ 8.0/10

Bridgewater and Thinking Machines Lab have developed a fine-tuned Qwen3-235B model that outperforms Gemini, Claude, and GPT in financial tasks at a lower cost

rss · The Decoder · 7月3日 11:16

**標籤**: `#AI products`, `#AI applications`, `#Finance`

---

<a id="item-10"></a>
## [Chinese AI video maker Kling raises $2 billion as it gears up for Hong Kong IPO](https://the-decoder.com/chinese-ai-video-maker-kling-raises-2-billion-as-it-gears-up-for-hong-kong-ipo/) ⭐️ 8.0/10

Kling, a Chinese AI video maker, has raised $2 billion from investors as it prepares for a Hong Kong IPO

rss · The Decoder · 7月3日 08:53

**標籤**: `#AI products`, `#AI startups`, `#Video technology`

---

<a id="item-11"></a>
## [H64LM: A 249M-parameter Mixture-of-Experts Transformer built from scratch in PyTorch (P)](https://www.reddit.com/r/MachineLearning/comments/1umqfd2/h64lm_a_249mparameter_mixtureofexperts/) ⭐️ 8.0/10

A researcher built H64LM, a 249M-parameter mixture-of-experts transformer from scratch in PyTorch, and is seeking feedback on the implementation.

reddit · r/MachineLearning · /u/Loose_Literature6090 · 7月3日 21:18

**標籤**: `#AI Research`, `#Machine Learning`, `#Transformer Architecture`, `#PyTorch`, `#Mixture-of-Experts`

---

<a id="item-12"></a>
## [What does "Safe AI" look like? (D)](https://www.reddit.com/r/MachineLearning/comments/1um9bs7/what_does_safe_ai_look_like_d/) ⭐️ 8.0/10

The author questions the practicality of studying defenses against post-release fine-tuning that weakens AI safety behavior and seeks input on the threat model and potential safety goals for open-weight model releases.

reddit · r/MachineLearning · /u/Aaron_Rock · 7月3日 09:07

**標籤**: `#AI Safety`, `#Machine Learning`, `#AI Ethics`

---

<a id="item-13"></a>
## [Leanstral 1.5: Proof abundance for all](https://mistral.ai/news/leanstral-1-5/) ⭐️ 7.0/10

Leanstral 1.5 is released with improved proof abundance and bug finding capabilities, sparking interesting discussions and comparisons with other models and verification tools.

hackernews · programLyrique · 7月3日 22:33 · [社群討論](https://news.ycombinator.com/item?id=48780801)

**標籤**: `#AI products`, `#Formal verification`, `#Software engineering`, `#Proof assistants`

---

<a id="item-14"></a>
## [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](https://github.com/FossPrime/Steam-Controller-Auto-Charge) ⭐️ 7.0/10

A GitHub project uses computer vision to create a Steam Controller auto-charge system that navigates the controller to a magnetic charging puck using haptic feedback motors.

hackernews · zdw · 7月3日 22:39 · [社群討論](https://news.ycombinator.com/item?id=48780865)

**標籤**: `#Computer Vision`, `#Gaming Technology`, `#Innovative Projects`, `#Steam Controller`, `#Automated Charging`

---

<a id="item-15"></a>
## [SearXNG: A free internet metasearch engine](https://github.com/searxng/searxng) ⭐️ 7.0/10

SearXNG is a free internet metasearch engine that allows users to search the internet without relying on a single search provider, with a community discussing its benefits and use cases.

hackernews · theanonymousone · 7月3日 20:15 · [社群討論](https://news.ycombinator.com/item?id=48779454)

**標籤**: `#search engine`, `#metasearch`, `#software engineering`, `#open source`, `#privacy`

---

<a id="item-16"></a>
## [Costco is the anti-Amazon](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

An analysis of Costco's business model as the 'anti-Amazon' highlights the company's approach to logistics and consumer behavior

hackernews · bookofjoe · 7月3日 15:14 · [社群討論](https://news.ycombinator.com/item?id=48776044)

**標籤**: `#retail`, `#logistics`, `#e-commerce`, `#business models`

---

<a id="item-17"></a>
## [Quoting Josh W. Comeau](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 7.0/10

Josh W. Comeau notes that his online course sales are down significantly, attributing the decline to the rise of AI and its effects on the demand for paid learning resources

rss · Simon Willison · 7月3日 21:25

**標籤**: `#AI products`, `#AI impact on education`, `#online learning`

---

<a id="item-18"></a>
## [Fable's judgement](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 7.0/10

The author shares tips on utilizing Fable's judgement for tasks like testing and model selection, learned from a Fireside Chat with the Claude Code team

rss · Simon Willison · 7月3日 18:51

**標籤**: `#AI products`, `#AI applications`, `#Software engineering`

---

<a id="item-19"></a>
## [Claude Code's complicated China problem involves bans on both sides of the Pacific](https://the-decoder.com/claude-codes-complicated-china-problem-involves-bans-on-both-sides-of-the-pacific/) ⭐️ 7.0/10

Anthropic's Claude Code is facing a complicated situation in China due to bans and restrictions from both Chinese companies and the Chinese government.

rss · The Decoder · 7月3日 17:11

**標籤**: `#AI products`, `#AI startups`, `#China technology policy`

---

<a id="item-20"></a>
## [Meta's AI agent push is moving slower than Zuckerberg planned](https://the-decoder.com/metas-ai-agent-push-is-moving-slower-than-zuckerberg-planned/) ⭐️ 7.0/10

Mark Zuckerberg admits that Meta's AI agent push is progressing slower than planned, despite his AI chief presenting a more optimistic view.

rss · The Decoder · 7月3日 11:05

**標籤**: `#AI products`, `#AI applications`, `#Meta AI`

---

<a id="item-21"></a>
## [Factories are just rooms](https://interconnected.org/home/2026/07/03/factories) ⭐️ 6.0/10

The article 'Factories are just rooms' inspires a thoughtful discussion on the nature of manufacturing and the importance of people and processes in creating value

hackernews · arbesman · 7月3日 15:13 · [社群討論](https://news.ycombinator.com/item?id=48776035)

**標籤**: `#manufacturing`, `#industry insights`, `#entrepreneurship`, `#innovation`

---

<a id="item-22"></a>
## [Tesla caps employee AI spending at $200 per week](https://the-decoder.com/tesla-caps-employee-ai-spending-at-200-per-week/) ⭐️ 6.0/10

Tesla has capped employee AI spending at $200 per week, according to an internal memo reported by The Information.

rss · The Decoder · 7月3日 10:56

**標籤**: `#AI products`, `#AI applications`, `#Tesla`

---