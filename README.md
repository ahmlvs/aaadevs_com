# aaadevs.com

Website for **AAA Devs** — a software studio building in **crypto & AI**.

A thin studio showcase: studio identity plus a card per project — each card carries its
project's own brand color. All product detail lives on the projects' own sites.

| project | what | brand on the card |
|---|---|---|
| [troniti.com](https://troniti.com) | non-custodial TRON yield management | orange `#f7941d` (see `troniti-web/design/brand.md`) |
| [plainai.tech](https://plainai.tech) | AI tools directory — honest reviews, news & guides | blue `#93cafa` |

The studio's own accent (red `#c23631`) stays for the studio identity — hero, links — and is
never used inside a project card.

## Tech Stack

- [Astro](https://astro.build) — static site generator
- [Tailwind CSS](https://tailwindcss.com) — styling

## Development

```bash
npm install
npm run dev        # dev server at localhost:4321
```

> Requires Node.js >= 22.12 (Astro 7). `astro dev` runs as a background daemon —
> `astro dev stop` / `status` / `logs` to manage it.

## Build

```bash
npm run build      # output: dist/
npm run preview    # preview build locally
```

## Deploy

GitHub Pages via GitHub Actions. Auto-deploy on push to `main`.
Custom domain `aaadevs.com` via `public/CNAME`.
