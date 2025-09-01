#!/usr/bin/env python3
"""
Network Reconnaissance Scanner
A comprehensive tool for network discovery and service enumeration
Author: Darshana Dhumal
"""

import argparse
import sys
import json
from modules.port_scanner import PortScanner
from modules.service_detector import ServiceDetector
from modules.report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description='Network Reconnaissance Scanner')
    parser.add_argument('target', help='Target IP address or range')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range (default: 1-1000)')
    parser.add_argument('-t', '--threads', type=int, default=50, help='Number of threads (default: 50)')
    parser.add_argument('-o', '--output', help='Output file for report')
    parser.add_argument('--timeout', type=int, default=3, help='Connection timeout (default: 3)')
    
    args = parser.parse_args()
    
    print(f"[+] Starting reconnaissance scan on {args.target}")
    print(f"[+] Port range: {args.ports}")
    print(f"[+] Threads: {args.threads}")
    print("-" * 50)
    
    # Initialize scanner
    scanner = PortScanner(args.target, args.ports, args.threads, args.timeout)
    
    # Perform port scan
    open_ports = scanner.scan()
    
    if not open_ports:
        print("[-] No open ports found")
        return
    
    print(f"[+] Found {len(open_ports)} open ports")
    
    # Service detection
    detector = ServiceDetector()
    services = detector.detect_services(args.target, open_ports)
    
    # Generate report
    report_gen = ReportGenerator()
    report_data = {
        'target': args.target,
        'open_ports': open_ports,
        'services': services,
        'scan_parameters': vars(args)
    }
    
    if args.output:
        report_gen.generate_report(report_data, args.output)
        print(f"[+] Report saved to {args.output}")
    else:
        report_gen.print_summary(report_data)

if __name__ == "__main__":
    main()