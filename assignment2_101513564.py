import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        result = s.connect_ex((host, port))
        if result == 0:
            return True   # port is open
        else:
            return False  # port is closed
    except:
        return False
    finally:
        s.close()


def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")


if __name__ == "__main__":
    target = input("Enter host (e.g., 127.0.0.1): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    scan_ports(target, start, end)