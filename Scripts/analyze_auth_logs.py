import re
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent LOG_FILE = PROJECT_ROOT / "logs" / "sample_auth.log"
FAILED_THRESHOLD = 3

PATTERN = re.compile(
    r"(Failed password|Accepted password) "
    r"for (?:invalid user )?(\S+) from "
    r"(\d{1,3}(?:\.\d{1,3}){3})"
)


def analyze_logs(log_file):
    failed_by_user_ip = Counter()
    successful_by_user_ip = Counter()
    total_events = 0

    with log_file.open("r", encoding="utf-8") as file:
        for line in file:
            match = PATTERN.search(line)

            if not match:
                continue

            event, username, source_ip = match.groups()
            total_events += 1
            key = (username, source_ip)

            if event == "Failed password":
                failed_by_user_ip[key] += 1
            else:
                successful_by_user_ip[key] += 1

    print("=== SOC AUTHENTICATION LOG ANALYSIS ===")
    print(f"Total parsed events: {total_events}")
    print(f"Failed login events: {sum(failed_by_user_ip.values())}")
    print(f"Successful login events: {sum(successful_by_user_ip.values())}")

    print("\nFailed login counts by username and source IP:")
    for (username, source_ip), count in sorted(
        failed_by_user_ip.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{username} | {source_ip} | {count} failures")

        if count >= FAILED_THRESHOLD:
            print("  ALERT: Repeated failed logins detected")

    print("\nSuccessful login counts by username and source IP:")
    for (username, source_ip), count in sorted(
        successful_by_user_ip.items()
    ):
        print(f"{username} | {source_ip} | {count} successes")


if __name__ == "__main__":
    if not LOG_FILE.is_file():
        raise SystemExit(
            f"Log file not found: {LOG_FILE}. "
            "Run this script from the repository root."
        )

    analyze_logs(LOG_FILE)
