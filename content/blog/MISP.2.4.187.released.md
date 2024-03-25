---
title: MISP 2.4.187 released with security fixes, new features and bugs fixes.
date: 2024-03-24
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

We are pleased to announce the immediate release of MISP 2.4.187, including security fixes, new features and bugs fixes.

### New Features
- **CLI Enhancements:**
  - Added `org list` to shell commands.
  - New command to change user role.
  - Fixes to role management.
- **OIDC Update:**
  - New option `OidcAuth.update_user_role` to disable role changes from OIDC.

### Changes
- **Version and Software Updates:**
  - Version bump.
  - Updates to PyMISP, misp-galaxy, misp-warninglists, misp-objects, and taxonomies.
- **Internal Updates:**
  - Added `ext-zstd` to suggested PHP extensions.
  - Fixed non-focusable relationship dropdown search field in analyst data.

### Fixes
- **General Fixes:**
  - Corrected variable unset in events:restsearch to prevent attribute override.
  - Ensured sync pulls continue after an event save failure.
  - Database update fixes for older MySQL versions.
  - Improved API consistency.
  - Fixed pulling from remote servers when analyst data is not supported.
  - Logging fix for `removeTagFromObject()`.
  - Security improvements for file and logo uploads.  (Thanks to Rémi Matasse and Raphael Lob from Synacktiv for the report)
      - [CVE-2024-29859](https://cvepremium.circl.lu/cve/CVE-2024-29859) < MISP 2.4.187 - add_misp_export in app/Controller/EventsController.php does not properly check for a valid file upload.
      - [CVE-2024-29858](https://cvepremium.circl.lu/cve/CVE-2024-29858) < MISP 2.4.187 - __uploadLogo in app/Controller/OrganisationsController.php does not properly check for a valid logo upload.
  - Correct message display when disabling a galaxy.
- **CLI Updates:**
  - Added new functionalities including listing roles and creating users.

Details changes are available in [Changelog](https://www.misp-project.org/Changelog.txt).

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

