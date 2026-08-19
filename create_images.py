import os

output_dir = r'C:\Users\Lenovo\Desktop\CCTV_Installation_Manual\images'

# The 25 missing images as described in README.md
images = {
    "old_vs_modern_cctv.svg": "Old CRT vs Modern LCD/IP CCTV / पुराना CRT बनाम आधुनिक LCD/IP CCTV",
    "analog_system_setup.svg": "Analog CCTV System Setup / एनालॉग CCTV सिस्टम सेटअप",
    "varifocal_camera.svg": "Varifocal Camera with Zoom Rings / वेरिफोकल कैमरा ज़ूम रिंग्स के साथ",
    "compression_comparison.svg": "H.264 vs H.265 Compression / H.264 बनाम H.265 कंप्रेशन",
    "ip_camera_types.svg": "IP Camera Types Comparison / IP कैमरा प्रकार तुलना",
    "troubleshooting_flowchart.svg": "Troubleshooting Flowchart / ट्रबलशूटिंग फ्लोचार्ट",
    "clear_vs_fuzzy_video.svg": "Clear vs Fuzzy Video / स्पष्ट बनाम धुंधला वीडियो",
    "rolling_lines.svg": "Horizontal Rolling Lines / क्षैतिज रोलिंग लाइनें",
    "bw_mode_issue.svg": "Camera B&W Mode Issue / कैमरा B&W मोड समस्या",
    "ghosting_effect.svg": "Video Ghosting Effect / वीडियो घोस्टिंग प्रभाव",
    "blue_screen.svg": "Blue Screen No Signal / ब्लू स्क्रीन नो सिग्नल",
    "day_night_comparison.svg": "Day vs Night Camera Mode / दिन बनाम रात कैमरा मोड",
    "compression_artifacts.svg": "Compression Artifacts / कंप्रेशन आर्टिफैक्ट्स",
    "dead_camera.svg": "Camera No Power LED / कैमरा कोई पावर LED नहीं",
    "led_blink_pattern.svg": "LED Blink Pattern / LED ब्लिंक पैटर्न",
    "ping_failure.svg": "Command Prompt Ping Failure / कमांड प्रॉम्प्ट पिंग फेल",
    "focus_issue.svg": "Focused vs Blurry Camera View / फोकस्ड बनाम धुंधला कैमरा व्यू",
    "ir_reflection.svg": "IR Reflection Glare / IR परावर्तन ग्लेयर",
    "wrong_day_night.svg": "Incorrect Day/Night Mode / गलत दिन/रात मोड",
    "overheating_warning.svg": "Camera Overheating Warning / कैमरा ओवरहीटिंग चेतावनी",
    "quotation_template.svg": "Professional Quotation Template / पेशेवर कोटेशन टेम्पलेट",
    "access_control_board.svg": "Access Control Board / एक्सेस कंट्रोल बोर्ड",
    "access_install_steps.svg": "Access Control Installation / एक्सेस कंट्रोल इंस्टॉलेशन",
    "outdoor_unit.svg": "Video Door Phone Outdoor Unit / वीडियो डोर फोन आउटडोर यूनिट",
    "indoor_monitor.svg": "Video Door Phone Indoor Monitor / वीडियो डोर फोन इंडोर मॉनिटर"
}

for filename, desc in images.items():
    # Create a simple technical SVG
    svg_content = f"""<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#ffffff" stroke="#333333" stroke-width="2"/>
  <rect x="10" y="10" width="580" height="380" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  
  <!-- Placeholder Icon -->
  <rect x="225" y="100" width="150" height="150" rx="12" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
  <text x="300" y="185" fill="#64748b" font-family="sans-serif" font-size="48" text-anchor="middle">📷</text>
  
  <!-- Description -->
  <text x="300" y="300" fill="#1e293b" font-family="sans-serif" font-size="14" text-anchor="middle" font-weight="bold">{desc}</text>
  
  <!-- Status Badge -->
  <rect x="225" y="320" width="150" height="30" rx="15" fill="#e2e8f0"/>
  <text x="300" y="340" fill="#475569" font-family="sans-serif" font-size="10" text-anchor="middle">PLACEHOLDER - REPLACE WITH REAL IMAGE</text>
</svg>"""
    
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created {filename}")

print(f"\nTotal {len(images)} images created.")
