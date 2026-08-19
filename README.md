# CCTV Installation Training Manual

A comprehensive, beginner-friendly training manual for CCTV installation technicians, diploma students, interns, electricians, and freshers. Written in Hinglish (Hindi + English mix) with practical-first approach.

---

## Quick Start

### One-Click Launch
```
Double-click: Open Manual.bat
```
This will:
1. Start a local server automatically
2. Open the full manual in your browser
3. You can read all 21,000+ lines with images

### Manual Commands
```bash
# Navigate to project folder
cd C:\Users\Lenovo\Desktop\CCTV_Installation_Manual

# Start server
python -m http.server 8080

# Open in browser
start http://localhost:8080/manual.html
```

### Available Launchers

| File | Purpose |
|------|---------|
| **`Open Manual.bat`** | ⭐ Opens full manual viewer |
| **`Open Dashboard.bat`** | Opens status dashboard |
| **`CCTV Manual Menu.bat`** | Menu with all options |
| **`Setup Images.bat`** | Splits grid image into 25 files |
| **`Convert Diagrams.bat`** | Converts Mermaid diagrams to PNG |

---

## UI/UX Features

### Manual Viewer (`manual.html`)
- **Modern Dark/Light Theme** - Toggle with one click
- **Responsive Design** - Works on desktop, tablet, mobile
- **Interactive Sidebar** - Auto-generated chapter navigation
- **Search Functionality** - Find any text instantly
- **Image Placeholders** - Yellow highlighted boxes for missing images
- **Diagram Placeholders** - Blue highlighted boxes for missing diagrams
- **Linked Images** - Green bordered, properly centered and scaled
- **ASCII Art** - Styled code blocks for text diagrams
- **Callout Boxes** - Warning, Tip, Note, Best Practice styles
- **Font Size Control** - Adjust text size for comfort
- **Back to Top** - Quick scroll to beginning
- **Status Panel** - Real-time image/diagram counts
- **Print Support** - Clean printing with hidden UI

### Dashboard (`index.html`)
- **Hero Section** - Overview with statistics
- **Chapter Cards** - Grid view of all 14 chapters
- **Image Gallery** - Grid of all 25 available images
- **Progress Status** - What's done and what's remaining
- **Quick Links** - Direct access to manual viewer

### Design Improvements
- **Google Fonts** - Inter for UI, JetBrains Mono for code
- **Smooth Animations** - Fade-in effects, hover transitions
- **Glass Morphism** - Backdrop blur on toolbar
- **Gradient Accents** - Modern color scheme
- **Rounded Corners** - 12-16px border radius
- **Proper Shadows** - Depth and elevation
- **Color-coded Status** - Green/Yellow/Blue/Red indicators

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

| Chapter | Title | File |
|---------|-------|------|
| 1 | Introduction to CCTV Systems | `CCTV_Training_Manual.md` |
| 2 | CCTV Components and Tools | `CCTV_Training_Manual.md` |
| 3 | Analog CCTV Systems | `CCTV_Training_Manual.md` |
| 4 | Networking Fundamentals | `CCTV_Training_Manual.md` |
| 5 | IP CCTV Systems | `CCTV_Training_Manual.md` |
| 6 | Storage | `CCTV_Training_Manual.md` |
| 7 | Wireless Cameras | `CCTV_Training_Manual.md` |
| 8 | Site Survey | `CCTV_Training_Manual.md` |
| 9 | Complete Troubleshooting Guide | `CCTV_Training_Manual.md` |
| 10 | Quotation, BOQ and Sales | `CCTV_Training_Manual.md` |
| 11 | Billing and Handover | `CCTV_Training_Manual.md` |
| 12 | Business Model | `CCTV_Training_Manual.md` |
| 13 | Complete Practical Examination | `CCTV_Training_Manual.md` |
| 14 | Feedback and Certification | `CCTV_Training_Manual.md` |
| A | Annexures (Reference Sheets) | `CCTV_Training_Manual.md` |
| I | Image Prompts Pack | `CCTV_Training_Manual.md` |

