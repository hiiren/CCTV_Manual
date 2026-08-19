# CCTV Manual - All Diagrams

This file contains all diagrams for the CCTV Installation Training Manual.
Diagrams are created in Mermaid syntax (for flowcharts/network diagrams) and ASCII art.

---

## How to Use These Diagrams

### Mermaid Diagrams
1. Copy the code between ` ```mermaid ` and ` ``` `
2. Go to https://mermaid.live/
3. Paste the code
4. Export as PNG/SVG
5. Save to `images/` folder with descriptive filename
6. Replace `[Diagram: ...]` placeholder in manual with `![Title](images/filename.png)`

### ASCII Art Diagrams
1. These are text-based diagrams already visible in the manual
2. They render in code blocks
3. No conversion needed

---

# CHAPTER 4 - NETWORKING FUNDAMENTALS

---

## Diagram 1: LAN Network Layout for CCTV

```mermaid
graph TB
    subgraph "Internet Cloud"
        ISP[ISP Router]
    end
    
    subgraph "Office / Building"
        Router[Router<br/>192.168.1.1]
        Switch[PoE Switch<br/>192.168.1.2]
        
        subgraph "Cameras"
            CAM1[Dome Camera<br/>192.168.1.10]
            CAM2[Bullet Camera<br/>192.168.1.11]
            CAM3[PTZ Camera<br/>192.168.1.12]
            CAM4[Dome Camera<br/>192.168.1.13]
        end
        
        DVR[DVR/NVR<br/>192.168.1.100]
        MON[Monitor]
        PC[Management PC<br/>192.168.1.50]
    end
    
    ISP -->|WAN| Router
    Router -->|LAN| Switch
    Switch --> CAM1
    Switch --> CAM2
    Switch --> CAM3
    Switch --> CAM4
    Switch --> DVR
    DVR --> MON
    Switch --> PC
    
    style Router fill:#4CAF50,color:#fff
    Switch fill:#2196F3,color:#fff
    DVR fill:#f44336,color:#fff
    CAM1 fill:#FF9800,color:#fff
    CAM2 fill:#FF9800,color:#fff
    CAM3 fill:#FF9800,color:#fff
    CAM4 fill:#FF9800,color:#fff
```

---

## Diagram 2: LAN vs WAN Architecture

```mermaid
graph LR
    subgraph LAN["LAN (Local Area Network)"]
        direction TB
        L_Switch[Switch]
        L_PC1[PC 1]
        L_PC2[PC 2]
        L_Printer[Printer]
        L_NAS[NAS Storage]
        
        L_Switch --> L_PC1
        L_Switch --> L_PC2
        L_Switch --> L_Printer
        L_Switch --> L_NAS
    end
    
    subgraph WAN["WAN (Wide Area Network)"]
        direction TB
        W_Building1[Building A<br/>Mumbai]
        W_Building2[Building B<br/>Delhi]
        W_Building3[Building C<br/>Bangalore]
        W_Internet[Internet]
        
        W_Building1 --> W_Internet
        W_Building2 --> W_Internet
        W_Building3 --> W_Internet
    end
    
    LAN["LAN: Same building<br/>10-100m range<br/>High speed (1Gbps+)"]
    WAN["WAN: Multiple cities<br/>1000+ km range<br/>Lower speed"]
    
    style LAN fill:#E3F2FD,stroke:#1565C0
    style WAN fill:#FFF3E0,stroke:#E65100
```

---

## Diagram 3: How Internet Works - Data Path

```mermaid
sequenceDiagram
    participant Camera as CCTV Camera<br/>192.168.1.10
    participant NVR as NVR<br/>192.168.1.100
    participant Router as Home Router<br/>192.168.1.1
    participant ISP as ISP Network
    participant Cloud as Internet
    participant Mobile as Mobile App
    
    Camera->>NVR: Video Stream (RTSP)
    Note over Camera,NVR: H.265 encoded video<br/>via PoE cable
    
    NVR->>Router: Forward to Internet
    Note over NVR,Router: Router performs NAT<br/>192.168.1.100 → Public IP
    
    Router->>ISP: Send to ISP
    ISP->>Cloud: Route via Internet
    Cloud->>ISP: Forward to destination
    ISP->>Mobile: Deliver to Mobile App
    Note over ISP,Mobile: P2P or Cloud Relay<br/>via manufacturer server
    
    Mobile->>Cloud: Request video
    Cloud->>ISP: Forward request
    ISP->>Router: Deliver to router
    Router->>NVR: Forward (port forwarding)
    NVR->>Camera: Request stream
    Camera->>Mobile: Live video stream
```

---

## Diagram 4: IPv4 Address Structure

