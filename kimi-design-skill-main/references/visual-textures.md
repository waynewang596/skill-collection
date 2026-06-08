# Kimi Visual Textures

This file defines how to use local texture assets for Card, Tile, Banner, Feature block, Empty State, and other media/cover slots. Texture assets may be PNG or SVG files.

Use this reference when a UI surface needs an abstract visual cover and no product screenshot, real photo, or user-provided image is available.

## Local Texture Pack

Default local manifest path:

```text
/Users/moonshot/kimi-texture-pack/manifest.json
```

Default local texture directory:

```text
/Users/moonshot/kimi-texture-pack/textures/
```

Expected product project path after sync:

```text
public/kimi-textures/{file}
```

Runtime URL:

```text
/kimi-textures/{file}
```

## Selection Priority

1. Use a product-owned screenshot, real product image, or user-provided image when one exists and fits the content.
2. Use a local texture cover from the Kimi Texture Pack when the media slot needs an abstract visual.
3. Use a plain tokenized fallback surface when no suitable texture exists or the selected texture is missing.
4. Do not invent a texture filename or remote image source.

## When To Check The Texture Pack

Check the texture pack manifest before creating an abstract cover image when the task includes:

- Card media slot
- Tile cover
- Banner visual
- Feature block visual
- Empty State visual
- Any media/cover slot that needs a non-photo abstract background

Do not check the texture pack for purely text-only UI, dense tables, data dashboards, settings pages, forms, or surfaces that already have appropriate product images.

## Selection Flow

1. Read the manifest if it exists.
2. Identify the content intent: AI, search, model, document, data, security, productivity, warning, success, editorial, etc.
3. Filter entries by `best_for`, `palette`, and `mood`.
4. Remove entries whose `avoid_for` matches the task.
5. Prefer textures whose palette aligns with the component state and Kimi tokens.
6. Check whether `public/kimi-textures/{file}` exists in the target product project.
7. If missing, copy the texture from the local texture pack when file edits are in scope; otherwise use `fallback_background` and record the missing asset.

Do not inspect every texture file unless the manifest is missing, ambiguous, or visually suspect.

## Composition Rules

- Texture belongs only inside the media/cover slot, not behind dense body text or form controls.
- Use one texture per media area.
- Keep texture opacity subtle, usually `0.06` to `0.18`; start from the manifest `default_opacity`.
- Use the manifest `blend_mode` unless it harms contrast.
- Apply `background-size: cover` and `background-position: center`.
- Match the media radius rules from the host component, especially Card media radius.
- If an icon is added on top of the texture, choose one semantic icon from `icon-system.md` and use `currentColor`.
- Do not place long body text directly over texture. If text must overlay, verify contrast in screenshot.

## Center Concept Icon

Source style reference: Figma `draft`, node `19:24129`. The reference uses `286 × 160.875px` media frames inside `302 × 176.875px` card frames, with a single `48 × 48px` icon instance centered in the media frame.

Use a centered concept icon only when the cover concept can be explained by one clear semantic icon from the Kimi icon system, such as model, search, document, data, security, code, task, automation, diagnosis, or settings.

Decision gate:

1. First decide whether the media cover needs a concept marker at all.
2. If the concept maps to one obvious icon in `icon-system.md`, place that icon at the exact center of the media slot.
3. If the concept is ambiguous, decorative, multi-part, or better explained by the card title, omit the icon.
4. Never add an icon only to make the texture look richer.

Do not add a centered icon when:

- the media slot already contains a product screenshot, real photo, chart, or user-provided image
- the concept is too broad or would require multiple icons
- the texture is used only as subtle material behind a visual asset
- the icon would compete with text or controls placed over the media slot

Icon selection rules:

1. Read `icon-system.md`.
2. Search `references/icons/manifest.json` by intent.
3. Prefer the closest semantic non-suffixed icon.
4. If no icon fits, omit the icon instead of inventing one.

Common concept mappings:

| Concept | Preferred icon |
| --- | --- |
| AI model, model routing | `ModelIcon` |
| Search, retrieval | `SearchIcon` or `ProSearchIcon` for deep research/search |
| Document, article, template | `DocumentIcon` |
| Knowledge base | `KnowledgeIcon` |
| Data, analysis | `DataIcon`, `DiagramIcon`, or `LinechartIcon` |
| Security, safe state | `SafeIcon` |
| Code, developer tool | `CodeIcon` |
| Task, automation | `TaskIcon` |
| Diagnosis, audit | `DiagnosisIcon` |
| Settings, configuration | `SettingIcon` |

Layout rules:

- Place the icon exactly at the center of the media slot.
- For the standard card cover size (`286 × 160.875px` media, or nearby `16:9` card media), use a direct `48 × 48px` icon.
- Do not wrap the icon in a stage, badge, button, translucent plate, or bordered container for the standard texture cover treatment.
- Use `currentColor`; set the icon color from the host composition, typically white or near-white on the reference dark and mid-tone textures.
- Treat the icon as part of the media composition, not as a Button, Badge, or interactive control.
- Verify in screenshot that the icon remains legible on both dark and light textures.

## Palette Guidance

| Intent | Preferred palette | Typical texture mood | Avoid |
| --- | --- | --- | --- |
| AI, model, automation, search | `blue`, `brand`, `cool` | `technical`, `clean` | warning/destructive textures |
| Documents, reading, editorial | `warm`, `neutral`, `paper` | `editorial`, `soft` | high-contrast noisy textures |
| System, admin, security | `graphite`, `neutral`, `cool` | `structured`, `quiet` | playful or warm editorial textures |
| Success, growth, ecosystem | `green`, `neutral` | `fresh`, `calm` | red/orange warning textures |
| Warning, risk, destructive | avoid texture by default | — | decorative texture behind critical state |

## Implementation Notes

Use tokenized overlays and backgrounds. Texture file paths are product assets, not tokens. Preserve the original texture file extension when copying into the product project.

Example CSS shape:

```css
.cover {
  background-color: var(--cover-fallback);
  background-image:
    linear-gradient(var(--cover-overlay), var(--cover-overlay)),
    url("/kimi-textures/blue-grain-01.svg");
  background-size: cover;
  background-position: center;
  background-blend-mode: normal, soft-light;
}
```

When a texture is selected, record the manifest `id`, source file, opacity, blend mode, and any missing asset note in implementation notes.
