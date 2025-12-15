# 🕵️ StealthScan - Advanced Red Team Network Reconnaissance Tool

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red.svg)](https://streamlit.io/)

---

## Overview

**StealthScan** is a professional-grade **red team reconnaissance and network analysis platform** built with **Streamlit**. It enables security professionals to upload **Wireshark PCAP files**, perform **stealth reconnaissance analysis**, apply **IPS/IDS evasion simulations**, and enrich findings with **real-time threat intelligence** from **VirusTotal** and **AbuseIPDB**.

Designed for **authorized penetration testers, red teamers, and cybersecurity analysts**, StealthScan transforms raw packet captures into actionable intelligence with minimal complexity.

---

## 🎯 Key Features

### Core Functionality
- **PCAP Upload & Validation** — Upload any Wireshark-captured PCAP or PCAPNG file
- **Network Traffic Analysis** — Automatic protocol distribution and endpoint profiling
- **Endpoint Intelligence** — Identify top communicating hosts and data flows
- **Stealth Scanning Simulation** — Apply realistic IPS/IDS evasion techniques

### Advanced Capabilities
- **Threat Intelligence Enrichment** — Cross-reference detected IPs with:
  - **VirusTotal** — Malware detection and reputation scoring
  - **AbuseIPDB** — Abuse confidence scores and geographic data
- **Evasion Engine** — Simulate and visualize:
  - Random packet delays
  - Packet obfuscation strategies
  - Port randomization tactics
- **Dynamic Report Generation** — Export comprehensive JSON intelligence reports

### User Experience
- **Web-Based UI** — No command-line required; works in any browser
- **Real-Time Visualization** — Charts, tables, and metrics update instantly
- **Non-Technical Friendly** — Intuitive interface for both technical and business stakeholders
- **Download Reports** — Export findings as JSON for further analysis or documentation

---

## 📋 System Architecture

```
StealthScan/
│
├── scanner/                          # Core scanning and intelligence logic
│   ├── __init__.py                   # Package initialization
│   ├── app.py                        # Streamlit UI orchestrator
│   ├── stealth_scan.py               # PCAP parser (Scapy-based)
│   ├── evasion.py                    # IPS/IDS evasion simulation engine
│   ├── threat_intel.py               # VirusTotal & AbuseIPDB integration
│   └── report.py                     # Report generation and export
│
├── utils/                            # Utility and helper modules
│   ├── __init__.py                   # Package initialization
│   ├── validators.py                 # PCAP file validation
│   └── visualization.py              # Streamlit UI components
│
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

---

## 🚀 Installation

### Prerequisites
- **Python 3.8+** installed
- **pip** package manager
- **VirusTotal API Key** (optional but recommended)
- **AbuseIPDB API Key** (optional but recommended)

### Step 1: Clone the Repository
```
git clone https://github.com/yourusername/StealthScan.git
cd StealthScan
```

### Step 2: Create Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Configure API Keys (Optional)
Set your threat intelligence API keys as environment variables:

- **Linux/macOS:**
export VT_API_KEY="your_virustotal_api_key_here"
export ABUSEIPDB_API_KEY="your_abuseipdb_api_key_here"

- **Windows (Command Prompt):**
set VT_API_KEY=your_virustotal_api_key_here
set ABUSEIPDB_API_KEY=your_abuseipdb_api_key_here

- **Windows (PowerShell):**
$env:VT_API_KEY="your_virustotal_api_key_here"
$env:ABUSEIPDB_API_KEY="your_abuseipdb_api_key_here"

### Step 5: Launch the Application
```
streamlit run scanner/app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 Usage Guide

### Basic Workflow

1. **Upload PCAP File**
   - Click the **"Upload PCAP"** button in the sidebar
   - Select a valid Wireshark PCAP or PCAPNG file
   - The tool validates the file automatically

2. **View Network Summary**
   - **Total Packets** metric shows packet count
   - **Top Endpoints** table displays communicating hosts and packet counts
   - **Protocol Distribution** chart shows protocol breakdown

3. **Run Stealth Analysis**
   - The **Stealth Evasion Analysis** section visualizes simulated evasion techniques
   - Each endpoint is assigned an **Evasion Score** (0.75–1.0)
   - Applied evasion modes include:
     - Random Delay
     - Packet Obfuscation
     - Port Randomization

4. **Check Threat Intelligence**
   - The tool automatically enriches the **top 5 endpoints** with:
     - **VirusTotal detection stats** (if API key configured)
     - **AbuseIPDB abuse confidence scores** (if API key configured)
   - Each result shows geographic, domain, and reputation data

5. **Download Report**
   - Click **"Download Full Intelligence Report"** button
   - Exports a comprehensive JSON file containing:
     - Network summary
     - Stealth evasion results
     - Full threat intelligence data
     - Timestamp of analysis

### Example Scenario

**Red Team Pre-Engagement:**
- Client provides a PCAP from their corporate network capture
- Upload PCAP → StealthScan identifies 47 endpoints
- Threat Intel identifies 3 IPs with VirusTotal malware detections
- Report exported and reviewed by team lead before engagement planning

---

## 🔑 API Configuration

### VirusTotal API
1. Create a free account at [virustotal.com](https://www.virustotal.com/)
2. Navigate to **API section** and copy your API key
3. Set environment variable: `VT_API_KEY`

### AbuseIPDB API
1. Create a free account at [abuseipdb.com](https://www.abuseipdb.com/)
2. Generate API key from **Account Settings**
3. Set environment variable: `ABUSEIPDB_API_KEY`

**Note:** Without API keys, the tool still functions fully but threat intelligence features will return error messages.

---

## 📊 Output Examples

### Network Summary
Total Packets: 12,847
Top Endpoints:
  192.168.1.10    3,421
  10.0.0.5        2,156
  172.16.0.8      1,897

### Threat Intelligence Result
{
  "ip": "192.168.1.10",
  "virustotal": {
    "detection_stats": {
      "malicious": 2,
      "suspicious": 1,
      "undetected": 65
    }
  },
  "abuseipdb": {
    "abuseConfidenceScore": 45,
    "countryCode": "US",
    "domain": "example.com"
  }
}

### Downloaded Report
Comprehensive JSON file including:
- Full scan summary
- Stealth evasion results for each endpoint
- Complete threat intelligence enrichment
- Generation timestamp

---

## 🛡️ Security & Ethical Use

### Intended Use
- **Authorized Penetration Testing** — With written permission from asset owner
- **Red Team Operations** — As part of approved adversarial simulation exercises
- **Security Research** — Academic and professional cybersecurity analysis
- **Blue Team Training** — Defensive simulation and threat hunting exercises

### Prohibited Use
- Scanning or analyzing networks **without explicit authorization**
- Reverse engineering of network protocols for malicious intent
- Use in any **illegal cyber operations**
- Distribution of threat intelligence for harmful purposes

**⚠️ Disclaimer:** The authors of StealthScan are **NOT responsible** for any misuse, damage, or legal consequences arising from unauthorized use of this tool. Users are solely responsible for ensuring their activities comply with all applicable laws and regulations.

---

## 🔧 Troubleshooting

### Issue: "Import 'streamlit' could not be resolved"
**Solution:** Ensure Streamlit is installed:
- ```pip install streamlit```
Restart your IDE to reload modules.

### Issue: "Import 'utils' could not be resolved"
**Solution:** Run the application from the project root:
- cd /path/to/StealthScan
- streamlit run scanner/app.py
- Or add this to the top of `scanner/app.py`:
```
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```
### Issue: "Invalid PCAP file"
**Solution:** Ensure the uploaded file is:
- Captured by Wireshark or tcpdump
- In PCAP or PCAPNG format
- Not corrupted (try re-capturing the network traffic)

### Issue: Threat Intelligence returns "API key not configured"
**Solution:** Set environment variables before launching:
- export VT_API_KEY="your_key"
- export ABUSEIPDB_API_KEY="your_key"
- streamlit run scanner/app.py

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | ≥1.0 | Web UI framework |
| `scapy` | ≥2.4.5 | PCAP parsing and network packet analysis |
| `pandas` | ≥1.0 | Data manipulation and visualization |
| `requests` | ≥2.25 | HTTP requests for API calls |

---

## 🏗️ Project Roadmap

### Current Version (v1.0)
- ✅ PCAP upload and validation
- ✅ Network traffic analysis
- ✅ Stealth evasion simulation
- ✅ VirusTotal & AbuseIPDB integration
- ✅ JSON report generation

### Planned Features (v1.1+)
- **MITRE ATT&CK Mapping** — Correlate detected indicators with tactics and techniques
- **Shodan Integration** — Port and service enrichment
- **Geolocation Mapping** — Visual world map of detected endpoints
- **Automated Anomaly Detection** — ML-based detection of beaconing and exfiltration
- **Custom Rules Engine** — Define custom reconnaissance patterns
- **Multi-file Analysis** — Compare multiple PCAPs over time
- **Dark Mode UI** — Enhanced visibility in low-light environments

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/your-feature`
3. **Commit changes:** `git commit -m "Add your feature"`
4. **Push to branch:** `git push origin feature/your-feature`
5. **Open a Pull Request**

### Code Standards
- Follow **PEP 8** naming conventions
- Add **docstrings** to all functions
- Include **type hints** where possible
- Write **unit tests** for new features

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

**Short Summary:** You are free to use, modify, and distribute StealthScan, provided you include the original license and copyright notice.

---

## 👨‍💻 Author

**Mangesh**  
Junior Cybersecurity & Software Developer  
Specialization: Red Team Operations, Bug Bounty Hunting, Network Security  

**Contact:**
- GitHub: [@mangesh-bhattacharya](https://github.com/mangesh-bhattacharya)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/mangesh-bhattacharya)

---

## 🙏 Acknowledgments

- **Scapy Team** — For the powerful packet manipulation library
- **Streamlit** — For the intuitive web framework
- **VirusTotal** — For threat intelligence API
- **AbuseIPDB** — For IP reputation data
- **OWASP & MITRE** — For security frameworks and standards

---

## ❓ FAQ

**Q: Can I use StealthScan on networks I don't own?**  
A: No. You must have explicit written permission from the network owner before using StealthScan for any analysis.

**Q: Does StealthScan perform active scanning?**  
A: No. StealthScan is **passive-only**. It analyzes pre-captured PCAP files without generating network traffic.

**Q: What if I don't have API keys?**  
A: The tool functions fully without them. Threat intelligence enrichment simply returns error messages, but all other features work.

**Q: Can I integrate StealthScan with my SIEM?**  
A: Yes. Export the JSON report and ingest it into your SIEM platform or custom workflow automation tools (e.g., n8n, Zapier).

**Q: Is StealthScan detectable by IDS/IPS?**  
A: No. StealthScan is passive and does not generate network traffic. It only analyzes existing PCAP files.

---

## 📞 Support

For issues, questions, or feature requests, please open an **Issue** on the GitHub repository or contact the author directly.

---

**Last Updated:** December 14, 2025  
**Version:** 1.0.0  
**Status:** Production-Ready