```
IPv4 Address: 192.168.1.100

┌─────────────────────────────────────────────────────────────────┐
│                    BINARY REPRESENTATION                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   192      .      168      .       1      .      100           │
│                                                                 │
│  11000000  .  10101000  .  00000001  .  01100100               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────┐  ┌────────────────────────────┐   │
│  │    NETWORK PORTION      │  │      HOST PORTION          │   │
│  │    (192.168.1)          │  │      (.100)                │   │
│  │    24 bits              │  │      8 bits                │   │
│  │    Subnet: 255.255.255.0│  │      Host ID: 100          │   │
│  └─────────────────────────┘  └────────────────────────────┘   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  SUBNET MASK: 255.255.255.0 (/24)                              │
│  • First 24 bits = 1s (network)                                │
│  • Last 8 bits = 0s (hosts)                                    │
│  • Supports 254 devices (192.168.1.1 - 192.168.1.254)          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Diagram 5: Subnetting for Multi-floor CCTV

```mermaid
graph TB
    subgraph Building["4-Story Building"]
        subgraph Floor4["Floor 4 - Admin"]
            F4_Switch[Switch]
            F4_Cam1[Camera 192.168.4.10]
            F4_Cam2[Camera 192.168.4.11]
            F4_PC[Office PC 192.168.4.50]
        end
        
        subgraph Floor3["Floor 3 - Warehouse"]
            F3_Switch[Switch]
            F3_Cam1[Camera 192.168.3.10]
            F3_Cam2[Camera 192.168.3.11]
        end
        
        subgraph Floor2["Floor 2 - Sales"]
            F2_Switch[Switch]
            F2_Cam1[Camera 192.168.2.10]
            F2_Cam2[Camera 192.168.2.11]
            F2_Cam3[Camera 192.168.2.12]
        end
        
        subgraph Floor1["Floor 1 - Reception"]
            F1_Switch[Switch]
            F1_Cam1[Camera 192.168.1.10]
            F1_Cam2[Camera 192.168.1.11]
            F1_Cam3[Camera 192.168.1.12]
            F1_Cam4[Camera 192.168.1.13]
        end
    end
    
    CoreSwitch[Core Switch<br/>192.168.0.1]
    Router[Router/Gateway<br/>192.168.0.254]
    NVR[NVR<br/>192.168.0.100]
    
    CoreSwitch --> Floor1
    CoreSwitch --> Floor2
    CoreSwitch --> Floor3
    CoreSwitch --> Floor4
    Router --> CoreSwitch
    NVR --> CoreSwitch
    
    style Floor1 fill:#E8F5E9,stroke:#2E7D32
    style Floor2 fill:#E3F2FD,stroke:#1565C0
    style Floor3 fill:#FFF3E0,stroke:#E65100
    style Floor4 fill:#F3E5F5,stroke:#6A1B9A
    style CoreSwitch fill:#f44336,color:#fff
    style NVR fill:#2196F3,color:#fff
```

**Subnet Table:**
| Floor | Subnet | Range | Devices |
|-------|--------|-------|---------|
| Floor 1 | 192.168.1.0/24 | .1 - .254 | 4 cameras, reception |
| Floor 2 | 192.168.2.0/24 | .1 - .254 | 3 cameras, sales team |
| Floor 3 | 192.168.3.0/24 | .1 - .254 | 2 cameras, warehouse |
| Floor 4 | 192.168.4.0/24 | .1 - .254 | 2 cameras, admin |

---

# CHAPTER 12 - BUSINESS MODEL

---

## Diagram 6: Access Control System Architecture

```mermaid
graph TB
    subgraph "Access Control System"
        Controller[Controller Board<br/>Main Unit]
        
        subgraph "Input Devices"
            Card1[Card Reader<br/>Front Door]
            Card2[Card Reader<br/>Back Door]
            Bio[Biometric Reader<br/>Server Room]
            ExitBtn[Exit Button<br/>All Doors]
            DoorSensor1[Door Sensor<br/>Front]
            DoorSensor2[Door Sensor<br/>Back]
        end
        
        subgraph "Output Devices"
            Lock1[Magnetic Lock<br/>Front Door]
            Lock2[Electric Strike<br/>Back Door]
            Lock3[Electromagnetic Lock<br/>Server Room]
            Alarm[Alarm Siren]
        end
        
        subgraph "Management"
            Server[Management Server<br/>Software]
            Log[Event Log Database]
        end
    end
    
    Card1 -->|Wiegand| Controller
    Card2 -->|Wiegand| Controller
    Bio -->|Wiegand/TCP| Controller
    ExitBtn -->|Dry Contact| Controller
    DoorSensor1 -->|Dry Contact| Controller
    DoorSensor2 -->|Dry Contact| Controller
    
    Controller -->|12V/24V| Lock1
    Controller -->|12V/24V| Lock2
    Controller -->|12V/24V| Lock3
    Controller -->|Relay| Alarm
    
    Controller -->|TCP/IP| Server
    Server --> Log
    
    style Controller fill:#f44336,color:#fff
    style Server fill:#2196F3,color:#fff
    style Lock1 fill:#FF9800,color:#fff
    style Lock2 fill:#FF9800,color:#fff
    style Lock3 fill:#FF9800,color:#fff
    style Alarm fill:#E91E63,color:#fff
