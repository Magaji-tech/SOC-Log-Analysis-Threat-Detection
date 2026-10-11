
SOC Authentication Log Analysis — Test Results

Test Environment

- Operating System: Kali Linux
- Python Version: 3.13.12
- Input File: logs/sample_auth.log

Verification Results

- Total authentication events: 10 — PASS
- Failed login events: 7 — PASS
- Successful login events: 3 — PASS
- Repeated failed-login alert at threshold of 3: PASS

Conclusion

The Python log analyzer successfully processed the sample authentication logs and detected repeated failed-login activity according to the configured threshold.

Scope

These tests use simulated authentication logs in a local lab environment. They do not establish that a real attack occurred or that the tool has been validated against production systems.
