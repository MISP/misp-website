---
title: MISP v2.4.209 and v2.5.11 Released with new features, security fixes and improvements in workflow engine.
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-05-07
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release introduces several new features, important security fixes, and major improvements to the workflow engine, sharing group logic, and plugin handling. It also includes enhancements developed during [hackathon.lu](https://hackathon.lu/) 2025.

## New Features

- **Workflow Editor**: Added the ability to run debugged ad-hoc workflows on event IDs.
- **Workflow Engine Enhancements**:
  - Added `_env` dictionary in Jinja rendering to provide environmental context (e.g., `base_url`).
  - Support for filtered/unfiltered overrides in workflow execution.
  - Stateless execution improvements and picker UI refinements.
- **OIDC Authentication**:
  - Introduced support for identity provider selection and `mixedAuth` configuration.
- **User IP Tools**: New tools `userIP` and `IPUser` added to the user controller.
- **Collections**:
  - Enabled editing, viewing, and deletion by UUID.
  - Extended OpenAPI documentation for collections.
- **Suricata Export**: Initial refactoring of Suricata support (work in progress).
- **Database Change**: `event.info` collation made case-insensitive.
- **Audit Log**: Fixed user audit log links.

## Changes

- **Workflow**:
  - Improved tag filtering in `filter-tag` module.
  - Ajax calls in workflow editor now return REST responses.
  - UI enhancements for manual debug runs.
  - Added documentation and examples for enrichment and warning data formats.
- **CRUD Components**: Added missing `PUT` method in CRUD `add`.

### Documentation
- Included concrete upgrade path examples from MISP 2.4 to 2.5.

## Fixes

### Workflow-Related Fixes
- Prevented cache invalidation when setting up workflow pickers.
- Corrected default values and scope in filter modules.
- Added fallbacks and fixed log messages in trigger executions.
- Debounced matrix rendering in event report editor.
- Fixed JSON import via paste and file upload in blueprint import.
- Improved handling of tag operations and fast lookup rebuilding.

### Sharing Group and Attribute Handling
- Relaxed checks for sharing group usage creation.
- Fixed issues related to galaxy deletion and event timestamp updates.
- Attribute correlation toggles now properly trigger unpublishing and timestamp changes.

### Security Fixes 

- Fixed multiple stored XSS issues:
  - In periodic summary.
  - In sync server rule creation.
  - In FontAwesome helper views.
- All reported by Jeroen Pinoy during hackathon.lu 2025.

### UI and Plugin Issues
- Addressed upgrade script issues by ensuring cache cleaning, avoiding missing plugin problems.
- Corrected UI population in `CorrelationRules:edit`.
- Improved error handling for links with missing labels in workflows.

## Other Notable Contributions
- Updates and improvements to:
  - `misp-stix`
  - `misp-galaxy`
- Numerous merges from `2.4-develop` and `develop` branches for integration and consistency.
- Contributions from Steve Clement, Luciano Righetti, Sami Mokaddem, Jeroen Pinoy, and others.

## Upgrade Note

This release is highly recommended for all users due to critical security updates, significant workflow engine enhancements, and improved upgrade/documentation support.

For full technical details and migration guides, please refer to the [MISP GitHub repository](https://github.com/MISP/MISP) and official documentation.

