SOC Log Analysis & Threat Detection

A hands-on Security Operations Center (SOC) project focused on authentication log analysis, repeated failed-login detection, and incident documentation.

Project Overview

This project demonstrates a basic SOC investigation workflow using simulated Linux SSH authentication logs. It combines Python-based log analysis, Splunk detection queries, structured testing, and incident reporting to identify potentially suspicious login activity.

The project is designed to demonstrate foundational skills in security monitoring, detection engineering, log analysis, and incident response.

Objectives

- Analyze authentication logs to identify failed and successful login attempts.
- Detect repeated failed logins using a configurable threshold.
- Group failed-login events by username and source IP address.
- Develop Splunk Search Processing Language (SPL) queries for detection.
- Document findings and recommended investigation steps.
- Validate expected behavior using test cases and simulated data.

Tools and Technologies

Tool| Purpose
Python 3| Automated authentication log analysis
Linux / Kali Linux| Lab environment and command-line investigation
Splunk SPL| Search and detection query development
SSH authentication logs| Simulated security event data
GitHub| Version control and project documentation

Detection Scenario

Scenario: Repeated failed SSH authentication attempts may indicate password guessing or brute-force activity.

The Python analyzer extracts authentication events and groups them by username and source IP address. It raises an alert when the number of failed login attempts for a username and source IP combination reaches the configured threshold of 3 or more failures.

The alert indicates suspicious activity requiring investigation; it does not, by itself, prove that an attack occurred.

Sample Lab Results

The simulated dataset contains 10 authentication events.

Metric| Observed result
Total authentication events| 10
Failed login events| 7
Successful login events| 3
Failed attempts for "test" from "192.168.1.50"| 3
Configured detection threshold| 3

Expected detection: The "test" account from "192.168.1.50" triggers the repeated-failed-login alert.

These results come from a controlled, simulated lab dataset and are not evidence of activity on a production network.

Methodology

1. Log collection: Prepare sample SSH authentication events.
2. Parsing: Extract event type, username, and source IP address using Python regular expressions.
3. Analysis: Count failed and successful login events.
4. Detection: Compare failed-login counts against the configured threshold.
5. Validation: Compare script output against expected test results.
6. Reporting: Document findings, limitations, and recommended investigation steps.


How to Run the Analyzer

Requirements

- Python 3.10 or later
- No third-party Python packages required

Steps

1. Clone or download this repository.
2. Open a terminal in the repository's root directory.
3. Run the analyzer:

python3 Scripts/analyze_auth_logs.py

The script reads "logs/sample_auth.log", summarizes failed and successful authentication events, and flags username/source-IP combinations with at least three failed login attempts.

Expected Results

For the included simulated dataset, the expected summary is:

- Total parsed events: 10
- Failed login events: 7
- Successful login events: 3
- Repeated failed-login alert for "test" from "192.168.1.50" 

Repository Structure

SOC-Log-Analysis-Threat-Detection/
├── README.md
├── Logs/
├── Scripts/
│   └── analyze_auth_logs.py
├── Queries/
│   ├── Failed_login_detection
│   └── Repeated_Failed_Login_Detection.spl
├── Document/
│   ├── Methodology.md
│   └── Detection_Rules.md
├── Reports/
│   └── Incident_report.md
├── Evidence/
│   └── README.md
└── Tests/
    ├── test_cases.md
    └── test_results.md


Incident Response Recommendations

When repeated failed logins are detected:

- Review the source IP address and authentication timeline.
- Determine whether the targeted account is valid and authorized.
- Check for successful logins from the same source after repeated failures.
- Correlate events with other available security logs.
- Follow organizational procedures before blocking an IP address or disabling an account.
- Document findings and escalate confirmed or high-risk activity according to the incident response process.

Limitations

- The dataset is simulated and does not represent a live production environment.
- The detection relies on log formats that match the implemented parser.
- A threshold-based alert can produce false positives and may miss activity spread across multiple source IP addresses.
- A successful login following failed attempts requires further investigation; it does not automatically confirm account compromise.
- Splunk query files demonstrate detection logic; their presence alone does not establish that the queries have been executed against a live Splunk instance.

Future Improvements

- Add automated unit tests for parsing and detection logic.
- Generate structured JSON or CSV investigation reports.
- Add time-window-based detection and configurable thresholds.
- Improve error handling for malformed log entries and missing files.
- Capture genuine lab execution evidence.
- Validate the SPL queries against a configured Splunk lab.


Execution Evidence

The screenshot below shows the Python analyzer running against the simulated SSH authentication logs in the Kali Linux lab. 


Author:

Magaji Abubakar Muhammad

Aspiring Cybersecurity Professional | SOC Analyst in Training | Threat Detection | Incident Response

GitHub: https://github.com/Magaji-tech/


Disclaimer

This project is intended for educational and portfolio demonstration purposes. All sample authentication events are simulated. It does not demonstrate an actual compromise, and testing should only be performed in authorized environments.


