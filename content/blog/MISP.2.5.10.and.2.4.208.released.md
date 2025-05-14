---
title: MISP v2.4.208 and v2.5.10 Released with Many Bugs Fixed 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-04-04
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release introduces important security fixes, enhancements in authentication plugin handling, and better cache management in the workflow editor. It also updates various MISP components and improves remote sync behavior.

## Changes

### General Improvements
- Updated documentation to clarify how to enable the `OidcAuth` plugin via `bootstrap.php`.
- Introduced support for loading authentication plugins based on configuration settings.
- Added a new configuration option to escape LDAP filters in `LdapAuth`.
- Updated component packages:
  - `misp-stix`
  - `misp-objects`
  - `warning-lists`
  - `misp-galaxy`

## Fixes

### Security Fixes (2.4.208)
- Resolved **stored XSS vulnerabilities**:
  - In Galaxy killchain elements.
  - In icon elements.
- Addressed **potentially insecure defaults** in `uploadFile/deleteFile`'s `type` parameter (requires a misconfiguration to be exploitable).
- Ensured **S3 access keys** are not exposed in plugin settings.

*Security issues reported by Patrik Wallström of Cparta Cyber Defense.*

### Sync and Validation
- Added warning logging for remote server version mismatches during sync.
- Introduced validation for S3 bucket prefix when deleting events.
- Fixed comment handling in warning lists, especially for list types like CIDR blocks.
- Bumped `pymisp` version in AppController for compatibility.

### Workflow and UI
- Improved AJAX caching and rendering behavior in the **workflow editor**, especially for `select_options_url` and chosen elements. (Potential fix for issue #10256)

## Other Notable Changes
- Merged multiple development and feature branches across 2.4 and 2.5 tracks to ensure consistency and integration.
- Regular version bumps and maintenance commits across modules and integrations.

## Upgrade Note

These updates are highly recommended, especially for those using:
- Authentication plugins (OIDC, LDAP).
- Remote sync features.
- S3 storage or Galaxy features.

Be sure to review your configuration for secure defaults and update custom settings accordingly. For more information, consult the [MISP GitHub repository](https://github.com/MISP/MISP) or refer to the latest documentation.
