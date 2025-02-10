---
title: MISP 2.4.204 and 2.5.6 released including new features, performance improvements and many other improvements. 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-01-13
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# Combined Release Notes: MISP v2.5.6 & v2.4.204 (2025-01-03)

The MISP team is excited to announce the release of **MISP v2.5.6** and **MISP v2.4.204**. These updates bring several new features, fixes, and performance improvements to enhance the platform's usability and efficiency. Here’s a summary of the key changes:

## Highlights of MISP v2.5.6

### Changes
- Improved **correlation engine performance**:
  - Splitting attribute correlation lookups into two distinct queries on `value1` and `value2` for optimized MySQL performance.
- Updated Continuous Integration (CI) process:
  - The `Check if Redis is ready` task is now executed earlier in the update sequence.
- Reduced memory usage when fetching index data from Redis cache.
- Schema diagnostic improvements via CLI.

### Fixes
- Eliminated a **duplicate correlation condition** for cleaner results.
- Reintroduced **advanced correlations** to the engine, offering a faster (albeit hacky) solution.
- Adjusted **user settings ACLs** for a more balanced approach, ensuring proper alignment with descriptions.
- Resolved **security vulnerabilities**:
  - Addressed reflected XSS in server settings reload.
  - Tightened enforcement of the `disableUserSelfManagement` feature to prevent users from modifying their settings when disallowed.
- Fixed **recursion issues** in the `analystdata/view` endpoint.
- Temporary fixes for broken analyst data views.

### Other Updates
- Added the **Threatmon MISP Community**.
- Merged various contributions from the community, improving Redis optimizations and internal functionality.

## Highlights of MISP v2.4.204

### Changes
- Enhanced **AuditLog filtering** with support for `SharingGroupOrg` and `SharingGroupBlueprint` options.
- Added creation timestamps to **application logs** for better tracking.
- Improved **category and types generator** tools.

### Fixes
- Enhanced **authkeys** to accept `user_id` via URL parameters or JSON body.
- Corrected descriptions for the **TrendingAttributesWidget**.
- Addressed **ACL inconsistencies** and fixed issues in sharing group blueprints.
- Resolved **security vulnerabilities**:
  - Reflected XSS in server settings reload.
  - Further tightened user self-management restrictions.
- Fixed multiple **analyst data view issues**, including recursion and broken views.
- Corrected response handling for API endpoints involving GalaxyClusterRelation and SightingsDB.

### Other Updates
- Integrated the **Threatmon MISP Community**.
- Merged several pull requests addressing typos, API enhancements, and overall improvements.

## Special Thanks
We extend our gratitude to contributors such as **Jeroen Pinoy**, **Jakub Onderka**, **Luciano Righetti**, **Tom King**, **Kadir YAPAR**, and many others for their efforts in improving the platform.

## How to Update
To benefit from these improvements, update your MISP instance by following the [official MISP update guide](https://www.misp-project.org/installation/).

Stay tuned for more updates as we continue enhancing the MISP platform for the global cybersecurity community. Your feedback and contributions are always welcome!

