# Detection Note — Suspicious Encoded PowerShell

## Purpose

This detection is intended to surface suspicious PowerShell executions that use encoded-command patterns or common in-memory execution strings.  It is designed as a **high-signal review candidate**, not as a standalone confirmation of malicious activity.

## ATT&CK mapping

- **Tactic:** Execution
- **Technique:** T1059.001 — PowerShell

## Covered artefacts

- **KQL example:** `detections/kql/suspicious_encoded_powershell.kql`
- **Sigma template:** `sigma/windows_suspicious_encoded_powershell.yml`

## Common benign causes

- enterprise administration scripts
- software deployment tooling
- encoded command usage in lab or automation environments

## Recommended tuning

- enrich with parent process reputation
- exclude known automation accounts where justified
- prioritise alerts involving unusual parent-child relationships
- increase risk when combined with download or credential-access behaviours

## Validation ideas

1. Generate a benign encoded PowerShell command in a lab.
2. Confirm the rule fires as expected.
3. Add environment-specific exclusions only after evidence review.
4. Re-run the rule and document the expected false-positive trade-off.
