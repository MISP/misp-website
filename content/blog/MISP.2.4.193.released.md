---
title: MISP 2.4.193 released with many bugs fixed, API improvements and security fixes 
date: 2024-06-07
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

MISP 2.4.193 released with many bugs fixed, API improvements and security fixes

![image](https://github.com/MISP/MISP/assets/3668672/81098352-619d-43b0-b44e-24b8d2646584)

## New

- **[attributes/enrich] endpoint added.**
  - Simply post a list of modules you wish to enrich the attribute by.
  - URL: `/attributes/enrich/[attribute_id|attribute_uuid]`
  - Post body format: `{"dns": 1, "foo_bar_baz": 1}` listing all modules to execute.
  
- **[misp-community] MISP-LEA information sharing community added.**

- **[events:view] New UI feature to collapse Attributes inside an object.**
  - Comes with an MISP setting to configure this behavior at an instance-wide level.

- **[fatal error] logging added.**
  - Helps administrators to easily see issues related to timeouts/OOM.

- **[feed acl] changed for feeds with visibility set to 1.**
  - Any user can now use open feeds to:
    - Browse the data.
    - Preview individual events.
    - Search the feed caches for the given feeds.
    - Run overlap comparisons on them.
  - For feeds/server correlations that do not allow users to see contents:
    - Correctly show server-wide opt-in correlations on local events as text, rather than non-functional links.

- **[feed] sync pull rule checks on manifest, fixes #9728.**
  - Added checks to rule out events from MISP feed pulls that do not match the filter rules.
  - Should speed up processes considerably.

## Changes

- **[version] bump.**
- **[PyMISP] Bump version.**
- **[misp-stix] Bumped latest version.**
- **[taxonomies] updated to latest version.**
- **[misp-galaxy] updated.**
- **[warning-lists] updated.**
- **[misp-objects] updated.**
- **[diagnostics] add Database/MysqlObserverExtended to valid data sources list.**
- **[attributes/enrich] added to ACL.**
- **[community] misp-lea.org is vetted by us.**
- **[PyMISP] Bump for testing.**
- **[event:view] Small UI improvement for attribute's type in object row.**
- **[events:view] Small UI tweak to prevent object name from wrapping.**
- **[galaxy:galaxy-matrix] Respect order of tabs based on kill_chain_order definition.**
- **[analyst-data:relationship] Prevent self-referencing relationships.**
- **[analyst-data:view] Always return attached analyst-data.**
- **[analyst-data:capture] Recursively capture nested analyst-data.**
- **[component:CRUD] Added support of afterFind in the delete function.**

## Fix

- **[feed settings] unpublish_event setting had the inverted effect, fixes #9739.**
- **[JS] invalid comparison fixed.**
  - 2jsirl4jsirl

- **[tag search] fixed.**
- **[modules] /queryEnrichment endpoint fixed in modules controller - correctly pass module data, fixes #9758.**
- **[event fetcher] pop the tag filter after the first round of lookups.**
  - Avoid adding the same condition twice.

- **[tag search] fixes #1.**
  - Correctly break execution for ANDed tag searches if one tag doesn't exist.
  - Correctly compare against event_id field in attribute_tags table.

- **[API] don't HTML encode JSON documents.**
  - Earlier fix caused issues.

- **[security] changed menu_custom_right_link to CLI only.**
  - Prevents malicious/hijacked admin accounts from embedding malicious JS in a global menu link.

- **[galaxyClusters:restSearch] filter on org_id and orgc_id if param set.**
- **[security] rest endpoints - additional sanitisation for non-JSON responses.**
  - Escape non-JSON response bodies.

- **[security] changed menu_custom_right_link_html to CLI only.**
  - Prevents embedding malicious JS in every page.

- **[PyMISP] Fix the tests.**
- **[Collections] path pluralisation fix in ACL check for collections, fixes #9745.**

- **[event:view] Correctly handle first click on toggle attribute visibility.**
- **[audit-logs:eventIndex] Fixed pagination issue while viewing event history, fixes #9726.**
- **[event-report:publishing] Do not reset the event timestamp when updating an event report.**
- **[feeds] function name change not handled everywhere.**
- **[ACL] private function name convention not kept for a new function.**
  - Prevents ACL self-test complaints about an accessible endpoint.

- **[correlation] small fix for preview_event.**
- **[server correlation UI] fixed link to index preview.**
- **[password reset] ACL fix.**
- **[ACL] fixed pre-auth dynamic function calls.**
- **[server/feed] correlation bug fix.**
  - Prevents MISP from failing due to too many correlating events.

- **[bruteforceProtection] Avoid failing when wrong username is used.**

## Other

- **Add Infoblox feed to defaults.json.**

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt). Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!



