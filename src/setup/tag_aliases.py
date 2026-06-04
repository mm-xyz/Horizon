"""Tag alias lookup for multilingual matching in setup wizard.

Mirrors horizon-site/app/lib/tagAliases.ts — canonical tag -> aliases
(including Chinese, abbreviations, and common variations).
"""

TAG_ALIASES: dict[str, list[str]] = {
    "ai": ["人工智慧", "AI", "artificial-intelligence"],
    "aigc": ["生成式AI", "生成式人工智慧", "generative-ai"],
    "algorithms": ["演算法", "Algorithms"],
    "analysis": ["分析", "Analysis"],
    "analytics": ["資料分析", "Analytics"],
    "android": ["Android", "安卓"],
    "angular": ["Angular"],
    "aws": ["AWS", "Amazon Web Services", "亞馬遜雲"],
    "azure": ["Azure", "微軟雲"],
    "backend": ["後端", "Backend"],
    "bigdata": ["大數據", "big-data", "Big Data"],
    "blockchain": ["區塊鏈", "Blockchain", "Web3"],
    "c": ["C語言", "C"],
    "chinese": ["中文", "Chinese"],
    "cicd": ["CI/CD", "持續整合", "持續部署"],
    "cli": ["命令列", "CLI", "command-line"],
    "cpp": ["C++", "c++"],
    "cryptography": ["密碼學", "加密"],
    "css": ["CSS", "樣式"],
    "cv": ["計算機視覺", "CV", "computer-vision"],
    "dataeng": ["資料工程", "data-engineering", "Data Engineering"],
    "datascience": ["資料科學", "data-science", "Data Science"],
    "datastructure": ["資料結構", "data-structures", "Data Structures"],
    "defi": ["DeFi", "去中心化金融"],
    "designpattern": ["設計模式", "design-patterns", "Design Patterns"],
    "devops": ["DevOps"],
    "distributed": ["分散式系統", "distributed-systems"],
    "django": ["Django"],
    "dl": ["深度學習", "deep-learning", "神經網路"],
    "docker": ["Docker", "docker", "容器"],
    "editor": ["編輯器", "Editor"],
    "embedded": ["嵌入式", "Embedded"],
    "embodied": ["具身智慧", "Embodied Intelligence"],
    "es": ["Elasticsearch", "elasticsearch", "搜尋引擎"],
    "ethereum": ["以太坊", "Ethereum"],
    "flutter": ["Flutter"],
    "frontend": ["前端", "Frontend"],
    "gcp": ["GCP", "Google Cloud", "谷歌雲"],
    "golang": ["Go", "Golang", "go語言"],
    "hardware": ["硬體", "Hardware"],
    "html": ["HTML"],
    "ios": ["iOS", "蘋果開發"],
    "java": ["Java", "java語言"],
    "javascript": ["JavaScript", "JS", "js", "ECMAScript"],
    "k8s": ["Kubernetes", "kubernetes", "容器編排"],
    "kernel": ["核心", "Kernel"],
    "kotlin": ["Kotlin"],
    "linux": ["Linux", "linux"],
    "llm": ["大語言模型", "LLM", "large-language-model", "大模型"],
    "llm-inference": ["大模型推理", "LLM Inference", "llm-inference", "推理"],
    "maker": [],
    "microservice": ["微服務", "microservices", "Microservices"],
    "ml": ["機器學習", "machine-learning"],
    "mongo": ["MongoDB", "mongodb"],
    "mysql": ["MySQL", "mysql"],
    "neovim": ["Neovim", "neovim"],
    "news": ["新聞"],
    "nextjs": ["Next.js", "NextJS"],
    "nft": ["NFT", "非同質化代幣"],
    "nlp": ["自然語言處理", "NLP", "natural-language-processing"],
    "nodejs": ["Node.js", "NodeJS", "node"],
    "os": ["作業系統", "operating-system"],
    "performance": ["效能最佳化", "Performance"],
    "php": ["PHP", "php語言"],
    "pl": ["程式語言", "programming-languages", "Programming Languages", "語言"],
    "postgres": ["PostgreSQL", "Postgres", "PG", "pg", "postgresql"],
    "python": ["Python", "python程式設計", "py"],
    "react": ["React", "ReactJS", "react.js"],
    "redis": ["Redis", "快取"],
    "research": ["研究", "Research"],
    "rl": ["強化學習", "reinforcement-learning"],
    "rn": ["React Native", "react-native"],
    "robotics": [],
    "ruby": ["Ruby", "ruby語言"],
    "rust": ["Rust", "rust語言", "rust程式設計"],
    "science": ["科學", "Science"],
    "security": ["安全", "網路安全", "Security"],
    "serverless": ["無伺服器", "Serverless"],
    "sglang": ["SGLang"],
    "smart-contract": ["智慧合約", "smart-contracts", "Smart Contracts"],
    "spring": ["Spring", "Spring Boot"],
    "svelte": ["Svelte"],
    "swift": ["Swift"],
    "systems": ["系統"],
    "terminal": ["終端", "Terminal"],
    "terraform": ["Terraform", "IaC"],
    "testing": ["測試", "Testing"],
    "theory": ["理論", "Theory"],
    "tools": ["工具", "Tools"],
    "trending": ["趨勢", "Trending"],
    "typescript": ["TypeScript", "TS", "ts"],
    "vue": ["Vue", "VueJS", "vue.js", "vue框架"],
    "zig": [],
}

# Reverse lookup: alias (lowercased) -> canonical tag
_REVERSE_MAP: dict[str, str] = {}
for _main, _aliases in TAG_ALIASES.items():
    _REVERSE_MAP[_main.lower()] = _main
    for _alias in _aliases:
        _REVERSE_MAP[_alias.lower()] = _main


def get_tag_aliases(tag: str) -> list[str]:
    """Return all aliases for a canonical tag (empty list if unknown)."""
    return TAG_ALIASES.get(tag.lower(), [])


def resolve_tag_alias(input_str: str) -> str:
    """Resolve a tag or alias to its canonical form (lowercased)."""
    normalized = input_str.lower().strip()
    resolved = _REVERSE_MAP.get(normalized)
    return resolved if resolved else normalized
