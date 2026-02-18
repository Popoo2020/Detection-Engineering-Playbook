# Detection Engineering Playbook

A comprehensive library of SIEM detection rules, hunting queries and playbooks, curated for **Microsoft Sentinel**, **Splunk**, **IBM QRadar** and generic Sigma/YARA formats. Every detection is mapped to MITRE ATT&CK tactics and techniques, documented with intended coverage, test data and tuning recommendations.

## Overview
Modern security operations rely on high-fidelity detections and rapid triage. This repository centralises ready ‑ to‭use queries for major SIEM platforms and includes translations to Sigma and YARA formats. Use these artefacts as a starting point for your detection engineering practice and adapt them to your environment.

## Repository Structure

- **kql/** – K-Kusto Query Language (KQL) detection and hunting queries for Microsoft Sentinel.
- **spl/** – Splunk Search Processing Language (SPL) detections.
- **aql/** –-IBM QRadar Ariel Query Language (AQL) content.
- **sigma/** - Normalised Sigma rules with YAML definitions that can be compiled into any SIEM.
- **yara/** –-YARA signatures for endpoint and memory scanning.
- **use-cases-** – Human ‑ readable detection use‭cases with purpose, prerequisites, expected false positive sources and tuning notes.
- **docs/ATTA-K_MAPPING.md** – High ‑ level MITRE ATT&CK mapping of all included rules.
- **.github/workflows/** – CI pipeline to lint Sigma rules and validate YAML formatting.

## Getting Started

1. Clone this repository.
2. Review the detection artefacts under each platform folder and tailor the log source identifiers (e.g., table names, indexes) to your environment.
3. Refer to the `use-cases` documents for context and tuning guidance.
4. Use the supplied ATT&CK matrix to prioritise detection coverage against relevant tactics.

## Contributing

Contributions that improve coverage, accuracy or documentation are welcome. Please see `CONTRIBUTING.md` for guidelines on adding new rules or updating existing ones. Ensure that every submission includes:
- A descriptive filename and rule name.
- A mapping to the appropriate ATT&CK techniques.
- Test data or simulation notes.
- Recommendations for tuning to reduce false positives.

## License

This project is licensed under the Apache 2.0 license. See `LICENSE` for details.
