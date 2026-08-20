# CCTV Installation Training Manual

A comprehensive, beginner-friendly training manual for CCTV installation technicians, diploma students, internships, electricians, and freshers. Written in Hinglish (Hindi + English mix) with a practical-first approach.

**Live Manual:** https://hiiren.github.io/CCTV_Manual/manual.html

---

## Quick Start

### Online (GitHub Pages)
Visit the live manual directly in your browser. No installation needed.

### Local
```bash
cd C:\Users\Lenovo\Desktop\CCTV_Installation_Manual
python -m http.server 8080
start http://localhost:8080/manual.html
```

---

## Features

### Manual Viewer (`manual.html`)
- **Light Theme** — Clean, classroom-friendly design (default)
- **Dark Theme** — Toggle with button (optional)
- **Interactive Sidebar** — Auto-generated chapter navigation with scroll spy
- **Search** — Find any text instantly across all chapters
- **Presentation Mode** — Press `F` for fullscreen, optimized for 1080p projectors
- **Keyboard Navigation** — Arrow keys to scroll, Escape to close panels
- **Font Size Control** — A-/A+ buttons for readability
- **25 Real Stock Photos** — Pexels free photos
- **54 SVG Diagrams** — Technical diagrams for networking, CCTV, access control
- **Callout Boxes** — Warning, Tip, Best Practice, Tool Required
- **YouTube Video Embeds** — Video cards for all chapters
- **AI Chatbot** — Built-in assistant for real-time Q&A (Hinglish)

### Chatbot (AI + Keyword Fallback)
- **Local mode:** NotebookLM MCP-powered (100+ topics, full manual knowledge)
- **GitHub Pages:** Keyword-matching fallback (100+ topics, all 20 chapters)
- **First time setup:** `npm start` → visit `/api/auth` → login with Google
- **Free tier:** 50 queries/day via NotebookLM

---

## Chapter Structure (20 Chapters)

| #   | Chapter                                      | Coverage              |
| --- | -------------------------------------------- | --------------------- |
| 1   | Introduction to CCTV Systems                 | Brands, types, basics |
| 2   | CCTV Components and Tools                    | Hardware, tools, cables |
| 3   | Analog CCTV Systems                          | DVR, analog cameras   |
| 4   | Networking Fundamentals                      | IP, LAN, VLAN, ports  |
| 5   | IP CCTV Systems                              | NVR, IP cameras, PoE  |
| 6   | Storage                                      | HDD, recording, retention |
| 7   | Wireless Cameras                             | WiFi, mobile access   |
| 8   | Site Survey                                  | Survey, planning      |
| 9   | Complete Troubleshooting Guide               | All common issues     |
| 10  | Quotation, BOQ and Sales                     | Pricing, estimates    |
| 11  | Billing and Handover                         | Invoicing, handover   |
| 12  | Business Model                               | Growth strategy       |
| 13  | Complete Practical Examination               | Hands-on tasks        |
| 14  | Feedback and Certification                   | Wrap-up               |
| 15  | **Home Automation & KNX**                        | **New** — Smart home, lighting, scenes |
| 16  | **Access Control & Biometric Systems**           | **New** — Card, fingerprint, face recognition |
| 17  | **Intercom/EPABX Systems**                       | **New** — Matrix, phone systems |
| 18  | **AV Solutions & Equipment**                     | **New** — Projector, speakers, display |
| 19  | **Smart Door Locks & Intrusion Detection**       | **New** — Smart locks, alarms |
| 20  | **FUDS Services & Product Guide**                | **New** — All FUDS International services |
| A   | Software & Tools Quick Reference             | **New** — Master software table |

---

## Project Status

| Item | Status |
|------|--------|
| Manual Content (14 chapters) | ✅ Complete |
| New Chapters (Ch 15-20 + Appendix) | ✅ Complete |
| HTML Viewer (light+dark, presentation, chatbot) | ✅ Complete |
| Images (25 real Pexels stock photos) | ✅ Complete |
| SVG Diagrams (54 technical diagrams) | ✅ Complete |
| YouTube Videos (all chapters) | ✅ Complete |
| QA Testing (96.2% pass rate) | ✅ Complete |
| GitHub Pages Deployment | ✅ Live |
| Chatbot AI Upgrade (NotebookLM) | ⬜ Phase 9 |

---

## File Structure

```
CCTV_Installation_Manual/
├── README.md                    <- This file
├── CCTV_Training_Manual.md      <- Main manual (27,000+ lines, 20 chapters)
├── manual.html                  <- HTML viewer with AI chatbot
├── index.html                   <- Status dashboard
├── opencode.json                <- MCP server config + plugins
├── TEST_REPORT.md               <- QA test results
├── REVAMP_TRACKER.md            <- Phase progress tracker
├── brain.md                     <- Skills/MCP/plugins reference
│
├── images/                      <- 79 files (25 JPGs + 54 SVGs)
└── diagrams/                    <- Diagram source files
```

---

## Tech Stack

- **HTML/CSS/JS** — Vanilla, no frameworks
- **Markdown** — 27,000+ lines of Hinglish content
- **MCP Servers** — notebooklm, puppeteer, memory, filesystem, fetch, github, playwright
- **Plugins** — firecrawl, conductor, goal-plugin, supermemory, md-table-formatter
- **Deployment** — GitHub Pages

---

## License

This training manual is for educational purposes. Use freely for CCTV training programs.
