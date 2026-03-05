# Detection‑Engineering‑Playbook

[![CI](https://github.com/your-org/Detection-Engineering-Playbook/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/Detection-Engineering-Playbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Detection‑Engineering‑Playbook** is a curated collection of detection rules,
guides and supporting artefacts aimed at helping security analysts build and
maintain high‑fidelity alerts across multiple platforms.  The focus is on
practical examples, MITRE ATT&CK mapping and documentation that encourages
continuous improvement through validation and tuning.

## Features

* **Multi‑platform detections** – Includes example queries for Azure Sentinel
  (KQL), Splunk (SPL) and other security analytics platforms, with
  detailed notes on false positives and tuning strategies.
* **MITRE ATT&CK alignment** – Each detection is mapped to relevant tactics
  and techniques, helping practitioners assess coverage and identify gaps.
* **Validation guidance** – Documentation outlines how to test detections
  against synthetic or real datasets and adjust thresholds for noise
  reduction.
* **Sigma templates** – Provides Sigma rules which can be converted into
  platform‑specific queries using available converters.
* **Contribution standards** – Defines naming conventions, metadata schema
  and guidelines for adding new rules responsibly.

## Quickstart

1. Clone or fork this repository.
2. Navigate to the `detections/` folder to explore platform‑specific examples.
3. Read the corresponding detection document to understand the query,
   MITRE mapping and tuning notes.
4. Use the `docs/validation_guide.md` to set up a lab environment or use
   your own logs to validate the detection and tailor it to your
   environment.
5. Convert Sigma rules in the `sigma/` folder to your platform using
   [`sigma-cli`](https://github.com/SigmaHQ/sigma-cli) or similar tooling.

## Documentation

The `docs/` directory contains:

* `validation_guide.md` – Step‑by‑step guide to testing detections and
  evaluating their effectiveness.

Future documents will cover naming conventions, metadata standards and
guidance for mapping detection coverage by MITRE tactic.

## Roadmap

1. Add additional KQL, SPL, AQL and other detections across varied attack
   tactics.
2. Expand the Sigma rule set and provide conversion scripts.
3. Develop a false‑positive playbook detailing common tuning knobs and
   baseline methodologies.
4. Introduce a dashboard template for visualising detection coverage by
   tactic.
5. Add CI workflows to lint and validate Sigma files.

See `CONTRIBUTING.md` to learn how to contribute new detection rules or
documentation.

## Known Limitations

Only a small sample of detections is included.  These examples may not
generalise to your environment without modification and additional
tuning.  There is no automated validation pipeline in this repository; as
more rules are added, a CI workflow should be created to lint and test
them.  Always validate detections in a safe lab environment before
deploying to production.