```

---

## Diagram 7: Access Control Working Flow

```mermaid
flowchart TD
    Start([User Approaches Door]) --> Present{Present Credential}
    
    Present -->|Card| Reader1[Card Reader Reads Card]
    Present -->|Fingerprint| Reader2[Biometric Scans Finger]
    Present -->|Face| Reader3[Camera Captures Face]
    
    Reader1 --> Capture[Reader Sends ID to Controller]
    Reader2 --> Capture
    Reader3 --> Capture
    
    Capture --> Check{Controller Checks<br/>Database}
    
    Check -->|Found & Authorized| Time{Check Time Zone?}
    Check -->|Not Found| Deny1[Access Denied<br/>Unknown Card]
    Check -->|Found & Blocked| Deny2[Access Denied<br/>Blocked User]
    
    Time -->|Within Allowed Hours| Unlock[Unlock Door<br/>Activate Relay]
    Time -->|Outside Allowed Hours| Deny3[Access Denied<br/>Wrong Time]
    
    Unlock --> Log1[Log: Access Granted<br/>User ID, Time, Door]
    Deny1 --> Log2[Log: Access Denied<br/>Unknown Card]
    Deny2 --> Log3[Log: Access Denied<br/>Blocked User]
    Deny3 --> Log4[Log: Access Denied<br/>Wrong Time]
    
    Log1 --> Buzzer[Door Buzzer ON<br/>5 seconds]
    Buzzer --> Sensor{Door Opened?}
    
    Sensor -->|Yes| Wait[Wait for Door Close]
    Sensor -->|No| Alarm[Alarm: Door Forced]
    
    Wait --> Close[Door Closed<br/>Re-lock]
    Close --> End([End])
    Alarm --> End
    
    Log2 --> End
    Log3 --> End
    Log4 --> End
    
    style Start fill:#4CAF50,color:#fff
    style Unlock fill:#4CAF50,color:#fff
    style Deny1 fill:#f44336,color:#fff
    style Deny2 fill:#f44336,color:#fff
    style Deny3 fill:#f44336,color:#fff
    style Alarm fill:#E91E63,color:#fff
```

---

## Diagram 8: Controller Board Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ACCESS CONTROL CONTROLLER BOARD                  │
│                        (4-Door Controller)                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐    ┌──────────────────────────────────────────────┐  │
│  │ POWER    │    │                  STATUS LEDs                 │  │
│  │ INPUT    │    │  [PWR] [RUN] [COM] [DOOR1] [DOOR2] [DOOR3] │  │
│  │          │    │   ●     ●     ●      ●       ●       ●      │  │
│  │ 12V ●───┤    └──────────────────────────────────────────────┘  │
│  │ GND ●───┤                                                       │
│  └──────────┘                                                       │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    READER INPUTS (Wiegand)                  │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │   │
│  │  │ Reader 1 │  │ Reader 2 │  │ Reader 3 │  │ Reader 4 │   │   │
│  │  │ DATA0 ●  │  │ DATA0 ●  │  │ DATA0 ●  │  │ DATA0 ●  │   │   │
│  │  │ DATA1 ●  │  │ DATA1 ●  │  │ DATA1 ●  │  │ DATA1 ●  │   │   │
│  │  │ GND  ●   │  │ GND  ●   │  │ GND  ●   │  │ GND  ●   │   │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    DOOR RELAY OUTPUTS                       │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │   │
│  │  │ Door 1   │  │ Door 2   │  │ Door 3   │  │ Door 4   │   │   │
│  │  │ COM  ●   │  │ COM  ●   │  │ COM  ●   │  │ COM  ●   │   │   │
│  │  │ NO   ●   │  │ NO   ●   │  │ NO   ●   │  │ NO   ●   │   │   │
│  │  │ NC   ●   │  │ NC   ●   │  │ NC   ●   │  │ NC   ●   │   │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    AUXILIARY I/O                            │   │
│  │  [Exit Btn 1] [Exit Btn 2] [Door Sensor 1] [Door Sensor 2]│   │
│  │      ●              ●              ●              ●        │   │
│  │  [Alarm Out 1] [Alarm Out 2]   [RS485 A]   [RS485 B]      │   │
│  │      ●              ●              ●              ●        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐   │
│  │  Ethernet    │  │   Reset      │  │     Terminal Block     │   │
│  │  Port        │  │   Button     │  │     (Expansion)        │   │
│  │  [RJ45]      │  │   [●]        │  │     ● ● ● ● ● ●      │   │
│  └──────────────┘  └──────────────┘  └────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Diagram 9: Magnetic Lock Installation

```
                    MAGNETIC LOCK INSTALLATION
                    
     DOOR FRAME (Fixed)              DOOR (Movable)
    ┌───────────────────┐           ┌───────────────────┐
    │                   │           │                   │
    │   ┌───────────┐   │           │   ┌───────────┐   │
    │   │           │   │           │   │           │   │
    │   │ELECTRO-   │   │  ←0.5mm→  │   │ ARMATURE  │   │
    │   │MAGNET     │   │   GAP     │   │ PLATE     │   │
    │   │           │   │           │   │ (Steel)   │   │
    │   │  12V+ ────┼───┼─── Power Wires ───┼──── 12V+│   │
    │   │  GND  ────┼───┼───────────────────┼──── GND │   │
    │   │           │   │           │   │           │   │
    │   └───────────┘   │           │   └───────────┘   │
    │                   │           │                   │
    │   Mounting Holes  │           │   Mounting Bolt   │
    │   (4x screws)     │           │   (Counter-sunk)  │
    │                   │           │                   │
    └───────────────────┘           └───────────────────┘
    
    SPECIFICATIONS:
    ┌────────────────────────────────────────────────┐
    │ Holding Force:    600 lbs (272 kg)             │
    │ Operating Voltage: 12V DC                      │
    │ Current Draw:     480mA @ 12V                  │
    │ Gap:              Maximum 0.5mm                │
    │ Material:         Electromagnet + Steel Plate  │
    │ Certification:    UL, CE                       │
    └────────────────────────────────────────────────┘
    
    WIRING:
    ┌──────────────────┐         ┌──────────────────┐
    │  Controller Board │         │  Magnetic Lock   │
    │                  │         │                  │
    │  LOCK+ ●────────┼─────────┼──── ● 12V+       │
    │  LOCK- ●────────┼─────────┼──── ● GND        │
    │                  │         │                  │
    │  (NO Contact)    │         │  (Optional)      │
    │  COM ●──────────┼─────────┼──── ● Door Sensor│
    │  NO  ●──────────┼─────────┼──── ● (to alarm) │
    └──────────────────┘         └──────────────────┘
