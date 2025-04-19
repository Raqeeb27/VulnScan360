# 🔍 VulnScan360

A powerful and modular Python-based CLI tool for network scanning, vulnerability detection, optional exploitation, and stylish PDF report generation — all from a single IP input.

---

## 📌 Project Vision

> "A Python-based CLI tool that performs network scans, identifies vulnerabilities, optionally runs exploits, and generates clean PDF reports — all with a single IP input."

---

## 🗂️ Project Structure

```
VulnScan360/
├── scan_engine/
│   ├── nmap_scanner.py          # Runs and parses Nmap
│   ├── vuln_finder.py           # CVE lookup using Vulners API or Searchsploit
│   └── exploit_module.py        # (Optional) Metasploit automation
│ 
├── report_generator/
│   ├── report_template.html     # Template report file
│   └── generate_report.py       # Converts data → Markdown → PDF
│ 
├── core/
│   └── main.py                  # CLI entry point
│ 
├── scan_engine/
│   └── generated-reports.pdf   
│ 
├── Utilities/
│   └── utilities for windows and linux   
│  
├── requirements.txt
│ 
├── README.md
│ 
└── .gitignore
```

---

## ⚙️ Tech Stack & Tools

| Function        | Tool                        |
|---------------- |-----------------------------|
| Scanning        | `Nmap` + `python-nmap`      |
| Vuln Discovery  | Vulners API / Searchsploit  |
| Exploitation    | Metasploit RPC (optional)   |
| Reporting       | Jinja2 + HTML + PDFKit      |
| CLI Interface   | `argparse`                  |
| Logging         | Python `logging` module     |

---

## 🚀 Features

✅ Full port and service version scan  
✅ CVE detection via Nmap Vulners script  
✅ Risk classification per service  
✅ Beautiful, color-coded PDF reports  
✅ (Coming soon) CVE enrichment via Vulners/Searchsploit  
✅ (Coming soon) Exploitation via Metasploit RPC  

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Raqeeb27/VulnScan360.git
cd VulnScan360
```

### 2. Install Dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
Install required packages:
```bash
pip install -r requirements.txt
```
### 3. Install External Tools

🔹 Nmap
Download Nmap and ensure it’s in your system PATH. Download [here](https://nmap.org/download.html)

🔹 Python
Download Python and ensure it’s in your system PATH. Download [here](https://www.python.org/downloads/)

🔹 wkhtmltopdf (for PDF generation)
Already included in the project, can be downloaded from: [here](https://wkhtmltopdf.org/downloads.html)

🔹 Metasploit Framework (Optional)
Install Metasploit

Enable and configure the RPC server for integration.

---

### 🧪 Usage
Basic Scan & Report (from project root directory)
```bash
python core/main.py --target 192.168.1.10
```
 - Performs a full Nmap scan

 - Parses service, version, CVE script output

 - Generates a styled PDF report in /scan_reports/

---

### 📄 Sample Report
The PDF includes:

IP summary & open ports

Risk-based color coding

CVE listings (if any)

Example:

Red border = High Risk  
Yellow = Medium Risk  
Green = Low Risk  

View sample generated pdf report [here](https://github.com/Raqeeb27/VulnScan360/tree/main/Utilities/sample_generated_report.pdf)

---

## 🔐 Ethical Disclaimer
This tool is intended for educational and authorized security testing purposes only.
Unauthorized scanning of systems without explicit permission is illegal and unethical.
Use responsibly.

---

### 📈 Roadmap
 🔍 Implement vuln_finder.py using Vulners API / Searchsploit

 💥 Add Metasploit RPC automation

 📬 Email reports to recipient

 🌐 Add multi-IP / CIDR range scanning

 📊 Summary charts (optional dashboard)

---

### 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

### 📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

### 🙌 Acknowledgements
Nmap  
Vulners  
wkhtmltopdf  
Metasploit
