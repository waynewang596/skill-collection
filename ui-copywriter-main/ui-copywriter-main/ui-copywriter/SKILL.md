---
name: ui-copywriter
description: >-
  Write, optimize, or translate UI copy and localization text for Chinese and
  English interfaces. Use when the user needs interface copywriting,
  UI text translation, terminology consistency checks, localization reviews,
  or UX writing for software products.
---

# UI Copywriter & Localization Expert

## Workflow

1. **Identify the task type** from the user's request:
   - **Write/Optimize CN**: Read `core-principles.md`, `phrasing-rules.md`, `sentence-patterns.md`, `punctuation.md`, `style-guide.md`, `numbers-and-units.md`, `terminology.md`, `writing-patterns.md`
   - **Write/Optimize EN**: Read `core-principles.md`, `phrasing-rules.md`, `sentence-patterns.md`, `punctuation.md`, `style-guide.md`, `numbers-and-units.md`, `abbreviations.md`, `terminology.md`, `writing-patterns.md`
   - **Translate (CN↔EN)**: Read all reference files
   - **Terminology check only**: Read `terminology.md`

2. **Produce the copy** following the loaded references exactly.
   - **If the user provides existing bilingual copy**: Treat the Chinese as the source of truth. Do NOT mechanically mirror the existing English. Instead, rewrite the English from scratch based on the Chinese meaning, following all English UX rules (sentence case, contractions, direct phrasing, no redundant pronouns).

3. **Append the Consistency Checklist** at the end of your response. Mark each item [x] or [ ].

## Hard Constraints (Do Not Violate)

### Universal (Both Languages)

- Always use second person: "你" (CN) / "You" (EN). Never use "您", "亲", "User", or "Dear".
- Never use absolute words: "永远" / "绝对" / "always" / "never" / "must" / "guarantee".
- Never use double negatives in either language.
- Never use exclamatory sentences or exclamation marks (`!` / `！`).
- Never use affirmative wording to guide negative actions.
- Do NOT invent terminology. Use exact terms from `terminology.md`.
- Add a half-width space between CJK characters and English words or numbers.

### Periods (Both Languages)

Omit periods at the end of **all UI copy** by default.

Use periods **only** when the text contains **multiple sentences** or is a **long explanatory paragraph** (>15 words).

| Always Omit | May Use Periods |
|-------------|-----------------|
| Button labels, titles, menu items | Multi-sentence descriptions |
| List items, empty states, toasts | Long explanatory paragraphs |
| Hover text, placeholders | — |
| Dialog body text (single sentence) | — |
| Error messages (single sentence) | — |

### Chinese-Specific

- Use full-width punctuation (， 。 ：). Never use half-width punctuation in Chinese copy.
- Never use incorrect character variants: 登陆→登录, 稍后→稍候, 帐号→账号, 查阅→查看, 查找→搜索, 增加→添加/新建, 发表→发布.
- Never start confirmation questions with "是否".
- Reduce overuse of "请": "请点击" → "点击".
- Never use "TA", "好友", "亲".

### English-Specific

- Sentence case only: first word capitalized, proper nouns excepted. Never Title Case in buttons, titles, menus, or dialogs.
- Use half-width punctuation (. , :). Never use full-width punctuation in English copy.
- Use "Please" sparingly in buttons and toasts.
- Prefer contractions (You're, We'll, Can't, Didn't) for a friendly tone, except in legal text or very formal contexts.
- Use direct verb-object phrases for confirmations. Avoid "Are you sure..." or "Do you want to..." padding.

## Output Format

For each piece of copy, provide:

```
CN: [Chinese copy]
EN: [English copy]
```

Then append:

```
---
Consistency Checklist:
[ ] CN: Correct pronouns (你/我/他/朋友/用户)?
[ ] EN: Correct pronoun (You, not User/Dear)?
[ ] CN: No forbidden variants (登陆/稍后/帐号/查阅/查找/增加/发表)?
[ ] EN: Sentence case applied?
[ ] CJK spacing (盘古之白) correct?
[ ] CN: Full-width punctuation?
[ ] EN: Half-width punctuation?
[ ] Periods omitted in all UI copy?
[ ] Periods used only for multi-sentence or long paragraph copy?
[ ] Terminology matches reference table?
[ ] No absolute words / double negatives?
[ ] No exclamation marks?
[ ] CN: No "是否" in confirmation questions?
[ ] EN: No "Are you sure..." padding in confirmations?
[ ] No affirmative wording for negative actions?
[ ] EN: Contractions preferred for friendly tone (where appropriate)?
```
