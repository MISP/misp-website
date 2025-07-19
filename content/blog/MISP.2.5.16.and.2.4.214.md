---
title: MISP Releases v2.5.16 & v2.4.214 - A Major Leap in Performance and Stability 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-07-19
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are thrilled to announce two new releases for the MISP project: a significant feature and performance release, **v2.5.16**, and a stable maintenance release, **v2.4.214**.

While v2.4.214 is a focused maintenance update, v2.5.16 is packed with new tools, major performance enhancements, and a host of crucial bug fixes that will make your MISP instance faster and more robust than ever.

Let's dive into what's new!

## ⭐ The Star of the Show: MISP v2.5.16

This release is all about **performance**. We've introduced new tools and refactored core components to make searching, correlating, and managing data significantly faster, especially on large-scale instances.

### 🚀 New Performance Toolkit: `cake Admin runDBScript`

For administrators looking to get the most out of their hardware, we've introduced a new console script to apply performance-enhancing database indexes.

You can now run `cake Admin runDBScript` with two new powerful options:

![MISP Performance Improvement with runDBScript](https://github.com/user-attachments/assets/4b465d4c-e9e4-435d-a6c0-d16456d19282)

*   **`highPerformance`**: This script re-indexes events, attributes, objects, and default correlations for much more performant queries. It will incur a disk space and RAM cost, but the speed improvements are substantial.
*   **`indexLogs`**: Adds indexes to the log table, allowing for rapid searching and auditing of logs.

> **Heads-Up!** A friendly warning from the development team:
>
> > Don't run these if you run MISP on a potato. Potatoes are known to have less than 16GB of RAM.

These scripts are re-runnable and error-resilient, making future updates and maintenance a breeze.

### ⚡ Under the Hood: Major Query Refactoring

The performance gains don't stop at new indexes. We've made fundamental changes to how MISP fetches data:

*   **Attribute Fetcher Rework**: We've moved from complex application-level logic to more efficient database `JOINs` (including `STRAIGHT_JOIN` where supported) for fetching attributes. This significantly reduces query time and complexity.
*   **Correlation Engine Rework**: A bug that caused overly aggressive de-correlation has been fixed. More importantly, the entire correlation process has been optimized to avoid performance-killing `NOT IN()` queries, now using temporary tables for much faster execution.
*   **Event `restSearch` Fix**: A massive performance drain has been resolved in the `restSearch` API. A bug was causing negative tag filters to be applied incorrectly, leading to slow queries and incorrect results on large instances. This fix alone can dramatically improve API responsiveness.

### 📊 Enhanced Logging and Benchmarking

To help you diagnose and monitor your instance, we've added several new tools:

*   **NDJSON Error Logs**: Error logs can now be generated in NDJSON format for easier parsing and integration with modern logging systems.
*   **SQL Slow Log Endpoint**: A new endpoint is available for benchmarking, allowing you to identify and analyze slow SQL queries directly from MISP. You can filter by controller/action and paginate through the results. You can also consider the threshold for what you consider to be a slow query. 
*   **Purge SQL Benchmark Logs**: Keep your logging data tidy with a new function to purge old benchmark logs.
*   **Error log details**: Added information about the user that caused an exception to be thrown as well as the exact place in the codebase that caused the exception
* 
<img width="1552" height="228" alt="image" src="https://github.com/user-attachments/assets/664e070a-cc46-4175-ba72-1af5b5a98c30" />


### ✅ Key Fixes and Enhancements

This release is packed with fixes. Here are some of the highlights:
*   **STIX Imports**: Imports are now more robust, correctly handling edits to existing events and including the original format name in the metadata.
*   **TAXII Server**: Fixed boolean validation issues that could cause unexpected behavior.
*   **Attribute Search**: Corrected a bug where an invalid organization name would cause the org filter to be ignored. Searches containing special characters like `%` are also now handled correctly.
*   **Mermaid.js**: Event reports can now correctly render mermaid.js diagrams containing arrows.
*   **Attribute Refactoring Fixes**: We've re-added some attribute tag functionalities that were missed during the major refactoring. (Sometimes even the developers' AI assistants have a bad day, with one commit noting: *"AI has brought great shame on its family."*)

### 🌍 Ecosystem and Community Updates

*   **New Feed**: A new OSINT feed from `phish.co.za` (Phishing.Database) has been added to the default feeds.
*   **Updated Components**: The `misp-galaxy`, `misp-object`, and `warning-lists` have all been updated to their latest versions.

## 🔧 Maintenance Release: MISP v2.4.214

This is a straightforward maintenance release for users on the 2.4 branch. It includes a bump of the underlying CakePHP framework, ensuring continued stability and security.


## How to Update

As always, you can update your MISP instance via the "Administration" -> "Server Settings" -> "Diagnostics" page in the UI, or by running a `git pull` on the command line from your MISP directory.

We strongly encourage all users, especially those with large instances, to update to **v2.5.16** to benefit from these incredible performance improvements.

A huge thank you to all the contributors, including Andras Iklody, Alexandre Dulaunoy, Christian Studer, Jeroen Pinoy, Koen Van Impe, and the many others who submitted code, bug reports, and feedback.

For a complete list of all changes, fixes, and contributions, please refer to the detailed [changelog](https://www.misp-project.org/Changelog.txt).

Happy threat sharing!
