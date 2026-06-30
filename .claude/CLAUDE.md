# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static studio site for **AAA Devs** (aaadevs.com) — a thin "we are a studio, here are our projects" showcase. It does NOT host product content. The current project is **troniti** ([troniti.com](https://troniti.com)): non-custodial TRON yield management. All product detail (how it works, yield, dashboard) lives on troniti.com — the studio site only carries a short card linking out.

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

Pages use `BaseLayout.astro` for the shared HTML shell (meta tags, fonts, global styles). The home page is three components: `Hero.astro` (logo + name + "Software studio"), `Project.astro` (troniti card → troniti.com), `Footer.astro`.

Global styles including Tailwind directives live in `src/styles/global.css`.

Static assets go in `public/` (`images/logo.svg` is the studio mark).

## Design System

- Dark theme, "data/finance" tone, modeled on tronscan.org
- Accent: TRON-red (`#c23631`)
- Font: Inter
- Colors: bg `#0b0e11`, cards `#161b22`, text `#f0f0f0`, muted `#8b949e`, border `#21262d`
- Detailed architecture doc: [docs/architecture.md](../docs/architecture.md)

## Scaling

New studio projects are added as additional cards in `Project.astro` (a grid). Product depth stays on each product's own landing (troniti.com, etc.).
