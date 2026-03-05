# Detection Validation Guide

This guide outlines a structured approach to validate detection rules before deploying them into production.

## 1. Understand the Detection Logic

Read the rule description and query to understand what behavior it is designed to detect and which MITRE tactics/techniques it maps to. Ensure the rule aligns with your threat model and data sources.

## 2. Generate or Collect Test Data

* For KQL or SPL detections, run the query against historical logs and verify that the results match known malicious or benign events.
* Use synthetic events or attack simulation tools to generate test data for specific techniques.

## 3. Evaluate Precision and Recall

* **True Positives:** Confirm that known malicious events trigger the detection.
* **False Positives:** Review benign events flagged by the rule and consider adding filters or contextual enrichment to reduce noise.

## 4. Tune and Document

Iteratively adjust the query or thresholds to balance coverage and noise. Document any assumptions, filters, or environment-specific parameters in the detection file's `false_positives` section.

## 5. Peer Review

Have another analyst review the detection logic, test data and tuning decisions. Peer review helps catch blind spots and ensures consistency across the detection library.