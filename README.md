<p align="center">
  <img src="assets/meta/favicon-32x32.png" alt="Lusion Logo" width="80" />
</p>

<h1 align="center">Lusion.co — Enhanced Clone</h1>

<p align="center">
  <strong>A customized recreation of the award-winning <a href="https://lusion.co">Lusion.co</a> website with unique visual enhancements</strong>
</p>

<p align="center">
  <a href="https://github.com/Tcode-Motion"><img src="https://img.shields.io/badge/Author-Tcode--Motion-7c3aed?style=for-the-badge&logo=github" alt="Author" /></a>
  <img src="https://img.shields.io/badge/Three.js-Powered-000000?style=for-the-badge&logo=three.js" alt="Three.js" />
  <img src="https://img.shields.io/badge/WebGL-3D%20Graphics-E44D26?style=for-the-badge&logo=webgl" alt="WebGL" />
  <img src="https://img.shields.io/badge/License-Educational-blue?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <a href="https://lusion.co">🌐 Original Site</a> •
  <a href="#-features">✨ Features</a> •
  <a href="#-getting-started">🚀 Setup</a> •
  <a href="#-deployment">☁️ Deploy</a> •
  <a href="#-project-structure">📁 Structure</a>
</p>

---

## 📸 Preview

<table>
  <tr>
    <td><img src="assets/projects/devin_ai/home.webp" alt="Home — Devin AI Project" width="400"/></td>
    <td><img src="assets/projects/porsche_dream_machine/home.webp" alt="Porsche Dream Machine" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><em>Featured Project — Devin AI</em></td>
    <td align="center"><em>Featured Project — Porsche Dream Machine</em></td>
  </tr>
  <tr>
    <td><img src="assets/projects/synthetic_human/home.webp" alt="Synthetic Human" width="400"/></td>
    <td><img src="assets/projects/spaace/home.webp" alt="Spaace NFT" width="400"/></td>
  </tr>
  <tr>
    <td align="center"><em>Synthetic Human — 3D Experience</em></td>
    <td align="center"><em>Spaace — NFT Marketplace</em></td>
  </tr>
</table>

---

## ✨ Features

### 🎯 Core Website Functions

| Function | Description | Status |
|---|---|:---:|
| **3D Hero Scene** | Three.js-powered WebGL background with interactive 3D objects | ✅ |
| **Preloader** | Animated percentage counter (0→100) with smooth reveal | ✅ |
| **SPA Routing** | Client-side navigation between Home, About, Projects, and detail pages | ✅ |
| **Video Reel** | Full-screen Vimeo-powered showreel with custom controls | ✅ |
| **Project Gallery** | 15 featured project pages with depth-mapped hover effects | ✅ |
| **Menu System** | Animated dropdown menu with newsletter signup | ✅ |
| **Contact Section** | "Let's Talk" CTA, email links, and social media links | ✅ |
| **Footer** | Address, newsletter form, social links, and "Back to top" | ✅ |
| **Responsive Design** | Fully responsive across desktop, tablet, and mobile | ✅ |
| **Audio System** | Hover/click sound effects (toggleable via sound button) | ✅ |
| **Scroll Navigation** | "Keep scrolling" page-to-page scroll nav between sections | ✅ |
| **Page Transitions** | Canvas-based transition overlays between pages | ✅ |

### 🎨 Custom Enhancements (Differentiators from Original)

| Enhancement | What It Does |
|---|---|
| 🟣 **Purple Accent Scheme** | Deep violet (`#7c3aed`) accent replacing the original neutral palette — applied to buttons, scroll bar, selection, preloader digits, and project card hover glow |
| 🖱️ **Custom Cursor** | Smooth trailing dot + ring cursor with hover expansion effect on interactive elements. Ring follows with spring-like easing |
| 📦 **Project Card Hover** | Cards lift 6px with a purple glow shadow (`box-shadow`) on hover |
| 🎬 **Page Entrance Animation** | Smooth `translateY(30px) → 0` slide-up with opacity fade on load |
| 👀 **Section Scroll Reveals** | `IntersectionObserver`-driven fade-in as each section enters viewport |
| ✍️ **Styled Text Selection** | Purple highlight with white text on any text selection |
| 💡 **Input Focus Glow** | Purple glow ring around newsletter inputs when focused |
| 📊 **Scroll Indicator Glow** | Accent-colored progress bar with subtle shadow |
| 🔘 **Enhanced Button Hover** | Scale + glow on "Let's Talk" and scroll-to-top buttons |
| 📅 **Dynamic Copyright** | Footer year auto-updates via JavaScript |

### 🔧 Technical Patches

| Patch | Purpose |
|---|---|
| **Error Suppression** | Catches Three.js parsing errors from placeholder `.buf` model files |
| **Preloader Timeout** | Forces page ready after 8 seconds if assets fail to load |
| **Scroll Reset** | Resets scroll position to top on page load |
| **Route Fix** | Strips `.html` extensions so SPA router recognizes pages correctly |
| **Redirect Block** | Prevents the router from redirecting to origin on unknown routes |
| **Menu Fallback** | Toggle + navigation fallback if the original JS init fails |

---

## 🚀 Getting Started

### Prerequisites

- Any modern browser with **WebGL** support (Chrome, Firefox, Edge, Safari)
- **One** of: Python 3.x / Node.js / PHP / any static file server

### 📥 Download

**Option 1 — Git Clone (recommended)**
```bash
git clone https://github.com/Tcode-Motion/Lusion.co-Enhanced-Clone.git
cd Lusion.co-Enhanced-Clone
```

**Option 2 — Download ZIP**
1. Click the green **`<> Code`** button at the top of this repo
2. Click **`Download ZIP`**
3. Extract the ZIP to any folder
4. Open a terminal in that folder

