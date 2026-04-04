import socket
import urllib.request

# Parent class
class Scanner:
    def __init__(self, target):
        self.target = target
        self.results = []

    def display_results(self):
        print(f"\nResults for {self.target}:")
        for r in self.results:
            print(r)


# Child class: Port Scanner
class PortScanner(Scanner):
    def __init__(self, target, ports):
        super().__init__(target)
        self.ports = ports

    def scan(self):
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((self.target, port))
            if result == 0:
                self.results.append(f"Port {port} is OPEN")
            else:
                self.results.append(f"Port {port} is CLOSED")
            s.close()


# Child class: HTTP Scanner
class HTTPScanner(Scanner):
    def __init__(self, target, paths):
        super().__init__(target)
        self.paths = paths

    def scan(self):
        for path in self.paths:
            url = f"http://{self.target}/{path}"
            try:
                urllib.request.urlopen(url)
                self.results.append(f"{path} exists")
            except:
                self.results.append(f"{path} not found")


# MAIN
if __name__ == "__main__":
    # Port scan
    ps = PortScanner("scanme.nmap.org", [22, 80, 443])
    ps.scan()
    ps.display_results()

    # HTTP scan
    hs = HTTPScanner("example.com", ["", "admin", "login"])
    hs.scan()
    hs.display_results()