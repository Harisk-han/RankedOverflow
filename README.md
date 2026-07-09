# Rank Overflow 🚀

> **Rank Higher. Grow Faster.**  
> A modern SEO agency website built with vanilla HTML, CSS, and JavaScript — powered by Vite.

---

## 📁 Project Structure

```
Rankedflow/
├── index.html          ← Home page
├── about.html          ← About Us page
├── contact.html        ← Contact page
├── services.html       ← Services page
├── score.html          ← SEO Score / Audit page
├── casestudies.html    ← Case Studies page
├── package.json        ← Project config & npm scripts
├── package-lock.json   ← Locked dependency versions
├── vite.config.js      ← Vite build configuration
└── vercel.json         ← Vercel deployment config
```

> Each page is a **self-contained file** — HTML structure, CSS styles (`<style>`), and JavaScript logic (`<script>`) all live in one file per page. No separate CSS or JS files needed.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| HTML5 | Page structure & semantic markup |
| CSS3 (inline `<style>`) | Styling, animations, responsive layout |
| Vanilla JavaScript (inline `<script>`) | Interactivity & dynamic behavior |
| [Vite 5](https://vitejs.dev/) | Dev server & production build tool |
| [Vercel](https://vercel.com/) | Deployment & hosting |
| Google Fonts (Syne + DM Sans) | Typography |

---

## 🚀 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher recommended)
- npm (comes with Node.js)

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

Opens at **http://localhost:3000** (or next available port).  
Hot-reloads on file save automatically.

### Build for Production

```bash
npm run build
```

Outputs optimised files to the `dist/` folder.

### Preview Production Build

```bash
npm run preview
```

---

## 📄 Pages

| Page | File | Description |
|------|------|-------------|
| Home | `index.html` | Landing page with hero, services overview, and CTA |
| About | `about.html` | Team, mission, and company story |
| Services | `services.html` | Detailed breakdown of SEO services offered |
| SEO Score | `score.html` | Free website audit / score tool |
| Case Studies | `casestudies.html` | Client success stories and results |
| Contact | `contact.html` | Contact form and office details |

---

## 🎨 Design System

All pages share a consistent design language defined via CSS custom properties:

```css
--ink: #0a0a0f;           /* Primary text */
--surface: #f5f4f0;       /* Page background */
--accent: #ff4d1c;        /* Brand orange */
--green: #00c472;         /* Success / growth */
--blue: #1a56ff;          /* Highlights */
--muted: #7a7a8c;         /* Secondary text */
```

**Fonts:** [Syne](https://fonts.google.com/specimen/Syne) (headings) + [DM Sans](https://fonts.google.com/specimen/DM+Sans) (body)

---

## ☁️ Deployment

The project is deployed on **Vercel** with clean URLs enabled (`vercel.json`):

```json
{
  "version": 2,
  "cleanUrls": true
}
```

`cleanUrls: true` means pages are served without `.html` extensions (e.g. `/about` instead of `/about.html`).

To deploy manually:
```bash
npx vercel
```

---

## 📦 Dependencies

```json
"devDependencies": {
  "vite": "^5.2.0"
}
```

Only one dev dependency — Vite for the local development server and build tooling.

---

## 📝 Notes

- `node_modules/` is gitignored and not committed to the repo.
- All CSS and JS is **inline per page** for simplicity — no bundling or imports required.
- The Vite config (`vite.config.js`) registers all 6 HTML pages as entry points for the production build.

---

## 🔗 Repository

**GitHub:** [github.com/Harisk-han/RankedOverflow](https://github.com/Harisk-han/RankedOverflow)
