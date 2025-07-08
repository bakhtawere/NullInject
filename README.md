# NullInject

**NullInject** is a professional-grade payload generation tool built during the Offensive Security Internship at ITSOLERA Pvt Ltd. It assists penetration testers and security researchers by generating modular, evasion-ready payloads for common web vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (SQLi), and Command Injection.

---

## Project Objective

To develop a modular, GUI-based payload generator capable of producing bypass-ready payloads with support for encoding, exporting, and simulated integration with tools such as Burp Suite and OWASP ZAP.

---

## Features

- Modular payload generators:
  - Cross-Site Scripting (Reflected, Stored, DOM-Based)
  - SQL Injection (Error-based, Union-based, Blind)
  - Command Injection (Linux and Windows variants)
- Encoding support:
  - Base64
  - URL encoding
  - Hexadecimal
- Export functionality:
  - JSON file
  - Clipboard copy
- Simulated integration with:
  - Burp Suite Repeater API
  - OWASP ZAP Scanner

---

## Folder Structure

```
NullInject/
├── gui/                  # Graphical User Interface (Tkinter)
│   └── gui.py
├── modules/              # Payload generators
│   ├── xss.py
│   ├── sqli.py
│   └── cmdinj.py
├── utils/                # Encoders, exporters, integrations
│   ├── encoder.py
│   ├── exporter.py
│   ├── burp_integration.py
│   └── zap_integration.py
├── output/               # JSON payload exports
├── docs/screenshots/     # GUI screenshots
├── samples/              # Sample payloads
│   ├── xss/
│   ├── sqli/
│   └── cmd/
├── main.py               # Entry point
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Linux (Ubuntu/Kali recommended) or WSL (for Windows)
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
```

---

## Running the Tool

```bash
python main.py
```

---

## GUI Preview

Make sure you've placed a screenshot in:
```
C:\Users\HP\Pictures\Screenshots\gui.png
```

Then, this will display the image on GitHub:

```markdown
![GUI Screenshot](docs/screenshots/gui.png)
```

---

## Burp Suite and ZAP Integration (Simulated)

This version includes simulated API calls for:

- `utils/burp_integration.py`
- `utils/zap_integration.py`

These do not require Burp/ZAP to be installed but can be extended for real-world usage.

---

## Sample Payloads

### XSS

```html
<script>alert(1)</script>
<svg/onload=confirm(1)>
<iframe srcdoc="<script>alert(1)</script>"></iframe>
```

### SQLi

```sql
' OR 1=1-- -
' UNION SELECT username, password FROM users-- -
' AND 1=CONVERT(int,@@version)-- -
```

### Command Injection

```bash
; id
&& cat /etc/passwd
| net user
```

---

## Export Options

- Export payload to a `.json` file in `output/`
- Copy payload directly to clipboard

---

## License

This tool was created as part of a student internship project. It is intended strictly for educational and authorized security testing purposes.

---

## Disclaimer

Unauthorized use of this tool is prohibited. The author is not responsible for any misuse or damage resulting from its usage.

---