---

## Project Status

### Overall Progress

| Item | Total | Done | Remaining |
|------|-------|------|-----------|
| **Images** | 50 | 25 (50%) | 25 placeholders |
| **Diagrams** | 26 | 22 (85%) | 4 placeholders |
| **Manual Content** | 14 chapters | 14 (100%) | Complete |
| **HTML Viewer** | 1 | 1 (100%) | Complete |

### Images Status

| Status | Count | Details |
|--------|-------|---------|
| ✅ Images in folder | 25 | All split from grid image |
| ✅ Images linked in manual | 25 | All referenced correctly |
| ⏳ Image placeholders | 25 | Need real photos |
| ✅ Diagram images | 2 | Access Control + Boom Barrier |
| ⏳ Diagram placeholders | 24 | Need to be created |

---

## Image Directory

All images are stored in the `images/` folder.

### Available Images (25 images)

| # | Filename | Description | Used In |
|---|----------|-------------|---------|
| 1 | `01_dome_camera.jpg` | Dome Camera | Ch 3 - Analog CCTV Systems |
| 2 | `02_bullet_camera.jpg` | Bullet Camera | Ch 3 - Analog CCTV Systems |
| 3 | `03_ptz_camera.jpg` | PTZ Camera | Ch 3 - Analog CCTV Systems |
| 4 | `04_dvr.jpg` | DVR (Digital Video Recorder) | Ch 3, Ch 9 (multiple) |
| 5 | `05_nvr.jpg` | NVR (Network Video Recorder) | Ch 1 - IP CCTV, Ch 5 |
| 6 | `06_bnc_connector.jpg` | BNC Connector | Ch 2 - 2.1.1 |
| 7 | `07_rj45_connector.jpg` | RJ45 Connector | Ch 2 - 2.1.3 |
| 8 | `08_dc_power_connector.jpg` | DC Power Connector | Ch 2 - Connectors |
| 9 | `09_coaxial_cable.jpg` | Coaxial Cable (RG59) | Ch 2 - Cables |
| 10 | `10_cat6_cable.jpg` | CAT6 Cable | Ch 2 - Cables |
| 11 | `11_fiber_optic_cable.jpg` | Fiber Optic Cable | Ch 2 - Cables |
| 12 | `12_bnc_crimping_tool.jpg` | BNC Crimping Tool | Ch 2 - Connectors |
| 13 | `13_rj45_crimping_tool.jpg` | RJ45 Crimping Tool | Ch 2 - Connectors |
| 14 | `14_cable_tester.jpg` | Cable Tester | Ch 2 - 2.4.3 |
| 15 | `15_multimeter.jpg` | Multimeter | Ch 2 - 2.4.2 |
| 16 | `16_surveillance_hdd.jpg` | Surveillance Hard Disk Drive | Ch 2, Ch 9 |
| 17 | `17_pvc_conduit.jpg` | PVC Conduit | Ch 2 - Cable Management |
| 18 | `18_trunking.jpg` | Cable Trunking | Ch 2 - 2.3.2 |
| 19 | `19_poe_switch.jpg` | PoE Switch | Ch 9 - Troubleshooting |
| 20 | `20_router.jpg` | Router | Ch 4 - 4.10 |
| 21 | `21_wifi_camera.jpg` | WiFi Camera | Ch 1 - Wireless CCTV |
| 22 | `22_smps_power.jpg` | SMPS Power Supply | Ch 9 - Troubleshooting |
| 23 | `23_hidden_camera.jpg` | Hidden/Covert Camera | Ch 1 - Hidden CCTV |
| 24 | `24_cable_ties.jpg` | Cable Ties | Ch 2 - 2.3.4 |
| 25 | `25_tool_kit.jpg` | CCTV Tool Kit | Ch 2, Ch 9 |

