---
title: "MISP v2.5.35: Decomposed Event Views, Overmind UI Enhancements, Security Hardening and MISP-STIX major update"
author:
 - MISP Project team
date: 2026-03-19
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/uav.png
---

The MISP v2.5.35 release introduces significant architectural improvements to the Event View, massive performance optimizations for attribute searching, and critical security hardening for installers. This version marks a major step forward in the "Overmind" UI project, transitioning toward a more modern, responsive user experience.

This version also includes all the update for the [latest version of misp-stix](https://www.misp-project.org/2026/03/16/misp-stix_indicator_and_observable_fingerprinting.html/) which includes significant changes.

### 🚀 Key New Features

#### **Decomposed AJAX Event View**
To improve performance and user experience, the monolithic `view()` action has been split into lightweight, purpose-built AJAX endpoints. This allows for asynchronous loading of event components.
* **New Endpoints:** `view2()` (metadata shell), `viewAttributes()`, `viewObjects()`, `viewRelatedEvents()`, and `viewWarninglistHits()`.
* **EventTest Theme:** A new reference UI implementation demonstrating these endpoints, featuring paginated attributes, quick filters, and a flatten toggle.
* **Performance:** A new correlation dispatcher enables efficient per-page correlation loading rather than loading all correlations for an entire event at once.
* **Availability:** This endpoint is only available on the Overmind theme, if themeing is enabled on the instance. We encourage communities to give the rework a shot and let us know about what they think of the new paradigm.

#### **Enhanced Attribute Search**
Significant rework has been done to the `restsearch` functionality to handle large datasets more efficiently.
* **Cursor-based Pagination:** Moved from traditional offsets to a cursor-based approach to eliminate performance degradation on deep pagination.
* **Benchmarking Suite:** A new benchmark suite and comparison tool have been added to track and document search pipeline performance.

#### **"Overmind" UI Project Evolution**
The ongoing UI modernization (Overmind) has reached several milestones:
* Transitioned from jQuery to **Vanilla JS**.
* Integrated **Tom Select** for improved dropdown and selection interactions.
* Added mass-select actions for publication, deletion, and export within the Event Index.
* Improved Card View, filtering bars, and navigation theme selection.

### 🛡️ Security & Installer Hardening
Following an audit by **The Scottish Cyber Coordination Centre (SC3)**, the installation scripts for Debian (12, 13) and RHEL 9.4 have been significantly hardened:
* **Credential Management:** Credentials moved to `/root/misp_settings.txt` with `600` permissions.
* **Secure API Capture:** Switched to `mktemp` for API key capture to prevent predictable path vulnerabilities.
* **Integrity:** The installer now performs a hard-fail on any Composer checksum mismatch.
* **Idempotency:** Improved re-run safety for MariaDB tuning, Supervisor configurations, and system symlinks.

### 🔧 Notable Changes & Fixes
* **Core Updates:** Taxonomies, Warning-lists, MISP-Galaxy, and MISP-STIX have all been updated to their latest versions.
* **Attribute Search:** Default ordering for `restsearch` has changed to accommodate the new cursor logic (though this can be overridden if a specific order is required).
* **Fixes:** * Fixed a bug where exporting attributes when pivoting from a Galaxy Cluster was broken (#10697).
    * Sticky headers for the attribute list in the event view (#10701).
    * Restored JavaScript functionality for "trigger all checkboxes" in the Overmind UI.
    * Hardened the installer to use the correct MariaDB service name instead of the `mysql` alias.

### Documentation
* **New developer documentation:** Attribute search internal pipeline documentation added.
* **Attribute search documentation:** Added.

### 📦 Requirement Updates
* **PyMISP:** Bumped to the latest version.
* **MISP-STIX:** Minimum version requirements updated to ensure compatibility with recent search pipeline changes.

