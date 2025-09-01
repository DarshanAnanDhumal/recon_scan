# Network Reconnaissance Scanner

A comprehensive Python tool for automated network reconnaissance and service enumeration during penetration testing engagements.

## Features

- Multi-threaded port scanning for speed
- Service detection and banner grabbing
- Version fingerprinting
- Professional HTML and JSON report generation
- Customizable scan parameters

## Installation

```bash
git clone https://github.com/yourusername/network-recon-scanner.git
cd network-recon-scanner
pip install -r requirements.txt

Usage
Basic scan:
python main.py <target>

Advanced scan with custom ports:
python main.py <target> -p 1-65535 -t 100 -o scan_report

parameterstarget: Target IP address-p, --ports: Port range (default: 1-1000)-t, --threads: Number of threads (default: 50)-o, --output: Output filename for reports--timeout: Connection timeout in secondsLegal NoticeThis tool is for authorized penetration testing and educational purposes only. Users are responsible for complying with applicable laws and regulations.

