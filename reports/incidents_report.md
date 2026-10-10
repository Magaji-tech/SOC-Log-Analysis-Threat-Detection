


SOC Incident Investigation Report

1. Incident Overview

Incident Title: Repeated Authentication Failures from a Single Source IP

Incident Type: Suspicious Authentication Activity

Severity: Medium — Preliminary Assessment

Environment: Simulated Linux Authentication Logs

Investigation Date: October 10, 2026

Analyst: Magaji Abubakar Muhammad

Project: SOC Log Analysis and Threat Detection

2. Executive Summary

This investigation examined simulated authentication logs to identify suspicious login activity and potential security threats.

A total of 10 authentication events were reviewed. Seven failed login attempts originated from the same source IP address, "192.168.1.50". The attempts targeted three usernames: "test", "admin", and "root".

Three successful authentication events were also recorded in the dataset. However, the available evidence does not establish that these successful logins were associated with the failed attempts.

The repeated failures targeting multiple accounts may indicate password guessing or brute-force activity. Further investigation would be required to determine whether the activity represents a genuine attack.

3. Evidence Collected

The simulated authentication logs contained the following findings:

Indicator| Observation
Total authentication events| 10
Failed login attempts| 7
Successful login events| 3
Suspicious source IP| 192.168.1.50
Username: test| 3 failed attempts
Username: admin| 2 failed attempts
Username: root| 2 failed attempts
Observation window| 08:03:21–08:07:49, October 10, 2026

The three successful authentication events were associated with:

- "admin" from "192.168.1.10" — two successful events.
- "analyst" from "192.168.1.20" — one successful event.

These successful events are recorded separately from the suspicious failed attempts. Their legitimacy has not been independently verified.

4. Technical Analysis

The investigation identified repeated authentication failures originating from a single IP address and targeting multiple usernames.

The targeted usernames included "admin" and "root", which are commonly associated with privileged access, as well as "test".

This pattern is consistent with possible password guessing or account enumeration activity. However, authentication failures can also result from mistyped credentials, automated tests, or misconfigured services.

The available logs do not independently confirm the attacker's identity, intent, or whether any account was compromised.

5. Potential Security Risks

The observed activity presents several potential risks:

1. Unauthorised Access: Repeated password guessing could eventually lead to account compromise.
2. Privileged Account Exposure: Attempts targeting "admin" and "root" could threaten administrative access if successful.
3. Account Enumeration: Attempts against multiple usernames may indicate efforts to identify valid accounts.
4. Insufficient Monitoring: Without alerting and correlation, repeated authentication failures may go unnoticed.

These are potential risks, not confirmed security impacts.

6. Recommended Defensive Actions

The following defensive measures are recommended:

- Review authentication logs for additional failed attempts from "192.168.1.50".
- Determine whether the source IP belongs to an authorized internal system or an unknown host.
- Verify whether any suspicious authentication attempts resulted in successful access.
- Review the affected accounts for unusual activity.
- Enforce strong passwords and multi-factor authentication where supported.
- Configure appropriate authentication monitoring and alerting.
- Apply rate limiting or account lockout policies carefully to reduce password-guessing risk while avoiding unnecessary denial of service.
- Restrict privileged account access according to the principle of least privilege.

Any blocking action should follow the organization's incident-response procedures and be based on verified evidence.

7. Incident Classification

Preliminary Classification: Suspicious Authentication Activity

Confidence Level: Moderate that the failed-login pattern warrants investigation; insufficient evidence to confirm a brute-force attack.

Confirmed Account Compromise: Not established by the available dataset.

Business Impact: Not determined.

8. Conclusion

The analysis identified seven failed authentication attempts from "192.168.1.50", targeting three usernames within a short observation window.

The pattern warrants further investigation because repeated failures across multiple accounts can indicate password guessing or other suspicious authentication behavior.

Additional log correlation, source-host verification, and account activity review would be necessary to determine whether an actual security incident occurred.

This exercise demonstrates a structured approach to authentication-log analysis, evidence-based incident classification, risk assessment, and defensive recommendations.

9. Skills Demonstrated

- Security Operations Center (SOC) investigation
- Linux authentication-log analysis
- Suspicious login detection
- Incident documentation
- Preliminary threat classification
- Risk assessment
- Defensive security recommendations
- Technical report writing

10. Disclaimer

This project uses simulated authentication-log data for educational and portfolio purposes. The findings do not represent a confirmed real-world security incident.
