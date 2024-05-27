---
title: MISP 2.4.192 released with many performance improvement, fixes and updates. 
date: 2024-05-07
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

### New Features
- **Security Enhancements:**
  - Ability to disable TOTP/HTOTP when linked to an identity provider with strong authentication.
  - Introduced Fast API Authentication with temporary storage of hashed API keys in Redis to enhance endpoint performance.

- **Logging and Tracking:**
  - Enhanced detailed tracking sent to Sentry as breadcrumbs.

- **User Interface Improvements:**
  - Addition of missing views for analyst data to enhance UI functionality.

### Changes
- **Performance and Functionality Improvements:**
  - Updated CRUD operations to support afterFind in the delete function.
  - Removal of redundant UI elements and dependencies, streamlined distribution settings, and enhanced event view loading.
  - Upgraded warning lists, MISP galaxies, and MISP objects to the latest versions.
  - Simplified JSON structure updates and UI enhancements, including a nicer menu design.

- **Configuration and Security Settings:**
  - Improved role management with OIDC and adjusted security settings to disable password resetting when changes are disabled.

### Fixes
- **Security and Stability Fixes:**
  - Addressed various security concerns including fixing redirect loops, removing redundant security tests, and patching stored XSS vulnerabilities.  CVE-2024-33855
  - Restored and fixed the Email OTP feature and ensured the proper functioning of external authentication.
  - Made several critical fixes in the handling of analyst data and UI operations, like pagination in logs and event view configurations.

- **Optimization and Error Corrections:**
  - Fixed issues in SQL logs, benchmarking, and handling of event indexes related to tags and threat levels.

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt).