```

---

## Diagram 10: Boom Barrier System

```mermaid
graph TB
    subgraph "Boom Barrier System"
        Power[Power Supply<br/>24VDC / 220AC]
        Controller[Controller Board]
        Motor[Motor + Gearbox]
        Boom[Boom Arm<br/>3 meters]
        
        Loop[Loop Sensor<br/>Ground Induction]
        CardReader[Card Reader / Remote]
        LimitUp[Limiter Switch<br/>Full Open]
        LimitDown[Limiter Switch<br/>Full Close]
    end
    
    Power --> Controller
    Controller --> Motor
    Motor --> Boom
    Loop -->|Signal| Controller
    CardReader -->|Signal| Controller
    LimitUp -->|Signal| Controller
    LimitDown -->|Signal| Controller
    Controller -->|24V| Motor
    
    style Power fill:#4CAF50,color:#fff
    style Controller fill:#f44336,color:#fff
    style Motor fill:#FF9800,color:#fff
    style Boom fill:#2196F3,color:#fff
```

---

## Diagram 11: Boom Barrier Working Flow

```mermaid
flowchart TD
    Start([Vehicle Approaches]) --> Loop{Loop Sensor<br/>Detects Vehicle?}
    
    Loop -->|No| Wait[Wait]
    Wait --> Loop
    
    Loop -->|Yes| Auth{Authorization<br/>Check}
    
    Auth -->|Valid Card/Remote| Rise[Boom Arm Rises<br/>3-5 seconds]
    Auth -->|Invalid| Deny[Access Denied<br/>Arm Stays Down]
    
    Rise --> Open{Fully Open?<br/>Limit Switch}
    Open -->|No| Rise
    Open -->|Yes| Hold[Hold Open Position]
    
    Hold --> Pass[Vehicle Passes Through]
    Pass --> Clear{Loop Sensor<br/>Cleared?}
    
    Clear -->|No| Hold
    Clear -->|Yes| Delay[Auto-Close Delay<br/>5 seconds]
    
    Delay --> Close[Boom Arm Lowers<br/>3-5 seconds]
    Close --> Closed{Fully Closed?<br/>Limit Switch}
    
    Closed -->|No| Close
    Closed -->|Yes| End([Ready for Next Vehicle])
    
    Deny --> Alarm[Optional Alarm]
    Alarm --> End
    
    style Start fill:#4CAF50,color:#fff
    style Rise fill:#2196F3,color:#fff
    style Deny fill:#f44336,color:#fff
    style End fill:#4CAF50,color:#fff
