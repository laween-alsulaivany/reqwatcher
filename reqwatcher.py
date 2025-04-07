import subprocess
import importlib.metadata
import os
import sys
import argparse
import json

CONFIG_FILE = ".reqwatcher.json"
DEFAULT_CONFIG = {
    "version_format": "==",        # could be "==", ">=", or none
    "auto_add": True,              # auto-append without asking
    "requirement_file": "requirements.txt"
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG
    with open(CONFIG_FILE, "r") as f:
        try:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
        except json.JSONDecodeError:
            print("[reqwatcher] ⚠️ Invalid config file. Using defaults.")
            return DEFAULT_CONFIG

def install_and_track(package):
    config = load_config()
    print(f"[reqwatcher] Installing {package}...")
    subprocess.run(["pip", "install", package])

    try:
        version = importlib.metadata.version(package)

        # Format line based on config
        if config["version_format"] == "==":
            line = f"{package}=={version}"
        elif config["version_format"] == ">=":
            line = f"{package}>={version}"
        else:
            line = package

        add_to_requirements(line, config)
    except importlib.metadata.PackageNotFoundError:
        print(f"[reqwatcher] ❌ Could not verify {package}. Skipped.")

def add_to_requirements(line, config):
    filename = config["requirement_file"]

    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(line + '\n')
        print(f"[reqwatcher] Created {filename} and added: {line}")
    else:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        if line not in lines:
            with open(filename, 'a') as f:
                f.write(line + '\n')
            print(f"[reqwatcher] Added: {line}")
        else:
            print(f"[reqwatcher] Already in {filename}: {line}")

def main():
    parser = argparse.ArgumentParser(description="Track pip installs and update requirements.txt")
    parser.add_argument("command", choices=["install", "undo", "list"], help="Command to run")
    parser.add_argument("packages", nargs="*", help="Package(s) to install")

    args = parser.parse_args()

    if args.command == "install":
        if not args.packages:
            print("Please provide at least one package to install.")
            return
        for package in args.packages:
            install_and_track(package)

    elif args.command == "list":
        list_tracked()

    elif args.command == "undo":
        undo_last()

def list_tracked():
    filename = "requirements.txt"
    if not os.path.exists(filename):
        print("[reqwatcher] No requirements.txt found.")
        return
    with open(filename, 'r') as f:
        print("[reqwatcher] Tracked packages:")
        for line in f:
            print("  -", line.strip())

def undo_last():
    filename = "requirements.txt"
    if not os.path.exists(filename):
        print("[reqwatcher] No requirements.txt found.")
        return

    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    if not lines:
        print("[reqwatcher] requirements.txt is empty.")
        return

    last_line = lines[-1]
    lines = lines[:-1]
    with open(filename, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"[reqwatcher] Removed last line: {last_line}")

if __name__ == "__main__":
    main()
