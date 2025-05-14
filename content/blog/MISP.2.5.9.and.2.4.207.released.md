---
title: MISP v2.4.207 and v2.5.9 Released with Many Bugs Fixed 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-03-26
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---
## Summary

This dual release of MISP (versions **2.4.207** and **2.5.9**) brings significant stability improvements, better performance, and architectural refinements, particularly around background job handling, workflow modules, and Galaxy cluster operations.

## Changes

### Core Improvements

- **Background Job Handling**: In `2.5.9`, test actions now use the new **SimpleBackgroundJobs** system (supervisor-based) instead of the legacy **CakeResque** framework. Default supervisor config included.
- **Password Change Flow**: Disabling password change on first login now respects the `disable_user_password_change` setting.

### Testing & Plugins
- ShibbAuth plugin is now enabled before tests run.
- CakeResque plugin is now conditionally enabled and correctly handled in testing workflows (2.5.9 only).

## Fixes

### Shared Across 2.4.207 and 2.5.9
- **Audit Logging**: Avoids recursively fetching user objects when logging, improving performance and avoiding unnecessary database loads.
- **Galaxy Clusters**:
  - Improved disambiguation of UUID origins.
  - Enforced correct ACL usage when fetching related clusters.
  - Fixed broken aliasing in cluster relations.
  - Resolved a query issue.
- **Attribute Save**:
  - Fixed a notice error when `disable_correlation` is not set.
- **Sharing Group Blueprint**:
  - Prevented premature failure during updates.
- **CRUD Components**:
  - Ensures pagination order is defined before use, improving UI consistency.
- **Workflow Engine**:
  - Fixed issues with ad-hoc workflow enablement and value persistence.
  - Optimized tag-based workflow modules (Fixes #10256).

### 2.5.9 Specific Fixes
- Re-enabled CakeResque for test actions during transition to SimpleBackgroundJobs.
- Fixed file paths and plugin initialization related to CakeResque.
- Corrected permission-handling regressions.

## Other Notable Changes
- Multiple development and feature branches were merged for consistency across both 2.4 and 2.5 tracks.
- Audit logging optimizations merged from contributor [Benni0].
- Improvements in test environments and plugin support by [Luciano Righetti].

For a complete list of changes, please refer to the [MISP GitHub repository](https://github.com/MISP/MISP).

We would also just like to remind everyone that MISP 2.5 has been out for a while and the originally announced grace period for 2.4 is coming to an end (2.4 security fixes will continue until the end of the year), we'd like to use this moment to encourage everyone to take a moment to upgrade. There are a host of options for installation or upgrade of MISP 2.5, including an [Ubuntu upgrade script](https://github.com/MISP/MISP/blob/2.5/INSTALL/UPGRADE.ubuntu2404.sh), fresh installation scripts for [Ubuntu](https://github.com/MISP/MISP/blob/2.5/INSTALL/INSTALL.ubuntu2404.sh), [Debian](https://github.com/MISP/MISP/blob/2.5/INSTALL/INSTALL.debian12.sh) and  [RHEL](https://github.com/MISP/MISP/blob/2.5/INSTALL/xINSTALL.rhel94.sh), as well as a production ready [dockerised instance](https://github.com/MISP/misp-docker) (massive shoutout to @ostefano for the incredible effort!)

Not only will this bring the MISP software stack to a more modern standard, but it will also prepare you for the next big chapter in MISP's lifecycle, namely MISP 3.x, which will be a major rework and modernisation of the tool. 
