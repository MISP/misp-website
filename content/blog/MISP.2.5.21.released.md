---
title: MISP 2.5.21 released with a new recorrelate feature, various fixes and updates. 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-09-11
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP 2.5.21 released (2025-09-10)

We are pleased to announce the release of **MISP v2.5.21**.  
This version introduces new features affecting the various correlation tools, important fixes, and various updates to objects, taxonomies, and galaxy.  

## New
- [recorrelate] event functionality added.  
  - Recorrelate any event on demand if you are a site admin.  
  - Also usable via the API (`/events/recorrelate/{event_id}`).  
  - Reuses existing internal faculties.  

## Changes
- [version] bump.  
- [top correlations] pass engine type to UI.  
- [misp-galaxy] updated to the latest release.  
- [galaxy cluster] should include the `tag_id` when possible for its connector tag.  
- [AttributeValidationTool] Supporting more vulnerability ID types.  
- [misp-objects] updated to the latest version.  
- [taxonomies] updated to the latest version.  
- [misp-galaxy] updated to the latest version.  
- [ondemand correlations] toplist reworked.  
- [misp-stix] bumped to latest version.  


## Fix
- [db_schema] updated.  
- [top correlations] removed incorrect cache age for onDemandCorrelations.  
- [overcorrelations] value links now lead to the filtered event index (not the search page).  
- [acl] name fixed for the recorrelation action to please the CI gods.  
- [tag:sync] removed temporary fix.  
- [indeces] forcing of event index usage temporarily disabled.  
  - A `use index` call on a subquery was leading to exceptions.  
  - Temporarily commented out.  
- [ondemand correlation] invalid correlations.  
  - Correlation disabled events should not be visible via correlations.  
  - Correlation disabled events should not attempt to load correlations on view.  

## Other
- Merge branch `develop` into `2.5`.  
- Merge branch `2.5` into `develop`.  
- Merge pull request #10464 from Renater/hotfix/javascript-error-with-french-language.  
  - Remove quotes, as they trigger a javascript syntax error.  
  - Even if escaped in the translation file, they were passed unescaped in javascript code.  
- Merge pull request #10469 from DocArmoryTech/patch-userview.  
  - Fix(users-view): correct action name in server link.  
  - Changed the link action from `view` to `previewIndex` to fix navigation to the correct "Bound Server".  
- Merge pull request #10465 from marjatech/fix-proposals-block-attributes.  
  - Bind `ShadowAttribute` Model also to allow proposals to block attributes.  
- Merge pull request #10470.  
  - Fix(task-ui): typo - missing parenthesis.  
    - The hour option for the `time_unit` field was missing a closing parenthesis (`hour(s` → `hour(s)`).  
- Merge pull request #10472.  
  - Fix(tasks): populate frequency fields in task edit form.  
  - Fix(tasks): decompose timer in `TasksController` edit action.  
    - Ensures existing frequency values are displayed correctly in the task edit form.  
- Merge pull request #10475 from ThomasLcr/local_tag.  
  - Solving the non-synchronization of local tags when pulling between internal instances.  
- Merge branch `develop` into `develop`.  


## Contributors
A big thanks to all contributors for this release:  
**iglocska, Alexandre Dulaunoy, Christian Studer, ThomasLcr, Guillaume Rousse, Andras Iklody, DocArmoryTech, marjatech**  


📦 [Download the release](https://github.com/MISP/MISP/releases/tag/v2.5.21)  
📚 [Upgrade guide](https://misp.github.io/MISP/INSTALL/)  

