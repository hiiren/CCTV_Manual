# CCTV Manual - Images & Diagrams Needed

This file lists all images and diagrams that need to be added to complete the CCTV Installation Training Manual.

---

## Images Needed (25 Total)

### Chapter 1 - Introduction to CCTV

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 1 | 1.1 | Old CRT monitor based CCTV setup vs modern LCD/IP CCTV setup | Split comparison photo: left side shows old bulky CRT monitor with analog cameras, right side shows modern flat LCD with IP cameras | Stock photo or AI-generated comparison |
| 2 | 1.3.1 | Typical analog CCTV camera connected to DVR with coaxial cables | Photo showing 2-3 dome/bullet cameras wired to a DVR unit with visible coaxial cables | Real installation photo or stock |

### Chapter 3 - Analog CCTV Systems

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 3 | 3.4 | Varifocal camera with zoom/focus adjustment rings, fixed vs varifocal comparison | Close-up photo of varifocal camera showing the adjustment rings, next to a fixed lens camera | Product photo from manufacturer |
| 4 | 3.3 | Comparison of same scene in H.264, H.265, H.265+ quality | Three screenshots of same CCTV footage showing quality differences at same bitrate | Screen capture from DVR/NVR |

### Chapter 5 - IP CCTV Systems

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 5 | 5.1 | IP Camera Types Comparison | Photo grid showing: Dome IP, Bullet IP, PTZ IP, Turret IP, Fisheye IP cameras side by side | Product photos from Hikvision/Dahua |

### Chapter 9 - Troubleshooting (14 Images)

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 6 | 9.1 | Troubleshooting flowchart overview | Flowchart diagram: Problem → Check Power → Check Cable → Check Settings → Resolve | Create in draw.io/Canva |
| 7 | 9.2.1 | Comparison of clear vs fuzzy video | Split screen: left = sharp clear video, right = blurry/out-of-focus video | Screenshot from DVR |
| 8 | 9.2.2 | Video showing horizontal rolling lines | Screenshot showing horizontal rolling/sync lines artifact | Screenshot of bad signal |
| 9 | 9.2.3 | Camera showing B&W instead of color | Screenshot showing camera stuck in black & white mode during daytime | Screenshot from DVR |
| 10 | 9.2.4 | Video showing ghosting effect | Screenshot showing double image/ghosting artifact | Screenshot of bad cable |
| 11 | 9.2.5 | Monitor showing blue screen for one camera | Screenshot of multi-camera view where one channel shows blue/no signal | Screenshot from DVR |
| 12 | 9.2.6 | Day vs Night camera comparison | Split screen: left = daytime color view, right = nighttime IR black & white view | Screenshot from same camera |
| 13 | 9.2.7 | Video showing compression artifacts | Screenshot showing blocky/pixelated compression artifacts | Screenshot with low bitrate |
| 14 | 9.3.1 | Camera with LED off showing no power | Photo of camera with no LED indicator lit, showing dead state | Real photo of powered-off camera |
| 15 | 9.3.2 | Camera LED blinking pattern | Close-up photo showing LED blinking in specific pattern (e.g., power cycling) | Real photo or diagram |
| 16 | 9.4.1 | Command prompt showing ping failure | Screenshot of Windows command prompt showing "Request timed out" ping failure | Screenshot from PC |
| 17 | 9.5.1 | Comparison of focused vs blurry camera view | Split screen: left = properly focused camera view, right = out-of-focus view | Screenshot from DVR |
| 18 | 9.5.2 | Camera with IR reflection problem showing white glare | Screenshot showing white glare/bloom from IR reflecting off wall/window | Screenshot of IR reflection |
| 19 | 9.5.3 | Camera showing incorrect day/night mode | Screenshot showing camera in wrong mode (e.g., color at night, B&W during day) | Screenshot from DVR |
| 20 | 9.5.4 | Camera with temperature warning | Screenshot or photo showing camera overheating warning message | Screenshot from IP camera web UI |

### Chapter 10 - Quotation & Sales

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 21 | 10.1 | Professional CCTV quotation format template | Screenshot of a professional CCTV quotation/estimate document | Create sample in Word/Excel |

### Chapter 12 - Business Model

| # | Section | Placeholder Text | What to Get | Suggested Source |
|---|---------|-----------------|-------------|------------------|
| 22 | 12.3 | Access Control Controller Board | Close-up photo of access control controller board showing terminals, relays, LEDs | Product photo from manufacturer |
| 23 | 12.3 | Access Control Installation Steps | Step-by-step photos: mounting reader, wiring controller, installing lock | Real installation photos |
| 24 | 12.5 | Outdoor Unit (Video Door Phone) | Front view photo of VDP outdoor unit showing camera, call button, speaker | Product photo from Hikvision/Dahua |
| 25 | 12.5 | Indoor Monitor (Video Door Phone) | Front view photo of VDP indoor monitor showing LCD screen, buttons | Product photo from manufacturer |

