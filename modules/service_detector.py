import socket
import re

class ServiceDetector:
    def __init__(self):
        self.common_services = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            993: 'IMAPS',
            995: 'POP3S',
            3389: 'RDP',
            5432: 'PostgreSQL',
            3306: 'MySQL'
        }
    
    def detect_services(self, target, ports):
        services = {}
        
        for port in ports:
            service_info = self._detect_service(target, port)
            services[port] = service_info
            print(f"[+] Port {port}: {service_info['service']} - {service_info['banner'][:50]}...")
        
        return services
    
    def _detect_service(self, target, port):
        service = self.common_services.get(port, 'Unknown')
        banner = self._grab_banner(target, port)
        
        return {
            'service': service,
            'banner': banner,
            'version': self._extract_version(banner)
        }
    
    def _grab_banner(self, target, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, port))
            
            # Send HTTP request for web services
            if port in [80, 443, 8080, 8443]:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            return banner
        except:
            return "No banner retrieved"
    
    def _extract_version(self, banner):
        version_patterns = [
            r'Server: ([^\r\n]+)',
            r'OpenSSH_([0-9.]+)',
            r'Apache/([0-9.]+)',
            r'nginx/([0-9.]+)'
        ]
        
        for pattern in version_patterns:
            match = re.search(pattern, banner, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return "Unknown"