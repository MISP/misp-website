---
title: "MISP v2.5.32 released bringing new workflow capabilities, enhancement, security fix and various bugs fixed"
author:
 - MISP Project team
date: 2026-01-15
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are pleased to announce the release of **MISP v2.5.32**, bringing new workflow capabilities, improvements to attachment handling, security fixes, and multiple dependency updates.

<img width="1514" height="1090" alt="wf2" src="https://github.com/user-attachments/assets/dd985087-d950-47e9-8c17-4c20411c9f02" />
<img width="862" height="934" alt="wf1" src="https://github.com/user-attachments/assets/40df5be8-d001-4187-beaf-dbc271b7fd24" />

## New Features

### Workflow Enhancements
- **Aggregate Comparator Module**  
  New workflow module to aggregate and compare field values, which can then be used in IF conditions.

- **Timestamp Filter Module**  
  New workflow module allowing filtering based on timestamps.

- **Event Deletion Trigger**  
  New workflow trigger to act upon event deletion (`trigger-event-before-delete`).

### Attachment Storage Bucketing
- **Bucketed storage system for file attachments** (fixes #10581)

  Key points:
  - New setting to enable bucketed storage.
  - Files are now stored as:
    ```
    MISP/app/files/bucket_5000/5333/1111111
    ```
    instead of:
    ```
    MISP/app/files/5333/1111111
    ```
  - Fully backward compatible: if a file is not found in the new location, the old path is checked.
  - Helps prevent filesystem issues caused by too many files in a single directory.

### Configurable Forgot Password Email
- The **forgot password email text is now configurable** via the server settings interface (fixes #10591).

## Changes & Improvements

- Version bump.
- **PyMISP updated**.
- **Taxonomies updated** to the latest version.
- **Warninglists updated**.
- **MISP objects updated** to the latest version.
- **MISP galaxy updated** to the latest version.
- **OIDC improvements**
  - Updated `openid-connect-php` dependency to version **1.3.0**.
  - Switched dependency source from JakubOnderka to CertMichelin.
- **Performance improvement**
  - Use of `simdjson_decode_from_stream` for faster JSON decoding from files.
- Removed stray debug statement in object:debug.

## Fixes

- **Workflow**
  - Correct return value when errors occur.
  - Renamed `toggle` to `enable` in `ids-operation` module (as reported by @Andurin).

- **Dashboard**
  - Fixed export functionalities not being aware of the Gridstack change.

- **Password Policy**
  - Moved logic higher to avoid unset rules after failed password change attempts.

- **Security**
  - Fixed XSS issues in crafted URLs requiring user interaction (reported by Mathis Franel). [ GCVE-1-2026-0003](https://vulnerability.circl.lu/vuln/gcve-1-2026-0003)

## OIDC & Proxy Handling

- Fixed OIDC proxy bug related to proxy settings.
- New OIDC auth setting to **skip or enforce global MISP proxy settings**.
- Improved backward compatibility with older OIDC clients.

## Contributors

The following people contributed to this release:

- Sami Mokaddem  
- iglocska  
- Alexandre Dulaunoy  
- Raphaël Vinot  
- Maxime Escourbiac  
- Jakub Onderka  
- Luciano Righetti  
- Andras Iklody  
- Mathis Franel

For full details, please refer to the commit history and [changelog](https://www.misp-project.org/Changelog.txt).


