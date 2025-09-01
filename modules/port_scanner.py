import socket
import threading
from concurrent.futures import ThreadPoolExecutor
import ipaddress

class PortScanner:
    def __init__(self, target, port_range, threads=50, timeout=3):
        self.target = target
        self.port_range = self._parse_port_range(port_range)
        self.threads = threads
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()
    
    def _parse_port_range(self, port_range):
        if '-' in port_range:
            start, end = map(int, port_range.split('-'))
            return list(range(start, end + 1))
        elif ',' in port_range:
            return [int(p.strip()) for p in port_range.split(',')]
        else:
            return [int(port_range)]
    
    def _scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    print(f"[+] Port {port}: OPEN")
            
            sock.close()
        except Exception as e:
            pass
    
    def scan(self):
        print(f"[+] Scanning {len(self.port_range)} ports...")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self._scan_port, self.port_range)
        
        self.open_ports.sort()
        return self.open_ports