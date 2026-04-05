# ============================================================
#  WEEK 09 LAB — Q1: SYSTEM INFORMATION REPORTER (SOLUTION)
#  COMP2152
# ============================================================

import os
import sys
import platform


# --- Helper (provided) — error handling example from Week 06 ---
def display(title, data):
    print(f"\n--- {title} ---")
    for k, v in data.items():
        print(f"  {k:<12} : {v}")


def safe_run(label, func, *args):
    try:
        result = func(*args)
        if result is None:
            print(f"  [!] {label} returned None — missing return?")
            return {}
        return result
    except Exception as e:
        print(f"  [ERROR] {label}: {e}")
        return {}


# ANSWER: get_system_info
def get_system_info():
    return {
        "os":      platform.system(),
        "node":    platform.node(),
        "release": platform.release(),
        "machine": platform.machine(),
    }


# ANSWER: get_python_info
def get_python_info():
    return {
        "version":    sys.version,
        "executable": sys.executable,
        "platform":   sys.platform,
    }


# ANSWER: get_directory_info
def get_directory_info(path):
    return {
        "path":         os.path.abspath(path),
        "exists":       os.path.exists(path),
        "file_count":   len(os.listdir(path)) if os.path.exists(path) else 0,
        "is_directory": os.path.isdir(path),
    }


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    info = safe_run("System Info", get_system_info)
    if info: display("System Info", info)

    info = safe_run("Python Info", get_python_info)
    if info: display("Python Info", info)

    info = safe_run("Directory Info", get_directory_info, ".")
    if info: display("Directory Info for '.'", info)

    print("\n" + "=" * 60)
