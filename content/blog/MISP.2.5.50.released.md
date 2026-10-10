---
title: "MISP 2.5.50 Released - Security hardening, Overmind improvements, and streamlined workflows"
author:
 - MISP Project team
date: 2026-10-09
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/object-view.png
---

MISP 2.5.50 brings a substantial set of security fixes, continued development of the **Overmind** user interface, and the consolidation of several legacy features into their modern replacements. The release also improves TAXII connectivity, object handling, event graphs, statistics, and day-to-day administration.

## Highlights

- **Security hardening:** Important access-control fixes, restrictions on sensitive server settings, and safer attachment download headers.
- **Overmind improvements:** A redesigned Server Settings interface, new workflow views, improved object and attribute handling, and numerous usability enhancements.
- **Simplified data model:** Legacy event discussions, templates, and signature allowedlists are migrated to analyst notes, event templates, and warninglists, respectively.
- **Better integrations and data quality:** A new phishing feed, fixes for TAXII connection management, and improved duplicate-attribute handling.
- **New statistics:** Object-relation usage reporting to help understand how MISP object templates are used in practice.

## Security improvements

This release includes several security and privacy fixes. **Upgrading is strongly recommended.**

- **Sensitive configuration settings are now CLI-only.** The Redis host settings (`MISP.redis_host`, `Plugin.ZeroMQ_redis_host`, and `SimpleBackgroundJobs.redis_host`) can no longer be changed through the web interface or API. The `download_attachments_on_load` setting is also restricted. These changes reduce the risks associated with a compromised administrative session. Thanks to **Logan Homolka** and **CERT.pl** for reporting the relevant issues.
- **Safer attachment downloads.** Updates to the CakePHP dependency correctly escape quotes and backslashes and strip control characters from filenames in `Content-Disposition` headers. This prevents crafted filenames from manipulating download headers or causing unintended inline rendering. Thanks to **Logan Homolka** for the reports.
- **Object search respects attribute visibility.** Searches in the event view now consider only attributes that the user is authorised to see, avoiding information disclosure through organisation-only, sharing-group-restricted, or soft-deleted attributes.
- **Event index access-control correction.** An ACL-related information leak in the event index has been fixed. Thanks to **Jeroen Pinoy** for the report.
- **Visibility-aware galaxy counts.** Galaxy cluster views now count only tagged attributes visible to the current user.

## Modernisation and migration of legacy features

### Event discussions are replaced by analyst notes

The legacy **Thread** and **Post** functionality has been removed in favour of analyst data notes.

Existing discussions are migrated as follows:

- Posts attached to events become notes on those events.
- General discussions become notes attached to the originating organisation.
- Replies become notes attached to the note they answer.
- Author organisation, timestamps, and appropriate visibility information are preserved.

The old discussion interfaces, related settings, notifications, workflow trigger, and ZMQ conversation topic have been removed. Records that cannot be migrated, and workflows using the removed trigger, are logged during migration.

### Legacy templates are replaced by event templates

The older template system has been retired in favour of **event templates**. Organisation-authored legacy templates are converted to active event templates; the bundled legacy seed templates are superseded by the event template library.

The migration logs definitions that cannot be saved or conflict with existing names. The `perm_template` permission remains in use for event templates.

**Behaviour change:** Event templates create new events; the legacy ability to populate an existing event from a template is removed.

### Signature allowedlists are replaced by warninglists

The legacy signature allowedlist is removed and its entries are migrated into an **enabled custom regular-expression warninglist**, covering all attribute types. Entries that cannot be migrated are logged.

**Behaviour change:** Matching values are no longer unconditionally removed from `restSearch`, TAXII push, OpenIOC, and Bro exports. Instead, they are identified as warninglist hits and excluded **only when `enforceWarninglist` is enabled**. Administrators who relied on the previous filtering behaviour should review their integrations and export settings.

## Overmind user interface

This release includes a broad set of improvements to the evolving Overmind interface:

- **Administration:** A complete redesign of Server Settings, a refined debug top bar, site-admin benchmark views, and improved user settings and user/organisation management screens.
- **Events and attributes:** Bulk actions in the event attribute index, more intuitive filters, improved event information display, preserved selections when switching between table and card views, and clearer navigation between event content tabs.
- **Objects and relationships:** Improved object creation and editing forms, enhanced object filtering and display, and object references and relationships shown in relevant views and forms.
- **Analysis and enrichment:** New workflow views, warninglist match indicators next to attributes, image thumbnails in attribute indexes, improved sighting features, and PDF downloads from event report quick actions.
- **Tagging and distribution:** Taxonomy filtering in tag dialogs, additional galaxy fields, dedicated sharing-group badges, and clearer distribution information.
- **Polish and fixes:** Better date fields, animations, navigation and redirects, validation messages, and functional SightingDB, Cerebrate, and TAXII server views.

## Feeds, statistics, and integrations

- **New phishing feed:** Added the **phishunt.io** feed of active phishing URLs, contributed by **Daniel López**.
- **Object-relation usage statistics:** A new `objectRelationUsage` statistics operation reports how frequently relations are populated across MISP objects, grouped by the latest version of each object template. The implementation accounts for previous template versions and processes records in bounded chunks for large instances.
- **TAXII connection management:** Fixed connection discovery and editing for Basic, Bearer, and saved-key authentication; improved URL handling, error reporting, and preservation of API-root and collection selections.
- **MISP feeds:** Missing events in feed manifests are handled more gracefully, allowing processing to continue with improved exception logging.

## Additional fixes and improvements

- Fixed duplicate-attribute detection with `breakOnDuplicate:0` when values are transformed during validation, including whitespace trimming, URL refanging, and IPv6 normalisation.
- Fixed event graph rendering for numeric node IDs and relationships without comments.
- Restored the `normalizeIpAddress` and `reportValidationIssuesAttributes` CLI operations after an attribute-model rename.
- Fixed ZeroMQ status checks with phpredis 5 timeout responses.
- Improved database schema diagnostics when an expected table is missing.
- Corrected event-index filter removal for extended-event filters.
- Improved sharing-group member counts, organisation administrator email filtering, and several Overmind navigation and validation cases.
- Updated the database schema and refreshed the **misp-objects**, **warning-lists**, and **misp-galaxy** submodules.

## Notes for administrators upgrading to 2.5.50

**Please review the following changes before upgrading:**

1. **Database migrations:** Legacy discussions, templates, and allowedlist entries are converted to their replacement data structures. Review migration logs for records that could not be converted and take a database backup in accordance with your normal upgrade procedure.
2. **Warninglist enforcement:** Verify export and API filtering expectations if you previously used signature allowedlists. Filtering now depends on `enforceWarninglist`.
3. **Workflows and integrations:** Review workflows relying on the removed discussion/post trigger, as well as any integrations using legacy template or discussion routes.
4. **Configuration management:** Redis host settings and `download_attachments_on_load` must now be managed through server configuration or CLI rather than the UI or API.
5. **Event templates:** Existing-event population through the removed legacy template mechanism is no longer available.

## Thank you

Thanks to everyone who contributed code, testing, security reports, and improvements to this release, including **Thomas Lacroix, Sami Mokaddem, Andras Iklody, Alexandre Dulaunoy, Daniel López, James Garratt, Jeroen Pinoy, Logan Homolka, CERT.pl**, **vpiserchia**, and the wider MISP community.
