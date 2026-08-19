# CCTV Installation Training Manual — Project Brief & Build Guide

> **Audience:** Classroom / Trainer-led Display  
> **Deployment:** GitHub Pages / Vercel  
> **Tool:** opencode (with MCP servers)  
> **Language:** Hinglish (Hindi + English mix)  
> **Status as of start:** Content 100% ✅ | UI Basic ⚠️ | Images 50% ⚠️ | Diagrams 85% ⚠️

---

## 📁 Project Structure

```
cctv-training-manual/
├── CCTV_Training_Manual.md      # Main manual (21,000+ lines, 14 chapters)
├── manual.html                  # HTML viewer (to be redesigned)
├── index.html                   # Status dashboard
├── opencode.json                # MCP server config
├── Open Manual.bat              # One-click launcher
├── images/                      # 25 of 50 images present
└── diagrams/                    # 22 of 26 diagrams completed
```

---

## 🔌 MCP Server Configuration

Add all 6 servers to your `opencode.json`. The first 3 you already have; add the bottom 3.

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp@latest"]
    },
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/ABSOLUTE/PATH/TO/YOUR/PROJECT"
      ]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    }
  }
}
```

### Why Each Server is Needed

| MCP Server | Status | Why You Need It |
|---|---|---|
| `notebooklm` | ✅ Already added | AI-powered Q&A on manual content |
| `puppeteer` | ✅ Already added | Screenshot testing, browser automation |
| `memory` | ✅ Already added | Persistent context across opencode sessions |
| `filesystem` | ❌ **Add now** | Read/write files directly — needed for bulk image & diagram work |
| `fetch` | ❌ **Add now** | Fetch YouTube metadata, embed URLs, free image APIs |
| `github` | ❌ **Add now** | Push to GitHub and deploy to GitHub Pages directly from Claude |

> ⚠️ **Important:** Replace `/ABSOLUTE/PATH/TO/YOUR/PROJECT` with the real path on your machine, e.g. `C:/Users/YourName/cctv-training-manual` on Windows.

---

## 🚀 Build Order (Do This Sequence)

| Step | Task | Priority |
|---|---|---|
| 1 | Add 3 new MCP servers to `opencode.json` | 🔴 First |
| 2 | Redesign UI (`manual.html`) | 🔴 Biggest classroom impact |
| 3 | Complete 4 missing diagrams as interactive SVGs | 🟠 High |
| 4 | Generate 25 missing images | 🟠 High |
| 5 | Add YouTube embed config | 🟡 Medium |
| 6 | Add clickable hotspots to wiring diagrams | 🟡 Medium |
| 7 | Deploy to GitHub Pages | 🟢 Final step |

---

## 📋 Prompt 1 — UI Redesign (manual.html)

Use this prompt in opencode:

```
Redesign manual.html into a professional e-learning UI optimised for 
classroom projector display (1080p). Requirements:

LAYOUT:
- Fixed left sidebar (280px) with chapter list and progress indicators 
  (✅ completed / 🔄 current / ⬜ not started)
- Sticky top navbar showing: current chapter title, overall progress bar 
  (Chapter X of 14), font size controls (+/-)
- Main content area with max-width 900px, centered
- Full-screen presentation mode toggled by pressing F or a button in navbar

