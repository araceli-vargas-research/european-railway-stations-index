# What changed from the branded prototype

If your current project is already running, the only files you need to replace are:

1. `app.py`
2. `styles.css`

Then optionally add the official logo as:

3. `assets/ccc-logo.png`

Everything else — the Excel workbook, processed CSV, build script, data loader, and current components — can stay exactly where it is.

## New in `app.py`
- AV-style top navigation
- automatic support for `assets/ccc-logo.png`
- ombré editorial hero retained
- `Explore the index` CTA
- dark definition band
- two-column About section with AV-style accordions
- editorial “2026 at a glance” section
- full-width dark punctuality / waiting-time story band
- Germany comparison callouts
- OECD-inspired personalized station weighting tool
- numbered research sections
- methodology accordion + data-freshness card
- CCC footer

## New in `styles.css`
- AV-tracker-inspired navigation, buttons, accordions and page hierarchy
- larger editorial typography
- polished ombré hero
- dark Leila reliability band
- personalized-ranking cards
- mobile-responsive rules

## Assets
If `assets/ccc-logo.png` exists, it is used automatically. If not, the page falls back to a temporary CSS mark so the app still runs.