### Diagram Images (2 images)

| # | Filename | Description | Used In |
|---|----------|-------------|---------|
| 1 | `diagram_access_control.png` | Access Control System Architecture | Ch 12 - 12.3 |
| 2 | `diagram_boom_barrier.png` | Boom Barrier System | Ch 12 - 12.4 |

---

## Images Needed (Placeholders in Manual)

These are placeholder references in the manual that need actual images to be added:

| # | Placeholder Text | Chapter/Section | Suggested Image |
|---|-----------------|-----------------|-----------------|
| 1 | `[Image: Old CRT monitor based CCTV setup vs modern LCD/IP CCTV setup]` | Ch 1 - 1.1 | Old vs Modern CCTV comparison photo |
| 2 | `[Image: Typical analog CCTV camera (dome and bullet) connected to DVR with coaxial cables]` | Ch 1 - 1.3.1 | Analog CCTV system setup photo |
| 3 | `[Image: Varifocal camera with zoom/focus adjustment rings, fixed vs varifocal comparison]` | Ch 3 - 3.1.4 | Varifocal camera close-up |
| 4 | `[Image: Comparison of same scene in H.264, H.265, H.265+ quality]` | Ch 3 - 3.3 | Compression comparison screenshot |
| 5 | `[Image: IP Camera Types Comparison]` | Ch 5 - 5.1 | All IP camera types side by side |
| 6 | `[Image: Troubleshooting flowchart overview]` | Ch 9 - 9.1 | Troubleshooting flowchart diagram |
| 7 | `[Image: Comparison of clear vs fuzzy video]` | Ch 9 - 9.2.1 | Clear vs blurry video comparison |
| 8 | `[Image: Video showing horizontal rolling lines]` | Ch 9 - 9.2.2 | Rolling lines video artifact |
| 9 | `[Image: Camera showing B&W instead of color]` | Ch 9 - 9.2.3 | B&W mode issue photo |
| 10 | `[Image: Video showing ghosting effect]` | Ch 9 - 9.2.4 | Ghosting effect example |
| 11 | `[Image: Monitor showing blue screen for one camera]` | Ch 9 - 9.2.5 | Blue screen / no signal display |
| 12 | `[Image: Day vs Night camera comparison]` | Ch 9 - 9.2.6 | Day/Night mode comparison |
| 13 | `[Image: Video showing compression artifacts]` | Ch 9 - 9.2.7 | Compression artifact example |
| 14 | `[Image: Camera with LED off showing no power]` | Ch 9 - 9.3.1 | Dead camera / no power LED |
| 15 | `[Image: Camera LED blinking pattern]` | Ch 9 - 9.3.2 | LED blink pattern on camera |
| 16 | `[Image: Command prompt showing ping failure]` | Ch 9 - 9.4.1 | Ping failure screenshot |
| 17 | `[Image: Comparison of focused vs blurry camera view]` | Ch 9 - 9.5.1 | Focus issue comparison |
| 18 | `[Image: Camera with IR reflection problem showing white glare]` | Ch 9 - 9.5.2 | IR reflection / glare image |
| 19 | `[Image: Camera showing incorrect day/night mode]` | Ch 9 - 9.5.3 | Wrong day/night mode |
| 20 | `[Image: Camera with temperature warning]` | Ch 9 - 9.5.4 | Camera overheating warning |
| 21 | `[Image: Professional CCTV quotation format template]` | Ch 10 - 10.1 | Quotation template screenshot |
| 22 | `[Image: Access Control Controller Board]` | Ch 12 - 12.3 | Access control board photo |
| 23 | `[Image: Access Control Installation Steps]` | Ch 12 - 12.3 | Step-by-step installation photos |
| 24 | `[Image: Outdoor Unit]` | Ch 12 - 12.5 | Video door phone outdoor unit |
| 25 | `[Image: Indoor Monitor]` | Ch 12 - 12.5 | Video door phone indoor monitor |

