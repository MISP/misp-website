---
title: "MISP 2.5.42: Major Codebase Hardening Release, Scheduled TAXII Push and Many Updates"
author:
 - MISP Project team
date: 2026-06-22
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/pivotick.png
---

This [MISP release 2.5.42](https://github.com/MISP/MISP/releases/tag/v2.5.42) and is primarily a security hardening release, alongside a large iteration on the new Overmind UI, new TAXII scheduled-push capability, and the usual data-library refreshes.

Security release — upgrading is strongly recommended. It closes two RCE vectors, an authentication-hardening issue, and a broad sweep of  mass-assignment / broken-access-control fixes across the controller layer.

The review covered 74 controllers and led to fixes for mass-assignment, broken-access-control, and authentication-related issues, as well as remediation of two remote-code-execution vectors. This focused audit demonstrated the value of a structured, codebase-wide security review: it uncovered issues that could have been difficult to identify through isolated testing and resulted in concrete, preventative hardening measures across the platform.

<img width="1944" height="1430" alt="Overmind preview ;-)" src="https://github.com/user-attachments/assets/9eb614de-8b71-4058-b001-d8670f1c008d" />


## Security

#### GCVE / CVEs:

-  [GCVE-1-2026-20105](https://vulnerability.circl.lu/vuln/gcve-1-2026-20105) - CVE-2026-56447
-  [GCVE-1-2026-20134](https://vulnerability.circl.lu/vuln/gcve-1-2026-20134) - CVE-2026-56446
-  [GCVE-1-2026-20091](https://vulnerability.circl.lu/vuln/gcve-1-2026-20091) - CVE-2026-56425
-  [GCVE-1-2026-20099](https://vulnerability.circl.lu/vuln/gcve-1-2026-20099) - CVE-2026-56424
-  [GCVE-1-2026-20094](https://vulnerability.circl.lu/vuln/gcve-1-2026-20094) - CVE-2026-56423
-  [GCVE-1-2026-20087](https://vulnerability.circl.lu/vuln/gcve-1-2026-20087) - CVE-2026-56422

 #### Remote Code Execution
  - RCE via arbitrary rdkafka config paths — the rdkafka config file path/name is now strictly validated, and the setting is restricted to CLI-only configuration. Previously only mitigated by requiring a compromised site-admin account. (Reported by Jakub Chyliński and Jeroen Pinoy)
  - RCE via arbitrary ndjson log paths — the ndjson log file path/name is now strictly controlled. Same prior mitigation as above. (Reported by Jakub Chyliński and Jeroen Pinoy)

 #### Authentication
  - Azure AD (AAD) authentication hardening. (Reported by Cormac Doherty)

  #### Mass-assignment & broken-access-control sweep
  - A systematic audit of the controller layer (74 controllers reviewed) resulted in 13 mass-assignment fix commits plus 2 preventative hardening commits, ensuring request data can no longer set fields outside each action's intended whitelist.
  - Broken-access-control / IDOR fixes (DPT-1 … DPT-7):
    - DPT-1: broken access control in EventReports and SharingGroups deleteSelection
    - DPT-2: cross-org IDOR in EventReports::removeTag 
    - DPT-3: wrong-entity authorization in CollectionElements::deleteSelection
    - DPT-4: capture path bypassed canEditAnalystData on update
    - DPT-5: wrong-entity authorization in TemplateElements::edit
    - DPT-6: missing edit-ownership check in the DecayingModel sub-system
    - DPT-7: crypto keys now restricted to the supported Event parent type

## New features & changes

#### Overmind UI (next-generation interface) — 24 commits continuing the Overmind/Insight UI buildout:
  - Tags & galaxy clusters can now be added directly from the Event View
  - Correlation graph integrated into the Insight UI 
  - Object index and event-report views/forms migrated, including attachment add and a migrated event-report add form
  - New colour scheme and bolder MISP element icons across the UI 
  - Item-count badges in index views, clickable breadcrumbs that return to the index, and various selection/handling fixes

#### TAXII (contributed by Cosive)
  - Scheduled TAXII push — TAXII added as a scheduled task type with single-server and all-enabled push modes, an enabled flag per TAXII server (defaults
  enabled on upgrade), and blocking of pushes for disabled servers (#10859)
  - Proxy support for TAXII push (#10860)

#### Authentication
  - Option to disable OIDC Pushed Authorization Requests (PAR) (contributed by BytesUnlimited-net, #10870)
  
#### Feeds
  - Added SiberKapan (Turkey-focused threat-intel platform) to the default feeds (contributed by OktayAlver, #10868)

## Bug fixes

  - csvimport: resolved attribute-tag erasure inside the `__fillAttribute` loop (contributed by Doemin04, #10869)
  - Sync (custom galaxies): fixed propagation of custom galaxy updates (contributed by Wachizungu, #10660)
  - Dashboards: EventStreamWidget now forces default columns when only invalid fields are requested (contributed by Wachizungu, #10867)
  - authkeys: unique_ips is now derive-only and can no longer be seeded on key creation (data-integrity fix)
  - Sighting: guard against a missing org_id to avoid a warning
  - Reverted the "only request event tags fingerprint instead of full tag list" sync change
  - db_schema fix
  - CI: run the PHP 8.3 job on ubuntu-24.04

# Data libraries

Updated to their latest upstream versions:
  - MISP galaxies
  - MISP objects
  - Taxonomies
  - Warning lists

