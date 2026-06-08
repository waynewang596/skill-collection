#!/usr/bin/env python3
"""Validate UI copy against the terminology database and style rules."""

import re
import sys
from pathlib import Path


def validate(text: str) -> list[str]:
    issues = []

    # ── Universal ──

    # Exclamation marks
    if "!" in text or "！" in text:
        issues.append("Exclamation mark detected (avoid exclamatory sentences)")

    # ── Chinese-Specific ──

    # Forbidden Chinese terms
    forbidden_cn = {"您", "亲", "登陆", "TA", "好友", "帐号", "对话", "社区", "笔记", "回忆", "粉丝", "查阅", "查找", "增加", "发表"}
    for word in forbidden_cn:
        if word in text:
            issues.append(f"CN Forbidden term: '{word}'")

    # Absolute terms (CN)
    absolute_cn = {"永远", "绝对"}
    for word in absolute_cn:
        if word in text:
            issues.append(f"CN Absolute term (avoid): '{word}'")

    # Double negatives (CN)
    double_neg_cn = ["不是不", "不能不", "没有不", "不得不", "非不"]
    for pat in double_neg_cn:
        if pat in text:
            issues.append(f"CN Double negative: '{pat}'")

    # "是否" in questions
    if "？" in text or "?" in text:
        if "是否" in text:
            issues.append("CN: '是否' in confirmation question (use verb-object + ?)")

    # Full-width punctuation check for Chinese copy
    # If text contains significant Chinese, warn on half-width punctuation
    if any('\u4e00' <= c <= '\u9fff' for c in text):
        if re.search(r'[\u4e00-\u9fff][.]', text) or re.search(r'[,][\u4e00-\u9fff]', text):
            issues.append("CN: Half-width punctuation detected in Chinese copy")

    # ── English-Specific ──

    lower = text.lower()

    # Forbidden English terms/phrases
    forbidden_en = {"user", "dear", "please click", "login success", "save is successful"}
    for phrase in forbidden_en:
        if phrase in lower:
            issues.append(f"EN Forbidden phrase: '{phrase}'")

    # Absolute terms (EN)
    absolute_en = ["always", "absolutely", "never"]
    for word in absolute_en:
        if re.search(r'\b' + word + r'\b', lower):
            issues.append(f"EN Absolute term (avoid): '{word}'")

    # Double negatives (EN)
    double_neg_en = [r"don't\s+not", r"cannot\s+not", r"no\s+not", r"never\s+not"]
    for pat in double_neg_en:
        if re.search(pat, lower):
            issues.append(f"EN Double negative: matches '{pat}'")

    # "Are you sure..." / "Do you want to..." padding in confirmations
    if "?" in text:
        if re.search(r'are\s+you\s+sure', lower) or re.search(r'do\s+you\s+want\s+to', lower):
            issues.append("EN: 'Are you sure...' or 'Do you want to...' padding in confirmation (use direct verb-object)")

    # Half-width punctuation check for English copy
    # If text is primarily English, warn on full-width punctuation
    en_chars = len(re.findall(r'[a-zA-Z]', text))
    cn_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    if en_chars > cn_chars and en_chars > 5:
        if '。' in text or '，' in text or '：' in text:
            issues.append("EN: Full-width punctuation detected in English copy")

    # Sentence case check for standalone English
    for line in text.splitlines():
        line_stripped = line.strip()
        if not line_stripped:
            continue
        en_portion = re.sub(r"[^\x00-\x7F\s]", "", line_stripped).strip()
        if en_portion and len(en_portion) > 3:
            words = en_portion.split()
            if words:
                first = words[0]
                if first.isupper() and len(first) > 1 and first not in ("I", "OK", "AI", "PPT", "PDF", "APP", "CN", "EN"):
                    continue
                if first[0].islower() and first.lower() not in ("a", "an", "the", "in", "on", "to", "of"):
                    issues.append(f"EN Possible sentence case violation: '{en_portion[:40]}...'")

    # ── Mixed / CJK ──

    # CJK spacing
    if re.search(r"[\u4e00-\u9fff][a-zA-Z0-9]", text):
        issues.append("Missing CJK spacing (Chinese char adjacent to EN/number)")
    if re.search(r"[a-zA-Z0-9][\u4e00-\u9fff]", text):
        issues.append("Missing CJK spacing (EN/number adjacent to Chinese char)")

    return issues


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_copy.py '<text>'")
        sys.exit(1)

    text = sys.argv[1]
    issues = validate(text)
    if issues:
        print("Issues found:")
        for i in issues:
            print(f"  - {i}")
        sys.exit(1)
    else:
        print("Validation passed.")
