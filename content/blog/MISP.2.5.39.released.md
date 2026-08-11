---
title: "MISP 2.5.39 - New Dashboard Experience, Stronger STIX, Sharper Analyst Workflows"
author:
 - MISP Project team
date: 2026-06-05
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/dashboard2.png
---

MISP 2.5.39 is now available. This release includes a large set of improvements around the new dashboard experience, analyst-focused dashboard widgets, STIX interoperability, security fixes, and operational stability.

We recommend that all MISP 2.5 users upgrade, especially instances exposed to multiple users or relying on dashboards, event templates, TAXII, LDAP mixed authentication, or STIX import/export workflows.

## Security fixes

This release fixes multiple vulnerabilities and hardening issues tracked as:

* [GCVE-1-2026-20092](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20092)
* [GCVE-1-2026-20069](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20069)
* [GCVE-1-2026-20059](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20059)
* [GCVE-1-2026-20080](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20080)
* [GCVE-1-2026-20083](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20083)
* [GCVE-1-2026-20101](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20101)
* [GCVE-1-2026-20047](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20047)
* [GCVE-1-2026-20066](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20066)
* [GCVE-1-2026-20081](https://vulnerability.circl.lu/vuln/GCVE-1-2026-20081)

The security-related fixes include:

* Preserved visibility rules for private galaxies during event template creation.
* Added ownership checks when overwriting event templates during forced imports.
* Removed an open redirect.
* Fixed a logic issue in the CRUD component delete flow.
* Prevented exposure of internal ordering fields.
* Ensured user fetches do not include sensitive settings.
* Fixed dashboard data leakage where users could force inclusion of arbitrary fields.
* Added mass-assignment protections for CakePHP add/edit behaviour.
* Prevented OTP bypass when `LdapAuth.mixedAuth=true` and `Security.require_otp=true`.
* Enforced stricter URL schemes and improved validation/error handling in the TAXII server controller.

Thanks to the reporters and contributors who helped identify, validate, and fix these issues, including Jeroen Pinoy and the wider MISP community.

## Dashboard and analyst dashboard improvements

MISP 2.5.39 continues the dashboard v2 work with a major set of usability, visualization, and analyst workflow improvements.

<img width="1900" height="245" alt="Trending widget in the MISP dashboard" src="https://github.com/user-attachments/assets/63ad486f-7810-4b7a-ae1e-3908f2ca90eb" />

<img width="1905" height="707" alt="Screenshot from 2026-06-05 16-02-41" src="https://github.com/user-attachments/assets/1f4994ff-4f37-4987-a542-24719e0d9e13" />
<img width="624" height="638" alt="Screenshot from 2026-06-05 16-03-10" src="https://github.com/user-attachments/assets/3fd16bd1-2bf0-4157-9dc6-c244a06cfd9e" />

Highlights include:

* “Save as template” now opens in the dashboard slide-in panel, saves via AJAX, and keeps users on the current board.
* New light/dark dashboard theme handling with persisted user preference and no-flash boot behaviour.
* Live dashboard theme switching, including chart retheming.
* WebGL globe support for attack-flow visualizations, including selectable globe skins and idle auto-rotation.
* New dashboard render kinds and widgets for analyst workflows, including:
  * trending vulnerabilities, threat actors, and ATT&CK techniques;
  * new-data KPI cards;
  * event cards;
  * recent event reports;
  * recent analyst notes and opinions;
  * recent local galaxy clusters;
  * “overlap with my org” correlation-based views.
* ATT&CK heatmap rendering was redesigned with parent/sub-technique aggregation, inactive technique hiding, readable labels, and a clearer red intensity ramp.
* Dashboard widgets gained improved typed configuration controls for dimensions, country/sector filters, `exclude_own_org`, event stream filters, and galaxy type filtering.
* The new `misp-iconify` icon set is now used for dashboard stat glyphs.


<img width="951" height="1101" alt="Configuring and live testing a widget in the new MISP dashboard" src="https://github.com/user-attachments/assets/2b2b4bc0-b76c-474b-ab62-a4e2c71a1957" />

## STIX and interoperability

This MISP release includes the latest `misp-stix` release, [`[misp-stix 2026.6.1](https://github.com/MISP/misp-stix/releases/tag/2026.6.1)`](https://github.com/MISP/misp-stix/releases/tag/2026.6.1), which improves MISP/STIX conversion behaviour.

The included `misp-stix` update brings:

* STIX 2 import pipeline cleanup with more explicit converter routing.
* Cleaner ownership of parser state and observable handling.
* Full TLP marking support shared across import and export paths.
* Expanded patterning-language support and regenerated mapping documentation.
* More deterministic, byte-stable conversions.
* STIX 1 export cleanup for collection framing.
* Dependency and maintenance updates.

The same conversion engine also powers [[CTI-Transmute](https://cti-transmute.org/)](https://cti-transmute.org), which provides a browser and REST API service for converting cyber threat intelligence between MISP and STIX formats.

## Other fixes and improvements

Additional fixes in this release include:

* Improved STIX library import management.
* Removed dependencies already provided by `misp-stix`.
* Required publish permission for publishing galaxy clusters.
* Forced galaxy distribution level to `0` in the database where appropriate.
* Fixed Attack Pattern sticky header conflicts.
* Improved task scheduler database reconnection.
* Handled array payloads in homepage validation to avoid PHP 8 `TypeError`.
* Improved CLI `runUpdates` behaviour by forcing reset of failures.
* Added support for EM SPACE (`U+2003`) in FreeText import.
* Fixed empty ID array handling when deleting events.
* Fixed sync caching timeout loops caused by header-case mismatches.
* Sanitized event info before blocklisting to avoid `PDOException`.
* Reduced very large `IN` lists when fetching large events.
* Added Overmind UI fixes across navigation, indexes, homepage handling, pagination, and dark theme support.
* Added database encoding fixes for galaxy clusters containing emoji characters.

## Upgrade

MISP 2.5.39 is available from the `2.5` branch.

As always, make sure to back up your instance before upgrading and run the standard update process for your deployment.
