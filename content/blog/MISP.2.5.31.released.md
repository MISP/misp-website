---
title: "MISP v2.5.31 released - Stability, Synchronization Improvements & Year-End Knowledge Base Refresh"
banner: /img/blog/uav.png
author:
 - MISP Project team
date: 2025-12-23
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP v2.5.31 Release Notes  
📅 **Release date:** 2025-12-23

## Stability, Synchronization Improvements & Year-End Knowledge Base Refresh

We are happy to announce the release of **MISP v2.5.31**, a maintenance-focused update bringing refreshed knowledge bases, UI refinements, improved synchronization behavior, and several important fixes.  

Alongside this release, **[misp-modules v3.0.5](https://github.com/MISP/misp-modules/releases/tag/v3.0.5)** has also been released and is recommended for full compatibility.

## ✨ Highlights

- Updated [taxonomies](https://www.misp-project.org/taxonomies.html), [galaxies](https://www.misp-galaxy.org/), warning lists, and [object templates](https://www.misp-project.org/objects.html)
- Improved sharing group synchronization logic for sync users
- Minor but useful UI cleanups and performance fixes
- Refinements to OpenAPI specifications
- Ongoing cleanup and correctness improvements in tests

## 🔄 Changes

### Knowledge & Data Updates
- Updated taxonomies
- Updated misp-galaxy (multiple updates)
- Updated misp-objects
- Updated warning-lists
- Updated GeoOpen to the latest version

### UI & UX
- Minor UI changes and cleanup
- Fixed a minor date display issue
- Removed the sighting sparkline from the tags index due to performance concerns
- Cleaned up leftover characters in event organization names

### Configuration & Behavior
- Default sighting visibility is now set to **“Everyone”** instead of **“Event Owner”**
- Refactored object template element tables
- Migrated object template index view to the factory pattern
- Improved OIDC client behavior by honoring proxy configuration

## 🐛 Fixes

- Removed incorrect or misleading tests whose premises were invalid
- Corrected test logic around sharing group editing by sync users
- Relaxed sharing group saving rules for sync users:
  - Sync users can now update sharing groups they can see
  - Updates can be pushed via different sync connections than the original source
- Prevented deletion of Regexp entries when type is set to `All`
- Preserved checkbox state in Regexp edit views
- Fixed SERPRO reputation feed freetext configuration

## 📘 API & Specification Improvements

- Refined the OpenAPI specification for `exportGalaxyClusters`:
  - Documented additive inclusion behavior for `default` and `custom` parameters
  - Allowed `distribution` to be specified as an array, matching existing backend behavior

## 🔧 Miscellaneous

- Enhanced sorting in `generic_picker.ctp` to prioritize the most relevant entries
- Added NOCACTI Adversary Infrastructure / Intrusion feeds
- Multiple branch merges and maintenance updates
- Updated default configuration files

## 🧩 Companion Release

- **[misp-modules v3.0.5](https://github.com/MISP/misp-modules/releases/tag/v3.0.5)** has been released and is recommended for use with this version of MISP.

## 🎄 Seasonal Message

The entire MISP team wishes you **happy holidays** and would like to warmly thank all contributors, users, intelligence analysts, operators, and supporters for making **2025 an impressive year** for the project.  
While we are keeping things intentionally a bit behind the scene, rest assured that **2026 is already shaping up with several exciting new services and evolutions for the MISP project**. More to come… 😉

Thank you for being part of the MISP community, and happy threat sharing! 🧠🔗

