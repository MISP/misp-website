---
title: "MISP 2.5.47 released - a major security hardening round, the new database migration system with PostgreSQL support, AI-assisted analysis and Overmind moving forward"
author:
 - MISP Project team
date: 2026-09-17
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/new-correlation2.jpeg
---

MISP 2.5.47 is the outcome of the most intensive security review the project has gone through in a long time, and it ships alongside three larger pieces of work: a ledger-based database migration system that also brings PostgreSQL support, the first release of the AI-assisted analysis integration, and another big batch of Overmind improvements. It also closes a background-job regression introduced in 2.5.45 and a set of CSRF regressions from the 2.5.46 hardening.

We strongly recommend updating.

## Major security hardening

This release is the result of a heavy security hardening and fixing effort, driven by the reports of multiple external parties who spent considerable time reviewing MISP over the past weeks. More than thirty findings were reviewed for this release alone, on top of what already went into 2.5.46; twenty-seven of them were confirmed as vulnerabilities, fixed and re-tested against a live instance.

The fixes cover the whole range: stored and reflected cross-site scripting in statistics, index and modal views; access-control bypasses in event reports, collections, sharing groups and the extended-event distribution checks; CSRF exemptions on actions that should never have had one; a read-only API key regaining the full role of its account; an MFA and brute-force protection bypass through an alternative HTTP verb on the login action; SSRF and local file read through XML parsing and MISP export uploads; path traversal in the organisation logo handling; and, most severely, a remote code execution reachable by any authenticated user through the argument handling of background jobs. The installers were also fixed to no longer create their log world-readable.

