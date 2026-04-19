# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — Areeb Shoukat
# ============================================================

import urllib.request

REQUIRED_HEADERS = {
    "Content-Security-Policy": "Prevents XSS and injection attacks",
    "X-Frame-Options": "Prevents clickjacking",
    "X-Content-Type-Options": "Stops MIME sniffing",
    "Strict-Transport-Security": "Forces HTTPS",
    "Referrer-Policy": "Controls referrer info"
}


def check_headers(url):
    try:
        response = urllib.request.urlopen(url)
        headers = dict(response.headers)
        results = []

        for header in REQUIRED_HEADERS:
            if header in headers:
                results.append({
                    "header": header,
                    "present": True,
                    "value": headers[header]
                })
            else:
                results.append({
                    "header": header,
                    "present": False,
                    "value": "MISSING"
                })

        return results
    except Exception:
        return []


def generate_report(url, results):
    print(f"\nURL: {url}")
    missing_count = 0

    for result in results:
        if result["present"]:
            print(f" ✓ {result['header']}: {result['value']}")
        else:
            print(f" ✗ {result['header']}: MISSING — {REQUIRED_HEADERS[result['header']]}")
            missing_count += 1

    print(f" Missing {missing_count} of {len(results)} security headers!")


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://example.com",
        "https://httpbin.org",
        "https://google.com"
    ]

    for url in urls:
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print(f"\nURL: {url}")
            print(" Error fetching headers.")

    print("\n" + "=" * 60)