---
title: MISP v2.4.205 and v2.5.7 Released - Enhancements, Fixes, and Improved Correlation Management 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-02-24
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# Combined Release Notes: MISP v2.5.7 & v2.4.205 (2025-02-24)

The MISP Project is pleased to announce the release of **[MISP v2.5.7](https://github.com/MISP/MISP/releases/tag/v2.5.7) and [v2.4.205](https://github.com/MISP/MISP/releases/tag/v2.4.205)**, bringing several new features, important fixes, and enhancements to improve the overall user experience and platform functionality. This release addresses critical improvements in synchronization filtering, correlation management, and UI enhancements, ensuring a more stable and efficient MISP environment.

### New Features

- **Quick Search for Overcorrelations**: A new feature enabling users to swiftly search for overcorrelations, making data investigation and management more efficient.
- **Test Sync Rules Widget**: A new UI widget to evaluate the number of filtered events under synchronization filtering rules, providing better insights into event propagation and filtering effectiveness.

### Changes & Enhancements

- **Synchronization Rule Enhancements**:
  - The use of **organization UUIDs instead of names** for sync filtering has been implemented, improving accuracy and reducing ambiguity in synchronization processes.
  - Initial work on testing the results of sync rules, offering users more visibility into applied rules.
- **JavaScript & Frontend Improvements**:
  - Updated `gridstack.js` from **v1.0.0 to v1.2.1**, resolving several issues and improving UI responsiveness.
  - Updated `markdown-it` from **v12.3.2 to v14.1.0**, fixing rendering bugs and enhancing markdown support.
- **Galaxy Cluster Search Improvements**:
  - Expanded search scope to include additional fields beyond synonyms, improving search flexibility and accuracy.
- **Updated Documentation & Versioning**:
  - References to the latest stable version updated from **2.4 to 2.5**.
  - Code of Conduct link updated to match the latest stable version.

### Fixes & Stability Improvements

- **Correlation Fixes**:
  - Fixed broken recorrelation in the **2.5 branch**, addressing inconsistencies in event correlation.
  - Avoid overcorrelating events when adding a full event, reducing unnecessary linkages.
- **Bug Fixes in UI & API**:
  - Resolved a bug preventing **galaxy clusters from being added to a galaxy by UUID**.
  - Fixed a **typo in date checking** within the global menu.
  - Improved handling of **attribute-less objects** in event imports to avoid errors.
  - Fixed regression issues in `events/export` affecting multiple formats.
- **Security & Access Control**:
  - Corrected unauthorized access toast removal.
  - Improved ACL (Access Control List) handling.
- **Performance & Backend Stability**:
  - Defaulted **Cerebrate sharing-group pull to roaming mode**.
  - Improved database handling for **TAXII server integrations**.

### Other Updates

- Merging of multiple branches to consolidate changes and ensure stability.
- Incremented `db_version` to accommodate **TAXII proxy changes**.
- Updated various submodules, including **misp-stix, misp-galaxy, and misp-objects**, to the latest versions.
- Various **spelling corrections and UI text improvements**.

Stay tuned for more updates as we continue enhancing the MISP platform for the global cybersecurity community. Your feedback and contributions are always welcome!