---

## Diagrams Needed (26 Total)

### Chapter 4 - Networking Fundamentals (5 Diagrams)

| # | Section | Diagram Title | Description | Create In |
|---|---------|--------------|-------------|-----------|
| 1 | 4.1 | LAN Network Layout for CCTV | Network diagram: DVR/NVR → Switch → Cameras; Switch → Router → Internet. Include IP addresses (192.168.1.x) | draw.io / Visio |
| 2 | 4.1 | LAN vs WAN Architecture | Side-by-side comparison: LAN shows devices in one building connected via switch; WAN shows multiple buildings connected via internet cloud | draw.io / Visio |
| 3 | 4.3 | How Internet Works - Data Path | Flow diagram: Camera → DVR → Router → ISP → Internet → Mobile App. Show data flow with arrows | draw.io / Canva |
| 4 | 4.5 | IPv4 Address Structure | Diagram showing: 192.168.1.100 broken into octets, binary representation (11000000.10101000.00000001.01100100), network vs host portion highlighted | draw.io / Canva |
| 5 | 4.6 | Subnetting for Multi-floor CCTV | Building cross-section showing 4 floors, each with separate subnet: Floor 1 (192.168.1.x), Floor 2 (192.168.2.x), Floor 3 (192.168.3.x), Floor 4 (192.168.4.x). Core switch connecting all | draw.io / Visio |

### Chapter 12 - Business Model (17 Diagrams + 3 more)

| # | Section | Diagram Title | Description | Create In |
|---|---------|--------------|-------------|-----------|
| 6 | 12.3 | Access Control System Architecture | Architecture diagram: Controller Board connected to Card Readers (x2), Biometric Reader, Magnetic Lock, Electric Strike, Exit Button, Door Sensor, Alarm. Label all connections | draw.io / Visio |
| 7 | 12.3 | Access Control Working Flow | Flowchart: User presents card → Reader captures ID → Controller checks database → Authorized? → YES: Unlock door + Log entry → NO: Deny + Alarm. Use proper flowchart symbols | draw.io / Lucidchart |
| 8 | 12.3 | Controller Board Layout | Labeled PCB layout diagram: Power terminals (12V/GND), Lock relay outputs (COM/NO/NC), Reader inputs (Wiegand DATA0/DATA1), RS485 port, Ethernet port, Status LEDs, Reset button | draw.io / Figma |
| 9 | 12.3 | Magnetic Lock Installation | Cross-section diagram: Door frame with electromagnet mounted on top, armature plate on door, gap specification (max 0.5mm), power wires routed through frame | draw.io / Canva |
| 10 | 12.4 | Boom Barrier System | System diagram: Boom arm (3m), Motor housing (motor, gearbox, limit switch), Controller board, Power supply (24VDC), Loop sensor, Card reader/remote | draw.io / Visio |
| 11 | 12.4 | Boom Barrier Working Flow | Flowchart: Vehicle approaches → Loop sensor detects → Authorization check → Valid: Boom rises (3-5 sec) → Vehicle passes → Loop sensor clears → Auto-close (5 sec delay) | draw.io / Lucidchart |
| 12 | 12.4 | Boom Barrier Component Layout | Exploded view diagram: Boom arm, Motor housing (showing motor, gearbox, limit switch, controller), Base plate, Foundation bolts | draw.io / Figma |
| 13 | 12.4 | Foundation Dimensions | Cross-section drawing: Concrete pit (60cm x 50cm x 50cm deep), Anchor bolts (M16 x 4), Base plate, PVC conduit for wiring, Drainage hole | draw.io / AutoCAD |
| 14 | 12.4 | Vehicle Loop in Ground | Two views: Top-view showing loop wire shape (rectangular) in saw-cut groove; Cross-section showing wire depth (5cm), sealant filling, detector unit location | draw.io / Canva |
| 15 | 12.5 | VDP System Overview | Split-view diagram: Left = Outdoor unit (camera, call button, speaker, mic); Right = Indoor unit (LCD screen, talk button, open door button); Connected by wires/network | draw.io / Visio |
| 16 | 12.5 | Outdoor Unit Anatomy | Labeled front-view diagram: Camera lens, IR LEDs, Call button, Microphone, Speaker grill, Mounting screws, IP65 weather housing | draw.io / Figma |
| 17 | 12.5 | Indoor Monitor | Labeled diagram: LCD screen, Speaker, Microphone, Talk button, Open Door button, Menu button, Power port, Ethernet port, Mounting bracket | draw.io / Figma |
| 18 | 12.5 | Wired VDP Connection | Wiring diagram: 5 color-coded wires between outdoor and indoor units: Red (12V Power), Black (GND), Yellow (Video), White (Audio), Green (Lock control) | draw.io / Canva |
| 19 | 12.5 | IP VDP Network Connection | Network diagram: Router → PoE Switch → Outdoor VDP Unit + Indoor Monitor + Mobile App (WiFi). Show IP addresses and connections | draw.io / Visio |
| 20 | 12.5 | VDP + CCTV Integration | Combined system diagram: CCTV section (NVR + 4 Cameras) + VDP section (Outdoor + Indoor) both connected to central PoE Switch, Switch to Router | draw.io / Visio |
| 21 | 12.6 | SLA Sample | Document template diagram: Header (Company/Client), Scope section, Response times table (Critical: 4h, Major: 24h, Minor: 72h), Penalty clause, Signatures | Word / Google Docs |
| 22 | 12.7 | Career Path Chart | Vertical ladder diagram: Trainee (8K) → Junior Tech (15K) → Technician (25K) → Senior Tech (40K) → Team Lead (55K) → Project Manager (80K) → Business Owner (1L+) | draw.io / Canva |
| 23 | 12.8 | Company Growth Stages | Staircase diagram with 5 steps: Solo Tech (30K/mo) → Solo+Helper (60K/mo) → Small Team 5 people (2L/mo) → Company 20 people (10L/mo) → Enterprise 50+ (50L+/mo) | draw.io / Canva |

