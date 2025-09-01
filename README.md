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