Beyond the individual fixes, a few defence-in-depth changes landed: the `phar` stream wrapper is now unregistered in both entry points, the module choice for enrichment is enforced against the enabled list, and the CakePHP fork that MISP ships was moved to [MISP/sachertortephp](https://github.com/MISP/sachertortephp) and carries the upstream fix for the `Xml::build()` URL fetching behaviour.

We are not listing the individual vulnerabilities here. The details, severities and CVE identifiers are published on the [MISP security page](https://www.misp-project.org/security/) as they are processed.

A big thank you to the people who reported these issues and worked with us on reproducing and validating the fixes:

- **Jeroen Pinoy**, who reported the vast majority of the findings in this round and reproduced several of the others
- **Niels Teusink** of **Eye Security**, whose batch included the most severe finding of the release
- **David André**, who reported the event report and event graph findings together with Jeroen Pinoy

We also want to thank **James Garratt** of **Cosive**, who tracked down and fixed the CSRF regressions the 2.5.46 hardening introduced in the session-based AJAX requests, the TAXII discovery calls and the collection view.

## A new database migration system, and MISP on PostgreSQL

The way MISP evolves its database schema has been rebuilt. The historic `db_version` counter and its `DB_CHANGES` corpus are frozen at version 159 and will not move again. From now on every schema change is a migration under `app/Lib/Migration/Migrations/`, tracked by identity in a new `schema_migrations` ledger rather than by a single integer. A migration that arrives late, or comes from a branch numbered independently, can no longer be silently skipped.

What this means for administrators:

- `runUpdates` (and logging in as a site admin) still applies everything pending, now stopping on the first failure instead of marking the failure as done.
- New console commands: `cake Admin migrationStatus` (applied, pending, failed), `cake Admin migrationApply` with `--dry-run` to print the SQL a migration will run, and `cake Admin migrationCreate` for developers.
- The diagnostics page, `cake Admin schemaDiagnostics` and the Overmind database status card now show pending and failed migrations by name. Fleet monitoring that alerted on `actual_db_version` differing from `expected_db_version` should move to the new `migrations_pending` and `migrations_failed` fields of the diagnostic payload, since the version pair can no longer diverge.
- Fresh installs now start at the current schema. Both `INSTALL/MYSQL.sql` and the new `INSTALL/POSTGRESQL.sql` are generated from a fully updated reference database, so a fresh instance no longer replays years of updates on first login. The upgrade path from the previous release baseline is covered in CI.

Migrations are declared against an engine-neutral schema DSL and rendered separately for MySQL/MariaDB and PostgreSQL. That work is what makes the second part possible: **MISP can now be installed on PostgreSQL** as an alternative to MySQL/MariaDB. This is a fresh-install path (existing MySQL instances are not migrated), it ships its own `PostgresObserverExtended` datasource, and it has been verified against PostgreSQL 16: an instance boots, upgrades, creates users and events, correlates and publishes. It has not seen performance work at scale yet and CI does not run the full test suite against it, so treat it as early support. The On Demand correlation engine and the search benchmark remain MySQL-only. See `docs/CONFIG.postgresql.md` for the install steps and `docs/dev/database-migrations.md` for the developer reference.

Migrations shipping in this release:

- `tags.name` becomes case-insensitive and is served by its unique index. Tag lookups used to go through `LOWER(name)`, which no index can serve, resulting in a full scan of the tags table per captured tag. This was especially painful during feed ingestion (#11114). Tag names that collide under the new collation are merged into the oldest tag, with every reference repointed and each merge audit-logged.
- `bruteforces`, `system_settings` and `attr_value_counts` gain an auto-increment `id` like every other table.
- `taxii_servers.auth_type` is narrowed to `varchar(191)`.
- `roles.perm_ai_tools` is added for the AI integration, granted to site administrators.

## AI-assisted analysis

This release introduces the first iteration of the AI integration in MISP, built around the `ai_connector` misp-module developed by Aaron Kaplan (see [MISP AI-connector](https://github.com/MISP/ai-connector)). MISP hands an event or an event report to the module and takes back a result that the analyst reviews and accepts. Four actions are available:

- **Summarise event**: produces a new event report on the event
- **Summarise report**: rewrites an existing event report with a summary block
- **Recommend tags**: suggests tags for the event, previewed in a modal and only attached once accepted
- **Extract indicators**: reads the indicators out of an event's reports and proposes them as attributes and objects through the familiar import review screen. Over REST and from a workflow, the extraction is applied directly.

Everything the module produces is tagged with the `ai-computer-assisted` provenance tags, so AI-derived content is always distinguishable from analyst-created content. Two workflow action modules are included, **Summarise report with AI** and **Extract indicators with AI**.

The feature is off by default. It is configured through the new **AI** tab of the server settings (`Plugin.AI_*`), which includes a module status card, a dry run and a **Test LLM** button that checks the LLM endpoint and the configured model are reachable. Access is gated by the new `perm_ai_tools` role permission. The earlier CTIInfoExtractor endpoint and its settings are removed in favour of this integration. The contract and the actions are documented in `docs/dev/ai_integration.md`, and a fake module server is included for testing without an LLM.

<img width="2380" height="1332" alt="image" src="https://github.com/user-attachments/assets/642f74a0-cf21-4b23-b113-c10203b8fc64" />

## Overmind continues to evolve

Overmind, the new MISP interface, received another large batch of improvements:

- **Event view**: reworked content layout, a collection card and an *add to collection* action, tag and galaxy relationships shown in place, coloured analyst data icons, an improved event report preview and markdown editor, and an add button on the reports tab. Correlation counts no longer include over-correlating and excluded correlations.
- **Indexes**: a new expandable **More filters** section on the users, servers, organisations, workflows, logs, galaxy clusters, collections and event attribute indexes; collapse and expand all on the object index; pagination and column sorting fixes in the object, attribute and AJAX tab indexes; the favourite star on the tags index; an improved active tags field on the taxonomies index; card display on the auth key index.
- **Forms**: a new JSON field component (used by the decaying model modal), reworked add/edit user, add event, import event and export forms, the new distribution component on the add forms, corrected sharing group edit fields, galaxy add/import fixes, and PGP key fetching now listing every available key.
- **Navigation**: Tags and Taxonomies swapped in the navbar.

## Fixes and usability improvements

- **Background jobs**: since 2.5.45, a job that exited successfully was marked as failed whenever it wrote anything to stderr, which MISP's own logging does routinely. Every sync and publish job could therefore show as failed. Job success is now decided on the exit code alone.
- **CSRF regressions from 2.5.46**: session-based AJAX requests (event graph, timeline, event report editor, Overmind), TAXII discovery requests and the collection view initialisation work again under the stricter CSRF validation.
- **Enrichment**: the background-jobs branch of event enrichment was unreachable, so bulk enrichment always ran synchronously in the web request. It is now queued as configured.
- **Sync**: custom galaxy cluster sync on a manual server push is fixed, and the sync buttons on the servers index of the default theme work again.
- **Event reports**: pasting pictures from the clipboard works for non site-admin users again, and a report's image upload is validated against forged paths.
- **STIX**: the STIX 1 import honours the distribution chosen in the upload form, STIX 1 export works on a scheme-less or empty baseurl, and STIX 2 import failures are reported in operator terms following the named errors introduced in misp-stix.
- **Event templates**: instantiating a template attaches a galaxy cluster's own tag name, so custom clusters are correctly tagged.
- **Event graph**: fixed loading and the extended view is honoured.
- **Workflows**: the edit page loads again and the error flash message is fixed.
- **Logs**: proposal acceptance is logged under the accepting organisation instead of SYSTEM (#824).
- **UI**: sticky table headers no longer cover the first row inside modals and scroll boxes, and the classic footer sits above them.
- **CLI**: shells exit non-zero when they stop on a usage or input error.
- **Feeds**: TweetFeed and several Threatbase feeds are added to the default feed list.
- **Login**: the pre-authentication TOTP lookup now fetches the user's disabled flag.

## Submodule updates

- **misp-galaxy**: MITRE ATLAS updated to the 2026.08 release with a new *MITRE ATLAS Case Study* galaxy, MITRE D3FEND techniques and relations updated, the MITRE Fraud Framework (F3) moved to 1.1 with relationships, new threat actors (CRPxO, VantaCore) and a fix for Sigma rules without a logsource block.
- **misp-objects**: four new detection rule objects, `elastic-detection-rule`, `kql-analytics-rule` (Microsoft Sentinel/Defender), `kunai-rule` and `splunk-rule`.
- **misp-warninglists**: 49 lists refreshed, with new generators for the Microsoft, sinkholes, dynamic DNS, RFC 6761 and Telegram IP lists, and the first update of the automated malware analysis list since 2020.
- **misp-stix**: bumped from 2026.7.8 to 2026.9.16, over 150 commits. STIX 1 import fixes (distribution parameters, object references, test mechanisms, galaxy tags and exploit targets are now applied), STIX 2 custom property names folded to the STIX character set on export and read back on import, dict-form objects, reporting of clusters and analyst data sharing one UUID, marking definitions no longer writing a second tag, new `diagnostics()` and `record_classification()` APIs for in-memory callers, named exceptions with input validation, and packaging fixes. `requirements.txt` now requires misp-stix 2026.9.16 or later.
- **CakePHP fork**: the submodule now points at [MISP/sachertortephp](https://github.com/MISP/sachertortephp) and carries the `Xml::build()` fix mentioned above.

The taxonomies, noticelists, decaying models, workflow blueprints, event templates and PyMISP submodules are unchanged in this release.

## Community contributions

Besides the security reporters above, thank you to everyone who contributed code to this release:

- Jeroen Pinoy for the galaxy cluster sync, servers index, workflows edit page, event graph loading and event report picture fixes
- James Garratt (Cosive) for the CSRF regression fixes
- elhoim for the enrichment background-jobs fix and the proposal acceptance log fix
- Thomas A. V. Sattolo for the event graph extended view fix
- Daniel López for the TweetFeed feed and Sujal Lamichhane for the Threatbase feeds

A big thank you to everyone who develops, reviews, tests, reports issues and contributes patches. MISP is what it is because of this community.

## Updating

Either just use the built in functionality in the server settings, or alternatively:

```bash
cd /var/www/MISP
sudo -u www-data git pull origin 2.5
sudo -u www-data git submodule update --init --recursive
sudo -u www-data /var/www/MISP/venv/bin/pip install -U app/files/scripts/misp-stix
sudo -u www-data app/Console/cake Admin runUpdates
```

Logging in as a site administrator runs the pending migrations as well. Notes for this release:

- The tags migration merges tag names that only differ by case into the oldest tag. Each merge is written to the audit log. Instances with many colliding tag names will see the migration take a moment.
- Monitoring that compares `actual_db_version` with `expected_db_version` should switch to `migrations_pending` and `migrations_failed`.
- The `perm_ai_tools` permission is granted to site administrators by the migration; the AI integration itself stays off until `Plugin.AI_services_enable` is set.
- Check `cake Admin migrationStatus` after the update if anything looks off.