### Chapter 13 - Practical Examination (2 Diagrams)

| # | Section | Diagram Title | Description | Create In |
|---|---------|--------------|-------------|-----------|
| 24 | 13.1 | Exam Station Layout | Floor-plan diagram: 4 camera mounting points (marked X), DVR + Monitor station, PVC conduit route (dotted line), Tool station, Power supply unit. Include dimensions | draw.io / AutoCAD |
| 25 | 13.2 | Network Test Topology | Network diagram: Router (192.168.1.1) → PoE Switch → 2x IP Cameras (192.168.1.10, .11) + NVR (192.168.1.100). Show all IP addresses and connections | draw.io / Visio |

### Chapter 14 - Feedback & Certification (1 Diagram)

| # | Section | Diagram Title | Description | Create In |
|---|---------|--------------|-------------|-----------|
| 26 | 14.1 | Feedback to Improvement Cycle | Circular flowchart with 6 steps: Collect Feedback → Analyze Data → Identify Gaps → Update Curriculum → Implement Changes → Re-collect. Arrows connecting each step in a circle | draw.io / Canva |

---

## Summary

| Type | Count | Status |
|------|-------|--------|
| Images in `images/` folder | 25 | Done |
| Images linked in manual | 18 | Done |
| Images NOT linked yet | 7 | Need to link |
| Image placeholders (need photos) | 25 | **Need to get/create** |
| Diagram placeholders (need diagrams) | 26 | **Need to create** |
| **Total items to complete** | **51** | |

---

## Unlinked Images to Link

These 7 images exist but are not referenced in the manual. Add them at these sections:

| Filename | Add to Section | Description |
|----------|---------------|-------------|
| `06_bnc_connector.jpg` | Ch 2 - 2.1.1 BNC Connector | Close-up of BNC connector |
| `07_rj45_connector.jpg` | Ch 2 - 2.1.3 RJ45 Connector | Close-up of RJ45 connector |
| `14_cable_tester.jpg` | Ch 2 - 2.4 Testing Tools | Cable tester in use |
| `15_multimeter.jpg` | Ch 2 - 2.4 Testing Tools | Multimeter for voltage check |
| `18_trunking.jpg` | Ch 2 - 2.3.2 Cable Trunking | Trunking installation |
| `20_router.jpg` | Ch 4 - Networking Fundamentals | Router setup for CCTV |
| `24_cable_ties.jpg` | Ch 2 - 2.3 Cable Management | Cable ties for organization |

---

## Recommended Tools for Creating Diagrams

1. **draw.io** (free) - https://app.diagrams.net/ - Best for network diagrams, flowcharts, architecture
2. **Canva** (free tier) - https://www.canva.com/ - Best for career charts, infographics
3. **Lucidchart** - https://www.lucidchart.com/ - Good for flowcharts
4. **Figma** (free tier) - https://www.figma.com/ - Good for PCB layouts, component diagrams
5. **AutoCAD / LibreCAD** - For precise floor-plans and foundation drawings

---

## Recommended Sources for Stock Photos

1. **Unsplash** (free) - https://unsplash.com/ - Search: CCTV, security camera, DVR
2. **Pexels** (free) - https://www.pexels.com/ - Search: surveillance, camera system
3. **Shutterstock** (paid) - https://www.shutterstock.com/ - Professional CCTV images
4. **Manufacturer sites** - Hikvision, Dahua, CP Plus product pages have official photos
5. **AI Generated** - Use DALL-E, Midjourney, or Stable Diffusion for custom comparisons
