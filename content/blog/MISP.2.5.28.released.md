---
title: "MISP v2.5.28 Release: Security, Dashboard Upgrade, and Community Enhancements"
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-12-11
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP v2.5.28 Release Notes (2025-12-10)

MISP v2.5.28 delivers critical security fixes, a major dashboard upgrade to Gridstack 12, and significant platform stability enhancements. This release includes extensive XSS vulnerability patching, refined tag filtering logic, and better support for Meta Communities.

## Changes

* **Dashboard Update:** Migrated the dashboard to **Gridstack 12**, involving several necessary adjustments.
* **Security & Sanitization:** Improved URL sanitization across the platform.
* **Meta Communities Review:** Enhanced the review process for MISP events shared within meta communities (e.g., CSIRT.SK MISP Community is now vetted).
    * Ensures events follow best practices (e.g., using object templates).
    * Proper utilization of sharing groups.
    * Addition of contextual information.
* **Tag Filtering Logic:** Refined the logic for tag filtering to more tightly decide between using `UNION` or `EXISTS` queries.
    * Uses the `EXISTS` branch for queries with heavier attribute filters to potentially limit the dataset.
    * Uses `UNION` otherwise.
* **Collections Data Redaction:** Redacted the **creator user information** for non-site administrators for consistency.
* **Dependencies Updates:**
    * Updated **CakePHP**.
    * Updated `misp-taxonomies` to the latest version.
* **OpenAPI:** MISP version added to the OpenAPI specification.
* **Cleanup:** Removed unused view files and dead code.
* **Metadata & Communities:** Fixed metadata and updated communities.

## Fixes

A significant number of security and functionality fixes, primarily addressing various Cross-Site Scripting (XSS) vulnerabilities and dashboard issues:

### Security Fixes (XSS)

* **World Map View:** Fixed XSS and restored widget configuration saving in the world map view, which was initially broken by the Gridstack 12 move.
* **Low Impact / High Difficulty XSS:** Fixed multiple low-impact XSS issues.
* **Sharing Group Edit:** Fixed XSS via `external_baseurl` in sharing group edit (requires compromised site admin).
* **Reflected XSS:** Fixed reflected XSS in preview index (requires site admin and user interaction).
* **Workflow Execution Path:** Fixed XSS in the workflow execution path.
* **Actions Table Element:** Fixed XSS via the actions table element.
* **HTTP Method Validation:** Tightened validation of HTTP method types.

### Functionality & Data Fixes

* **Enrichment:** Ensured graceful passing to the next enrichment module if a previous one returns nothing (prevents exceptions).
* **JS Alignment:** Aligned JS function parameters with calls.
* **Map Widget:** Fixed behaviour for correct resizing.
* **Dashboard:** Fixed the functionality for adding a new widget.
* **Proposal Sync:** Correctly captures the proposal's organization context (`orgc`) when PUSHing proposals.
* **Events Index Filtering:** Ensured that filtering using `searchall` ignores deleted attributes.
* **Galaxy Cluster Validation:** Added default value for `collection_uuid` and added UUID uniqueness validation.
* **Analyst Data:** Added missing validation rules.
* **OpenAPI Doc:** Fixed documentation for Galaxy import.

## Other

* Includes various branch merges and minor updates.
* Added **installation guide for OpenBSD 7.8**.
* Updated `defaults.json` with a new entry for the Slovak CSIRT.SK MISP Community.

