# aaadevs.com

Website for **AAA Devs** — a software studio building on the TRON ecosystem.

A thin studio showcase: studio identity plus a card for the current project,
**troniti** ([troniti.com](https://troniti.com)) — non-custodial TRON yield
management. All product detail lives on the project's own site.

## Tech Stack

- [Astro](https://astro.build) — static site generator
- [Tailwind CSS](https://tailwindcss.com) — styling

## Development

```bash
npm install
npm run dev        # dev server at localhost:4321
```

> Requires Node.js >= 22.12 (Astro 6).

## Build

```bash
npm run build      # output: dist/
npm run preview    # preview build locally
```

## Deploy

GitHub Pages via GitHub Actions. Auto-deploy on push to `main`.
Custom domain `aaadevs.com` via `public/CNAME`.
