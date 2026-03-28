from assignment2_101513564 import scan_port

def test_open_port():
    # Common open port (may vary depending on system)
    result = scan_port("google.com", 80)
    print("Test Open Port:", result)

def test_closed_port():
    # Random high port likely closed
    result = scan_port("127.0.0.1", 9999)
    print("Test Closed Port:", result)


if __name__ == "__main__":
    test_open_port()
    test_closed_port()