---

## Diagrams Status

### Completed Diagrams (22 of 26)

| # | Diagram | Format | Status |
|---|---------|--------|--------|
| 1 | LAN Network Layout | Mermaid | ✅ Done |
| 2 | LAN vs WAN Architecture | Mermaid | ✅ Done |
| 3 | Internet Data Path | Mermaid | ✅ Done |
| 4 | IPv4 Address Structure | ASCII Art | ✅ Done |
| 5 | Subnetting Multi-floor | Mermaid | ✅ Done |
| 6 | Access Control Architecture | Image | ✅ Done |
| 7 | Access Control Working Flow | Mermaid | ✅ Done |
| 8 | Magnetic Lock Installation | ASCII Art | ✅ Done |
| 9 | Boom Barrier System | Image | ✅ Done |
| 10 | Boom Barrier Working Flow | Mermaid | ✅ Done |
| 11 | Vehicle Loop Sensor | ASCII Art | ✅ Done |
| 12 | VDP System Overview | Mermaid | ✅ Done |
| 13 | Wired VDP Connection | ASCII Art | ✅ Done |
| 14 | IP VDP Network | Mermaid | ✅ Done |
| 15 | VDP + CCTV Integration | Mermaid | ✅ Done |
| 16 | SLA Sample | ASCII Art | ✅ Done |
| 17 | Career Path Chart | Mermaid | ✅ Done |
| 18 | Company Growth Stages | Mermaid | ✅ Done |
| 19 | Network Test Topology | Mermaid | ✅ Done |
| 20 | Feedback Cycle | Mermaid | ✅ Done |
| 21 | Controller Board Layout | ASCII Art | ✅ Done |
| 22 | Boom Barrier Components | Mermaid | ✅ Done |

### Remaining Diagrams (4 of 26)

| # | Diagram | Tool Needed | Why |
|---|---------|-------------|-----|
| 1 | Foundation Dimensions | AutoCAD | Precise measurements |
| 2 | Outdoor Unit Anatomy | draw.io / Figma | Labeled product |
| 3 | Indoor Monitor | draw.io / Figma | Labeled product |
| 4 | Exam Station Layout | AutoCAD | Floor plan |

---

## File Structure

```
CCTV_Installation_Manual/
├── README.md                    <- You are here
├── CCTV_Training_Manual.md      <- Main training manual (21,000+ lines)
├── Promt.md                     <- Master prompt used to generate content
├── STATUS.md                    <- Project status summary
├── IMAGES_AND_DIAGRAMS_NEEDED.md <- Detailed list of images/diagrams to create
│
├── LAUNCHERS
├── Open Manual.bat              <- ⭐ Main launcher (opens manual)
├── Open Dashboard.bat           <- Opens status dashboard
├── CCTV Manual Menu.bat         <- Menu with all options
├── Setup Images.bat             <- Splits grid image into 25 files
├── Convert Diagrams.bat         <- Converts Mermaid diagrams to PNG
├── start-server.bat             <- Starts local server
│
├── HTML FILES
├── manual.html                  <- Full manual viewer (renders .md)
├── index.html                   <- Status dashboard
│
├── SCRIPTS
├── split_images.py              <- Splits grid image into 25 files
├── copy_diagrams.py             <- Copies diagram images
│
├── images/                      <- All images (27 files)
│   ├── 01_dome_camera.jpg
│   ├── 02_bullet_camera.jpg
│   ├── ... (25 images total)
│   ├── 25_tool_kit.jpg
│   ├── diagram_access_control.png
│   └── diagram_boom_barrier.png
│
└── diagrams/                    <- Diagram source files
    ├── ALL_DIAGRAMS.md          <- All 26 diagrams (Mermaid/ASCII)
    ├── convert-all.bat          <- Converts .mmd to PNG
    ├── 01_lan_network.mmd
    ├── 07_access_control_flow.mmd
    ├── 11_boom_barrier_flow.mmd
    ├── 26_feedback_cycle.mmd
    └── ChatGPT Image *.png      <- Source diagram images
```

