# Structure Contract (Document Organization)

## Document Section Hierarchy

The document is a single continuous file (DOCX) with the following flat, simple hierarchy:

### Level 1: Main Title
`# 保代不定项选择题生成指令 V13.0` — Document title as H1

### Level 2: Major Sections
Six main sections marked with `##`:
1. `## 【V13.0 三大核心变更】`
2. `## 一、工具使用规范`
3. `## 二、核心执行摘要`
4. `## 三、分阶段生成流程`
5. `## 四、铁律熔断系统速查`
6. `## 五、核心原则`
7. `## 六、引用文件`

Then three additional top-level content blocks (also H1) that form the main body:
- `# 三十条铁律（V13.0 最终版——每条均配熔断机制）`
- `# 命题十步法（V13.0最终版）—— 分阶段生成 + 全铁律熔断`
- `# 配额与校验系统（V13.0版——全铁律对应熔断 + 否定性设问硬约束 + 分阶段校验）`

### Level 3: Subsections
Marked with `###`, e.g.:
- `### 1.1 PDF读取方式`
- `### 1.2 状态追踪工具`
- `### 第一阶段：题目生成（Step 0-9）`
- `### Step 0：预设答案序列`

### Level 4: Sub-subsections
Marked with `####`, e.g.:
- `#### 连续强制规则`
- `#### 进度检查节点`

## Content Blocks

### Tables
Two types of tables appear:
1. **Compact summary tables**: 3-4 columns, e.g., the 铁律熔断系统速查 table (铁律 | 内容 | 熔断)
2. **Quota tables**: Multi-row data tables with clear column headers, e.g., 50题配额总表, 答案组合配额表

All tables use plain markdown pipe format: `| col1 | col2 | col3 |` with `|------|------|------|` separators.

### Code Blocks
Python code blocks appear for:
- Tracking dictionary initialization
- Conditional logic examples (fuse checks)
Code blocks use triple-backtick fencing with `python` language tag.

### Lists
- Unordered lists with `-` for tool specifications, principles, checklists
- Ordered lists with `1. 2. 3.` for procedural steps
- Checklist items use `- [ ]` format

## Reference Files (External)
The main SKILL.md references three external files in a `references/` folder:
1. `references/三十条铁律.md` — Complete 30 rules with A/B/C fuse levels
2. `references/命题十步法.md` — Phased ten-step method (Step 0-13)
3. `references/配额与校验系统.md` — Full fuse table + negative question checks + phased verification

## Key Metrics and Thresholds (50-question batch)
| Metric | Target | Notes |
|--------|--------|-------|
| 数字题 | 18-20 | Permanent fuse at >20 |
| 否定性设问 | >=15 (30%) | A-level fuse if final <15 |
| 跨板块对比 | >=18 (36%) | C-level warning |
| 板块辨析 | >=12 (24%) | C-level warning |
| 新考点优先 | >=20 (40%) | C-level warning |
| 考点覆盖率 | >=90% | A-level fuse |
| 同考点上限 | <=3 | B-level fuse |
| ABCDE全选 | <=1 | A-level fuse |
| 文档三区 | 各>=15 | C-level warning |
| 连续肯定式 | <=3 | C-level forced switch |

## Page Breaks
- NO forced page breaks between sections
- Content flows continuously
- Natural page breaks occur at normal text flow boundaries only