```

---

## Diagram 14: Vehicle Loop Sensor in Ground

```
                    VEHICLE LOOP SENSOR INSTALLATION
                    
    TOP VIEW:
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │    Saw-cut groove (5mm wide x 50mm deep)                   │
    │    ┌─────────────────────────────────────────────────┐     │
    │    │                                                 │     │
    │    │    ┌─────────────────────────────────────┐     │     │
    │    │    │                                     │     │     │
    │    │    │         VEHICLE LOOP WIRE           │     │     │
    │    │    │         (4-6 turns)                 │     │     │
    │    │    │                                     │     │     │
    │    │    │    ┌───────────────────────┐       │     │     │
    │    │    │    │                       │       │     │     │
    │    │    │    │   DETECTION ZONE      │       │     │     │
    │    │    │    │   (Vehicle stops here)│       │     │     │
    │    │    │    │                       │       │     │     │
    │    │    │    └───────────────────────┘       │     │     │
    │    │    │                                     │     │     │
    │    │    └─────────────────────────────────────┘     │     │
    │    │                                                 │     │
    │    └─────────────────────────────────────────────────┘     │
    │                          │                                  │
    │                    Lead wires to                           │
    │                    Detector Unit                           │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    
    CROSS SECTION:
    
    Ground Level
    ═══════════════════════════════════════════════════════════════
    ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
    │ Sealant │  │ Sealant │  │ Sealant │  │ Sealant │  ← Polyurethane
    │ (filled)│  │ (filled)│  │ (filled)│  │ (filled)│    sealant
    └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘
         │            │            │            │
    ┌────┴────┐  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐
    │  Loop   │  │  Loop   │  │  Loop   │  │  Loop   │  ← Loop wire
    │  Wire   │  │  Wire   │  │  Wire   │  │  Wire   │    (insulated)
    │ (turn 1)│  │ (turn 2)│  │ (turn 3)│  │ (turn 4)│
    └─────────┘  └─────────┘  └─────────┘  └─────────┘
    
    ├─────────── 50mm depth ───────────┤
    ├──── 5mm width ────┤
    
    TO DETECTOR UNIT:
    ┌─────────────────────────────────────────┐
    │         LOOP DETECTOR UNIT              │
    │                                         │
    │  [Loop Input]  [Sensitivity] [Relay Out]│
    │      ●             ●             ●      │
    │                                         │
    │  LED: [POWER] [DETECT] [FAULT]         │
    │         ●        ●        ●            │
    └─────────────────────────────────────────┘
```

---

## Diagram 15: VDP System Overview

```mermaid
graph LR
    subgraph "OUTDOOR UNIT (Gate/Front Door)"
        Camera[Camera<br/>HD/2MP]
        CallBtn[Call Button]
        Speaker1[Speaker]
        Mic1[Microphone]
        IR[IR LEDs<br/>Night Vision]
        Housing[IP65 Housing<br/>Weatherproof]
    end
    
    subgraph "INDOOR UNIT (Living Room)"
        LCD[LCD Screen<br/>7 inch]
        Speaker2[Speaker]
        Mic2[Microphone]
        TalkBtn[Talk Button]
        OpenBtn[Open Door Button]
        MenuBtn[Menu Button]
    end
    
    subgraph "CONNECTION"
        Wire[5-Wire Cable / IP Network]
    end
    
    Camera -->|Video| Wire
    CallBtn -->|Signal| Wire
    Speaker1 <-->|Audio| Wire
    Mic1 -->|Audio| Wire
    
    Wire --> LCD
    Wire --> Speaker2
    Wire --> Mic2
    Wire --> TalkBtn
    Wire --> OpenBtn
    
    style Camera fill:#4CAF50,color:#fff
    style LCD fill:#2196F3,color:#fff
    style Wire fill:#FF9800,color:#fff
```

---

## Diagram 18: Wired VDP Connection

```
            WIRED VDP CONNECTION (5-WIRE SYSTEM)
            
┌──────────────────────┐                    ┌──────────────────────┐
│    OUTDOOR UNIT      │                    │    INDOOR UNIT       │
│                      │                    │                      │
│  ┌──────────────┐    │    5-WIRE CABLE    │  ┌──────────────┐    │
│  │   Camera     │    │                    │  │   LCD Screen │    │
│  └──────────────┘    │                    │  └──────────────┘    │
│                      │                    │                      │
│  ┌──────────────┐    │   ┌──────────┐    │  ┌──────────────┐    │
│  │ Call Button  │──┼──────│ RED      │────┼──│ Power Input  │    │
│  └──────────────┘    │   │ (12V)    │    │  └──────────────┘    │
│                      │   ├──────────┤    │                      │
│  ┌──────────────┐    │   │ BLACK    │    │  ┌──────────────┐    │
│  │  Speaker     │──┼──────│ (GND)   │────┼──│ Ground       │    │
│  └──────────────┘    │   ├──────────┤    │  └──────────────┘    │
│                      │   │ YELLOW   │    │                      │
│  ┌──────────────┐    │   │ (Video)  │    │  ┌──────────────┐    │
│  │  Microphone  │──┼──────│          │────┼──│ Video In     │    │
│  └──────────────┘    │   ├──────────┤    │  └──────────────┘    │
│                      │   │ WHITE    │    │                      │
│  ┌──────────────┐    │   │ (Audio)  │    │  ┌──────────────┐    │
│  │ IR LEDs      │    │   │          │    │  │ Audio In/Out │    │
│  └──────────────┘    │   ├──────────┤    │  └──────────────┘    │
│                      │   │ GREEN    │    │                      │
│  ┌──────────────┐    │   │ (Lock)   │    │  ┌──────────────┐    │
│  │  Lock Out    │──┼──────│          │────┼──│ Open Button  │    │
│  └──────────────┘    │   └──────────┘    │  └──────────────┘    │
│                      │                    │                      │
└──────────────────────┘                    └──────────────────────┘

