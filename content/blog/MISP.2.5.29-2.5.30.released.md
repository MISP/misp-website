---
title: "MISP v2.5.30 and v2.5.29 released: Beta UI/UX Mode, New Workflow modules and Performance Enhancements"
banner: /img/blog/new-ui.png
author:
 - MISP Project team
date: 2025-12-13
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release introduces a foundational **beta UI/UX mode** (which will be the foundation for the next versions, feedback is more than welcome), new workflow modules, improvements to the Event Index, and important security updates.

The MISP Core team is incredibly happy with the contribution of this significant UX/UI rework from [Chris Horsley](https://github.com/chorsley) of [Cosive](https://www.cosive.com/), marking a positive step towards further collaboration on improving the user experience of MISP.

## ✨ New Features

* **Beta UI/UX Mode**: An opt-in **beta UI / UX mode** () is now available via user settings, featuring a redesigned Event Index and top navigation bar.
    * **Redesigned Event Index**: Includes responsive design, reorganized columns, distribution widgets, humanized timestamps, and consolidated action icons into a dropdown menu.
    * **Navigation Changes**: Main navigation is reorganized for better clustering and utilizes fly-out menus.
* **Faster Organization Logo Loading**: The **Event Index** now uses a new dedicated endpoint for loading organization logos, utilizing cached images instead of base64 decoding live, resulting in much faster rendering.
* **Action Modules for Workflow**: New **Action modules** are available to **add tags based on [MMDB](https://github.com/adulau/mmdb-server) and vulnerability information from [vulnerability-lookup.org](https://vulnerability.circl.lu/)**, enhancing automated data enrichment workflows.

## Changes and Improvements

* **Warninglists**: Updated to the latest version which includes many new warning-lists.
* **Bookmarks**: The `url` field has been changed to `text` to support long URLs (Fixes #10564).
* **RegExp View Migration**: The Regular Expression views have been migrated to the factory pattern.
* **Upgrade Script Optimization**: MISP updates and database update commands have been removed from the standard upgrade script as they now run automatically.
* **Vulnerability Lookup Update**: Switched the external reference for vulnerability lookups from `cvepremium.circl.lu` to `vulnerability.circl.lu`.

## Fixes

* **Sharing Groups**: Fixed an issue where **sharing groups edit** could become inoperable under certain conditions.
* **REST Search**: Added `org_id` and `orgc_id` filters to `restsearch`.
* **On-Demand Correlation**: Fixed an issue where long `value2` values were breaking event loading during on-demand correlation.
* **Correlation**: Fix for **ipv4-mapped ipv6 address handling** to ensure correct correlation logic.
* **Dashboard**: Fixed an issue with the add function in the dashboard.
* **OpenAPI**: Aligned the sharing group blueprint to correctly add the `sharing_group_id` definition.
* **General**: Minor fixes for variable handling, regexp generator issues, and notice errors.

## 🛡️ Security Fixes

This release includes important fixes for several vulnerabilities:

* **[GCVE-1-2025-0040](https://vulnerability.circl.lu/vuln/GCVE-1-2025-0040), [GCVE-1-2025-0039](https://vulnerability.circl.lu/vuln/GCVE-1-2025-0039), [GCVE-1-2025-0038](https://vulnerability.circl.lu/vuln/GCVE-1-2025-0038)**: This update provides fixes for additional regression on different security security fixes and source code review.  
* Resolved **further XSS vectors** discovered during regression testing of sharing group edit functionality.
* Fixed a **possible XSS vulnerability** via a malicious `external_baseurl`.