TYPOGRAPHY & THEME:
- Dark theme as default (background #0f0f1a, text #e8e8f0)
- Light theme toggle option
- Minimum 18px body font, 26px headings — readable from 3 metres away
- Line height 1.8 for comfortable reading

NAVIGATION:
- Smooth scroll between chapters with animated transitions
- Keyboard navigation: Left/Right arrow keys move between chapters
- Click any chapter in sidebar to jump instantly

CALLOUT BOXES (styled distinctly):
- ⚠️  Warning box — red border, light red background
- 💡 Tip box — blue border, light blue background  
- ✅ Best Practice box — green border, light green background
- 🔧 Tool Required box — orange border, light orange background

VIDEO SECTION:
- Add a config block at top of file: const CHAPTER_VIDEOS = { ch1: "", ch2: "", ... ch14: "" }
- Wherever [VIDEO_PLACEHOLDER] appears in content, render a styled card with a ▶ play button
- On click, open the YouTube URL from config in a modal overlay (not a new tab)
- If URL is empty, show "Trainer: Add YouTube URL in config" message

TECHNOLOGY:
- Use Tailwind CSS via CDN (no npm install needed)
- Vanilla JS only — no React, no Vue
- Must work offline (all CDN links have local fallback)
- Optimised for Chrome on Windows (classroom PC assumption)
```

---

## 📋 Prompt 2 — Complete the 4 Missing Diagrams

```
Using the filesystem MCP server, read CCTV_Training_Manual.md and identify 
the 4 diagram placeholders that do not have a corresponding file in /diagrams/.

For each missing diagram, create an SVG file in /diagrams/ with:
- Dark background: #1a1a2e
- White/yellow component labels in English + Hindi below each label
- Clean directional arrows showing connections between components
- A Hinglish caption at the bottom of the SVG
- Canvas size: 1200 x 800px (projector-friendly 3:2 ratio)
- Component shapes: rectangles for devices, lines for cables, circles for 
  junction points
- Each component clickable (add id attribute matching component name)

Save files as: diagram_[chapter_number]_[topic_name].svg
```

---

## 📋 Prompt 3 — Generate 25 Missing Images

```
Using the filesystem MCP server, read CCTV_Training_Manual.md and list all 
image references (![...](images/...)) where the file does not exist in /images/.

For each missing image, create a clean technical illustration as an SVG file:
- White background (#ffffff)
- Accurate technical representation (not cartoon style)
- English label + Hindi label for each major component
- Suitable for classroom projection — bold lines, large text (min 14px)
- Border: 2px solid #333333 with 16px padding inside

Save with the exact filename expected by the markdown reference.
After creating all images, update CCTV_Training_Manual.md so any broken 
image references now correctly point to the new files.
```

---

## 📋 Prompt 4 — Clickable Wiring Diagram Hotspots

```
Take the 3 main wiring diagrams in /diagrams/ (DVR wiring, camera wiring, 
power supply wiring) and convert them into interactive hotspot maps inside 
manual.html.

For each diagram:
1. Embed the SVG inline in the HTML (not as <img> tag)
2. For each major component in the SVG (camera, DVR, monitor, power supply, 
   cables, BNC connectors, balun):
   - Add an invisible <rect> overlay on top of that component
   - On hover: show component name + Hindi name as a floating tooltip
   - On click: open a right-side panel (300px wide) showing:
     * Component name (English + Hindi)
     * Small photo from /images/ if available
     * 3-bullet "Kya hai yeh?" (What is this?) explanation in Hinglish
     * 1 "Common Mistake" callout box in red

3. Add a "Reset / Close Panel" button
4. Panel slides in from right with CSS transition (no JS animation libraries)

Use only vanilla JS + CSS. No external libraries.
```

---

## 📋 Prompt 5 — YouTube Video Embed Config

```
In manual.html, find the const CHAPTER_VIDEOS config block and fill it with 
relevant YouTube search queries for each chapter topic using the fetch MCP server.

For each of the 14 chapters:
1. Identify the chapter's main topic from CCTV_Training_Manual.md
2. Use fetch to search YouTube for "[topic] CCTV installation tutorial Hindi"
3. Get the top result's video ID
4. Populate the config: ch1: "https://www.youtube.com/embed/VIDEO_ID"

Also update the video card UI:
- Show video thumbnail (use YouTube thumbnail URL pattern)
- Show video title below thumbnail
- Duration badge in top-right corner of thumbnail
- "Watch in class" label in Hindi: "कक्षा में देखें"
```

---

## 📋 Prompt 6 — Deploy to GitHub Pages

```
Using the github MCP server:

1. Create a new public GitHub repository named "cctv-training-manual" 
   under my account

2. Push all project files:
   - manual.html
   - index.html  
   - CCTV_Training_Manual.md
   - All files in /images/ folder
   - All files in /diagrams/ folder
   - README.md (create one with project description)

3. Enable GitHub Pages:
   - Branch: main
   - Folder: / (root)

4. Return the live GitHub Pages URL

5. Also create a README.md with:
   - Project title and description in English + Hindi
   - Screenshot placeholder
   - Link to the live manual
   - "How to use" section for trainers
```

---

## 📋 Prompt 7 — Quality Check with Puppeteer

Run this after deployment:

```
Using the puppeteer MCP server, open the deployed GitHub Pages URL and:

1. Take a full-page screenshot of the manual homepage
2. Navigate to Chapter 3 and take a screenshot
3. Click on a wiring diagram component and screenshot the hotspot panel
4. Toggle dark/light theme and screenshot
5. Test keyboard navigation (simulate Right arrow key press 3 times)
6. Check that all images load (report any broken image URLs)
7. Check that all diagram SVGs render correctly

Save all screenshots to /screenshots/ folder.
Generate a QA report: qa_report.md listing what passed ✅ and what failed ❌
```

---

## 🎓 Trainer Guide (Add to README)

Once deployed, share this with the trainer:

```
HOW TO USE — Trainer Instructions

1. Open the manual URL in Chrome, press F11 for full screen
2. Use → arrow key to move forward through chapters
3. Use ← arrow key to go back
4. Click any component in a wiring diagram to see its details
5. Press F to enter/exit presentation mode
6. To add your own YouTube videos:
   - Open manual.html in Notepad
   - Find the line: const CHAPTER_VIDEOS = {
   - Paste your YouTube embed URL next to the chapter number
   - Save and refresh
```

---

## ✅ Final Checklist

- [ ] 3 new MCP servers added to `opencode.json`
- [ ] UI redesigned with dark theme, keyboard nav, presentation mode
- [ ] All 26 diagrams completed
- [ ] All 50 images present in `/images/`
- [ ] YouTube embed config populated for all 14 chapters
- [ ] Clickable hotspots on 3 main wiring diagrams
- [ ] Deployed to GitHub Pages
- [ ] Puppeteer QA check passed
- [ ] Trainer guide shared with trainer

---

*Generated for: CCTV Installation Training Manual Project*  
*Build tool: opencode with MCP*  
*Target: Classroom display, deployed on GitHub Pages*
