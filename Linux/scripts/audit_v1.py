# What this script does:
# Find users with shell access
# Find world writable files
# Find SUID files

import os
import subprocess

# -----------------------------
# 1. List Users
# -----------------------------

print("\n[*] Finding users with shell access...\n")

with open("/etc/passwd", "r") as f:
    for line in f:
        parts = line.strip().split(':')
        user = parts[0]
        shell = parts[-1]

        if "bash" in shell:
            print(f"[+] User: {user} , Shell: {shell}")
            

print("\n[*] Finding world writable files...")

# -----------------------------
# 2. Find World-Writable Files
# -----------------------------

print("\n[!] World-writable files (security risk):\n")

try:
    result = subprocess.run(
        ["find", "/", "-type", "f", "-perm", "-0002"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )
    
    files = result.stdout.strip().split("\n")
    
    for f in files[:20]:  # limit output
        print(f)

    print(f"\nTotal found: {len(files)}")

except Exception as e:
    print("Error scanning world-writable files:", e)

# -----------------------------
# 3. Find SUID Files
# -----------------------------
print("\n[!] SUID files (run as root):\n")

try:
    result = subprocess.run(
        ["find", "/", "-perm", "-4000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )
    
    files = result.stdout.strip().split("\n")
    
    for f in files[:20]:  # limit output
        print(f)

    print(f"\nTotal found: {len(files)}")

except Exception as e:
    print("Error scanning SUID files:", e)

print("\n=== AUDIT COMPLETE ===")

