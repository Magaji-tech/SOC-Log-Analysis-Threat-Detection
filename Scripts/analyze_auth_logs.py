

import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path("logs/sample_auth.log")
FAILED_THRESHOLD = 3


def analyze_logs(log_file):
    failed_by_ip = Counter()
    failed_by_user = Counter()
    successful_by_ip = Counter()
    total_events = 0

    pattern = re.compile(
        r"(Failed password|Accepted password) "
        r"for (?:invalid user )?(\S+) from "
        r"(\d{1,3}(?:\.\d{1,3}){3})"
    )

    with log_file.open("r", encoding="utf-8") as file:
        for line in file:
            match = pattern.search(line)

            if not match:
                continue

            event, username, source_ip = match.groups()
            total_events += 1

            if event == "Failed password":
                failed_by_ip[source_ip] += 1
                failed_by_user[username] += 1
            else:
                successful_by_ip[source_ip] += 1

    print("=== SOC AUTHENTICATION LOG ANALYSIS ===")
    print(f"Total parsed events: {total_events}")
    print(f"Failed login events: {sum(failed_by_ip.values())}")
    print(f"Successful login events: {sum(successful_by_ip.values())}")

    print("\nFailed attempts by source IP:")
    for source_ip, count in failed_by_ip.most_common():
        print(f"{source_ip}: {count}")

        if count >= FAILED_THRESHOLD:
            print("  ALERT: Repeated failed logins detected")

    print("\nFailed attempts by username:")
    for username, count in failed_by_user.most_common():
        print(f"{username}: {count}")


if __name__ == "__main__":
    if not LOG_FILE.exists():
        raise SystemExit(
            f"Log file not found: {LOG_FILE}. "
            "Run this script from the repository root."
        )

    analyze_logs(LOG_FILE)
