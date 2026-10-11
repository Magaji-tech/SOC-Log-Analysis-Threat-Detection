SOC Investigation Evidence

Purpose

This directory organizes evidence collected during the simulated Security Operations Center (SOC) investigation.

Evidence Checklist

- [ ] Authentication log samples
- [ ] Screenshots showing suspicious authentication events
- [ ] Evidence of repeated failed login attempts
- [ ] Screenshots of investigation findings



Investigation Summary

The simulated investigation examined 10 authentication events, including seven failed login attempts and three successful authentication events.

Seven failed attempts originated from "192.168.1.50", targeting the usernames "test", "admin", and "root".

The observed pattern warrants further investigation but does not independently confirm a brute-force attack or account compromise.

Evidence Integrity

All evidence must correspond to the actual project data. Screenshots should avoid exposing passwords, authentication tokens, or unrelated personal information.



Detection Evidence and Expected Results

Project Scope

This project analyzes 10 simulated SSH authentication events to demonstrate failed-login detection using Splunk Search Processing Language (SPL).

Observed Findings

- Total authentication events: 10
- Failed login attempts: 7
- Successful login events: 3
- Source IP associated with failed attempts: "192.168.1.50"
- Targeted usernames: "test", "admin", and "root"

Threshold-Based Detection

The repeated failed-login detection rule uses a threshold of three or more failed attempts for the same username and source IP combination.

Expected result:

Username| Source IP| Failed attempts| Threshold met?
test| 192.168.1.50| 3| Yes
admin| 192.168.1.50| 2| No
root| 192.168.1.50| 2| No

Security Interpretation

The repeated authentication failures are consistent with possible password-guessing activity. They do not, by themselves, prove a successful attack or compromise.

Evidence Limitations

These findings are based on simulated log data and documented expected query results. They should not be presented as screenshots or results from an actual Splunk execution unless the queries have been run in Splunk.

Recommended Supporting Evidence

- Screenshot of the baseline SPL query
- Screenshot of the threshold-based SPL query
- Screenshot of actual query results, if executed in Splunk
- Incident report describing the findings and recommended actions


Disclaimer

This evidence directory supports an educational cybersecurity portfolio project using simulated authentication logs.


