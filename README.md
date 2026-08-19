# CCTV Installation Training Manual

A comprehensive, beginner-friendly training manual for CCTV installation technicians, diploma students, internships, electricians, and freshers. Written in Hinglish (Hindi + English mix) with a practical-first approach.

**Live Manual:** https://hiiren.github.io/CCTV_Manual/manual.html

---

## Quick Start

### Online (GitHub Pages)
Visit the live manual directly in your browser. No installation needed.

### Local
```bash
# Navigate to project folder
cd C:\Users\Lenovo\Desktop\CCTV_Installation_Manual

# Start server
python -m http.server 8080

# Open in browser
start http://localhost:8080/manual.html
```

---

## Features

### Manual Viewer (`manual.html`)
- **Light Theme** - Clean, classroom-friendly design
- **Interactive Sidebar** - Auto-generated chapter navigation with scroll spy
- **Search** - Find any text instantly across all chapters
- **Presentation Mode** - Press `F` for fullscreen, optimized for 1080p projectors
- **Keyboard Navigation** - Arrow keys to scroll, Escape to close panels
- **Font Size Control** - A-/A+ buttons for readability
- **Image Placeholders** - Yellow boxes for missing images (25 JPGs are placeholders)
- **Diagram Placeholders** - Blue boxes for missing diagrams (now 24 SVG diagrams added)
- **Linked Images** - Green bordered, centered and scaled
- **Callout Boxes** - Warning, Tip, Best Practice, Tool Required
- **Status Panel** - Real-time image/diagram counts
- **Interactive Wiring Diagrams** - Click components to see details
- **YouTube Video Embeds** - Video cards for each chapter

### AI Chatbot
- Built-in AI assistant that answers questions about CCTV installation
- Trained on the manual content
- Works in Hinglish (Hindi + English)
- Answers troubleshooting queries, explains concepts, and provides tips

---

## MCP Server Configuration

The project uses 7 MCP (Model Context Protocol) servers via opencode:

| Server | Purpose |
|--------|---------|
| `notebooklm` | AI-powered Q&A on manual content |
| `puppeteer` | Browser automation and screenshot testing |
| `memory` | Persistent context across sessions |
| `filesystem` | Read/write project files |
| `fetch` | Fetch URLs, YouTube metadata, APIs |
| `github` | Push to GitHub and deploy |
| `playwright` | Browser testing and screenshots |

Configuration is in `opencode.json`.

---

## About This Manual

- **Audience:** New Technicians, Diploma Students, Interns, Electricians, Freshers
- **Language:** Hindi + English Mix (Hinglish)
- **Edition:** 2026 Edition
- **Experience Level:** From Zero to Professional
- **Total Lines:** 21,000+ lines of Markdown
- **Chapters:** 14 chapters + Annexures

---

## Table of Contents

| Chapter | Title |
|---------|-------|
| 1 | Introduction to CCTV Systems |
| 2 | CCTV Components and Tools |
| 3 | Analog CCTV Systems |
| 4 | Networking Fundamentals |
| 5 | IP CCTV Systems |
| 6 | Storage |
| 7 | Wireless Cameras |
| 8 | Site Survey |
| 9 | Complete Troubleshooting Guide |
| 10 | Quotation, BOQ and Sales |
| 11 | Billing and Handover |
| 12 | Business Model |
| 13 | Complete Practical Examination |
| 14 | Feedback and Certification |

---

## Project Status

| Item | Status |
|------|--------|
| Manual Content (14 chapters) | 100% Complete |
| HTML Viewer | 100% Complete |
| Images (25 placeholder JPGs + 25 SVG diagrams) | 100% Coverage |
| Diagrams (24 SVG technical diagrams) | 100% Coverage |
| Interactive Wiring Diagrams | Complete |
| AI Chatbot | Complete |
| GitHub Pages Deployment | Live |

> **Note:** The 25 JPG images in `images/` are currently placeholder/dummy images. These will be replaced with real CCTV equipment photos (from Unsplash/Pexels free stock) in a future update.

---

## File Structure

```
CCTV_Installation_Manual/
├── README.md                    <- This file
├── CCTV_Training_Manual.md      <- Main manual (21,000+ lines)
├── manual.html                  <- HTML viewer with AI chatbot
├── index.html                   <- Status dashboard
├── opencode.json                <- MCP server config
├── project.md                   <- Project summary
├── Promt.md                     <- Master prompt
├── STATUS.md                    <- Project status
│
├── images/                      <- All images (70+ files)
│   ├── 01_dome_camera.jpg       <- 25 placeholder JPGs (to be replaced with real photos)
│   ├── ... (25 equipment placeholders)
│   ├── diagram_*.svg            <- 24 technical SVG diagrams
│   ├── old_vs_modern_cctv.svg   <- SVG illustration placeholders
│   └── All25Images.png          <- Combined reference image
│
└── diagrams/                    <- Diagram source files
    ├── ALL_DIAGRAMS.md
    ├── foundation_dimensions.svg
    ├── outdoor_unit_anatomy.svg
    ├── indoor_monitor.svg
    └── exam_station_layout.svg
```

---

## How It Was Built

This project was built using **opencode** with 6 MCP servers:

1. **Content Generation** - 14 chapters of CCTV training content generated via AI
2. **UI Design** - HTML/CSS/JS viewer built with vanilla JS (no frameworks)
3. **Diagrams** - 24 SVG technical diagrams (LAN, WAN, IPv4, access control, etc.)
4. **Images** - 25 placeholder JPGs + 24 SVG illustrations (real photos pending)
5. **Interactive Features** - Wiring diagrams, video embeds, search, presentation mode
6. **AI Chatbot** - Built-in assistant for real-time Q&A
7. **Deployment** - Pushed to GitHub and deployed to GitHub Pages

---

## License

This training manual is for educational purposes. Use freely for CCTV training programs.
