# UI Copywriter Skill

[中文](#中文) | [English](#english)

---

<a name="中文"></a>

## 中文

### 简介

用于撰写、优化和翻译中英双语界面文案的可复用 Agent Skill。

### 功能

本 Skill 帮助 AI Agent 生成简洁、友好且一致的 UI 文案，强制遵循以下规范：

- **术语一致性** — 使用经过整理的术语库中的精确词汇
- **标点规则** — 中文使用全角标点，英文使用半角标点；UI 文案默认省略句末句号
- **语气与风格** — 使用第二人称（你/You），禁用绝对词、感叹号、双重否定
- **CJK 间距** — 中文与英文/数字之间自动添加半角空格
- **大小写规范** — 英文界面标签、按钮、标题和菜单统一使用 Sentence case

### 安装

通过 [`skills`](https://github.com/vercel-labs/skills) CLI 安装：

```bash
# 全局安装（所有项目可用）
npx skills add https://dev.msh.team/xujianxuan/ui-copywriter.git -g

# 或仅安装到当前项目
npx skills add https://dev.msh.team/xujianxuan/ui-copywriter.git
```

> 注意：安装前需连接公司 VPN，因为 `dev.msh.team` 为公司内网 GitLab。

#### 支持的 Agent

本 Skill 兼容 `skills` CLI 支持的所有 Agent，包括：

- **Kimi Code CLI**
- **Claude Code**
- **Cursor**
- **Codex**
- **OpenCode**
- …以及 [40 余种更多 Agent](https://github.com/vercel-labs/skills#supported-agents)

### 使用方式

安装完成后，在 prompt 中提及本 Skill，或让 Agent 在处理 UI 文案任务时自动检测：

> "帮我写一下删除会话的确认弹窗文案。"

Skill 会自动加载相关参考文件（术语库、标点规则、措辞规范等），并生成符合 Kimi UI 文案规范的文案。

### Skill 结构

```
ui-copywriter/
├── SKILL.md                 # Skill 清单与工作流
├── agents/
│   └── openai.yaml          # Agent 提示词配置
├── references/              # 参考文档
│   ├── core-principles.md
│   ├── phrasing-rules.md
│   ├── sentence-patterns.md
│   ├── punctuation.md
│   ├── style-guide.md
│   ├── numbers-and-units.md
│   ├── abbreviations.md
│   ├── terminology.md
│   ├── writing-patterns.md
│   └── linguistic-logic.md
└── scripts/
    └── validate_copy.py     # 文案检查脚本
```

### 贡献

欢迎提交 Issue 或 Pull Request 来完善术语、补充规则或优化翻译。

### 协议

MIT

---

<a name="english"></a>

## English

### Introduction

A reusable agent skill for writing, optimizing, and translating UI copy and localization text for Chinese and English interfaces.

### What it does

This skill helps AI agents produce concise, friendly, and consistent UI copy by enforcing:

- **Terminology consistency** — Exact terms from a curated terminology database
- **Punctuation rules** — Full-width for Chinese, half-width for English; omit periods in UI copy by default
- **Tone & style** — Second person (你/You), no absolute words, no exclamation marks, no double negatives
- **CJK spacing** — Proper spacing between CJK characters and English words / numbers
- **Sentence case** — For all English UI labels, buttons, titles, and menus

### Installation

Install via the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
# Install to user directory (available across all projects)
npx skills add https://dev.msh.team/xujianxuan/ui-copywriter.git -g

# Or install to current project only
npx skills add https://dev.msh.team/xujianxuan/ui-copywriter.git
```

> Note: Company VPN is required before installation, as `dev.msh.team` is an internal GitLab instance.

#### Supported Agents

This skill is compatible with all agents supported by the `skills` CLI, including:

- **Kimi Code CLI**
- **Claude Code**
- **Cursor**
- **Codex**
- **OpenCode**
- …and [40+ more](https://github.com/vercel-labs/skills#supported-agents)

### Usage

Once installed, mention the skill in your prompt or let your agent auto-detect it when working on UI copy tasks:

> "Help me write the confirmation dialog copy for deleting a chat session."

The skill will automatically load the relevant reference files (terminology, punctuation, phrasing rules, etc.) and produce copy that follows the Kimi UI writing guidelines.

### Skill Structure

```
ui-copywriter/
├── SKILL.md                 # Skill manifest & workflow
├── agents/
│   └── openai.yaml          # Agent prompt configuration
├── references/              # Reference documents
│   ├── core-principles.md
│   ├── phrasing-rules.md
│   ├── sentence-patterns.md
│   ├── punctuation.md
│   ├── style-guide.md
│   ├── numbers-and-units.md
│   ├── abbreviations.md
│   ├── terminology.md
│   ├── writing-patterns.md
│   └── linguistic-logic.md
└── scripts/
    └── validate_copy.py     # Validation script for copy checks
```

### Contributing

Feel free to open issues or pull requests to improve terminology, add new rules, or refine translations.

### License

MIT
