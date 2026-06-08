# Kimi Logo System

This file defines Kimi logo and wordmark asset rules. Read it when a task involves brand marks, wordmarks, logo placeholders, app identity, header brand slots, or sub-brand lockups.

Logo assets are separate from the Kimi icon system. Do not register wordmarks as `24×24` UI icons.

## Assets

Logo assets live in:

```text
assets/logos/
```

Machine-readable index:

```text
references/logos/manifest.json
```

Current assets:

| Asset | Source | Type | Use |
| --- | --- | --- | --- |
| `KimiLogo.svg` | `/Users/moonshot/Downloads/logo.svg` | Symbol, no text | Compact Kimi brand mark |
| `KimiLogoText.svg` | `/Users/moonshot/Downloads/LogoText.svg` | Wordmark | Recommended default for header logo placeholders |
| `KimiLogoSub.svg` | `/Users/moonshot/Downloads/Logo+sub.svg` | Sub-brand lockup | Recommended for header logo placeholders only when paired with a concrete sub-brand |

## Selection Rules

1. Use `KimiLogoText.svg` for the default header logo placeholder when text branding is expected.
2. Use `KimiLogoSub.svg` for a header logo placeholder only when the product has a specific attached sub-brand.
3. Use `KimiLogo.svg` for compact brand-mark contexts where text would not fit or would duplicate nearby brand text.
4. Do not use `KimiLogoText.svg` or `KimiLogoSub.svg` as toolbar icons, button icons, texture concept icons, or inline text icons.
5. Do not use `KimiLogoSub.svg` as a generic Kimi wordmark.

## Sizing

Use the SVG intrinsic aspect ratio. Do not force wordmarks into a square icon frame.

| Asset | Intrinsic size | Preferred use size |
| --- | ---: | ---: |
| `KimiLogo.svg` | `128×128` | `32px` high for compact brand slots; scale by context |
| `KimiLogoText.svg` | `77×26` | `26px` high in header logo placeholders |
| `KimiLogoSub.svg` | `66×26` | `26px` high in header logo placeholders |

Rules:

- Preserve aspect ratio.
- Set one dimension, usually height, and let the other dimension auto-size.
- Do not crop, stretch, recolor, outline, or add effects.
- Keep clear space around the logo at least `8px` in compact header contexts.

## Color

`KimiLogoText.svg` and `KimiLogoSub.svg` are decolored, theme-aware logo assets.

Rules:

- Use `KimiLogoText.svg` as an inline SVG/component and set `color` from the theme. Do not use it through a plain `<img>` when it needs to follow light/dark theme color.
- In light theme, `KimiLogoText.svg` should use `color.labels.primary.light.default`.
- In dark theme, `KimiLogoText.svg` should use `color.labels.primary.dark.default`.
- Use `KimiLogoSub.svg` as an inline SVG/component and provide both CSS variables:
  - `--kimi-logo-sub-bg`
  - `--kimi-logo-sub-fg`
- In light theme, map `--kimi-logo-sub-bg` to `color.labels.primary.light.default` and `--kimi-logo-sub-fg` to `color.background.primary.light.default`.
- In dark theme, map `--kimi-logo-sub-bg` to `color.labels.primary.dark.default` and `--kimi-logo-sub-fg` to `color.background.primary.dark.default`.
- Do not recolor logo SVGs with CSS filters for production UI.
- Do not add a local background plate unless the source asset already includes one or the header component requires a logo container.

Example CSS:

```css
.kimi-logo-text {
  color: var(--color-labels-primary);
}

.kimi-logo-sub {
  --kimi-logo-sub-bg: var(--color-labels-primary);
  --kimi-logo-sub-fg: var(--color-background-primary);
}
```

## Relationship To Icons

Use `references/icon-system.md` for UI icons and concept markers. Use this logo system for brand identity.

Examples:

- Header brand slot: `KimiLogoText.svg` or `KimiLogoSub.svg`.
- Compact app mark: `KimiLogo.svg`.
- Texture cover concept icon: use a semantic icon from `assets/icons/`, not a wordmark.
- Toolbar action: use a semantic UI icon from `assets/icons/`, not a logo.
