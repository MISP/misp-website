---
title: "MISP 2.5.44: Hotfix release (pull mechanism) and Overmind theme update"
author:
 - MISP Project team
date: 2026-07-14
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/new-correlation.jpeg
---

This is a hotfix release, primarily addressing a bug in the pull synchronisation mechanism that could cause failures when pulling events without any tags.
It also ships a large batch of Bootstrap 5 views for the Overmind theme along with a couple of smaller fixes.

### Key fix — pull mechanism & untagged events

The main driver for this release: pulling events that carried no tags could fail during synchronisation. When comparing local vs. remote tags on an
internal server, areLocalTagsDifferent() was handed the EventTag / Event.Tag keys directly, which are simply absent on untagged events — leading to
failures on affected pulls. These are now safely defaulted to empty arrays, so tag-less events pull cleanly again.

  - fix: [sync] conditional check for event tags — avoids failures on pulled events without any tags (app/Model/Event.php)

### Overmind theme — Bootstrap 5 views

Continued migration of admin/list screens to the new Overmind (Bootstrap 5) look and feel. New BS5 views added for:

  - Organisations (index, add/edit, view)
  - Roles (index, add/edit, view)
  - Analyst Data
  - User Login Profiles
  - Workflow Blueprints
  - Bookmarks
  - News
  - Correlation Rules
  - Blocklist family: Org, Event, Sighting, Galaxy Cluster and Analyst Data blocklists

<img width="3405" height="1314" alt="image" src="https://github.com/user-attachments/assets/b93eb6d0-a76d-4a59-98c0-d3aa778da431" />

###  Related theme fixes:

  - fix: [ui] Match $bootstrap5Pages case-insensitively, so pages register with the correct Overmind chrome regardless of casing
  - hotfix: [Overmind|Pivotick] Corrected asset files (misp-iconify.css, Pivotick JS/CSS)

### Other fixes

  - fix: [install] Keep the browser cache enabled by default in the installers (Security.disable_browser_cache set to false) across the Debian 12, Debian
  13, Ubuntu 24.04 and RHEL 9.4 scripts, reverting an over-eager hardening default.

###  Upgrade notes

No schema-breaking changes — a standard git pull / update is sufficient.

