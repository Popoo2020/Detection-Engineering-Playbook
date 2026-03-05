---
title: Encoded PowerShell command execution
id: det-002
platform: Splunk
mitre_tactics:
  - Execution
mitre_techniques:
  - T1086
description: |
  Detects the execution of PowerShell with the `-EncodedCommand` argument, which is often used by attackers to obfuscate commands. The detection searches Windows event logs for PowerShell processes invoking encoded commands.
false_positives: |
  Administrators may legitimately use encoded commands for automation. Consider alerting only when the Base64 payload decodes to suspicious keywords (e.g., `Invoke-WebRequest`, `DownloadString`).
query: |
  # Splunk SPL example
  index=wineventlog EventCode=4688 (NewProcessName="*powershell.exe" OR NewProcessName="*pwsh.exe") CommandLine="*-EncodedCommand*"
    | table _time, Computer, User, NewProcessName, CommandLine
---