---
title: MISP 2.4.211 & 2.5.13 Released - A Double Dose of Security, Search, and Stability 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-06-06
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are excited to announce the parallel release of two new MISP versions: **2.5.13** for our latest branch and **2.4.211** for the 2.4 branch. These releases are packed with critical security patches, a major overhaul of the search functionality, and a host of improvements and bug fixes to enhance your threat intelligence experience.

Many of the fixes and improvements have been backported to the 2.4 branch, ensuring all our users benefit from a more secure and stable platform. Let's dive into what's new.

## 🔒 Critical Security Vulnerabilities Patched

Security is our top priority, and these releases address several important vulnerabilities. We strongly advise all users to update their instances as soon as possible.

*   **SMIME Path Traversal (Phar Deserialization):** A significant vulnerability was discovered that could allow a rogue administrator to set arbitrary file paths for SMIME via the GUI or API. This could be abused for attacks such as Phar deserialization. We thank **Raimonds Liepins** (https://raimonds-liepins.com) for reporting this issue.
*   **Dangerous Object Edit Endpoint:** A flaw in an object editing endpoint has been fixed. This could have potentially led to attribute ID overwrites, corrupting event data.
*   **Log Search ACL Bypass:** We've patched a vulnerability that could allow for the circumvention of some Access Control List (ACL) restrictions when searching through the logs.

## 🚀 A Revamped Search Experience

One of the biggest changes in these releases is a complete rework of the attribute and log search functionalities.

Previously, complex searches using GET requests could hit URL length limits and cause issues with pagination. To solve this, we've brought back a more robust solution:

*   **Searches now use `POST` requests again.**
*   A **token-based system** has been implemented to manage search queries. Your search parameters are now stored securely in Redis and accessed via a token.
*   **The benefit?** This allows for flawless pagination on even the most complex queries and enables you to have multiple, independent search tabs open simultaneously without interference.

## ⚙️ API Enhancements and New Features

The MISP API continues to evolve, becoming more powerful and intuitive with each release.

*   **New Event Filtering:** You can now filter events on the index and via the REST API based on whether they are `extending` another event or are `extended` by one.
*   **Warninglist Filtering in Attribute Search:** The `/attributes/search` endpoint now supports filtering based on warning lists.
*   **Improved API Syntax:** To avoid confusion, the old `extend[ing/ed]` parameter for merging data has been renamed to a more descriptive `include_*` syntax. The `extended` and `extending` flags now consistently accept boolean values like `0` and `1`.
*   **Flexible Content-Type:** The API is now more flexible, allowing you to define the desired response format directly in the `Accept` header.

## ✨ Usability and Data Management Improvements

We've also rolled out several quality-of-life improvements to make your daily operations smoother.

*   **Attachments:** You can now add attachments directly via the quick-add attribute form, and attachments are correctly preserved when you group multiple attributes into a MISP object.
*   **Galaxy Clusters:** An update process has been added to ensure that when a galaxy is updated, its local ID is correctly reassigned, preventing inconsistencies during synchronization.
*   **Analyst Data:** The analyst data view for organizations has been cleaned up to show only the most relevant fields.
*   **Event Reports:** You can now look up event reports by their UUID.

## 🔧 Other Notable Changes and Fixes

For our instance administrators, a small but important change has been made to `bootstrap.php` to load `cakeresque` if `simplebackgroundjobs` aren't enabled. But please, enable `simplebackgroundjobs`. As the commit message wisely states: _"For every new installed instance using cakeresque, cthulhu kills a kitten."_

As always, core components have been updated to their latest versions, including **misp-galaxy**, **misp-objects**, **taxonomies**, and **warning-lists**, bringing in the latest community contributions.

---

## Acknowledgements

These releases would not be possible without the hard work of our development team and the invaluable contributions from our community. A huge thank you to iglocska, Sami Mokaddem, ThomasLcr, Alexandre Dulaunoy, Christophe Vandeplas, Luciano Righetti, and everyone who reported bugs, submitted pull requests, and helped us improve MISP.
