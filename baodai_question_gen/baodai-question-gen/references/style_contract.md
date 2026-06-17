# Style Contract (Visual Style Requirements)

## Reference Source
- **Type**: Uploaded DOCX artifact
- **Reference artifact type**: DOCX
- **Reference File Type**: DOCX
- **Primary language**: Chinese (CJK)
- **Visual character**: Plain, minimal, markdown-rendered document

## Typography
- **Font family**: Sans-serif CJK-compatible (NotoSansCJKjp-Regular or equivalent)
- **Body text size**: 10.5pt
- **Heading hierarchy**: Use markdown-style `#` / `##` / `###` / `####` heading markers
- **Bold**: Use `**text**` markers for emphasis (rendered as bold)
- **Code**: Use triple-backtick ``` fenced code blocks and `inline code` with backticks
- **No decorative heading numbering**: Do NOT use large decorative section numbers like "一、" "二、" as visual elements; use simple markdown heading levels

## Color Palette
- **Background**: White only
- **Text**: Black/dark gray only
- **No accent colors**: No colored text, no colored backgrounds, no color-coded elements
- **No colored fuse-level indicators**: A/B/C fuse levels appear as plain text letters, not colored badges

## Page Layout
- **NO cover page**: Document begins directly with content
- **NO back cover page**
- **NO Table of Contents (TOC)**
- **NO running headers**: No text in page headers
- **NO running footers**: No text in page footers
- **NO page numbers**
- **Margins**: Standard document margins (reasonable defaults)
- **Single column layout** throughout

## Tables
- **Style**: Plain markdown pipe-delimited tables
- **No styled headers**: No gray background, no colored header rows, no bold header text
- **Borders**: Simple horizontal separator lines (`|------|------|`)
- **No vertical borders or grid lines**
- **No alternating row colors**
- Tables should look like raw markdown tables rendered with minimal formatting

## Callouts and Boxes
- **NO warning callout boxes**
- **NO info/tip boxes**
- **NO colored highlight boxes**
- **NO bordered callout blocks**
- Important notes use plain bold text (`**note**`) inline, not boxed callouts

## Code Blocks
- Use fenced code blocks with triple backticks
- Plain monospace font, no syntax highlighting colors (or minimal)
- No background shading on code blocks (or very light gray if needed)

## Lists
- Use `-` for unordered lists
- Use `1. 2. 3.` for ordered lists
- Standard markdown indentation

## Overall Aesthetic
The document must look like a **plain markdown file rendered with minimal formatting** — functional, utilitarian, text-focused. It should NOT look like a professionally designed document, brochure, or report. The intentional aesthetic is raw-text readability, not visual polish.

## PROHIBITED Elements (will cause style mismatch)
The following elements must NEVER appear in the output:
1. Cover pages with titles, subtitles, versions, dates
2. Table of Contents with page numbers
3. Page headers or footers
4. Page numbers
5. Colored table headers or styled table borders
6. Warning/info callout boxes with colored backgrounds or borders
7. Color-coded badges (for A/B/C fuse levels or any other categorization)
8. Decorative section numbering (large Chinese numerals as section markers)
9. Horizontal rule separators between sections
10. Background colors on any element
11. Shadow effects, rounded corners, or any decorative effects
