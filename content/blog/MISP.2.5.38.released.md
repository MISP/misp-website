---
title: "MISP 2.5.38 - UI and security update"
author:
 - MISP Project team
date: 2026-05-26
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/uav.png
---

A focused release with two security fixes, a new workflow action module, continued **Overmind UI** migration of the Sync tab, TAXII 2 conformance work, and the usual round of community-contributed bug fixes.

## Security fixes

- **OIDC authentication bypass** under certain insecure IdP configurations via automatic email account linking. *Reported by Ali Ganiyev (independent researcher).*
- **Stored XSS** in template element attribute type. *Reported by Bjørn Helseth, TV 2 Norway.*

Operators are encouraged to upgrade promptly.

## New features

- **Workflows — Blocklist action module** (#10771, @cudeso): a new workflow module that writes event attributes into a blocklist file. Supports removal-by-tag, atomic writes with one-generation backup, and optional rolling filesystem snapshots.
- **TAXII 2 — spec & schema v148 conformance** (#10775, @Cosive).
- **Overmind UI — Sync tab migration** (@ThomasLcr): Servers, SharingGroup, SharingGroupBlueprints, Sightingdb, TaxiiServers, Communities, and Cerebrate views ported to the Overmind theme, plus the shared Sync-tab scaffolding.

## Bug fixes

- `[utf8]` Sanitize the `change` field on log entries so invalid UTF-8 and 4-byte characters no longer abort log writes
- `[DB]` `galaxy_clusters.description` widened to utf8mb4 — emoji and other 4-byte characters in cluster descriptions no longer break ingestion
- `[Feed]` Correct typos in `__filterEventsIndex` conditions (#10783, @Wachizungu)
- `[SharingGroup]` Only save sharing-group servers once on update (#10782, @Wachizungu)
- `[ServersController]` CSP report size validation corrected to 1 KB
- `[Bookmarks]` Use `mayView` for the `view()` ACL check (#10777, @Wachizungu)
- `[ObjectReference]` Fix assignment-instead-of-comparison bug in `smartSave()` (#10776, @Wachizungu)
- `[UI]` Show the "add custom galaxy" side-menu button to users who actually have access (#10774, @Wachizungu)
- `[AttributeValidationTool]` Add start anchor to UUID validation regex (#10773, @Wachizungu)
- `[ServersController]` CSP report size validation corrected to 1 KB (#10778, @skraft9)
- `[Servers:index]` Correctly show the PUSH state
- `[Warninglist:enableWarninglist]` Return the correct flash message when disabling via `0` URL param (#10770, @Wachizungu)
- `[MispAttribute:advancedAddMalwareSample]` Set correct sharing-group id (#10769, @Wachizungu)
- `[Attributes:addTag]` Allow adding multiple tags at once via a list of strings (#10768, @Wachizungu)
- `[ShadowAttribute]` Unset `id` from request data (#10779, @skraft9)
- `[User]` Use the correct password-reset email template when admin-configured ones exist (#10761, @Wachizungu)
- `[objects/restSearch]` Implement `includeEventUuid` (#10760, @UFOSmuggler)
- `[ACLComponent]` `canModifyWarninglist` now returns true for roles with `perm_warninglist` (#10756, @Wachizungu)
- `[Collections]` Fix typo preventing members of the creating/syncing user's org from modifying data (#10765, @Wachizungu)
- `[CollectionElement]` Correct typo in `mayView` (#10764, @Wachizungu)
- `[Bookmark]` Now logged to audit logs (#10767, @Wachizungu)
- `[docs]` Fix default release to 2.5 (#10780, @frbayart)

## Dependencies & data

- **misp-stix**, **misp-objects**, **misp-galaxy**, **taxonomies**, **warninglists** — bumped to latest
- **GeoOpen-Country** updated; **GeoOpen-Country-ASN** added

## Thanks

Big thanks to everyone who reported or contributed in this cycle — in particular @Wachizungu (the long string of bug fixes above), @ThomasLcr (Overmind Sync tab migration), @cudeso (workflow blocklist module), @Cosive (TAXII 2), @UFOSmuggler, @skraft9, @frbayart, and the security researchers Ali Ganiyev and Bjørn Helseth.

**Full changelog:** https://github.com/MISP/MISP/compare/v2.5.37...v2.5.38
