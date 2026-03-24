# ============================================================
#  WEEK 14 LAB — Q1: API EXPLORER
#  COMP2152 — [Your Name Here]
# ============================================================

import urllib.request
import json


# TODO: Complete make_request(url)
#   Use urllib.request.urlopen(url)
#   Read response body: response.read().decode()
#   Return: {"status": response.status, "headers": dict(response.headers), "body": body}
#   If error occurs, return: {"status": 0, "headers": {}, "body": "", "error": str(e)}
def make_request(url):
    pass


# TODO: Complete parse_json(body)
#   Use json.loads(body) to convert JSON string to a dictionary
#   If it fails (ValueError), return None
def parse_json(body):
    pass


# TODO: Complete check_api_info(response)
#   Create a findings list
#   Check headers for security issues:
#     If "Server" in headers → append f"Server version exposed: {value}"
#     If "X-Powered-By" in headers → append f"Technology exposed: {value}"
#     If headers.get("Access-Control-Allow-Origin") == "*" → append "CORS: open to all origins"
#   Return findings
def check_api_info(response):
    pass


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: API EXPLORER")
    print("=" * 60)

    url = "http://httpbin.org/headers"
    print(f"\n--- Requesting {url} ---")

    resp = make_request(url)

    if resp and resp.get("status"):
        print(f"  Status: {resp['status']}")

        print("\n--- Response Headers ---")
        for key, val in resp["headers"].items():
            print(f"  {key:<16}: {val}")

        print("\n--- Parsed JSON Body ---")
        data = parse_json(resp["body"])
        if data:
            for key, val in data.items():
                print(f"  {key}: {val}")
        else:
            print("  (not JSON or parse failed)")

        print("\n--- Security Findings ---")
        findings = check_api_info(resp)
        if findings:
            for f in findings:
                print(f"  {f}")
        else:
            print("  (no issues found)")
    else:
        error = resp.get("error", "unknown") if resp else "make_request returned None"
        print(f"  Error: {error}")

    print("\n" + "=" * 60)
