---
title: MISP 2.4.188 released major performance improvements and many bugs fixed.
date: 2024-03-25
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

We are pleased to announce the immediate release of MISP 2.4.188, with major performance improvements and many bugs fixed.

### New Features
- **Datasource Improvements:**
  - Updates to some datasources with the `ignoreIndexHint` parameter (`mysqlExtended`, `mysqlObserverExtended`).
  - Fix for `forceIndexHint`.
- **Settings:**
  - Added setting to temporarily disable the loading of sightings via the API (affects `restsearch` and `/events/view` endpoints). This helps with performance issues caused by large sighting data sets.

### Changes
- **PyMISP:**
  - Multiple version bumps.
- **Version and Internal Updates:**
  - General version bump.
  - Improved error handling and marking `BadRequestException` as fail log in CI.
  - Attempt to fix a failing test.
  - Updated `misp-galaxy`, `misp-object`, and `warning-lists`.
- **Attribute Search Rework:**
  - Significant performance improvement when using MysqlExtended or MysqlObserverExtended data sources.
  - Event level lookup moved to subqueries for faster queries.
  - Ignoring the deleted index to improve speed.
- **OpenAPI Updates:**
  - Added content for `analyst-data` and `event-reports`.
- **Sighting Policy Support:**
  - Added support of sighting policy in `sightings:getLastSighting`.
- **Attribute Search Performance:**
  - Improved performance of `includeDecayScore` by a factor of 5.
- **Attribute Fetch Refactor:**
  - Simplified conditions and optimizations.

### Fixes
- **Attribute Search:**
  - Enforced `unpublishedprivate` directive.
- **Internal Error Handling:**
  - Error handling improvements in AttachmentScan.
- **CurlClient HEAD Request:**
  - Added `CURLOPT_NOBODY` for HEAD requests.
- **CLI and ECS Updates:**
  - Fix for `redisReady` in dragonfly.
  - Change type from `Exception` to `Throwable` in ECS.
- **OIDC:**
  - Default organization handling if not provided by OIDC.
- **Publishing and Sync Issues:**
  - Fix for publishing and sync errors.
- **Performance Improvements:**
  - Bulk loading of analyst data to speed up event loading.
- **UI Update:**
  - Added `MISP.email_reply_to` to server config.

### Other

- Multiple merges of branches and updates.
- Fixes and changes in `misp-stix`, attachment scan error handling, OIDC default org handling, alert email titles, shadow attribute handling, and community additions (ICS-CSIRT.io).

### Community and Contribution Updates
- Additions and changes to the community, including the introduction of the [ICS-CSIRT.io community](https://ICS-CSIRT.io).

Details changes are available in [Changelog](https://www.misp-project.org/Changelog.txt).

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

