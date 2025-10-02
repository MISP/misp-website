---
title: MISP 2.5.22 released with improvements and bugs fixes
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-10-02
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are pleased to announce the release of **MISP v2.5.22**.  

This release brings new features, improvements, fixes, and important updates to keep MISP stable and up to date.

## 🚀 New
- **Forgejo Actions**: Added the synchronisation workflow.

## 🔧 Changes
- Version bump.
- **Event Report View**: Better support for extended events
  - All children of the current event are visible.
  - All children of the parent of the current event are visible.
- Schema bump.
- **MISP Galaxy**: updated.
- **Warning-lists**: updated to the latest version.
- **Taxonomies**: updated to the latest version.
- **MISP Object**: updated.

## 🐛 Fixes
- **Forgejo Actions**: Updated PATH for synchronisation CI.
- Attribute search form inputs now correctly filled with values from named URL parameters.
- **Event Report View**: Fixed MISP element cache to prevent override by parent data.
- **Indexing**: Improved handling for high performance indexing in value-based event search.
  - Handles non-existent `value1/value2` indices gracefully with fallback.
- **REST Search**: Added complex query support to value filter.
- **Event**: Switched Correlation and Warninglist filtering option.
- **Attribute Search**: UUID field now behaves as expected.
  - Allows numeric IDs for events.
  - Maintains proper behavior when using valid UUIDs.
- Check PyMISP version in submodule, AppController, and requirements.


## 📦 Other
- Various merges from `develop` and `2.5` branches.
- Forgejo pipeline for synchronisation.
- Support for creating locked events on feed pulls.
- Set correct property on new events.


## 🙏 Authors
This release was made possible thanks to the contributions of:

**Thomas Lacroix (ThomasLcr), iglocska, Sami Mokaddem, Alexandre Dulaunoy, Jeroen Gui, Karsa Rigó, Raphaël Vinot, Sid Odgers**


📦 [Download the release](https://github.com/MISP/MISP/releases/tag/v2.5.22)  
📚 [Upgrade guide](https://misp.github.io/MISP/INSTALL/)  