WIRE COLOR CODE:
┌─────────┬────────────┬─────────────────────────┐
│ Color   │ Function   │ Voltage/Signal          │
├─────────┼────────────┼─────────────────────────┤
│ RED     │ Power      │ +12V DC (1A)            │
│ BLACK   │ Ground     │ 0V (Common)             │
│ YELLOW  │ Video      │ Composite Video (1Vpp)  │
│ WHITE   │ Audio      │ Bidirectional Audio     │
│ GREEN   │ Lock       │ Dry Contact / 12V       │
└─────────┴────────────┴─────────────────────────┘
```

---

## Diagram 19: IP VDP Network Connection

```mermaid
graph TB
    subgraph "IP VDP Network System"
        Router[Router<br/>192.168.1.1]
        PoE[PoE Switch<br/>192.168.1.2]
        
        subgraph "VDP Units"
            Outdoor[Outdoor VDP<br/>192.168.1.10]
            Indoor[Indoor Monitor<br/>192.168.1.11]
        end
        
        subgraph "Mobile Access"
            Phone1[Mobile App<br/>iOS/Android]
            Phone2[Second Phone]
        end
        
        Internet[Internet / WiFi]
    end
    
    Router --> PoE
    PoE -->|Ethernet| Outdoor
    PoE -->|Ethernet| Indoor
    Router --> Internet
    Internet -.->|WiFi/P2P| Phone1
    Internet -.->|WiFi/P2P| Phone2
    
    style Router fill:#4CAF50,color:#fff
    style PoE fill:#2196F3,color:#fff
    style Outdoor fill:#FF9800,color:#fff
    style Indoor fill:#FF9800,color:#fff
    style Phone1 fill:#9C27B0,color:#fff
    style Phone2 fill:#9C27B0,color:#fff
```

---

## Diagram 20: VDP + CCTV Integration

```mermaid
graph TB
    subgraph "CCTV System"
        Cam1[Camera 1]
        Cam2[Camera 2]
        Cam3[Camera 3]
        Cam4[Camera 4]
        NVR[NVR<br/>192.168.1.100]
    end
    
    subgraph "VDP System"
        VDP_Out[Outdoor VDP<br/>192.168.1.10]
        VDP_In[Indoor Monitor<br/>192.168.1.11]
    end
    
    subgraph "Network Infrastructure"
        PoE[PoE Switch 16-Port<br/>192.168.1.2]
        Router[Router<br/>192.168.1.1]
    end
    
    Cam1 -->|PoE| PoE
    Cam2 -->|PoE| PoE
    Cam3 -->|PoE| PoE
    Cam4 -->|PoE| PoE
    NVR -->|Ethernet| PoE
    VDP_Out -->|Ethernet| PoE
    VDP_In -->|Ethernet| PoE
    Router --> PoE
    
    NVR -.->|Recording| Cam1
    NVR -.->|Recording| Cam2
    NVR -.->|Recording| Cam3
    NVR -.->|Recording| Cam4
    
    style NVR fill:#f44336,color:#fff
    style VDP_Out fill:#FF9800,color:#fff
    style VDP_In fill:#FF9800,color:#fff
    style PoE fill:#2196F3,color:#fff
