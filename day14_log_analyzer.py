# Day 14 - Log Analyzer
# This program reads scan.log and counts OPEN and CLOSED ports.

open_count = 0
closed_count = 0

try:
    with open("scan.log", "r") as log_file:
        lines = log_file.readlines()

    for line in lines:
        if "OPEN" in line:
            open_count += 1
        elif "CLOSED" in line:
            closed_count += 1

    print("=== Log Analyzer Summary ===")
    print(f"Open ports found: {open_count}")
    print(f"Closed ports found: {closed_count}")
    print(f"Total scanned results: {open_count + closed_count}")

except FileNotFoundError:
    print("scan.log file not found.")
    print("Run a scanner project first to create scan.log.")