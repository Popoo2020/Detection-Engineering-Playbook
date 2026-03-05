---
title: Suspicious sign-in from new country
id: det-001
platform: Azure Sentinel
mitre_tactics:
  - Initial Access
mitre_techniques:
  - T1078
description: |
  Detects sign-ins to Azure AD from countries not previously seen for the user in the last 30 days. A sudden login from a new country may indicate credential compromise.
false_positives: |
  Business travel or legitimate VPN usage may trigger this detection. Tune by maintaining a known-travel list or allowlisted VPN egress IPs.
query: |
  // Azure Sentinel KQL
  let lookback = 30d;
  let recentCountries = identitySigninEvents
    | where TimeGenerated > ago(lookback)
    | summarize by UserPrincipalName, CountryOrRegion;
  identitySigninEvents
    | where ResultType == "0"
    | where CountryOrRegion !in (toscalar(recentCountries | where UserPrincipalName == identitySigninEvents.UserPrincipalName | project CountryOrRegion))
    | project TimeGenerated, UserPrincipalName, CountryOrRegion, IPAddress
---