---
name: baodai-question-gen
description: 保荐代表人考试高质量不定项选择题生成。当用户要求生成保代考试练习题、不定项选择题、或基于PDF教材出题时触发。支持单批次50题规模生成，严格遵循30条铁律、配额熔断机制、十步命题法。要求题目100%锚定PDF原文，九大偷换维度设计干扰项，考点覆盖率达到90%以上。
---

# 保代不定项选择题生成指令 V13.0

## CRITICAL: Output Document Style

The output DOCX must follow a **plain, minimal, markdown-like aesthetic**. Read `references/style_contract.md` BEFORE generating any document.

**Key style rules (non-negotiable):**
- NO cover page, NO back cover, NO Table of Contents
- NO page headers, NO page footers, NO page numbers
- NO colored table headers, NO styled table borders — use plain markdown pipe tables
- NO warning/info callout boxes, NO color-coded badges
- NO decorative section numbering as visual elements
- Tables use `|------|------|` separators only, no background colors
- Document must look like a minimally-formatted markdown render
- White background, black text only throughout

For full style details: see `references/style_contract.md`
For document structure: see `references/structure_contract.md`

## V13.0 三大核心变更

1. **分阶段生成**：第一阶段只生成题目（不含解析），第二阶段排序分离，第三阶段（待用户命令）生成解析
2. **全铁律熔断**：30条铁律每条均配A/B/C三级熔断机制
3. **否定性设问硬约束**：连续3题肯定式则第4题强制否定式，<30%一票否决

## 一、工具使用规范

### 1.1 PDF读取方式
- **必须使用 `read_file` 工具直接读取PDF原文**
- **绝对禁止**将PDF页面截图后使用OCR识别
- **绝对禁止**使用任何图片转文字工具处理PDF内容

### 1.2 状态追踪工具
- 每生成5题后，使用 `ipython` 工具更新配额监控表
- 否定性设问计数必须实时追踪
- 最终交付前，用 `ipython` 执行完整校验清单

## 二、核心执行摘要

执行顺序：**Step0预设答案 -> Step1考点盘点 -> Step2-9逐题生成 -> Step10排序 -> Step11分离交付 -> (待命令)Step12-13生成解析**

关键数字（50题批次）：
- 数字题：18-20题（永久熔断线20）
- 否定性设问：>=15题（>=30%），连续3题肯定则第4题强制否定
- 跨板块对比题：>=18题（>=36%）
- 板块辨析题：>=12题（>=24%）
- 新考点优先题：>=20题（>=40%）
- 考点覆盖率：>=90%
- 同一考点上限：3题（熔断）
- ABCDE全选：<=1题（熔断）
- 文档前/中/后三区：各>=15题

## 三、分阶段生成流程

### 第一阶段：题目生成（Step 0-9）
- **Step 0**：预设答案序列（反向生成基础）
- **Step 1**：考点盘点+追踪系统初始化
- **Step 2-8**：逐题生成（只含题干+选项+预设答案，不含解析）
- **Step 9**：每5题中间校验（含否定性设问检查）

### 第二阶段：后处理（Step 10-11）
- **Step 10**：按章节编号升序（第6章在前，第7章在后）
- **Step 11**：分离为题目正文+答案速查表两个区块

### 第三阶段：解析生成（Step 12-13）——需用户明确命令
- **Step 12**：按排序后的题目顺序，逐题生成解析
- **Step 13**：解析与题目合并或独立交付

## 四、铁律熔断系统速查

| 铁律 | 内容 | 熔断 |
|------|------|------|
| 一 | 不定项强制4-5选项 | A |
| 二 | 每题>=2正确选项 | A |
| 三 | 三独立原则 | A |
| 四 | 选项互斥 | B |
| 五 | 九大偷换维度 | B |
| 六 | 答案非全选<=1 | A |
| 七 | 正确答案>=50字 | B |
| 八 | 数字题18-20 | B |
| 九 | 否定性设问>=30% | A |
| 十 | 否定选项不书名号 | B |
| 十一 | 新考点优先>=40% | C |
| 十二 | 考点覆盖率>=90% | A |
| 十三 | 同考点<=3 | B |
| 十四 | 跨板块>=36% | C |
| 十五 | 设问方式交替 | C |
| 十六 | 否定性设问连续3题强制 | C |
| 十七-三十 | 详见references/三十条铁律.md | 各配熔断 |

## 五、核心原则

- **反向生成**：先冻结预设答案序列，再按预设答案反向设计题目
- **PDF锚定**：每道题必须100%锚定PDF原文
- **分阶段交付**：第一阶段只交题目+答案，解析待后续命令
- **全铁律熔断**：任何铁律违反触发对应级别熔断

## 六、引用文件

- `references/三十条铁律.md` — 30条铁律完整版（每条均配A/B/C熔断）
- `references/命题十步法.md` — 分阶段十步法（Step 0-13）
- `references/配额与校验系统.md` — 全铁律熔断表+否定性设问进度检查+分阶段校验

## 熔断级别定义

| 级别 | 名称 | 处理方式 | 适用铁律 |
|------|------|----------|----------|
| A | 一票否决 | 该题/整批立即作废，必须重来 | 一、二、三、六、九、十二、十八、十九、二十、二十二、二十六、二十八、二十九、三十 |
| B | 永久熔断 | 该题作废，相关考点/题型冻结 | 四、五、七、八、十、十三、十七、二十三、二十四、二十五、二十七 |
| C | 预警熔断 | 预警+强制修正后续题目 | 十一、十四、十五、十六、二十一 |
