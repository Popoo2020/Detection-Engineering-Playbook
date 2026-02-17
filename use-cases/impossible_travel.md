# Use Case: Impossible Travel

Detects authentication events where a user signs in from two geographically distant locations in a period shorter than the minimum travel time.

- **Platforms:** Applicable to Microsoft Sentinel, Splunk, QRadar
- **Log sources:** Sign-in logs, network events
- **False positives:** VPN or proxy usage; service accounts
- **Tuning:** Exclude known VPN IP ranges and service principals
