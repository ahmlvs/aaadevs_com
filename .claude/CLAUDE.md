# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static studio site for **AAA Devs** (aaadevs.com) — a thin "we are a studio, here are our projects" showcase. Positioning: software studio building in **crypto & AI**. It does NOT host product content. Current projects: **troniti** ([troniti.com](https://troniti.com)) — non-custodial TRON yield management, and **PlainAI** ([plainai.tech](https://plainai.tech)) — AI tools directory with honest reviews, news and guides. All product detail lives on each product's own site — the studio site only carries short cards linking out.

## Commands

- `npm run dev` — start dev server
- `npm run build` — production build (output: `dist/`)
- `npm run preview` — preview production build locally

## Tech Stack

- **Astro 6** (static site generator, zero JS by default)
- **Tailwind CSS 4** (via `@tailwindcss/vite` plugin)
- **TypeScript** (strict mode)
- **Deploy target**: GitHub Pages (static site, via GitHub Actions)

## Architecture

Single-page site (`src/pages/index.astro`) + `privacy.astro`, `terms.astro`, `404.astro`.

Pages use `BaseLayout.astro` for the shared HTML shell (meta tags, fonts, global styles). The home page is three components: `Hero.astro` (logo + name + "Software studio · building in crypto & AI"), `Project.astro` (grid of project cards: troniti → troniti.com, plainai → plainai.tech), `Footer.astro`.

Global styles including Tailwind directives live in `src/styles/global.css`.

Static assets go in `public/` (`images/logo.svg` is the studio mark).

## Design System

- Dark theme, "data/finance" tone, modeled on tronscan.org
- Accent: TRON-red (`#c23631`); PlainAI brand blue `#93cafa` is used for its card border, the "AI" word in the tagline, and the "ai" part of its logo
- Font: Inter
- Colors: bg `#0b0e11`, cards `#161b22`, text `#f0f0f0`, muted `#8b949e`, border `#21262d`
- Detailed architecture doc: [docs/architecture.md](../docs/architecture.md)

## Scaling

New studio projects are added as additional cards in `Project.astro` (a grid). Product depth stays on each product's own landing (troniti.com, etc.).
