---
title: MISP v2.5.27 - released with new features and various fixes 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-11-27
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release delivers important new modules, major internal performance optimisations, updates to validation logic, and several security fixes. A large amount of work focused on improving JSON handling, filter pipelines, encoding performance, and overall system robustness.


## New Features

### Schema & Modules
- **JSON schema updated** to match the latest 2.5 features.
- **New workflow module:** `flowintel-create-case` added. [flowintel](https://github.com/flowintel/flowintel)
- **Attribute fetcher pipeline created and reorganised.**
  - Includes early attempts at improving query optimisation.

## Changes

### Internal Improvements
- Reworked internal JSON handling:  
  - Use **JsonTool** for template generation.  
  - Prefer **SimdJsonBase64Encode** when `simdjson_php` is available.  
  - Use `json_encode` native unicode escaping.  
  - Use `simdjson_encode_to_stream` for events and large arrays.  
  - Use `simdjson_encode` when the extension is installed.  
- Optimised handling of **compressed requests**, including **zstd support**.
- Use data file for **postsemail background job**.

### Platform & Pipelines

- **Warning-list** updated to the latest version.
- **Webhook workflow module:** stronger parameter validation.
- **Index tuning** continues.  
  - Working to resolve a major performance bottleneck.
- **Filter pipeline:** several iterations and reworks.

### CI / Infrastructure
- CI added for feature branch workflows.

## Fixes

### Versioning
- Fixed version string and applied version bump.

### Internal
- Prevent decoding compressed content twice in error controller.

### UI / UX
- Updated handling of `last_login` to use the latest value after `_postlogin->updateLoginTimes` (fixes #10487).

### [Security](https://misp-project.org/security/) Fixes

- **Path traversal fixed** in site-admin picture view.  
  - Reported during *Hack the Government 2025 (Belgium)*.
- **Reflected XSS** issues fixed in two forms.  
  - Reported by an external security researcher.

### Other Fixes
- Redirect fix for `/users/index` for all non-siteadmins (fix #10543).
- **MAC address** validation tightened.
- **Telfhash** validated as hex-only.
- Multiple fixes to tag filter logic and join conditions.

## Summary

This release focuses heavily on internal performance enhancements, validation improvements, new workflow capabilities, and critical security patches. The team continues to push forward on improving scalability, pipeline reliability, and robustness of the 2.5 branch.