```

---

## Diagram 21: SLA Sample Document

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SERVICE LEVEL AGREEMENT (SLA)                    │
│                   CCTV Maintenance Contract                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CLIENT: _______________________    DATE: ___/___/______           │
│  SITE:   _______________________    CONTRACT #: _________          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  1. SCOPE OF SERVICE                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ • Preventive Maintenance: Quarterly                        │   │
│  │ • Corrective Maintenance: As needed                        │   │
│  │ • Remote Monitoring: 24/7                                   │   │
│  │ • Software Updates: Included                               │   │
│  │ • Spare Parts: Included (up to ₹5,000/year)               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  2. RESPONSE TIMES                                                  │
│  ┌────────────────┬──────────────┬──────────────┬──────────────┐   │
│  │ Priority       │ Response     │ Resolution   │ Escalation   │   │
│  ├────────────────┼──────────────┼──────────────┼──────────────┤   │
│  │ CRITICAL       │ 1 hour       │ 4 hours      │ Immediate    │   │
│  │ (Full system   │              │              │              │   │
│  │  down)         │              │              │              │   │
│  ├────────────────┼──────────────┼──────────────┼──────────────┤   │
│  │ MAJOR          │ 4 hours      │ 24 hours     │ 8 hours      │   │
│  │ (Multiple      │              │              │              │   │
│  │  cameras down) │              │              │              │   │
│  ├────────────────┼──────────────┼──────────────┼──────────────┤   │
│  │ MINOR          │ 24 hours     │ 72 hours     │ 48 hours     │   │
│  │ (Single camera │              │              │              │   │
│  │  issue)        │              │              │              │   │
│  └────────────────┴──────────────┴──────────────┴──────────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  3. PENALTIES                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ • Response time exceeded: 5% credit per incident           │   │
│  │ • Resolution time exceeded: 10% credit per incident       │   │
│  │ • Monthly uptime below 99%: 15% credit                    │   │
│  │ • Maximum credit: 30% of monthly fee                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  4. MONTHLY FEE: ₹ _____________                                   │
│                                                                     │
│  CLIENT SIGNATURE: _________________  DATE: ___/___/______         │
│  PROVIDER SIGNATURE: ________________ DATE: ___/___/______         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Diagram 22: Career Path Chart

```mermaid
graph TB
    Start([Starting Point]) --> Trainee
    
    Trainee[Trainee / Intern<br/>₹8,000 - 12,000/mo<br/>0-6 months]
    Junior[Junior Technician<br/>₹15,000 - 20,000/mo<br/>6-18 months]
    Tech[Technician<br/>₹25,000 - 35,000/mo<br/>1-3 years]
    Senior[Senior Technician<br/>₹40,000 - 55,000/mo<br/>3-5 years]
    Lead[Team Lead<br/>₹55,000 - 75,000/mo<br/>5-7 years]
    PM[Project Manager<br/>₹80,000 - 1,20,000/mo<br/>7-10 years]
    Owner[Business Owner<br/>₹1,50,000+/mo<br/>10+ years]
    
    Trainee -->|Learn basics| Junior
    Junior -->|Gain experience| Tech
    Tech -->|Specialize| Senior
    Senior -->|Lead teams| Lead
    Lead -->|Manage projects| PM
    PM -->|Start company| Owner
    
    style Trainee fill:#E3F2FD,stroke:#1565C0
    style Junior fill:#E8F5E9,stroke:#2E7D32
    style Tech fill:#FFF3E0,stroke:#E65100
    style Senior fill:#F3E5F5,stroke:#6A1B9A
    style Lead fill:#FCE4EC,stroke:#C62828
    style PM fill:#E0F7FA,stroke:#00695C
    style Owner fill:#FFF9C4,stroke:#F57F17
```

---

## Diagram 23: Company Growth Stages

```mermaid
graph LR
    subgraph "Stage 1: Solo Tech"
        S1[₹30,000/mo<br/>1 person<br/>Own tools]
    end
    
    subgraph "Stage 2: Solo + Helper"
        S2[₹60,000/mo<br/>2 people<br/>Basic inventory]
    end
    
    subgraph "Stage 3: Small Team"
        S3[₹2,00,000/mo<br/>5 people<br/>Company vehicle]
    end
    
    subgraph "Stage 4: Company"
        S4[₹10,00,000/mo<br/>20 people<br/>Office + warehouse]
    end
    
    subgraph "Stage 5: Enterprise"
        S5[₹50,00,000+/mo<br/>50+ people<br/>Multiple branches]
    end
    
    S1 -->|Hire helper| S2
    S2 -->|Hire 3 more| S3
    S3 -->|Scale up| S4
    S4 -->|Expand| S5
    
    style S1 fill:#E3F2FD,stroke:#1565C0
    style S2 fill:#E8F5E9,stroke:#2E7D32
    style S3 fill:#FFF3E0,stroke:#E65100
    style S4 fill:#F3E5F5,stroke:#6A1B9A
    style S5 fill:#FFF9C4,stroke:#F57F17
```

---

# CHAPTER 13 - PRACTICAL EXAMINATION

---

## Diagram 25: Network Test Topology

```mermaid
graph TB
    subgraph "Exam Network Setup"
        Router[Router<br/>192.168.1.1<br/>Gateway]
        Switch[PoE Switch<br/>192.168.1.2]
        
        subgraph "IP Cameras"
            CAM1[IP Camera 1<br/>192.168.1.10<br/>Dome - Entrance]
            CAM2[IP Camera 2<br/>192.168.1.11<br/>Bullet - Parking]
        end
        
        NVR[NVR<br/>192.168.1.100<br/>4-Ch]
        Monitor[Monitor<br/>HDMI Output]
        PC[Exam PC<br/>192.168.1.50<br/>Web Browser]
    end
    
    Router --> Switch
    Switch --> CAM1
    Switch --> CAM2
    Switch --> NVR
    Switch --> PC
    NVR --> Monitor
    
    CAM1 -.->|RTSP Stream| NVR
    CAM2 -.->|RTSP Stream| NVR
    PC -.->|Web Access| NVR
    PC -.->|Ping Test| CAM1
    PC -.->|Ping Test| CAM2
    
    style Router fill:#4CAF50,color:#fff
    style Switch fill:#2196F3,color:#fff
    style NVR fill:#f44336,color:#fff
    style CAM1 fill:#FF9800,color:#fff
    style CAM2 fill:#FF9800,color:#fff
    style PC fill:#9C27B0,color:#fff
