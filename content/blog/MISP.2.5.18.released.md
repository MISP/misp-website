---
title: MISP v2.5.18 released with new on-demand correlation engine, a new improved task scheduling system and many more updates 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-08-20
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP v2.5.18 Release Notes  

We are pleased to announce the release of **MISP v2.5.18**, featuring a brand-new on-demand correlation engine, new improved  task scheduling, Forgejo CI integration, and a wide range of fixes and refinements.  

## ✨ New Features

###  **OnDemand Correlation Engine**   

A new correlation mode (complementary to the existing engines) that fetches correlating values *live* without storing them persistently.  

  **Pros**  
  - No extra correlation table needed → lower disk usage  
  - Faster inserts  
  - Correlation rules applied immediately and retroactively  
  - No need to re-run correlation jobs  
  - No risk of missed correlations due to worker issues  

  **Cons**  
  - Does not respect ACLs  
  - Currently incompatible with advanced correlations  
  - 10–15% slower than `NoACLCorrelation`  
  - Requires additional indexing for optimal performance (CLI tool available)  

###  **Forgejo CI Integration**  
  - Added worker file with specific Forgejo path  
  - Added Forgejo-compatible YAML workflow  

### **High-performance indexing** for No-ACL correlations

###  A new **Task Scheduler** system, giving administrators more flexibility to automate recurring actions (check below for details). 

## 🔄 Changes

- Task scheduling refactored to use a new `scheduled_tasks` table (reverting changes to `tasks`)  
- Supervisor configuration updated to include scheduler worker
- Consistent job creation and better cache handling  
- New `last_run_at` column for tasks, improved job status handling  
- Refactored task scheduler worker shell, UI, and controller  
- Multiple CI improvements:  
  - STIX tests disabled for CI stability  
  - Added branch support to GitHub workflows  
- Various UI, schema, and refactor cleanups  

## 🐛 Fixes

- **Event index recursion bug** fixed – previously broke event index for regular users  
- **Galaxy cluster improvements**  
  - Smarter relation loading to avoid unintended recursive depth issues  
  - Fixed internal snafu and relation handling issues  
- **Attribute & search**  
  - Fixed broken attribute indexing for users (#10438)  
  - Fixed attribute search downloads for large parameter sets (REST search now uses tokens)  
- **CustomAuth**  
  - Fail early when using authorization header to avoid excessive error logging  
- **Scheduler & tasks**  
  - Multiple fixes for job handling, missing ACLs, undefined vars, and modal rendering issues  
  - Fixed process_id handling → replaced with `last_job_id`  
- **Forgejo Actions**  
  - Corrected workflow runner paths  
  - Replaced lasting PWD with `$WORKSPACE`  

- **Security Fix**  
  - Arbitrary homepage in user settings fixed
  - Reported by **Lassi K** & **Teemu H** of *Second Nature Security Oy (2NS)*  


## 📦 Other Updates

- Numerous branch merges (`develop`, `2.4-develop`, `2.5`, `ondemandcorr`)  
- Added new installer configs for task scheduler worker  
- Added periodic user summary task  
- UI improvements for job/alert visibility and workflow picker dropdowns  
- Several fixes for feed/task parameter handling and ad-hoc workflows  
- Migration of GitHub Actions workflow to Forgejo Actions 

## New Scheduled Tasks in MISP 2.5.18

MISP v2.5.18 introduces a new **Task Scheduler** system, giving administrators more flexibility to automate recurring actions.

* Access it at: `https://YOUR_MISP_HOST/tasks`

If you see a red warning stating that the scheduler is not enabled, follow the setup guide here: [Supervisor Task Scheduler Install Guide](https://github.com/MISP/MISP/wiki/Supervisor-Task-Scheduler-Guide-%282.5%29)

## What can you schedule?

The scheduler supports creating recurring actions for:

* **Feeds**

  * Fetch
  * Cache
* **Servers**

  * Pull
  * Push
  * Cache
* **Workflows**

  * Run ad-hoc workflows
* **Summaries**

  * Generate periodic reports

For **Feed** and **Server** actions, you can choose to target a specific Feed/Server or apply the action to *all*.

## Key Features

* Tasks must be enabled after creation to start running
* Execution logs from the last run are available
* Tasks can be triggered manually at any time with the ▶ (*play*) button
* The scheduled task is always run as a given user.
* Only available to site-admins.

## Why a Scheduler?

The new **Task Scheduler** makes automation part of MISP itself. This means:

- No need to manage extra system-level scheduling.
- More consistent and reliable execution of recurring jobs.
- A central place to review, enable, or force-run tasks.

In short, it reduces overhead and keeps routine operations — like feed updates or server syncs — running smoothly in the background.

## UI Previews

**Add Scheduled Task form:**
<img width="622" height="788" alt="upload_373d68fd73c2b9ff371394bd5596d140" src="https://github.com/user-attachments/assets/8f8907ba-6dbf-493e-98fe-b4a1108a5581" />

**Scheduled Tasks index:**
<img width="2338" height="879" alt="upload_e710c4a69c121906661fca7854a6ed91" src="https://github.com/user-attachments/assets/1a4330ff-1976-48ce-9f7b-c4f7bf79b410" />


**Scheduled Task logs**:
<img width="3096" height="1071" alt="upload_fd9e9f35c1e4f46ed588353d5b710663" src="https://github.com/user-attachments/assets/825b72d6-8844-40fe-89ff-096e93e7b5a3" />

## 🔖 Contributors

Special thanks to all contributors in this release:  

**iglocska, Luciano Righetti, ThomasLcr (Thomas Lacroix), Sami Mokaddem, Alexandre Dulaunoy**  

🚀 *MISP v2.5.18 continues to enhance performance, streamline task scheduling, and introduce a powerful new on-demand correlation engine while addressing important bug fixes and security issues.*  

