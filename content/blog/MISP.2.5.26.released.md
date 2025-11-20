---
title: MISP v2.5.26 - released with performance improvements and interoperability fixes 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-11-20
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release brings new features focused on **performance improvements**, **logging enhancements**, and **data standardisation** with the introduction of the UUID attribute type. It also includes several important bug fixes and dependency updates.

###  New Features

* **Event Linking with UUIDs**: Added an option to prioritize creating event links using **UUIDs** instead of traditional IDs, where possible, improving consistency across distributed systems.
* **Performance Optimizations**: Introduced new **database indices** to significantly enhance overall MISP performance.
* **JSON Syslog Support**: A new option allows saving syslog messages in **JSON format** for better logging sanity and easier processing. (Fixes #10539).
* **UUID Attribute Type**: Added a dedicated **UUID attribute type** to meet requirements from standards like FlowIntel and object templates, offering a better alternative to using text fields for unique identifiers.

### ⚙️ Changes & Updates

* **misp-stix Improvements**: Updated `misp-stix` to feature **better STIX 2 input handling**. This update helps prevent issues when loading content or files that might contain an invalid STIX 2 format produced by some non-compliant TIP platforms.
* **Dependency Bumps**: Updated numerous dependencies, including **PyMISP**, `requirements.txt`, and the requirement for **taxii client version**.
* **Object & Data Updates**:
    * **misp-object** updated.
    * **warning-lists** updated to the latest version.
    * **misp-taxonomies** updated to the latest version.
    * **misp-galaxy** updated to the latest version.
    * **misp-objects** updated to the latest version.
* **Frontend Cleanup**: Removed reference to the non-existing `vis.map` file in `vis.js`.

### 🛠️ Fixes

* **Security**: Forced **stronger cipher suites** to be set as the default, enhancing security (reported by Jakub Tomaszewski of Zigrin Security).
* **Attribute Validation**: Added validation for **Attributes of type `uuid`**.
* **Code Cleanup**: Removed the use of `eval` from `doT.js` in favor of `globalThis`.
* **UI Fix**: Corrected the event ID link in the **side menu**.
* **Object Enrichment Fixes**: Several **bugs in object enrichment** have been fixed.
