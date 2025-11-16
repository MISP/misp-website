---
title: MISP v2.5.25 - Performance Update 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-11-16
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release introduces a security fix, significant performance improvements for REST searches, new default feeds, and several important bug fixes.

## Security
* Fixed a vulnerability that could expose user passwords in workflows.

## Enhancements & Features
* **New Feeds:** Added three new "hideNseek LAB" Threat Intelligence Feeds (JSON, CSV, and IP Blocklist).
* **Accessibility:** Significantly improved accessibility for screen reader users when editing server settings. Users can now use an ARIA button to switch cells to edit mode, removing the need to double-click.
* **STIX:** The `misp-stix` submodule has been updated to the latest version.

##  Fixes & Performance
* **Performance:** Implemented a major performance fix for attribute-level REST searches that use tag filters. This was achieved by moving to a unioned subquery and removing an inefficient join.
* **REST Search:** Fixed a bug that caused event-level REST searches to fail when searching by tag.
* **UI (Galaxies):** Added the missing sharing group distribution level to the "quick-relation-add" interface for galaxy clusters.
* **UI (Relations):** Corrected an issue with editing cluster relations and improved the confirmation text.
* **UI (Picker):** Restored the correct behavior for the generic UUID picker.
* **Documentation:** The background jobs migration guide has been updated to include the new scheduler worker.
* Fixed a typo in the benchmarks.

## 🧹 Other

* The Mirai tracker project has been discontinued and removed.
