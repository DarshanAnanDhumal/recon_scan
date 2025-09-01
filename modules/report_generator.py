import json
from datetime import datetime
import os

class ReportGenerator:
    def generate_report(self, data, filename):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = {
            'scan_info': {
                'timestamp': timestamp,
                'target': data['target'],
                'total_ports_scanned': len(data['scan_parameters']['ports'].split('-')),
                'open_ports_found': len(data['open_ports'])
            },
            'results': {
                'open_ports': data['open_ports'],
                'services': data['services']
            },
            'scan_parameters': data['scan_parameters']
        }
        
        # Create reports directory if it doesn't exist
        os.makedirs('reports', exist_ok=True)
        
        # Save JSON report
        json_file = f"reports/{filename}.json"
        with open(json_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Generate HTML report
        html_file = f"reports/{filename}.html"
        self._generate_html_report(report, html_file)
        
        print(f"[+] Reports generated: {json_file}, {html_file}")
    
    def _generate_html_report(self, data, filename):
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Network Reconnaissance Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #2c3e50; color: white; padding: 20px; }}
                .summary {{ background-color: #ecf0f1; padding: 15px; margin: 20px 0; }}
                .port {{ margin: 10px 0; padding: 10px; border-left: 4px solid #3498db; }}
                .service {{ font-weight: bold; color: #2980b9; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Network Reconnaissance Report</h1>
                <p>Target: {data['scan_info']['target']} | Scan Time: {data['scan_info']['timestamp']}</p>
            </div>
            
            <div class="summary">
                <h2>Scan Summary</h2>
                <p><strong>Open Ports Found:</strong> {data['scan_info']['open_ports_found']}</p>
                <p><strong>Total Ports Scanned:</strong> {data['scan_info']['total_ports_scanned']}</p>
            </div>
            
            <h2>Detailed Results</h2>
        """
        
        for port, service_info in data['results']['services'].items():
            html_content += f"""
            <div class="port">
                <span class="service">Port {port}: {service_info['service']}</span><br>
                <strong>Version:</strong> {service_info['version']}<br>
                <strong>Banner:</strong> {service_info['banner'][:100]}...
            </div>
            """
        
        html_content += "</body></html>"
        
        with open(filename, 'w') as f:
            f.write(html_content)
    
    def print_summary(self, data):
        print("\n" + "="*50)
        print("SCAN SUMMARY")
        print("="*50)
        print(f"Target: {data['target']}")
        print(f"Open Ports: {len(data['open_ports'])}")
        print(f"Services Detected: {len(data['services'])}")
        print("\nDETAILED RESULTS:")
        print("-"*30)
        
        for port, service_info in data['services'].items():
            print(f"Port {port}: {service_info['service']}")
            print(f"  Version: {service_info['version']}")
            print(f"  Banner: {service_info['banner'][:80]}...")
            print()