```

**IP Assignment Table:**
| Device | IP Address | Subnet Mask | Gateway |
|--------|------------|-------------|---------|
| Router | 192.168.1.1 | 255.255.255.0 | - |
| PoE Switch | 192.168.1.2 | 255.255.255.0 | 192.168.1.1 |
| IP Camera 1 | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| IP Camera 2 | 192.168.1.11 | 255.255.255.0 | 192.168.1.1 |
| NVR | 192.168.1.100 | 255.255.255.0 | 192.168.1.1 |
| Exam PC | 192.168.1.50 | 255.255.255.0 | 192.168.1.1 |

---

# CHAPTER 14 - FEEDBACK & CERTIFICATION

---

## Diagram 26: Feedback to Improvement Cycle

```mermaid
graph TB
    Collect[1. Collect<br/>Feedback<br/>Forms]
    Analyze[2. Analyze<br/>Data &<br/>Responses]
    Gaps[3. Identify<br/>Gaps &<br/>Issues]
    Update[4. Update<br/>Curriculum<br/>& Materials]
    Implement[5. Implement<br/>Changes<br/>Next Batch]
    Recollect[6. Re-collect<br/>Feedback<br/>from New Batch]
    
    Collect --> Analyze
    Analyze --> Gaps
    Gaps --> Update
    Update --> Implement
    Implement --> Recollect
    Recollect --> Collect
    
    style Collect fill:#4CAF50,color:#fff
    style Analyze fill:#2196F3,color:#fff
    style Gaps fill:#FF9800,color:#fff
    style Update fill:#9C27B0,color:#fff
    style Implement fill:#f44336,color:#fff
    style Recollect fill:#00BCD4,color:#fff
```

---

# DIAGRAMS THAT NEED EXTERNAL TOOLS

These diagrams cannot be created in Mermaid/ASCII and require specialized tools:

| # | Diagram | Tool Needed | Why |
|---|---------|-------------|-----|
| 8 | Controller Board Layout | draw.io / Figma | Detailed PCB layout with labeled components |
| 12 | Boom Barrier Component Layout | draw.io / AutoCAD | Exploded view with dimensions |
| 13 | Foundation Dimensions | AutoCAD / draw.io | Precise cross-section with measurements |
| 16 | Outdoor Unit Anatomy | draw.io / Figma | Labeled product photo overlay |
| 17 | Indoor Monitor | draw.io / Figma | Labeled product photo overlay |
| 24 | Exam Station Layout | AutoCAD / draw.io | Floor plan with dimensions |

---

# SUMMARY

| Diagram # | Title | Format | Status |
|-----------|-------|--------|--------|
| 1 | LAN Network Layout | Mermaid | ✅ Done |
| 2 | LAN vs WAN Architecture | Mermaid | ✅ Done |
| 3 | Internet Data Path | Mermaid | ✅ Done |
| 4 | IPv4 Address Structure | ASCII Art | ✅ Done |
| 5 | Subnetting Multi-floor | Mermaid | ✅ Done |
| 6 | Access Control Architecture | Mermaid | ✅ Done |
| 7 | Access Control Working Flow | Mermaid | ✅ Done |
| 8 | Controller Board Layout | External | ❌ Need draw.io |
| 9 | Magnetic Lock Installation | ASCII Art | ✅ Done |
| 10 | Boom Barrier System | Mermaid | ✅ Done |
| 11 | Boom Barrier Working Flow | Mermaid | ✅ Done |
| 12 | Boom Barrier Component Layout | External | ❌ Need draw.io |
| 13 | Foundation Dimensions | External | ❌ Need AutoCAD |
| 14 | Vehicle Loop Sensor | ASCII Art | ✅ Done |
| 15 | VDP System Overview | Mermaid | ✅ Done |
| 16 | Outdoor Unit Anatomy | External | ❌ Need Figma |
| 17 | Indoor Monitor | External | ❌ Need Figma |
| 18 | Wired VDP Connection | ASCII Art | ✅ Done |
| 19 | IP VDP Network | Mermaid | ✅ Done |
| 20 | VDP + CCTV Integration | Mermaid | ✅ Done |
| 21 | SLA Sample | ASCII Art | ✅ Done |
| 22 | Career Path Chart | Mermaid | ✅ Done |
| 23 | Company Growth Stages | Mermaid | ✅ Done |
| 24 | Exam Station Layout | External | ❌ Need AutoCAD |
| 25 | Network Test Topology | Mermaid | ✅ Done |
| 26 | Feedback Cycle | Mermaid | ✅ Done |

**Created: 20 diagrams | Need External Tools: 6 diagrams**
