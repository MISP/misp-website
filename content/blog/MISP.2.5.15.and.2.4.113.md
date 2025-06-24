---
title: MISP 2.4.213 & 2.5.15 Released - A Double Dose of Security, Search, and Stability 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-06-24
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are thrilled to announce a dual release of MISP, bringing significant enhancements to both our stable and development branches with versions **2.4.213** and **2.5.15**.

This release is packed with major reworks under the hood, performance boosts, new features, and a host of bug fixes to improve your threat intelligence experience. A huge thank you to all the contributors who made this release possible!

Let's dive into the key highlights.

## Key Highlights

### 🚀 Correlation Engine Overhaul (Both Versions)

The correlation rule based exclusion engine, has received a major rework. Previously, correlations exclusions based on defined rules were primarily triggered when new data was added and compared against existing data. Now, correlation rules work **bi-directionally**! This means existing data will successfully avoid correlating against newly added information when the rules would prohibit it, ensuring a more consistent way of cleaning your data clean of unwanted correlations.

Additionally, we've improved `event.info` based filtering and fixed UI glitches, making correlation rules more powerful and intuitive.

### ⚡ Performance & Database Enhancements (Both Versions, 2.5 focus)

We've unified the `extended` and `observerextended` database handlers, streamlining the codebase for better maintainability and performance.

You'll see a noticeable **speed-up in object `restSearch` queries**. We've optimized the query builder to prioritize event table lookups and introduced new caps on object lookups. This is designed to drastically reduce CPU load, especially when dealing with massive exports.

### ✨ New Features and UI Improvements

The latest versions introduce several new user-facing features to improve workflow and administrative control:

*   **Import Choice Button:** A new "Import Choice" button has been conveniently placed above the attribute list in the event view.
*   **Role-Based Result Limits:** Administrators can now define a limit on the number of results returned per API request at the role level, giving you more granular control over resource usage.
*   **Enhanced Filtering:** You can now filter attributes based on their `object_relation`, adding another powerful layer to your searches.
*   **Galaxy View Counter:** When viewing a galaxy, you will now see the number of attributes linked to each galaxy cluster, providing immediate context.

---

## Detailed Changelog Summary

Here's a breakdown of the most significant changes across both versions.

### New Features

*   **Correlation Rules Rework:** As highlighted above, correlations are now bi-directional, and event.info filters work correctly.
*   **Database Handler Rework:** Unified `extended` and `observerextended` handlers for a cleaner, more efficient backend.
*   **[v2.4.213] Import Button on Event View:** A new "Import Choice" button is now available directly on the event page.
*   **[v2.4.213] Role-Based API Limits:** Admins can now configure the maximum number of results a user can fetch via the API based on their role.
*   **[v2.4.213] New Search Filter:** Added the ability to filter attributes on `object_relation`.
*   **[v2.4.213] Galaxy Attribute Count:** The galaxy view now displays the number of attributes linked to a galaxy.

### Changes and Improvements

*   **[v2.5.15] Object `restSearch` Speed-up:** Significant performance improvements for object lookups through query optimization.
*   **Updated `misp-stix`:** Both versions include the latest `misp-stix` library with important fixes.
*   **Larger TAXII API Keys:** The database schema has been updated to accommodate "ginormous" TAXII server API keys.
*   **Improved REST Search Docs:** Documentation has been updated to clarify how to specify a galaxy matrix in your `restSearch` queries.
*   **[v2.4.213] Internal Sync:** A potential fix has been implemented for syncing protected events with internal MISP instances.
*   **[v2.4.213] UI/UX Improvements:** The Roles page has been updated with clearer text and a more intuitive layout.

### Notable Fixes

*   **Enrichment Modules:** Enrichment for `first/last_seen` from modules is now correctly supported. This also works for attributes within MISP Objects.
*   **Suricata Export:** Fixed an unsafe string concatenation that could cause the Suricata export to fail.
*   **Attribute Search:** Correctly handles Windows-style line breaks in the search form.
*   **Tag UI:** Clicking a tag on an attribute now correctly redirects to the attribute index instead of a generic search page.
*   **Internal Sync:** Editing the `protected` flag on an event is now considered a significant change and will be properly synchronized.
*   A large number of other fixes related to database handling, comprehensive tests, and UI consistency have been implemented.

### Acknowledgements

A special thank you to the many contributors to these releases, including Andras Iklody, Christian Studer, Sami Mokaddem, ThomasLcr, Alexandre Dulaunoy, Jeroen Pinoy, and many others from the community who reported issues, submitted pull requests, and helped improve MISP.

As always, we encourage you to update your instances to benefit from these latest improvements and fixes. For a complete list of changes, please refer to the detailed [changelog](https://www.misp-project.org/changelog.txt).