**Option 3 — GitHub CLI**
```bash
gh repo clone Tcode-Motion/Lusion.co-Enhanced-Clone
cd Lusion.co-Enhanced-Clone
```

### ▶️ Run Locally

Pick **any one** method below:

<table>
<tr><th>Method</th><th>Command</th></tr>
<tr>
  <td>🐍 Python</td>
  <td>

```bash
python -m http.server 8000
```
  </td>
</tr>
<tr>
  <td>📦 Node.js</td>
  <td>

```bash
npx serve .
```
  </td>
</tr>
<tr>
  <td>🐘 PHP</td>
  <td>

```bash
php -S localhost:8000
```
  </td>
</tr>
<tr>
  <td>🦀 Rust (miniserve)</td>
  <td>

```bash
npx miniserve . --port 8000
```
  </td>
</tr>
</table>

Then open **http://localhost:8000** in your browser. 🎉

> [!IMPORTANT]
> The site **must** be served via HTTP — opening `index.html` directly as a file **will not work** because it uses ES modules and `fetch()` requests.

### 🪟 Windows Quick Start

```powershell
# If you have Python installed:
cd "C:\path\to\Lusion.co-Enhanced-Clone"
py -m http.server 8000
# Open http://localhost:8000 in Chrome
```

### 🐧 Linux / 🍎 macOS Quick Start

```bash
cd ~/Lusion.co-Enhanced-Clone
python3 -m http.server 8000
# Open http://localhost:8000
```

---

## ☁️ Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

Or connect your GitHub repo at [vercel.com/new](https://vercel.com/new) → Import → Deploy.

### Netlify

1. Push to GitHub
2. Go to [app.netlify.com](https://app.netlify.com)
3. "Add new site" → "Import from Git" → Select repo
4. Build command: *(leave empty)*
5. Publish directory: `.`
6. Click **Deploy**

Or use the CLI:

```bash
npm i -g netlify-cli
netlify deploy --prod --dir .
```

### GitHub Pages

1. Push to your repo
2. Go to **Settings → Pages**
3. Source: **Deploy from a branch**
4. Branch: `main` / Root: `/ (root)`
5. Save — your site will be live at `https://tcode-motion.github.io/Lusion.co-Enhanced-Clone/`

### Cloudflare Pages

1. Connect your GitHub repo at [dash.cloudflare.com](https://dash.cloudflare.com) → Pages
2. Build command: *(leave empty)*
3. Output directory: `.`
4. Deploy

---

## 📁 Project Structure

```
Lusion.co-Enhanced-Clone/
│
├── index.html                  # 🏠 Home page
├── about.html                  # 👥 About page
├── projects.html               # 📋 Projects listing
├── projects/                   # 📂 15 individual project pages
│   ├── devin_ai.html
│   ├── porsche_dream_machine.html
│   ├── synthetic_human.html
│   ├── spatial_fusion.html
│   ├── spaace.html
│   ├── ddd_2024.html
│   ├── choo_choo_world.html
│   ├── soda_experience.html
│   ├── worldcoin.html
│   ├── zero_tech.html
│   ├── lusion_labs.html
│   ├── infinite_passerella.html
│   ├── maxmara_bearings_gifts.html
│   ├── my_little_story_book.html
│   └── the_turn_of_the_screw.html
│
├── patch.js                    # 🩹 Loading, routing & menu fixes
├── custom.css                  # 🎨 Custom visual enhancements
├── custom.js                   # 🖱️ Custom cursor & scroll animations
│
├── _astro/
│   ├── about.e7252178.css      # 📄 Original compiled styles
│   └── hoisted.81170750.js     # ⚙️ Main Three.js app bundle (patched)
│
├── assets/
│   ├── fonts/                  # 🔤 Aeonik font family
│   ├── meta/                   # 🏷️ Favicons, social sharing images
│   ├── models/                 # 🧊 3D model files (.glb, .buf)
│   ├── projects/               # 🖼️ Project images & depth maps
│   ├── textures/               # 🎨 3D scene textures
│   └── team/                   # 👤 Team member photos
│
├── robots.txt                  # 🤖 Search engine directives
└── README.md                   # 📖 This file
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **Three.js** | 3D WebGL rendering, scene management, model loading |
| **Vimeo Player SDK** | Video reel playback with custom controls |
| **Astro** | Original SSG framework (pre-built, served as static HTML) |
| **GLSL Shaders** | Custom post-processing effects, transitions |
| **IntersectionObserver** | Scroll-triggered animations |
| **CSS Custom Properties** | Theming and accent color system |

---

## 📄 Pages Overview

| Page | URL | Description |
|---|---|---|
| Home | `/` | Hero, video reel, featured projects, philosophy section, footer |
| About | `/about.html` | Studio story, team, approach, and values |
| Projects | `/projects.html` | Full project grid with category filters |
| Project Detail | `/projects/*.html` | Individual project case studies with image galleries |

---

## 🔗 Links

| | |
|---|---|
| 🌐 **Original Website** | [lusion.co](https://lusion.co) |
| 👤 **Author** | [Tcode-Motion](https://github.com/Tcode-Motion) |
| 🏢 **Lusion Studio** | [lusion.co](https://lusion.co) — Bristol, UK |

---

## ⚠️ Disclaimer

> This project is a **learning exercise and portfolio piece**. It is **not affiliated** with Lusion Ltd. All original design, branding, and creative work belongs to [Lusion](https://lusion.co). This clone is intended solely for educational purposes to study modern web development techniques including Three.js, WebGL, and advanced CSS animations.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/Tcode-Motion">Tcode-Motion</a>
</p>
