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
- **Light Theme** - Clean, classroom-friendly design (default)
- **Dark Theme** - Toggle with button (optional)
- **Interactive Sidebar** - Auto-generated chapter navigation with scroll spy
- **Search** - Find any text instantly across all chapters
- **Presentation Mode** - Press `F` for fullscreen, optimized for 1080p projectors
- **Keyboard Navigation** - Arrow keys to scroll, Escape to close panels
- **Font Size Control** - A-/A+ buttons for readability
- **25 Real Stock Photos** - Pexels free photos replacing all placeholders
- **54 SVG Diagrams** - Technical diagrams for networking, CCTV, access control
- **Callout Boxes** - Warning, Tip, Best Practice, Tool Required
- **Status Panel** - Real-time image/diagram counts
- **Interactive Wiring Diagrams** - Click components to see details
- **YouTube Video Embeds** - Video cards for all 14 chapters
- **AI Chatbot** - Built-in assistant for real-time Q&A (Hinglish)

---

## QA Status

| Metric | Result |
|--------|--------|
| Test Cases | 26 |
| Pass Rate | 96.2% (25/26) |
| Images Loaded | 58/59 (1 known headless-only issue) |
| Tables | 540 |
| Code Blocks | 369 |
| Callouts | 52 |
| Nav Links | 251 |

See `TEST_REPORT.md` for full details.

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
| Manual Content (14 chapters) | ✅ Complete |
| HTML Viewer (light+dark, presentation, chatbot) | ✅ Complete |
| Images (25 real Pexels stock photos) | ✅ Complete |
| SVG Diagrams (54 technical diagrams) | ✅ Complete |
| YouTube Videos (14 chapters configured) | ✅ Complete |
| QA Testing (96.2% pass rate) | ✅ Complete |
| GitHub Pages Deployment | ⬜ Pending (enable in Settings) |

---

## File Structure

```
CCTV_Installation_Manual/
├── README.md                    <- This file
├── CCTV_Training_Manual.md      <- Main manual (21,000+ lines)
├── manual.html                  <- HTML viewer with AI chatbot
├── index.html                   <- Status dashboard
├── opencode.json                <- MCP server config + plugins
├── TEST_REPORT.md               <- QA test results (26 cases)
├── REVAMP_TRACKER.md            <- 7-phase progress tracker
│
├── images/                      <- 79 files (25 JPGs + 54 SVGs)
│   ├── 01_dome_camera.jpg       <- Real Pexels stock photos
│   ├── ... (25 equipment photos)
│   ├── exam_station_layout.svg  <- Technical SVG diagrams
│   └── ... (54 SVG diagrams)
│
└── diagrams/                    <- Diagram source files (4 SVGs)
```

---

## License

This training manual is for educational purposes. Use freely for CCTV training programs.
