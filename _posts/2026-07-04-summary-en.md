---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 31 items, 22 important content pieces were selected

---

1. [Contrastive Decoding Diffing Recovers Finetuning Data](#item-1) ⭐️ 9.0/10
2. [GLM5.2 on AMD MI355X Achieves 2626 tok/s/node](#item-2) ⭐️ 8.0/10
3. [Running SOTA LLMs Locally](#item-3) ⭐️ 8.0/10
4. [EU Parliament Member Hacked with Pegasus Spyware](#item-4) ⭐️ 8.0/10
5. [Open Source AI Gap Map Launched](#item-5) ⭐️ 8.0/10
6. [Microsoft Enters AI Super App Race](#item-6) ⭐️ 8.0/10
7. [AI Models Boost Security Vulnerability Reports](#item-7) ⭐️ 8.0/10
8. [UK's AI Security Institute Finds AI Benchmarks Flawed](#item-8) ⭐️ 8.0/10
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
## [Contrastive Decoding Diffing Recovers Finetuning Data](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

Researchers introduced Contrastive Decoding Diffing (CDD), a method that can recover verbatim finetuning data from logits alone without needing weight access. This breakthrough achieves a high verbatim recovery score across multiple model families. This development is significant because it advances the field of model diffing, allowing for the recovery of finetuning data without full model access. It has implications for understanding and analyzing the differences between models and their training data. CDD contrasts the base and finetuned model's logits directly to achieve a verbatim recovery score of 4+/5 on 19/20 organism x model pairs across four model families. This method outperforms Activation Difference Lens (ADL), which requires full weight access.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing is the process of identifying, analyzing, and explaining differences in computational models. It involves understanding both structural and behavioral variations between models. The Activation Difference Lens (ADL) is a methodology for diagnosing and interpreting the effects of narrow finetuning in LLMs by analyzing differences in hidden activations between models pre- and post-finetuning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/nlp/contrastive-decoding-in-natural-language-processing/">Contrastive Decoding in Natural Language Processing - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2309.09117">[2309.09117] Contrastive Decoding Improves Reasoning in Large Language Models</a></li>

</ul>
</details>

**Discussion**: The community discussion on Reddit indicates high interest and engagement, with users exploring the implications of this breakthrough for model transparency and data privacy.

**Tags**: `#Machine Learning`, `#Model Diffing`, `#AI Research`, `#LLMs`

---

<a id="item-2"></a>
## [GLM5.2 on AMD MI355X Achieves 2626 tok/s/node](https://www.wafer.ai/blog/glm52-amd) ⭐️ 8.0/10

GLM5.2 has achieved a performance of 2626 tokens per second per node on the AMD MI355X, outperforming Blackwell at over 2x lower cost. This breakthrough was made possible by advancements in quantization and optimization techniques. This achievement is significant as it demonstrates the competitiveness of AMD's MI355X in the AI hardware market, potentially disrupting the dominance of Nvidia's products. It also highlights the importance of quantization in achieving efficient and cost-effective AI model deployment. The performance was achieved using quantization to FP4, which reduces the precision of the model's parameters and activations, resulting in faster inference times and lower memory usage. However, some community members have raised concerns about the potential loss of accuracy due to quantization.

hackernews · latchkey · Jul 3, 21:49 · [Discussion](https://news.ycombinator.com/item?id=48780417)

**Background**: GLM5.2 is a large language model developed by Z.ai, a Chinese technology company specializing in artificial intelligence. The AMD MI355X is a data center GPU designed for high-performance computing and AI workloads. Quantization is a technique used to reduce the precision of machine learning models, enabling faster inference times and lower memory usage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html">AMD Instinct™ MI355X GPUs</a></li>

</ul>
</details>

**Discussion**: Community members have discussed the importance of considering performance per watt and the potential trade-offs between accuracy and efficiency. Some have also raised concerns about the lack of transparency in quantization methods and the need for more standardized benchmarks.

**Tags**: `#AI Benchmarks`, `#AMD`, `#Nvidia`, `#AI Hardware`, `#Machine Learning`

---

<a id="item-3"></a>
## [Running SOTA LLMs Locally](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob has created a guide to running state-of-the-art Large Language Models (LLMs) locally, sparking a discussion on Hacker News about the costs, benefits, and limitations of local LLM setups. The guide provides a detailed overview of the hardware and software requirements for running SOTA LLMs locally. This guide is significant because it highlights the trade-offs between cost, quality, and safety when running LLMs locally, and provides a starting point for developers and researchers to explore the possibilities of local LLM setups. The discussion on Hacker News also sheds light on the limitations and potential risks of local LLMs, such as high costs and potential security vulnerabilities. The guide recommends a $40K budget for a high-end setup, which includes 4 GPUs that cost $12K each, and suggests using quantization and technique to optimize performance. However, community members have pointed out that the actual cost may be higher, and that local setups often rely on quantization and technique, which can affect model quality.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Large Language Models (LLMs) are neural networks trained on vast amounts of text data for natural language processing tasks, and are a foundational technology behind modern chatbots. SOTA LLMs are the most advanced models in this field, and are capable of generating, summarizing, translating, and analyzing text in many contexts. However, training and running these models requires significant computational resources and expertise.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@paul.k.pallaghy/we-dont-understand-exactly-how-llms-work-but-there-is-progress-a1e1a2532e38">We don’t understand *exactly* how LLMs work. But there is... | Medium</a></li>

</ul>
</details>

**Discussion**: The community discussion on Hacker News highlights the concerns and limitations of running LLMs locally, including high costs, potential security vulnerabilities, and the trade-offs between cost, quality, and safety. Some members suggest alternative approaches, such as using cloud services or optimizing model performance through quantization and technique.

**Tags**: `#AI products`, `#LLMs`, `#Software Engineering`, `#Machine Learning`

---

<a id="item-4"></a>
## [EU Parliament Member Hacked with Pegasus Spyware](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

A member of the European Parliament's committee investigating spyware was found to have been hacked with Pegasus spyware, highlighting concerns about government surveillance and cybersecurity. The hacking occurred on or around October 21, 2022, and again on March 6 and 7, 2023. This incident is significant as it raises concerns about the vulnerability of government officials to cyber attacks and the potential compromise of sensitive information. It also highlights the need for stronger cybersecurity measures to protect against such threats. The Pegasus spyware is capable of reading text messages, call snooping, collecting passwords, location tracking, accessing the target device's microphone and camera, and harvesting information from apps. The hacking was detected by the Citizen Lab, which conducted a forensic analysis of the affected iPhone.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a commercial spyware suite developed by NSO Group, an Israeli cyber-intelligence firm. It is designed to be covertly and remotely installed on mobile phones running iOS and Android. The sale of Pegasus licenses to foreign governments must be approved by the Israeli Ministry of Defense.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>

</ul>
</details>

**Discussion**: Community members discussed the incident, with some expressing concern about the potential compromise of sensitive information and others noting that this is not an isolated incident, as similar cases have been reported in other countries, such as Greece and Poland.

**Tags**: `#cybersecurity`, `#espionage`, `#government surveillance`, `#Pegasus spyware`, `#European Parliament`

---

<a id="item-5"></a>
## [Open Source AI Gap Map Launched](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit organization, has launched the Open Source AI Gap Map, which indexes the current state of open-source AI with 421 products in depth across 14 categories. The map is backed by significant funding, with $400m already committed. The Open Source AI Gap Map is significant because it provides a comprehensive overview of the current state of open-source AI, which can help researchers, developers, and organizations identify gaps and opportunities in the field. This initiative has the potential to accelerate the development of open-source AI and promote collaboration among stakeholders. The Gap Map v0.1 details 421 products, including 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects, produced by 228 organizations. The underlying data is released under an MIT license and is available on GitHub.

rss · Simon Willison · Jul 3, 22:04

**Background**: The concept of a gap map is not new, and it has been used in various fields to identify gaps and opportunities. In the context of open-source AI, a gap map can help identify areas where more research and development are needed. Current AI is a non-profit organization founded in 2025, with the goal of building a public option for AI.

**Tags**: `#AI products`, `#open-source AI`, `#AI applications`

---

<a id="item-6"></a>
## [Microsoft Enters AI Super App Race](https://the-decoder.com/microsoft-follows-anthropic-and-openai-into-the-ai-super-app-race-with-overhauled-copilot-and-autopilot-agents/) ⭐️ 8.0/10

Microsoft is overhauling its Copilot app and introducing new AutoPilot agents to compete with Anthropic and OpenAI in the AI super app space. The updated Copilot app will merge consumer and enterprise versions into a single app, with rarely used features being cut and new AI agents handling tasks in the background for an extra fee. This development is significant as it indicates Microsoft's commitment to the AI super app space, where it will compete with major players like Anthropic and OpenAI. The introduction of AutoPilot agents and the overhaul of Copilot will likely impact the way users interact with AI-powered tools and services. The updated Copilot app will feature new AI agents called AutoPilot, which will handle tasks in the background for an extra fee. The app will also cut rarely used features like Copilot Podcasts, streamlining the user experience.

rss · The Decoder · Jul 3, 19:24

**Background**: The AI super app space has seen significant growth in recent years, with companies like Anthropic and OpenAI developing large language models and AI-powered tools. Microsoft's entry into this space with its updated Copilot app and AutoPilot agents marks a notable development in the industry. Anthropic, founded by former OpenAI members, has developed a series of large language models named Claude and has a focus on AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_AI">Anthropic AI</a></li>
<li><a href="https://help.clickup.com/hc/en-us/articles/37045015737111-What-are-Autopilot-Agents">What are Autopilot Agents ? – ClickUp Help</a></li>

</ul>
</details>

**Tags**: `#AI products`, `#AI applications`, `#Microsoft`

---

<a id="item-7"></a>
## [AI Models Boost Security Vulnerability Reports](https://the-decoder.com/security-vulnerability-reports-have-exploded-since-ai-models-started-hunting-for-bugs/) ⭐️ 8.0/10

Security vulnerability reports have increased sharply since the introduction of AI models designed to hunt for bugs, with a record 1,500 high-severity and critical CVEs reported in June 2026. This surge in reports coincides with the launch of AI-powered bug-hunting programs. The significant increase in security vulnerability reports due to AI-powered bug-hunting programs indicates a notable impact on the field of cybersecurity and AI applications. This development could lead to improved security measures and more efficient bug detection. The record 1,500 high-severity and critical CVEs reported in June 2026 is more than 3.5 times the previous monthly record. AI-powered bug-hunting programs are designed to automatically identify and report vulnerabilities in software and hardware.

rss · The Decoder · Jul 3, 16:49

**Background**: Common Vulnerabilities and Exposures (CVEs) are a global standard for identifying and cataloging cybersecurity vulnerabilities and exposures in software and hardware. The use of AI models to hunt for bugs is a relatively new development in the field of cybersecurity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>
<li><a href="https://www.rapid7.com/fundamentals/common-vulnerabilities-and-exposures-cve/">What are CVEs? | Common Vulnerabilities and Exposures Guide - Rapid7</a></li>

</ul>
</details>

**Tags**: `#AI applications`, `#Cybersecurity`, `#Bug detection`, `#AI-powered tools`, `#Security vulnerability reports`

---

<a id="item-8"></a>
## [UK's AI Security Institute Finds AI Benchmarks Flawed](https://the-decoder.com/uks-ai-security-institute-finds-standard-benchmarks-systematically-underestimate-what-ai-agents-can-actually-do/) ⭐️ 8.0/10

The UK's AI Security Institute has discovered that standard AI benchmarks systematically underestimate the capabilities of AI agents due to limited compute budgets. This underestimation leads to a significant misrepresentation of actual progress in AI research and development. This finding is significant because it highlights the need for a reassessment of current evaluation methods in AI research, which could impact the development of more advanced AI models. The underestimation of AI capabilities could also have implications for AI security and the potential risks associated with more powerful AI systems. The study found that increasing the token budget by a factor of ten resulted in a 25% increase in success rates for software engineering tasks, with newer models benefiting the most. The actual progress at the frontier of AI research is about 60% steeper than previous measurements suggested.

rss · The Decoder · Jul 3, 16:14

**Background**: AI benchmarks are used to evaluate the performance of AI models, and compute budgets are a critical factor in these evaluations. However, the use of fixed compute budgets can limit the ability of AI models to demonstrate their full capabilities. The concept of token budgeting is also relevant, as it refers to the practice of treating tokens as a scarce resource in AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@vasanthancomrads/token-budgeting-architecture-for-large-ai-apps-8c2ba5cd9c82">Token Budgeting Architecture for Large AI Apps | Medium</a></li>
<li><a href="https://gentic.news/article/aisi-fixed-compute-budgets">AISI: Fixed compute budgets underestimate AI … | gentic.news</a></li>

</ul>
</details>

**Tags**: `#AI Research`, `#AI Benchmarks`, `#AI Security`, `#Machine Learning`, `#Software Engineering`

---

<a id="item-9"></a>
## [GPT and Claude failed Bridgewater's finance tests because the right answers were never public](https://the-decoder.com/gpt-and-claude-failed-bridgewaters-finance-tests-because-the-right-answers-were-never-public/) ⭐️ 8.0/10

Bridgewater and Thinking Machines Lab have developed a fine-tuned Qwen3-235B model that outperforms Gemini, Claude, and GPT in financial tasks at a lower cost

rss · The Decoder · Jul 3, 11:16

**Tags**: `#AI products`, `#AI applications`, `#Finance`

---

<a id="item-10"></a>
## [Chinese AI video maker Kling raises $2 billion as it gears up for Hong Kong IPO](https://the-decoder.com/chinese-ai-video-maker-kling-raises-2-billion-as-it-gears-up-for-hong-kong-ipo/) ⭐️ 8.0/10

Kling, a Chinese AI video maker, has raised $2 billion from investors as it prepares for a Hong Kong IPO

rss · The Decoder · Jul 3, 08:53

**Tags**: `#AI products`, `#AI startups`, `#Video technology`

---

<a id="item-11"></a>
## [H64LM: A 249M-parameter Mixture-of-Experts Transformer built from scratch in PyTorch (P)](https://www.reddit.com/r/MachineLearning/comments/1umqfd2/h64lm_a_249mparameter_mixtureofexperts/) ⭐️ 8.0/10

A researcher built H64LM, a 249M-parameter mixture-of-experts transformer from scratch in PyTorch, and is seeking feedback on the implementation.

reddit · r/MachineLearning · /u/Loose_Literature6090 · Jul 3, 21:18

**Tags**: `#AI Research`, `#Machine Learning`, `#Transformer Architecture`, `#PyTorch`, `#Mixture-of-Experts`

---

<a id="item-12"></a>
## [What does "Safe AI" look like? (D)](https://www.reddit.com/r/MachineLearning/comments/1um9bs7/what_does_safe_ai_look_like_d/) ⭐️ 8.0/10

The author questions the practicality of studying defenses against post-release fine-tuning that weakens AI safety behavior and seeks input on the threat model and potential safety goals for open-weight model releases.

reddit · r/MachineLearning · /u/Aaron_Rock · Jul 3, 09:07

**Tags**: `#AI Safety`, `#Machine Learning`, `#AI Ethics`

---

<a id="item-13"></a>
## [Leanstral 1.5: Proof abundance for all](https://mistral.ai/news/leanstral-1-5/) ⭐️ 7.0/10

Leanstral 1.5 is released with improved proof abundance and bug finding capabilities, sparking interesting discussions and comparisons with other models and verification tools.

hackernews · programLyrique · Jul 3, 22:33 · [Discussion](https://news.ycombinator.com/item?id=48780801)

**Tags**: `#AI products`, `#Formal verification`, `#Software engineering`, `#Proof assistants`

---

<a id="item-14"></a>
## [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](https://github.com/FossPrime/Steam-Controller-Auto-Charge) ⭐️ 7.0/10

A GitHub project uses computer vision to create a Steam Controller auto-charge system that navigates the controller to a magnetic charging puck using haptic feedback motors.

hackernews · zdw · Jul 3, 22:39 · [Discussion](https://news.ycombinator.com/item?id=48780865)

**Tags**: `#Computer Vision`, `#Gaming Technology`, `#Innovative Projects`, `#Steam Controller`, `#Automated Charging`

---

<a id="item-15"></a>
## [SearXNG: A free internet metasearch engine](https://github.com/searxng/searxng) ⭐️ 7.0/10

SearXNG is a free internet metasearch engine that allows users to search the internet without relying on a single search provider, with a community discussing its benefits and use cases.

hackernews · theanonymousone · Jul 3, 20:15 · [Discussion](https://news.ycombinator.com/item?id=48779454)

**Tags**: `#search engine`, `#metasearch`, `#software engineering`, `#open source`, `#privacy`

---

<a id="item-16"></a>
## [Costco is the anti-Amazon](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

An analysis of Costco's business model as the 'anti-Amazon' highlights the company's approach to logistics and consumer behavior

hackernews · bookofjoe · Jul 3, 15:14 · [Discussion](https://news.ycombinator.com/item?id=48776044)

**Tags**: `#retail`, `#logistics`, `#e-commerce`, `#business models`

---

<a id="item-17"></a>
## [Quoting Josh W. Comeau](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 7.0/10

Josh W. Comeau notes that his online course sales are down significantly, attributing the decline to the rise of AI and its effects on the demand for paid learning resources

rss · Simon Willison · Jul 3, 21:25

**Tags**: `#AI products`, `#AI impact on education`, `#online learning`

---

<a id="item-18"></a>
## [Fable's judgement](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 7.0/10

The author shares tips on utilizing Fable's judgement for tasks like testing and model selection, learned from a Fireside Chat with the Claude Code team

rss · Simon Willison · Jul 3, 18:51

**Tags**: `#AI products`, `#AI applications`, `#Software engineering`

---

<a id="item-19"></a>
## [Claude Code's complicated China problem involves bans on both sides of the Pacific](https://the-decoder.com/claude-codes-complicated-china-problem-involves-bans-on-both-sides-of-the-pacific/) ⭐️ 7.0/10

Anthropic's Claude Code is facing a complicated situation in China due to bans and restrictions from both Chinese companies and the Chinese government.

rss · The Decoder · Jul 3, 17:11

**Tags**: `#AI products`, `#AI startups`, `#China technology policy`

---

<a id="item-20"></a>
## [Meta's AI agent push is moving slower than Zuckerberg planned](https://the-decoder.com/metas-ai-agent-push-is-moving-slower-than-zuckerberg-planned/) ⭐️ 7.0/10

Mark Zuckerberg admits that Meta's AI agent push is progressing slower than planned, despite his AI chief presenting a more optimistic view.

rss · The Decoder · Jul 3, 11:05

**Tags**: `#AI products`, `#AI applications`, `#Meta AI`

---

<a id="item-21"></a>
## [Factories are just rooms](https://interconnected.org/home/2026/07/03/factories) ⭐️ 6.0/10

The article 'Factories are just rooms' inspires a thoughtful discussion on the nature of manufacturing and the importance of people and processes in creating value

hackernews · arbesman · Jul 3, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48776035)

**Tags**: `#manufacturing`, `#industry insights`, `#entrepreneurship`, `#innovation`

---

<a id="item-22"></a>
## [Tesla caps employee AI spending at $200 per week](https://the-decoder.com/tesla-caps-employee-ai-spending-at-200-per-week/) ⭐️ 6.0/10

Tesla has capped employee AI spending at $200 per week, according to an internal memo reported by The Information.

rss · The Decoder · Jul 3, 10:56

**Tags**: `#AI products`, `#AI applications`, `#Tesla`

---