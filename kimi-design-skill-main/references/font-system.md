# Kimi Font System

This reference owns display-font exceptions. It does not replace `tokens.json` as the source of truth for normal UI typography.

## MiSans Display Exception

Use MiSans only for explicit hero section titles where the title is the primary brand or product display moment.

Allowed use:

- Page-level hero section title.
- Brand, product, or campaign display heading in the first viewport.
- Large editorial title when the design source explicitly treats it as a hero/title asset, not normal UI text.

Do not use MiSans for:

- Controls, buttons, tabs, menus, navigation, form labels, input text, tables, dialogs, modals, toasts, tooltips, cards, dense lists, sidebars, settings, chat messages, body copy, captions, generated content, or long-form reading surfaces.
- Component titles unless the component is itself the page hero surface.
- Solving missing token coverage. Missing typography roles should still be recorded as token gaps.

## Implementation Rule

MiSans is a family override for the allowed hero-title role only. Keep size, weight, line-height, letter spacing, color, spacing, and responsive behavior token-driven unless the design source provides an explicit hero title spec.

Recommended CSS stack:

```css
.kimi-hero-title {
  font-family: "MiSans", "PingFang SC", "Microsoft YaHei", -apple-system,
    BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

Use `letter-spacing: 0`. Do not use viewport-scaled type. Use responsive layout constraints and wrapping rules instead of fluid font scaling.

## Asset Availability

No MiSans font asset is currently bundled in this skill. When implementing:

1. Use a locally available or product-provided MiSans asset if the target project already ships it.
2. Otherwise keep the fallback stack above and note that MiSans requires a font asset or platform installation.
3. Do not add font files to this skill or edit `tokens.json` unless the user provides the source font file and confirms the asset/license path.
