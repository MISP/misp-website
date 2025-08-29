---
title: MISP 2.5.19 brings important fixes, improvements to the on-demand correlation engine, refinements in the task scheduler, and better error handling.
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-08-29
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP 2.5.19 Release Notes

_Release date: 2025-08-20_

MISP 2.5.19 brings important fixes, improvements to the on-demand correlation engine, refinements in the task scheduler, and better error handling.  

This release includes many community contributions — thank you for your continued support and improvements!

## ✨ New Features

- **On-demand correlation**:  
  Added support for *top correlations* in the on-demand correlation engine.

## 🔄 Changes

- Bumped version number.
- Improved exception handling — errors now point users to the error log.
- Scheduled tasks:
  - Restricted to own organisation users.
  - Default user selection now pre-fills with the current user.
- Worker configuration files can differ across environments.
- More descriptive warning messages for the new task scheduler.

## 🐛 Fixes

- **Sync / Events**:  
  Correctly pass fingerprint to `_add` if it exists to avoid issues.
- **On-demand correlation**:  
  Fixed multiple issues with `value2-value2` matching and upgraded the correlation script.
- **Shadow attributes**:  
  Support for accept/discard operations by UUID.
- Removed obsolete `periodic_summary` from server options.
- **Stack traces**:  
  Now show the actual origin of errors.
- **Attribute search** rework:  
  - Downloaded results now match UI results.  
  - Added additional fields for CSV export.
- **Attribute / Add**:  
  Correctly adhere to provided tag locality in `/attributes/add`.
- **Workflow editor**:  
  Running a workflow in debug mode now shows the expected response.
- **Logs controller**:  
  Fixed broken named params search (#10424).
- **Tag index improvements**:  
  - Removed edit/distribution graph icons from the tag name field.  
  - Fixed notice error for regular users (`maymodify` always set to `false`).
- JSON parsing fixes for authentication key IP lists.

## 🧩 Other Improvements

- Updated `bootstrap.default.php`.
- Multiple branch merges and code cleanups from community contributions.
- Fixed JSON parsing error for `ip-port` format in auth key handling.

## ✅ Upgrade Notes

- It is recommended to upgrade to this version to benefit from correlation engine improvements, more robust task scheduling, and bug fixes.  
- After upgrade, ensure worker configurations are checked if running across different environments.

## 🙏 Acknowledgements

Thanks to all contributors for their work on this release.  


[MISP Project](https://www.misp-project.org) • [GitHub Repository](https://github.com/MISP/MISP)


