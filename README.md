# Detection-Engineering-Playbook

[![CI](https://github.com/Popoo2020/Detection-Engineering-Playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/Popoo2020/Detection-Engineering-Playbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Detection-Engineering-Playbook** is a practical workspace for building, documenting and validating security detections.  
It currently includes working **KQL detection examples**, a **Sigma rule template**, **validation guidance**, and a **test harness that verifies Sigma file structure**.

> **Status:** active detection engineering baseline / designed for expansion.

## What is implemented

| Capability | Status |
|---|---|
| KQL detection for encoded PowerShell patterns | ✅ Implemented |
| KQL detection for rapid cross-location sign-in anomalies | ✅ Implemented |
| Sigma rule for suspicious encoded PowerShell execution | ✅ Implemented |
| Detection tuning note with ATT&CK mapping | ✅ Implemented |
| General validation guide | ✅ Implemented |
| CI that validates Sigma rule structure | ✅ Implemented |
| Larger ATT&CK coverage library | 🟡 Planned |
| SPL/AQL examples | 🟡 Planned |
| Sigma conversion automation | 🟡 Planned |
| Detection coverage dashboard | 🟡 Planned |

## Repository structure

```text
detections/
  kql/
    suspicious_encoded_powershell.kql
    impossible_travel_signin.kql

sigma/
  windows_suspicious_encoded_powershell.yml

docs/
  detections/
    encoded_powershell.md

validation_guide.md
requirements.txt
.github/workflows/ci.yml
```

## Implemented detection examples

### 1. Suspicious Encoded PowerShell

- **KQL:** `detections/kql/suspicious_encoded_powershell.kql`
- **Sigma:** `sigma/windows_suspicious_encoded_powershell.yml`
- **ATT&CK:** T1059.001 — PowerShell
- **Use case:** highlight encoded-command and in-memory execution patterns for analyst review

### 2. Rapid Cross-Location Sign-In Review

- **KQL:** `detections/kql/impossible_travel_signin.kql`
- **ATT&CK:** T1078 — Valid Accounts
- **Use case:** surface rapid sign-ins from differing locations for contextual review

## Validation philosophy

The playbook is designed around a simple principle: a detection is not “good” merely because it fires.  It must be:

- understandable
- tunable
- mapped to an attack hypothesis
- reviewable for false positives
- validated against representative data

The repository includes `validation_guide.md` as a concise workflow for testing and refining rules before deployment.

## Quickstart

```bash
git clone https://github.com/Popoo2020/Detection-Engineering-Playbook.git
cd Detection-Engineering-Playbook

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## Current CI coverage

The CI workflow currently:

- installs test/YAML dependencies
- runs pytest
- validates that Sigma files contain core structural metadata such as:
  - title
  - id
  - logsource
  - detection
  - level

## Roadmap

1. Add more KQL detections across credential access, persistence and privilege escalation
2. Expand the Sigma catalogue
3. Add SPL examples and conversion notes
4. Add metadata schemas for detections
5. Introduce a basic coverage dashboard by ATT&CK tactic / technique
6. Add test fixtures for detection documentation consistency

## Limitations

- The rules are reference detections and require local tuning before production use
- The rapid cross-location example is illustrative and should be adapted to real identity context and geo enrichment
- Current automated tests validate structure, not analytical precision or recall
