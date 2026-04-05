import platform
import sys
import os


def get_system_info():
    return {
        "os": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "machine": platform.machine()
    }


def get_python_info():
    return {
        "version": sys.version,
        "executable": sys.executable,
        "platform": sys.platform
    }


def get_directory_info(path):
    exists = os.path.exists(path)
    return {
        "path": os.path.abspath(path),
        "exists": exists,
        "file_count": len(os.listdir(path)) if exists else 0,
        "is_directory": os.path.isdir(path)
    }


if __name__ == "__main__":
    print("System Info:", get_system_info())
    print("Python Info:", get_python_info())
    print("Directory Info:", get_directory_info("."))