---

## Image Alignment Fixes

### Problems Fixed
1. **Images not centered** - Now using `display: flex; justify-content: center`
2. **Images too large** - Added `max-width: 100%; max-height: 500px`
3. **Images breaking layout** - Added proper containment with `object-fit: contain`
4. **No spacing** - Added proper margins and padding
5. **Inconsistent borders** - Unified green border with rounded corners

### CSS Improvements
```css
/* Image container - centered with green border */
.img-linked {
  border: 3px solid var(--green);
  border-radius: 12px;
  padding: 8px;
  margin: 24px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--green-bg);
  max-width: 100%;
}

/* Image sizing - responsive and contained */
.img-linked img {
  display: block;
  max-width: 100%;
  max-height: 500px;
  height: auto;
  border-radius: 8px;
  object-fit: contain;
}
```

### Responsive Behavior
- **Desktop:** Images centered, max 500px height
- **Tablet:** Images scale down proportionally
- **Mobile:** Images fill container width, maintain aspect ratio
- **Print:** Images show at full size without UI elements

---

## How to Add New Images & Diagrams

### Adding Images
1. Place image files in the `images/` folder
2. Use descriptive filenames with underscores (e.g., `06_bnc_connector.jpg`)
3. In the manual, reference images using Markdown:
   - `![Alt Text](images/filename.jpg)` — for inline images
   - `[Image: Description]` — for placeholder text
4. Update the **Available Images** table above when adding new images

### Adding Diagrams
1. Create diagrams using tools like draw.io, Mermaid, PlantUML, or any diagram tool
2. Export as PNG/SVG and save in `images/` folder with descriptive names
3. Replace the `[Diagram: Description]` placeholder in the manual with:
   - `![Diagram Title](images/diagram_filename.png)` — for static images
   - Or embed Mermaid/draw.io code directly in the Markdown
4. Update the **Diagrams Needed** table above and mark as completed

### Using Mermaid Diagrams
1. Copy Mermaid code from `diagrams/ALL_DIAGRAMS.md`
2. Go to https://mermaid.live/
3. Paste the code
4. Export as PNG/SVG
5. Save to `images/` folder

---

## Viewing Options

### Option 1: Full Manual Viewer (Recommended)
```
Double-click: Open Manual.bat
```
Features:
- Full 21,000+ line manual
- Chapter navigation sidebar
- Search functionality
- Dark/Light theme
- Image placeholders highlighted
- Diagram placeholders highlighted

### Option 2: Status Dashboard
```
Double-click: Open Dashboard.bat
```
Features:
- Chapter overview
- Available images gallery
- Image placeholders list
- Diagram placeholders list
- Progress statistics

### Option 3: Manual Markdown
Open `CCTV_Training_Manual.md` in any Markdown editor (VS Code, Typora, etc.)

---

## Troubleshooting

### Server Won't Start
- Make sure Python is installed: `python --version`
- If not, install from https://python.org
- Check "Add Python to PATH" during installation

### Images Not Showing
- Run `Setup Images.bat` to split the grid image
- Check that images are in the `images/` folder
- Refresh the browser page

### Diagrams Not Rendering
- Mermaid diagrams need to be converted to PNG
- Run `Convert Diagrams.bat` (requires Node.js)
- Or use https://mermaid.live/ to export manually

---

## Support

For issues or questions:
- Check `STATUS.md` for current project status
- Check `IMAGES_AND_DIAGRAMS_NEEDED.md` for image/diagram requirements
- Check `diagrams/ALL_DIAGRAMS.md` for diagram source code

---

## License

This training manual is for educational purposes. Use freely for CCTV training programs.
