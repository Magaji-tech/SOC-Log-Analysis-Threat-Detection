# SOC-Log-Analysis-Threat-Detection
A hands-on SOC analysis lab demonstrating security log analysis, suspicious authentication detection, incident  investigation, and defensive security recommendation.
SOC Log Analysis & Threat Detection

Project Overview

This project demonstrates a practical Security Operations Center (SOC) investigation using authentication logs to identify suspicious login activity.

The lab focuses on security event analysis, failed-login detection, incident investigation, and defensive security recommendations.

Note: The initial investigation uses simulated security events for educational purposes.

Objectives

- Analyze authentication logs.
- Identify repeated failed login attempts.
- Investigate suspicious login patterns.
- Develop detection queries using Splunk.
- Document findings in a professional incident report.

Tools and Technologies

- Splunk
- Linux
- Authentication log files
- GitHub

Investigation Scope

The investigation focuses on authentication events, including:

- Successful logins.
- Failed login attempts.
- Repeated authentication failures.
- Potential indicators of brute-force activity.

Methodology

1. Prepare sample authentication logs.
2. Import and index the logs in Splunk.
3. Search for failed login attempts.
4. Analyze event patterns and identify suspicious activity.
5. Document findings and recommend defensive measures.

Expected Deliverables

- Sample authentication logs.
- Splunk detection queries.
- Security investigation methodology.
- Dashboard screenshots.
- Incident investigation report.

Security Recommendations

Depending on the investigation findings, recommended defensive measures may include:

- Monitoring repeated authentication failures.
- Enforcing multi-factor authentication.
- Reviewing account lockout policies.
- Investigating unusual login patterns.
- Improving security logging and alerting.

Limitations

Repeated failed login attempts do not automatically confirm a brute-force attack. Findings must be evaluated against the available evidence and the context of the environment.


 Investigation Results

This project demonstrates a structured approach to investigating suspicious authentication activity using simulated Linux authentication logs.

Key Findings

- Total authentication events: 10
- Failed login attempts: 7
- Successful login events: 3
- Suspicious source IP: "192.168.1.50"
- Accounts targeted: "test", "admin", and "root"

Threat Assessment

Repeated authentication failures from a single source IP targeting multiple usernames may indicate password guessing or brute-force activity.

The available evidence warrants further investigation but does not independently confirm a successful attack or account compromise.

Recommended Security Controls

1. Enable multi-factor authentication (MFA).
2. Monitor repeated authentication failures.
3. Configure alerts for suspicious login patterns.
4. Review privileged account activity.
5. Apply appropriate rate limiting and account protection policies.
6. Investigate suspicious source IP addresses.

 Project Documentation

The repository includes documentation covering:

- SOC investigation methodology
- Authentication-log analysis
- Incident investigation report
- Threat assessment and defensive recommendations

Incident Report: "reports/incident_report.md"

 Skills Demonstrated

- Security Operations Center (SOC) fundamentals
- Linux security-log analysis
- Authentication-event investigation
- Suspicious activity detection
- Incident response documentation
- Threat assessment
- Defensive security controls
- Technical reporting

Disclaimer

This project uses simulated authentication logs for educational purposes. The findings demonstrate an investigation methodology and do not represent a confirmed real-world security incident.


Author: Magaji Abubakar Muhammad

Focus: Cybersecurity | SOC Analysis | Threat Detection | Incident Response


GitHub: https://github.com/Magaji-tech/




