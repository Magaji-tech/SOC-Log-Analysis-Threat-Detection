#Failed Login Detection Rules


Objective
Identify repeated SSH authentication failures that may indicate password guessing or brute-force activity.
Data Source
Sample SSH authentication logs
Splunk Search Processing Language (SPL)


Detection Logic
The detection query extracts the attempted username and source IP address, counts failed login events for each combination, and flags combinations with three or more failures.


Detection Threshold
Threshold: 3 or more failed attempts
Grouping: Username and source IP address
Event: Failed SSH password authentication


Expected Finding
In the simulated dataset, the username test has three failed attempts from 192.168.1.50. This meets the detection threshold.


Recommended Analyst Actions
Review the source IP and targeted usernames.
Check authentication logs for any subsequent successful login.
Correlate the activity with other security events.
Consider blocking or restricting the source only after validating the activity and following organizational procedures.


Limitations

This rule counts failed attempts in the searched dataset. It does not establish that a successful compromise occurred. The query must be executed in a suitably configured Splunk environment to validate its operation against ingested logs.
Scope
This is an educational project using simulated authentication events. The findings do not represent a confirmed real-world incident.
