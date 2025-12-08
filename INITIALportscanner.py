import socket
import sys
from datetime import datetime

def scan_port(host, port, timeout=1):
    """
    Attempt to connect to a specific port on the target host.
    
    Args:
        host (str): Target hostname or IP address
        port (int): Port number to scan
        timeout (int): Connection timeout in seconds
    
    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Attempt connection
        result = sock.connect_ex((host, port))
        sock.close()
        
        return result == 0
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{host}'")
        sys.exit(1)
    except socket.error:
        print(f"Error: Could not connect to host '{host}'")
        sys.exit(1)

def scan_host(host, start_port, end_port, timeout=1):
    """
    Scan a range of ports on the target host.
    
    Args:
        host (str): Target hostname or IP address
        start_port (int): Starting port number
        end_port (int): Ending port number
        timeout (int): Connection timeout in seconds
    """
    print(f"\nScanning host: {host}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    open_ports = []
    
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(host, port, timeout):
                open_ports.append(port)
                print(f"Port {port}: OPEN")
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        sys.exit(1)
    
    print("-" * 50)
    print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Open ports found: {len(open_ports)}")
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")

if __name__ == "__main__":
    # Example usage
    target_host = "localhost"
    start_port = 1
    end_port = 1024
    
    scan_host(target_host, start_port, end_port, timeout=1)