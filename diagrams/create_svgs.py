import os

output_dir = r'C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\diagrams'

diagrams = {
    "foundation_dimensions.svg": """<svg width="1200" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1a1a2e"/>
  <text x="600" y="50" fill="white" font-family="sans-serif" font-size="24" text-anchor="middle">Foundation Dimensions / फाउंडेशन डाइमेंशन</text>
  
  <!-- Ground -->
  <rect x="100" y="200" width="1000" height="400" fill="#2d2d4a" stroke="#6366f1" stroke-width="2"/>
  <text x="600" y="230" fill="#fbbf24" font-size="16" text-anchor="middle">Ground Level / जमीन का स्तर</text>
  
  <!-- Foundation Pit -->
  <rect x="300" y="250" width="600" height="300" fill="#363654" stroke="#818cf8" stroke-width="2"/>
  <text x="600" y="410" fill="white" font-size="20" text-anchor="middle">M20 Concrete / M20 कंक्रीट</text>
  
  <!-- Dimensions -->
  <line x1="280" y1="250" x2="280" y2="550" stroke="#34d399" stroke-width="2"/>
  <text x="260" y="410" fill="#34d399" font-size="14" text-anchor="end" transform="rotate(-90 260 410)">50cm Depth</text>
  
  <line x1="300" y1="570" x2="900" y2="570" stroke="#34d399" stroke-width="2"/>
  <text x="600" y="590" fill="#34d399" font-size="14" text-anchor="middle">60cm Length</text>
  
  <!-- Base Plate -->
  <rect x="350" y="200" width="500" height="20" fill="#f87171" stroke="white" stroke-width="1"/>
  <text x="600" y="195" fill="white" font-size="12" text-anchor="middle">Base Plate / बेस प्लेट</text>
  
  <!-- Anchor Bolts -->
  <line x1="400" y1="150" x2="400" y2="250" stroke="white" stroke-width="4"/>
  <line x1="800" y1="150" x2="800" y2="250" stroke="white" stroke-width="4"/>
  <text x="400" y="140" fill="white" font-size="12" text-anchor="middle">Anchor Bolt</text>
  
  <!-- Conduit -->
  <rect x="580" y="450" width="40" height="100" fill="#fbbf24" opacity="0.5"/>
  <text x="600" y="520" fill="white" font-size="10" text-anchor="middle">PVC Conduit</text>
</svg>""",

    "outdoor_unit_anatomy.svg": """<svg width="1200" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1a1a2e"/>
  <text x="600" y="50" fill="white" font-family="sans-serif" font-size="24" text-anchor="middle">VDP Outdoor Unit / वीडियो डोर फोन आउटडोर यूनिट</text>
  
  <!-- Main Body -->
  <rect x="400" y="100" width="400" height="600" rx="20" fill="#363654" stroke="#818cf8" stroke-width="3"/>
  
  <!-- Camera -->
  <circle cx="600" cy="200" r="60" fill="#0f0f1a" stroke="#6366f1" stroke-width="2"/>
  <circle cx="600" cy="200" r="30" fill="#252542" stroke="#818cf8" stroke-width="1"/>
  <text x="600" y="280" fill="white" font-size="14" text-anchor="middle">Camera / कैमरा</text>
  
  <!-- IR LEDs -->
  <circle cx="520" cy="180" r="10" fill="#f87171"/>
  <circle cx="680" cy="180" r="10" fill="#f87171"/>
  <text x="750" y="185" fill="#f87171" font-size="12">IR LEDs</text>
  
  <!-- Call Button -->
  <circle cx="600" cy="400" r="50" fill="#34d399" stroke="white" stroke-width="2"/>
  <text x="600" y="405" fill="white" font-size="24" text-anchor="middle">CALL</text>
  <text x="600" y="470" fill="white" font-size="14" text-anchor="middle">Call Button / कॉल बटन</text>
  
  <!-- Speaker -->
  <rect x="450" y="550" width="300" height="60" fill="#2d2d4a" stroke="#4a4a6a" stroke-width="1"/>
  <text x="600" y="585" fill="#9090a8" font-size="12" text-anchor="middle">Speaker / स्पीकर</text>
  
  <!-- Mic -->
  <circle cx="600" cy="500" r="5" fill="#9090a8"/>
  <text x="620" y="505" fill="#9090a8" font-size="10">Mic</text>
  
  <!-- Labels -->
  <text x="150" y="200" fill="#fbbf24" font-size="16">IP65 Weatherproof Housing</text>
  <text x="150" y="220" fill="#9090a8" font-size="12">IP65 मौसम प्रतिरोधी हाउसिंग</text>
  
  <text x="900" y="400" fill="#fbbf24" font-size="16">Viewing Angle: 120°</text>
  <path d="M 600 200 L 200 500 M 600 200 L 1000 500" stroke="#6366f1" stroke-width="1" stroke-dasharray="5,5" fill="none"/>
</svg>""",

    "indoor_monitor.svg": """<svg width="1200" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1a1a2e"/>
  <text x="600" y="50" fill="white" font-family="sans-serif" font-size="24" text-anchor="middle">VDP Indoor Monitor / वीडियो डोर फोन इंडोर मॉनिटर</text>
  
  <!-- Main Body -->
  <rect x="350" y="100" width="500" height="600" rx="10" fill="#2d2d4a" stroke="#6366f1" stroke-width="2"/>
  
  <!-- Screen -->
  <rect x="380" y="130" width="440" height="350" fill="#0f0f1a" stroke="#34d399" stroke-width="2"/>
  <text x="600" y="300" fill="#34d399" font-size="20" text-anchor="middle">7-inch LCD Screen</text>
  <text x="600" y="320" fill="#9090a8" font-size="14" text-anchor="middle">7 इंच एलसीडी स्क्रीन</text>
  
  <!-- Speaker -->
  <rect x="450" y="500" width="300" height="40" fill="#363654"/>
  <text x="600" y="525" fill="#9090a8" font-size="12" text-anchor="middle">Speaker</text>
  
  <!-- Buttons -->
  <rect x="400" y="560" width="120" height="60" rx="8" fill="#34d399"/>
  <text x="460" y="595" fill="white" font-size="14" text-anchor="middle">Talk</text>
  
  <rect x="540" y="560" width="120" height="60" rx="8" fill="#f87171"/>
  <text x="600" y="595" fill="white" font-size="14" text-anchor="middle">Unlock</text>
  
  <rect x="680" y="560" width="120" height="60" rx="8" fill="#363654"/>
  <text x="740" y="595" fill="white" font-size="14" text-anchor="middle">Menu</text>
  
  <!-- Ports -->
  <text x="150" y="600" fill="#fbbf24" font-size="14">Ports: 12V DC, Ethernet, USB</text>
</svg>""",

    "exam_station_layout.svg": """<svg width="1200" height="800" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1a1a2e"/>
  <text x="600" y="50" fill="white" font-family="sans-serif" font-size="24" text-anchor="middle">Exam Station Layout / परीक्षा स्टेशन लेआउट</text>
  
  <!-- Floor Plan -->
  <rect x="200" y="100" width="800" height="600" fill="#2d2d4a" stroke="#6366f1" stroke-width="2"/>
  <text x="600" y="130" fill="#9090a8" font-size="14" text-anchor="middle">Exam Room / परीक्षा कक्ष</text>
  
  <!-- Cameras -->
  <circle cx="250" cy="150" r="20" fill="#34d399"/>
  <text x="250" y="155" fill="white" font-size="10" text-anchor="middle">Cam 1</text>
  
  <circle cx="950" cy="150" r="20" fill="#34d399"/>
  <text x="950" y="155" fill="white" font-size="10" text-anchor="middle">Cam 2</text>
  
  <circle cx="250" cy="650" r="20" fill="#34d399"/>
  <text x="250" y="655" fill="white" font-size="10" text-anchor="middle">Cam 3</text>
  
  <!-- Workstation -->
  <rect x="500" y="300" width="200" height="100" fill="#363654"/>
  <text x="600" y="350" fill="white" font-size="14" text-anchor="middle">DVR + Monitor</text>
  
  <!-- Tools -->
  <rect x="750" y="450" width="150" height="80" fill="#363654"/>
  <text x="825" y="490" fill="#fbbf24" font-size="12" text-anchor="middle">Tool Box</text>
  
  <!-- Cable Route -->
  <path d="M 250 170 L 250 350 L 500 350" stroke="#f87171" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="350" y="340" fill="#f87171" font-size="12">Cable Route</text>
</svg>"""
}

for filename, content in diagrams.items():
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")
