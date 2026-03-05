# Changelog

This document follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
format and uses [Semantic Versioning](https://semver.org/).  All
significant changes to **Detection‑Engineering‑Playbook** will be recorded
here.

## [0.1.0] – 2026‑03‑01

### Added

* **Detection examples:** Added two initial detection rules:
  * `detections/kql_suspicious_signin.md` implements an Azure Sentinel KQL
    detection for anomalous sign‑ins, mapped to relevant MITRE ATT&CK tactics
    and including guidance on tuning and false positives.
  * `detections/spl_suspicious_powershell.md` provides a Splunk SPL query
    detecting encoded PowerShell commands, with explanatory notes.
* **Validation guide:** Added `docs/validation_guide.md` explaining how to
  validate detection rules against sample data, interpret results and iterate
  tuning.
* **Sigma rule:** Added `sigma/sample_rule.yml` as a starting point for
  Sigma‑formatted detections and notes on conversion to platform‑specific
  queries.
* **Standard project files:** Added licensing, security policy, code of
  conduct and contribution guidelines to align with open‑source best
  practices.
* **Initial release:** Tagged version `v0.1.0` to denote the project’s
  first structured release.
