<!-- DO NOT EDIT — auto-copied from skills/auto-empirical-research-skills/details/chinese-de-aigc.md -->

# `chinese-de-aigc`

Chinese academic de-AIGC rewriting targeting CNKI/Wanfang/VIP/Turnitin-zh detectors — a five-step locate/diagnose/rewrite/self-score/recheck loop over 17 diagnostic rules for the five structural signatures of Chinese LLM prose, with per-section strategies.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../auto-empirical-research-skills/">Auto-Empirical Research Skills (AERS) — first-party skills</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)</code></div><div><b>Updated:</b> 2026-07-22</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Auto-Empirical-Research-Skills/contents/skills/48-copaper-ai-chinese-de-aigc/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/auto-empirical-research-skills/chinese-de-aigc/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/48-copaper-ai-chinese-de-aigc/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Auto-Empirical-Research-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## 中文学术降 AIGC Skill

> 中文学术实证论文的 AI 痕迹消除器。不是"改同义词"，不是"打乱语序"，而是**系统性地重构中文 AI 文本的统计学特征**，让它回归到真实研究者写作的语言分布上。

### 适用场景

- 中文期刊投稿前的 AIGC 率自查与修改
- 学位论文（本/硕/博）应对知网 AMLC 检测
- 基金申请书、开题报告、研究报告去 AI 化
- 已完成英文投稿、需要中文摘要/中文版本的场景
- CoPaper.AI 等工具生成初稿后的人工化处理

### 核心理念

**三个错误的做法**（很多教程都在做但无效）：

1. ❌ **同义词替换**：把"关键"改成"核心"，把"重要"改成"显著"——检测器看的是 n-gram 统计分布，不是单词替换
2. ❌ **句式倒装**：简单把"由于 A，所以 B"改成"B，这是因为 A"——句法模板没变
3. ❌ **全文重写交给 AI**：换另一个 AI 改写，只是从一种 AI 痕迹换成另一种

**本 Skill 的正确路径**：针对**中文 AI 的五大结构性特征**做定点破坏，而非字词层面的表面修改。

### 中文 AI 文本的五大结构性特征

与英文 AI 不同，中文大模型的痕迹主要表现在：

1. **四字套话密度过高**：每 200 字出现 3+ 个"综上所述/不可否认/毋庸置疑/显而易见"之类
2. **虚词与关联词冗余**：过度使用"然而/因此/此外/而且/并且/以及/等等"
3. **主语回避与隐藏被动**：大量"本文认为/本研究发现/相关研究表明"式的模糊主语
4. **句长方差低**：句子长度集中在 20-35 字，缺乏人类写作的节奏跳跃
5. **结论绝对化**：倾向使用"证明了/确立了/充分说明/必然导致"等过强断言

本 Skill 针对上述 5 大特征，提供 **17 类细分诊断规则**（详见 `references/patterns.md`）。

### 五步闭环工作流

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ 1. 定位扫描 │ →  │ 2. 诊断分类 │ →  │ 3. 差异化改写 │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
┌─────────────┐    ┌─────────────┐          │
│ 5. 二次复查 │ ←  │ 4. 五维自评 │ ←────────┘
└─────────────┘    └─────────────┘
```

#### Step 1 · 定位扫描

接收用户提交的文本，按 `references/patterns.md` 的 17 类规则做全文扫描，**输出结构化问题清单**：

```markdown
### AI 痕迹定位报告

