---
title: "MISP 2.5.43 strengthens collaborative threat intelligence with major OverMind improvements, collection synchronisation and enhanced security."
author:
 - MISP Project team
date: 2026-06-22
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/dashboard2.png
---

<img width="3405" height="1314" alt="image" src="https://github.com/user-attachments/assets/9e6842e1-ccc0-4abb-b01c-fdc119f59128" />

A sizeable feature release headlined by collection synchronisation between instances, continued rollout of the Overmind (Bootstrap 5) UI, the first cut of
the Pivotick pivot explorer, environment-variable-based settings, and a batch of security and sync hardening fixes.

## Highlights

###  Collection synchronisation

MISP collections can now be synchronised between instances, in both pull and push directions. This includes:

  - New per-server pull_collections / push_collections toggles
  - Feature negotiation so a modern instance detects whether a remote peer supports collection sync (and skips it gracefully otherwise), with paginated negotiation to keep memory usage low
  - A collections.locked flag and origin-protection to mirror the model used for galaxy clusters, so synced collections are handled safely and idempotently
  - Developer documentation and a checked-in two-instance E2E test script

###  Overmind theme (Bootstrap 5)

  The Overmind UI rework advanced considerably, migrating many more screens to the new look:
  - User index, Categories & types, Application / Audit / Access logs, Galaxies / Galaxy Clusters / Galaxy Relationships, and Proposals (now fully
  operational)
  - Add tags/galaxies on attributes directly from the event view, "Populate from" modal, object add/edit form, collection card in the event view, clickable
  compatibility matrix, and numerous badge/display refinements

###  Pivot Explorer (Pivotick)

  Initial integration of [Pivotick](https://github.com/Pivotick/Pivotick) as a drop-in replacement for the legacy event graph, plus a draft drag-and-drop reference editor. This is an early
  work-in-progress / proof-of-concept and is not yet a finished feature.

  Settings via environment variables (#10811)
  
  Environment variables are now supported as a third settings source, alongside the config file and database — useful for containerised and
  infrastructure-as-code deployments.

  TAXII server improvements

  - Bearer authentication for TAXII servers, plus a streamlined add flow for basic auth
  - The TAXII "API key" is renamed to Token in the UI and obfuscated in the server view

### Security fixes

  - [security] ACL tightening for toggleEnable on galaxies, and hardening for massenable
  - [security] Fix XSS via the automation page and malicious API keys
  - [security] Tighten the sharing-group check so it also runs when distribution is not explicitly set to sharing groups
  - [security] Honor per-org module restriction in getEnabledModule()
  - [security] Enforce modify rights on the importModule / misp_standard write path
  - [security] Fix invalid attribute name used for CLI-only settings

### Sync & server fixes

  - [sync] Restrict full tag loading of all local events to internal-only sync; request only the event-tag fingerprint instead of the full tag list
  - [internal sync] Various issues resolved
  - [server:remove-older-events] Ensure the local event exists before checking its tags
  - [ServersController] Correctly return update results when not using async update
  - [sharingGroup] Guard RemoteOrg uuid in checkIfServerInSG
  - [Servers] Add the remote user's org name and uuid to "view sync user"

### Other fixes & changes

  - [dashboard] Geomap country sources now derive from geolocation + country-code objects (#10817)
  - [freetext import] Keep a valid category on type change (#10873)
  - [StixExport] Properly pass the meta field to event galaxy clusters alongside an attribute collection
  - [Export] Remove stray leading newlines from module export files
  - [OrgEventsWidget] Fix target date computation
  - [Galaxy] Set the initial version correctly using max() of the cluster version fields
  - [csp] Allow blob: workers so the Pivotick graph can render
  - [collections] Guard optional element keys in captureElements
  - Add zeromq supervisor setting and status check; smartDelete reference handling; workflow roaming data written to temp file for walkGraph
  - Add HoneyLabs default feeds (active exploiters, malware infrastructure)
  - [ci] Accept the ondrej/php PPA metadata change in apt-get update

### Library & data updates

  - Updated warninglists, misp-objects, taxonomies, and misp-galaxy to their latest versions
  - Bumped misp-stix (2026.7.8) and the [Pivotick JS library](https://github.com/Pivotick/Pivotick)

