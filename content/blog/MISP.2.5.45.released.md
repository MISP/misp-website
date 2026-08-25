---
title: "MISP v2.5.45 released - Overmind Everywhere, LDAP Reworked, Security Hardened and Many Fixes"
author:
 - MISP Project team
date: 2026-08-25
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/new-correlation.jpeg
---
A large six-week cycle (herding kids, pets, bots is tiring in the heat, especially without an HVAC). Three themes dominate: the continued Overmind (Bootstrap 5) UI migration, a full revamp of LDAP authentication, and a concentrated  security and correctness hardening pass.

# Highlights

<img width="1644" height="993" alt="Screenshot from 2026-08-25 16-25-33" src="https://github.com/user-attachments/assets/d569fb55-bf65-4cab-8738-a0b0a91461eb" />

 ## Overmind UI migration (83 commits)

  The single largest workstream in this release. Server settings, the Workflow indexes (ad-hoc, triggers, modules) and the workflow editor, the Decaying
  Model index, misp-module enrichment, and the complete registration / user settings / forgot-password / change-password flows have all been migrated. Feed
  migration is now complete, including a freetext feed preview index and import modals. New BS5 views landed for Jobs, Tasks, AnalystData, Feeds,
  TaxiiServers, CryptographicKeys and GalaxyClusterRelations.

  Alongside the migrations, the add/edit modals were overhauled across roughly a dozen entity types — Cerebrates, TaxiiServers, SightingDB, Collections,
  SharingGroups and Blueprints, Correlation Rules, blocklists, Regexp, Allowedlist, warninglists, tags and tag collections, servers. Also new: an
  organisation merge feature, an import action on the event index, server preview views, and a reworked header/action display.

 ## LDAP authentication revamp (PR #10956)

  - Role and organisation mapping now supported via either a directory field or group membership
  - ldapNestedGroups resolves nested group membership
  - Users flagged ACCOUNTDISABLE in userAccountControl are disabled in MISP (behind a setting)
  - MISP accounts can be synced from LDAP via the User check_validity task, schedulable as an admin task
  - Authentication against a header asserted by a trusted proxy
  - ldapOrgGroupMapping / ldapRoleGroupMapping precedence now follows settings order
  - Security: passwordless binds to LDAP are now prevented, and a DN-linking bug causing incorrect matching is fixed
  - A full pytest suite (tests/ldapauth/) with an OpenLDAP service running in CI

 ## Security hardening

  - Eight XSS escaping fixes: correlation data in event-view JS rendering, event date in the index table time element, parent object name in sub-attribute
    rows, object name in attribute row data attributes, highlighted and missing taxonomy namespaces in ajaxTags, JS-safe encoding of warninglist match
    values in onclick, and contributor org names in the event view
  - Per-org module restrictions are now honoured on all getEnabledModule() paths
  - Event modify ACL is now enforced on attribute enrichment
  - REST search honours the distribution=0 filter in fetchEvent

 ## Other new features
  
  - Serve the instance GPG key via /gpg.asc, with caching
  - Manage Supervisor-backed workers directly from the CLI

 # Bug fixes

 ## Collections, analyst data and objects
  - Compare distribution numerically in Collection::mayView; align buildConditions org visibility with mayView
  - Check event visibility before collection attachment
  - NOT-rule-only orgc_name filter no longer drops all rows (collections and analyst data)
  - Log CollectionElement save failures instead of swallowing them; reset skipCollectionModifiedBump via finally
  - Drop the stale-modified conflict guard from user edit
  - Report the real id/uuid for intra-batch duplicate objects
  - Propagate object-level first_seen/last_seen to new attributes
  - Log when an attribute delete cascade does not fully save; only unpublish the event when the cascade succeeded
  
 ## Core and API
  - Repair an invalid character class in _harvestParameters wildcard matching
  - Serialise validation errors before throwing in AuditLog::insert
  - Add a missing org_id guard to object/attribute correlation ACL
  - Fix inverted null checks in the changeInTagOrCluster flag
  - Avoid a recursive read in the generateCount bulk update
  - Stop re-including theme files when building theme labels
  - Check the populated stderr property rather than an unset variable in background jobs
  - Scheduler now recovers from lost database connections (#10624)
  - TAXII getObject queried api_root instead of the object path
  - Cache export: fix event scope export and allow specifying the hash algorithm
  - Drop a dead $model reference in attachNestedAnalystData
  
##  UI and dashboard
  - Add the missing BenchmarkTool import in BenchmarkTopListWidget
  - Fetch skip_proxy for the sync test widget connection test
  - Purge the real count display on the attribute index
  - Numerous Overmind fixes: taxonomy indexes, warninglist edit and index display, freetext import silent error, server settings hidden from org admins,
    enrichment result column order, fixed-height index tables so action dropdowns aren't clipped, galaxy search input and loader, N/A instead of 0000 for
    empty timestamps, flash overlay z-order, active menu for admin pages, event report add permission check, dark-mode Default badge colours
    
##  Installer and packaging
  - Correct cake Admin quoting in INSTALL.ubuntu2404.sh (#10919)
  - Add the missing bootstrap-datepicker.css.map (#10913)
  - Further INSTALL.ubuntu2404.sh corrections
  
##  Data and documentation
  
  - misp-galaxy, misp-objects, taxonomies and warninglists updated to their latest versions
  - Added a privacy statement
  - Linked MISP professional services
  - Added a Software Heritage ID section to the README
  - Major updates in [misp-warninglists](https://github.com/MISP/misp-warninglists), [misp-galaxy](https://github.com/MISP/misp-galaxy), [misp-object](https://github.com/MISP/misp-objects) and [misp-taxonomies](https://github.com/MISP/misp-taxonomies).
  
# Contributing

- Thanks a lot to everyone that contributed to this release, AI has been a serious enabler this round, thanks for putting it to good use. Apologies to everyone that had to wait (or still has to wait) for their PRs to be merged, it's a bit overwhelming at the moment (but in a good way). 