| 段落 | 原文片段 | 命中规则 | 严重度 |
|------|---------|---------|--------|
| ¶2   | "毋庸置疑，数字化转型..." | P01 四字套话 | 高 |
| ¶3   | "...此外，该研究还..."   | P04 显性连接词 | 中 |
| ¶5   | "本文认为该机制充分证明了..." | P12 绝对化断言 | 高 |
```

⚠️ **不要**此时就开始改写，先让用户/作者看到问题全貌。

#### Step 2 · 诊断分类

按**段落功能**分类：

- **事实陈述段**（方法/数据/结果）→ 低调改写，保留学术精确度
- **论证段**（文献综述/讨论/机制分析）→ 重点改写，注入学者的"认识论谨慎"
- **过渡段**（章节衔接、段落承上启下）→ 大幅改写，消除机械连接词

参考 `references/academic-sections.md` 的**分章节策略表**决定每段的改写力度。

#### Step 3 · 差异化改写

针对 Step 1 清单里的每一条，按以下四条原则逐一修复：

1. **还原研究者视角**：把"本研究发现"改成具体的"我们用 2015-2023 年 CFPS 面板数据发现"——加入**可验证的颗粒度**
2. **制造句长方差**：在一段 200 字内，强制包含至少 1 个 ≤15 字的短句 + 1 个 ≥50 字的长句
3. **消灭显性连接词**：去掉"此外/而且/因此/从而"这类段首连接词，改用**语义接力**（下一句主语呼应上一句宾语的关键概念）
4. **绝对→谨慎**：所有"证明/确立/必然/充分说明"降级为"为...提供了证据/与...的预期一致/可能意味着"

⚠️ **禁止事项**：
- 禁止为了"显得人类"而刻意制造错别字或不规范表达
- 禁止使用生僻词、文言化词汇强行降困惑度——这会损害学术性
- 禁止篡改数据、结论或研究主张——只改表达，不改实质

#### Step 4 · 五维自评

对改写后的文本做**中文学术版 5 维评分**（每维 1-10 分，详见 `references/scoring.md`）：

| 维度 | 检查点 | 权重 |
|------|--------|------|
| **具体性** | 是否用具体数据/案例/作者替代了模糊表达 | 1.5× |
| **节奏性** | 句长方差是否 ≥ 150（50 字长句 + 15 字短句混排） | 1.2× |
| **谨慎性** | 绝对化断言是否已降级为条件化表述 | 1.3× |
| **隐衔接** | 段落之间是否消除了显性关联词（此外/因此等） | 1.0× |
| **研究者语气** | 是否出现"我们/本团队/我"等第一人称研究立场 | 1.0× |

**加权总分 < 35 → 返回 Step 3 再改一轮。加权总分 ≥ 42 → 通过。**

#### Step 5 · 二次复查

用"冷读者"视角重新审视全文，执行三项终审：

1. **通顺性复查**：改写后的逻辑链是否依然连贯？有没有为了降 AIGC 伤到学术表达？
2. **事实性复查**：数据、引用、作者名、年份有没有被误改？
3. **风格一致性复查**：全文语气是否统一，有没有出现"改过的段落 vs 没改的段落"断层？

**输出终稿 + 改动摘要**（哪些段落改了多少、为什么改）。

### 调用接口

用户可以用以下任意触发词调用：

- `请对这段文本降 AIGC 检测率`
- `把这篇论文改得不像 AI 写的`
- `走 chinese-de-aigc 五步闭环`
- `诊断这段文字的 AI 痕迹，给出修改建议`

### 与其他 Skill 的配合

- **先用 revision-guard** 防止过度修改（本 Skill 改写完后交给它把关）
- **与 humanizer_academic 互补**：那个针对英文，这个针对中文，一篇双语论文需要两个都用
- **写完初稿再用本 Skill**：不要一边写一边降 AIGC，会干扰创作思路

### 参考资料

- `references/patterns.md` — 17 类中文 AI 痕迹模式库（每类含识别规则 + 典型样本）
- `references/examples.md` — 12 组原文/改写前后对比（覆盖实证论文七个主要章节）
- `references/academic-sections.md` — 按章节差异化的改写策略表（摘要/引言/文献综述/方法/结果/讨论/结论）
- `references/scoring.md` — 五维评分量表细则

### 重要声明

本 Skill 的目标是**让人工写作和 AI 辅助写作的文本回归到真实研究者的语言分布**，而不是"帮 AI 生成内容骗过检测"。

- ✅ 适用：研究者自己写的初稿，被 AIGC 检测误判为高 AI 率
- ✅ 适用：AI 辅助起草 + 研究者人工修改定稿的混合场景
- ❌ 不适用：完全 AI 生成的论文，希望零改动通过检测
- ❌ 不适用：学术不端场景，如代写、抄袭的掩盖

**学术诚信优先于检测率**。任何改写都不应触及研究结论、数据真实性、引用准确性。
