---
title:  MISP 2.4.202 and 2.5.4 released with numerous enhancements including analyst data, bug fixes, and security improvements
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2024-12-24
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

## Changes

### Configuration
- **Base URL Setting**: Added a new setting to skip base URL coercion for the framework. This resolves issues when running MISP under a subdirectory but may have adverse effects for other setups.

### Settings
- **REST Client Settings**: Enhanced security by tightening REST client-related settings:
  - `rest_client_baseurl` is now CLI-only.
  - Updated `rest_client_enable_arbitrary_urls` description for clarity.
- **Removed Unused Setting**: `Security.disable_form_security`, a legacy setting for testing purposes, has been removed.

### Updates
- **Taxonomies, Warning Lists, Objects, Galaxy**: Updated to their latest versions.
- **MISP-STIX and PyMISP**: Updated to the latest versions.

### Analyst Data
- Analyst Data objects like Notes and Opinions are now flattened lists attached to their data layer instead of nested.
- Improved handling of analyst data in various endpoints and views.
- Added new metrics for analyst data and event reports.

### UI
- Minor tweaks and improvements.

### Attributes
- Support for adding combinations of tag collection tags and other tags simultaneously.

### Statistics
- Added metrics for analyst data and event reports.

### CI
- Path fixes and branch updates.

## Fixes

### Security
- Resolved multiple vulnerabilities:
  - Stored XSS in `JsonTool::encode()` used in JavaScript.
  - Tightened template elements endpoint to prevent abuse.
  - File upload process improved to prevent abuse.
  - Prevented TOTP secret logging in audit logs.
- Updated encoding in the `upload_file` view element.

### Analyst Data
- Addressed issues with nested data handling and JSON export.
- Fixed data fetching inconsistencies and restored functionality for viewing nested analyst data.

### REST Search
- Adjusted deleted flag behavior to improve results consistency.

### Miscellaneous
- Corrected variable definition, CLI arguments, and template index naming.

## Other
- **Merge Requests**: Integrated various feature and fix branches into `2.4-develop`.
- **Community Additions**: Added Threatmon MISP Community.
- **Custom Image Path Check**: Updated image path validation logic.

This release includes several critical security fixes, updates, and enhancements, improving the overall functionality and stability of MISP. Users are encouraged to update promptly to benefit from the latest improvements and security measures.

