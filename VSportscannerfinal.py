import socket
import sys
from datetime import datetime

def get_target_host():
    """Prompt user for target host IP address or hostname."""
    while True:
        target = input("Enter target host (IP or hostname): ").strip()
        if target:
            return target
        print("Error: Please enter a valid host.")


def get_port_range():
    """Prompt user for port range to scan."""
    while True:
        try:
            port_input = input("Enter port(s) to scan (e.g., '80' or '80-443'): ").strip()
            
            if '-' in port_input:
                # Handle port range
                start, end = port_input.split('-')
                start_port = int(start.strip())
                end_port = int(end.strip())
                
                if 1 <= start_port <= end_port <= 65535:
                    return range(start_port, end_port + 1)
                else:
                    print("Error: Ports must be between 1 and 65535, and start <= end.")
            else:
                # Handle single port
                port = int(port_input)
                if 1 <= port <= 65535:
                    return [port]
                else:
                    print("Error: Port must be between 1 and 65535.")
        except ValueError:
            print("Error: Invalid input. Use format '80' or '80-443'.")


def scan_port(host, port, timeout=1):
    """
    Attempt to connect to a specific port on the target host.
    
    Args:
        host: Target IP address or hostname
        port: Port number to scan
        timeout: Connection timeout in seconds
    
    Returns:
        True if port is open, False otherwise
    """
    try:
        # Create socket and set timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Attempt connection
        result = sock.connect_ex((host, port))
        sock.close()
        
        # Port is open if connection succeeds (result == 0)
        return result == 0
    except socket.gaierror:
        print(f"Error: Cannot resolve hostname '{host}'")
        sys.exit(1)
    except socket.error:
        print(f"Error: Cannot connect to host '{host}'")
        sys.exit(1)


def main():
    """Main function to orchestrate port scanning."""
    print("=" * 50)
    print("Python Port Scanner")
    print("=" * 50)
    
    # Get target host and ports from user
    target_host = get_target_host()
    ports = get_port_range()
    
    print(f"\nScanning {target_host} for open ports...")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    open_ports = []
    
    # Scan each port
    for port in ports:
        if scan_port(target_host, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")
    
    print("-" * 50)
    print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nSummary: Found {len(open_ports)} open port(s)")
    
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")


if __name__ == "__main__":
    main()