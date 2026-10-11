Authentication Log Analyzer — Test Cases

Purpose

Document the expected behavior of the Python authentication log analyzer.

Test Cases

Test ID| Scenario| Expected Result
TC-01| Analyze the supplied sample log| Parse 10 authentication events
TC-02| Count failed logins| Report 7 failed events
TC-03| Count successful logins| Report 3 successful events
TC-04| Detect repeated failures| Flag a source IP with at least 3 failed attempts
TC-05| Analyze an unknown username| Count the username if it appears in a matching event
TC-06| Log file is missing| Display a clear error and stop

Validation Status

These are expected outcomes based on the supplied simulated log dataset. Mark each test as passed only after executing the script and checking the actual output.

Scope

This is an educational blue-team project using simulated authentication events. It does not establish that a real system was attacked or compromised.
