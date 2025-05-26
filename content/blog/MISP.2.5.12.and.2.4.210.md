---
title: MISP 2.4.210 / 2.5.12 released with many improvements, UI enhancement and various fixes 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-05-14
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release provides a critical round of **security fixes**, significant improvements to **attribute validation**, and UI enhancements for event views and analyst workflows. Multiple components including Galaxy, STIX, and warning lists were also updated. Special attention has been given to improving compatibility, performance, and documentation.

## Changes

- Added a default value for `extendedEvents` in the event index to avoid undefined behavior.
- Database schema updated to support recent improvements.
- Console: Updated `ls-shell` for compatibility with LS25.
- Documentation:
  - Clarified upgrade steps from MISP 2.4 to 2.5.
  - Added warnings related to potentially unsafe configuration defaults.
- Attribute Validation:
  - Extended validation for `vulnerability` attributes across all supported ID formats (via vulnerability-lookup).
  - Included missing sources and syntax corrections.
- UI Enhancements:
  - Split "Known Identifier" from "False Positive" indicators in the event view.
  - Introduced optional display of extended events in the index.
- Component Updates:
  - `misp-stix`, `misp-galaxy`, and `warning-list` were updated to the latest versions.
  - OpenPhish feed now points to a more stable and officially supported GitHub-based URL.

### Authentication Enhancements
- Improved support for multiple authentication methods (OTP/OIDC).
  - Fixed issues related to route loading when combining multiple auth methods.

## Fixes

### Security Fixes

Addressed multiple vulnerabilities reported by Lassi K. (Second Nature Security), including:

- Reflected and stored XSS in:
  - Server edit view
  - User login profiles
  - Show attribute tag view
  - Server comparison tool
  - Feed configuration (with tag collections)
  - Attribute replacement tool
  - Galaxy JSON views
  - REST client when rendering malicious JSON in HTML mode
  - Thread views (blind fix)
- Clarified the behavior of `download_attachments_on_load` setting to highlight its security implications.

### Other Fixes and Improvements
- Analyst Tools:
  - Fixed search filter in analyst data index.
  - Ensured organizational checks use UUIDs, not numeric IDs.
- Internationalization and UI:
  - Hid unnecessary "extending" columns in views.
  - I18n-related adjustments.
- General stability:
  - Merged key improvements from `develop` and `2.4-develop` branches.

## Other Notable Updates
- Merged multiple PRs from the community for doc fixes, schema sync, and feed consistency.
- Continued integration of `develop` and `2.4-develop` into stable branches to ensure alignment.
- Enhanced usability and configuration reliability across multiple MISP plugins and tools.

## Upgrade Notes

All users are strongly encouraged to update due to the high number of security vulnerabilities addressed and improvements in validation and compatibility. Pay close attention to:
- Authentication method configurations (especially mixed OTP/OIDC).
- Extended vulnerability attribute checks.
- REST/HTML rendering behavior in external clients.

Refer to the [MISP GitHub repository](https://github.com/MISP/MISP) and upgrade documentation for migration best practices.

