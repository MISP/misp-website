---
title: MISP v2.4.206 and v2.5.8 Released - new workflow modules, improved graph object relationship management and many other improvements 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-03-19
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
slug: MISP.2.5.8.and.2.4.206.released 
---
## Summary

MISP v2.4.206 and v2.5.8  introduces new workflow modules, enhanced object relationship management and significant improvements to the event synchronisation mechanism. Key highlights include improved a reworked attribute search functionality, better handling of event reports, and various security fixes. Additionally, numerous optimizations and bug fixes enhance stability and performance.

{{<video src="https://github.com/user-attachments/assets/ed65cddc-0efe-4182-9809-e6a3147b6742" title="New workflow modules in MISP" >}}


## New Features

- **[workflow-module:filter-tag]** Added new module to filter data based on tags.
- **[object-relationships]** Added CRUD and highlighting support for relationship_types.
- **[workflow:user_notification]** Added new module `notify_user_toast` to create notification toast.
- **[workflow-module:add_analyst_data]** Added new module to create analyst data.
- **[galaxy]** Added new default distribution setting.
- **[event:pull]** Added support for `remove_missing_tags` on the Event level.
- **[sync:perm_sync_internal]** Added new flag to allow internal pull.
  - Previously, pull would downgrade the distribution regardless of the `internal instance` flag.
  - If the remote user has the `perm_sync_internal` permission, the pulling instance will no longer downgrade the distribution.
  - The remote instance now decides whether a downgrade happens.
- **[attribute search]** Major rework.
  - Removed session variables.
  - Added the ability to pass parameters as query strings.
  - Converted search form to GET form.
  - Enabled easy downloading of search results.
  - Ensured consistent search with restsearch behavior.
  - Removed duplicate index/search_index endpoints.
  - Improved pagination.

## Changes

- **[version]** Bump.
- **[misp-objects]** Updated.
- **[taxonomies]** Updated to the latest version (major changes with UUID).
- **[misp-galaxy]** Updated to the latest version.
- **[warning-list]** Updated.
- **[db_schema]** Updated.
- **[workflow-module:if-tag]** Added support for event-report filtering.
- **[users:otp]** Purged invalid OTP codes on failure and added `autocomplete=off` on the OTP field.
- **[object-relationship:CRUD]** Added support for the `highlighted` field in /add and /edit.
- **[misp-stix]** Updated to the latest version.
- **[workflow:editor]** Added support for more HTML attributes in form inputs.
- **[server:index]** Added number of events to be synced when testing sync rules.

## Fixes

- **[tests]** Fixed test cases.
- **[workflow modules]** Fixed usage of the `Attribute` class name in 2.4.
- **[authkeys]** Fixed an issue where ordering by a non-existent field caused errors.
- **[acl]** Added missing entry.
- **[submodules]** Added default branches for every submodule.
- **[correlation rule]** Fixed JSON encoding/decoding issue when data doesn't exist.
- **[event-report:md-parsing]** Fixed issue when handling objects without attributes.
- **[suricata-export:url-rule]** Removed rules using HTTPS paths, as they cannot be used by IDS.
- **[diagnostic]** Updated Python libraries version check and STIX dependencies diagnostic.
- **[galaxy:sync]** Fixed typo with undefined index.
- **[event-report:editReport]** Fixed a branching issue when attaching tags.
- **[security]** Fixed stored XSS in event reports (mermaid rendering function).
- **[web:event-report]** Fixed Mermaid diagrams rendering according to API changes.
- **[component:compressed-request-handler]** Decompress requests before `appController::beforeFilter` is called.

## Other

- Merged several branches into `2.4-develop`.
- **[security]** Updated Mermaid to the latest version (11.4.1) to fix stored XSS in event reports.

For a complete list of changes, please refer to the [MISP GitHub repository](https://github.com/MISP/MISP).

We would also just like to remind everyone that MISP 2.5 has been out for a while and the originally announced grace period for 2.4 is coming to an end (2.4 security fixes will continue until the end of the year), we'd like to use this moment to encourage everyone to take a moment to upgrade. There are a host of options for installation or upgrade of MISP 2.5, including an [Ubuntu upgrade script](https://github.com/MISP/MISP/blob/2.5/INSTALL/UPGRADE.ubuntu2404.sh), fresh installation scripts for [Ubuntu](https://github.com/MISP/MISP/blob/2.5/INSTALL/INSTALL.ubuntu2404.sh), [Debian](https://github.com/MISP/MISP/blob/2.5/INSTALL/INSTALL.debian12.sh) and  [RHEL](https://github.com/MISP/MISP/blob/2.5/INSTALL/xINSTALL.rhel94.sh), as well as a production ready [dockerised instance](https://github.com/MISP/misp-docker) (massive shoutout to @ostefano for the incredible effort!)

Not only will this bring the MISP software stack to a more modern standard, but it will also prepare you for the next big chapter in MISP's lifecycle, namely MISP 3.x, which will be a major rework and modernisation of the tool. 
