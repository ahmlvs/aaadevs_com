# Landing Page Architecture — aaadevs.com (studio)

## Overview

The site of the software studio **AAA Devs** (aaadevs.com). As simple as possible: a studio business
card with a card for the current project that links to the project's own landing.

The studio's flagship project → **troniti** ([troniti.com](https://troniti.com)): a non-custodial
TRX-yield management service for large TRON holders. **All product content** (how it works, the trust
model, yield, dashboard, cabinet) lives on troniti.com — we do not duplicate it on the studio site.
Here it's just a short card + a link.

> The studio site makes no yield claims and describes no mechanics — that's the job of troniti's own
> landing. aaadevs.com simply says "we're a studio, here's our project" and links out to troniti.com.

## Tech stack

| Component | Technology |
|-----------|-----------|
| SSG | Astro |
| Styling | Tailwind CSS |
| Deploy | GitHub Pages (static site) |
| Domain | aaadevs.com |

## Project structure

```
aaadevs_com/
├── src/
│   ├── layouts/
│   │   └── BaseLayout.astro       # HTML shell, meta, fonts, global styles
│   │
│   ├── pages/
│   │   └── index.astro            # The single page (Hero + Project + Footer)
│   │
│   ├── components/
│   │   ├── Hero.astro             # Studio logo, name, tagline
│   │   ├── Project.astro          # troniti card → link to troniti.com
│   │   └── Footer.astro           # Copyright, email
│   │
│   └── styles/
│       └── global.css             # Tailwind directives + custom styles
│
├── public/
│   ├── images/
│   │   ├── logo.svg               # AAA Devs studio logo (TRON-red)
│   │   └── og-image.png           # Open Graph 1200×630 (generated from logo.svg)
│   ├── CNAME                      # aaadevs.com
│   └── favicon.ico
│
├── astro.config.mjs
└── package.json
```

One page, three components — nothing more is needed. No privacy/terms on the studio site (legal pages,
if needed, live on troniti.com).

## Sections (single page)

### Screen 1 — Hero (fullscreen)
- Studio logo SVG, centered
- Heading: **"AAA Devs"**
- Tagline: *"Software studio · building on TRON"* (the word TRON as an accent)
- Minimal, lots of whitespace, dark background, subtle gradient

### Screen 2 — Project (troniti card)
- A single project card with a thin red gradient border
- The troniti brand mark (tilted orbit) + lowercase wordmark **troniti** + a green status badge
  (**Live**) + one line of description: *"Non-custodial TRON yield management"*
- CTA button: **"Visit troniti.com →"** (→ troniti.com)
- No metrics, no mechanics — name, status, one line, link.
- (Future: new studio-project cards get added here — a grid.)

### Screen 3 — Footer
- © 2026 AAA Devs
- Contact email
- (Optional) links to socials / the studio's GitHub

## SEO and meta tags

```html
<title>AAA Devs — Software studio · building on TRON</title>
<meta name="description" content="AAA Devs is a software studio. Current project: troniti — non-custodial TRON yield management.">
<meta property="og:image" content="https://aaadevs.com/images/og-image.png">
<meta property="og:title" content="AAA Devs — Software studio · building on TRON">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://aaadevs.com">
```

## Design

Reference — **tronscan.org** as the de-facto standard of the TRON ecosystem.

### Style
- Dark theme (like tronscan dark), clean, "data/finance" tone
- Accent: **TRON-red** (`#c23631` / `#e50914` family, as on tronscan)
- Font: Inter (system, neutral — in the spirit of tronscan)
- Large typography, lots of space, minimal elements
- Subtle: thin red gradient borders, soft shadows, a light glass effect on the card
- No excess animation — restrained and serious

### Colors (palette tuned to tronscan + TRON-red)
```css
--bg:           #0b0e11;   /* dark background à la tronscan dark */
--bg-card:      #161b22;
--text:         #f0f0f0;
--text-muted:   #8b949e;
--accent:       #c23631;   /* TRON-red */
--accent-hover: #e04b45;
--border:       #21262d;
```

## Deploy

### GitHub Pages (Static Site)
- Auto-deploy via GitHub Actions: push to `main` → `npm run build` → publish `dist/`
- Workflow `.github/workflows/deploy.yml` (the official `actions/deploy-pages`)
- Automatic HTTPS
- Custom domain aaadevs.com via `public/CNAME` (or the repo's Pages settings)
- Set `site: 'https://aaadevs.com'` in `astro.config.mjs` (with a custom domain, no `base` is needed)

## Scaling (post-MVP)

- **New studio projects**: add cards to the Project section (a grid) — the structure already allows for it
- The studio site stays thin: all product depth lives on the projects' own landings (troniti.com, etc.)
