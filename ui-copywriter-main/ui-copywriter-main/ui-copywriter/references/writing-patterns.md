# Writing Patterns by Scenario

## 1. Error Messages

Structure: Specific cause + Solution. Never say just "error".

Omit periods for single-sentence error messages. Use periods only for multi-sentence error descriptions.

| CN | EN |
|----|-----|
| 密码长度必须至少为 8 个字符。 | Password must be at least 8 characters. |
| 提交失败，请重试。 | Submission failed. Please try again. |

## 2. Confirmation Dialogs

- **Title**: Verb-object phrase + question mark. **No period.**
- **Body**: State the consequence (especially for irreversible actions). Omit periods for single-sentence body text.

| | CN | EN |
|---|----|-----|
| Title | 删除此会话？ | Delete chat? |
| Body | 此会话将被永久删除，不可恢复。 | This chat will be permanently deleted and cannot be recovered. |

### Dialog Button Patterns

| Position | Role | Wording Rule | Chinese Examples | English Examples |
|----------|------|--------------|------------------|------------------|
| Right | Recommended action | Reuse the **verb** from the title's verb-object phrase | 删除 / 退出 / 更改 / 注销账号 | Delete / Exit / Change / Deactivate |
| Left | Non-recommended action | Usually "取消" or action-specific | 取消 / 继续使用 | Cancel / Keep using |

## 3. Empty States

Structure: State description + Call to action.
**No period** — empty state text is typically a fragment.

| CN | EN |
|----|-----|
| 暂无收藏 | No favorites yet |
| 暂未连接到网络 | No internet connection |

## 4. Button Text

Rule: Verb-first, keep it short.
**No period** — buttons are always fragments.

| CN | EN |
|----|-----|
| 保存 | Save |
| 确定 | OK |
| 删除 | Delete |

Avoid "Yes/No" in confirmation buttons. Use action verbs instead.

## 6. Avoid Redundant Pronouns

In buttons, links, and short UI copy, the verb alone is sufficient. Do not add pronouns like *one / it / them*.

| ❌ Redundant | ✅ Clean |
|-------------|----------|
| Create one | Create |
| Add one | Add |
| Delete it | Delete |
| View all | View |

## 5. Toast / Feedback

Provide timely and clear feedback after user actions.
**No period** — toast messages are fragments.

| CN | EN |
|----|-----|
| 已保存 | Saved |
| 上传失败，请重试 | Upload failed. Please try again |
