---
title: "MISP 2.5.37 - Templates, Assemble!"
author:
 - MISP Project team
date: 2026-04-29
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/template-ui.png
---

We are happy to announce the release of **MISP v2.5.37**, headlined by the brand-new **Event Templating system** — a complete redesign that replaces the legacy templating engine. This release also introduces a dedicated `suricata` attribute type, continues the Overmind UI migration, switches the STIX 2 stack to the upstream library bundled with `misp-stix`, ships several security fixes, and brings new performance tooling for large instances.

## Event Templating System (New)

A ground-up rewrite of MISP's templating engine. Event templates are now first-class objects with their own schema, validation pipeline, instantiation flow, library catalogue, and dedicated UI on both the default and Overmind themes.

<img width="1892" height="762" alt="list of templates" src="https://github.com/user-attachments/assets/2ea5348b-f6dc-43b4-92a7-e06c195e4877" />

<img width="1914" height="952" alt="template editor" src="https://github.com/user-attachments/assets/e898abc8-b8dd-45d7-9caa-d27fe61f699f" />

<img width="1914" height="952" alt="create event from template" src="https://github.com/user-attachments/assets/ada5f7d0-5ffe-4e96-9a92-2210cf532691" />


Highlights:

- **Schema and storage** — JSON-defined templates conforming to a versioned `event-template-v1` schema, backed by dedicated `event_templates` and `event_template_object_dependencies` tables; distribution model aligned with events.
- **Builder UI** — drag-to-reorder canvas, per-element type partials, inline definition validation via `/event_templates/validate_definition`, searchable object-template picker, taxonomy and galaxy pickers, file upload pipeline, and a Preview button on both themes.
- **User form (template instantiation)** — section-organised flow with collapsible object instances, per-type renderers, inline element-level error surfacing, file upload progress, automatic summary report, entity auto-linking in event reports, and audit-log row on event creation.
- **Templates Library** — the new [misp-event-templates](https://github.com/MISP/misp-event-templates) submodule provides a managed catalogue with first-touch auto-update, library-managed badge, update toolbar, library-status endpoint, and ten starter templates out of the box.
- **Import / Export / Duplicate** — REST round-trip for templates including full object-template dependency tracking.
- **Documentation** — admin guide, creator guide, and user quickstart added under `docs/`.
- **Migration helper** — `app/Console/cake Admin migrateOldTemplates` converts legacy templates to event templates, with dedicated handling for complex File / CnC objects.

> A separate blog post covering the new event templating system in depth — design, authoring, library workflow, and migration — will follow shortly.

### Old templating system soft-deprecated

The legacy `/templates/*` controller, model, and views remain reachable for the duration of this release, but **all menu entry points have been removed** from the global menu, navbar helper, and side menus on both default and Overmind themes. The controller and view stack will be removed in 2.5.38.

## New `suricata` Attribute Type

A dedicated `suricata` attribute type has been introduced alongside `snort`, added to support the new release of [rulezet.org](https://rulezet.org). IDS rules in Suricata format can now be modeled with a first-class type and validated as such, with corresponding support in PyMISP.

## Overmind UI (Development Preview)

Continued migration of MISP's modules to the Bootstrap 5 Overmind theme. New in 2.5.37:

- **Tags, Tag Collections, and Taxonomies** — full migration
- **Templates, Object Templates, Object Relationships** — migrated views and CRUD
- **REST Client** — migrated
- **Automation & Export Views** — migrated
- **Correlation graph** — re-implemented in vanilla JS
- **Event Templates** — full coverage (index, view, builder, user form, picker modal, import, preview)

Supporting fixes include ACL gap closures, condition tightening on index actions, a unified copy-to-clipboard helper, `setting/role` ACL backfills, and XSS hardening in the Collection view, IndexTable fields, and event-template builder.

> **Note:** Overmind UI remains a development preview; production use is not yet recommended. It can be enabled via the theme selector in the MISP settings.

## Workflow Improvements

- **Ad-hoc workflows** — environment variables can now be passed in, and module-returned data is captured under `_env.misp_module_results` for use by downstream nodes.
- **New trigger** — `analyst-data:after-save`.
- **Documentation** — info-modal documentation added describing misp-module return data.
- **Fix** — `event:run-workflow` no longer includes the env variable twice.

## STIX 2 Stack Switch

MISP no longer ships its own fork of `cti-python-stix2`. The upstream `stix2` library bundled with `misp-stix` is now used directly:

- The custom `cti-python-stix2` submodule has been removed.
- STIX 2 export now defaults to **version 2.1**.
- New library entry point enables exporting MISP Object collections to STIX 2.x.
- `misp-stix` and `misp-lib-stix2` bumped to the latest aligned versions — see the [misp-stix 2026.4.28 release notes](https://github.com/MISP/misp-stix/releases/tag/2026.4.28) for the full changelog on that side.

## Performance Tooling

- **Search performance diagnostics** — new tool to profile attribute search behaviour on large datasets.
- **Performance shell** — updated to use approximations, making it usable on very large instances.
- **Attribute search** — incremental performance fix for certain query shapes.

## Security Fixes

- **SQL injection via `order` / `sort` parameters** — user-controlled values on `POST /events/index` and `GET /shadow_attributes/index` reached the SQL `ORDER BY` clause without validation, allowing any authenticated user (including read-only) to extract arbitrary database content via blind injection. Both paths now route through `AppModel::findOrder()` / a schema allowlist (reported by Jeroen Gui).
- **Privilege escalation via authkey reset** — an organisation admin in the same org as a site admin could reset the site admin's authentication key via `POST /users/resetauthkey/<id>` and receive the new key in the response. Fixed by adding a `perm_site_admin` check in `User::resetauthkey()` and tightening `AuthKeysController::__prepareConditions()` to exclude site-admin users from the org-admin listing scope (reported by Jeroen Gui).
- **UUID validation on Collections** — collection UUID input is now validated against RFC 4122 (reported by Jeroen Pinoy).
- **Event-template XSS hardening** — XSS-surface review of the event-template builder, picker modal, and user form on both default and Overmind themes.

### GCVE Allocation

- [GCVE-1-2026-0029](https://vulnerability.circl.lu/vuln/gcve-1-2026-0029) < MISP 2.5.37 - Improper UUID validation in MISP Collections
- [GCVE-1-2026-0030](https://vulnerability.circl.lu/vuln/gcve-1-2026-0030) < MISP 2.5.37 - MISP - Improper access control in auth key reset allows privilege escalation to site administrator
- [GCVE-1-2026-0031](https://vulnerability.circl.lu/vuln/gcve-1-2026-0031) < MISP 2.5.37 - MISP - SQL injection via unvalidated ordering parameters in event and shadow attribute listings

## Bug Fixes

- Decay score no longer collapses to zero when `last_seen` is in the future.
- Geolocation markers — missing icon assets restored.
- `baseurl` no longer prepended in places where it caused accordions to fail; `baseurl` handling tightened in several other views.
- Tag search re-enabled on the event index.
- Sticky table header on the role index page.
- Line breaks now allowed in analyst-data notes.
- Domain restrictions render with proper line breaks.
- Padding adjustments and undefined-variable fixes across Overmind views.
- ARIA labels improved on icon-only controls.
- Stale Danish MISP community entry removed.
- `db_schema` consistency fix.
- Missing `usersetting` ACL entry restored.
- LDAP plugin gains support for `memberOf` queries.
- Add-attachment flow rework.

## Installer / CI / Developer Experience

- `.gitmodules` `cakephp` `branch` metadata corrected from the historic `2.x` to the actually-tracked `master-cakephp2-php8`. The pinned SHAs were already on the correct branch; this just fixes misleading metadata.
- CI workflow updated to `actions/checkout@v4`.
- CI raises PHP `memory_limit` to 512M before MISP starts.
- Python required-version bump.
- Composer / asset query-version bump (184 → 185).

## Submodule Updates

Code-side libraries:

- [`PyMISP`](https://github.com/MISP/PyMISP) — bumped to 2.5.34.1 (includes the `suricata` validator).
- [`misp-stix`](https://github.com/MISP/misp-stix) — bumped to [2026.4.28](https://github.com/MISP/misp-stix/releases/tag/2026.4.28).
- [`misp-lib-stix2`](https://github.com/MISP/misp-lib-stix2) — aligned with upstream `cti-python-stix2`.

Data libraries — notable changes since v2.5.36:

- [`misp-galaxy`](https://github.com/MISP/misp-galaxy) — 73 commits
  - **New galaxies**: SPARTA, MITRE Fraud Framework, VERIS framework, RMM tools, operating systems, IT-equipment types, software vendors, taxonomy of fraud.
  - **New tooling**: Python tooling for galaxy-relationship graphs (with multiple output formats incl. GraphML and static HTML), threat-actor similarity report tooling, similarity-distance tool, matrix-view tooling, `gen_sparta.py` empty-tactics handling.
  - **Content updates**: threat-actor metadata sweep, Iranian threat-actor review, preventive-measures update, additional threat actors and botnets.
- [`misp-objects`](https://github.com/MISP/misp-objects) — 37 commits
  - **New object templates**: `rulezet-bundle`, `ruleset-metadata`, `dga-domain`, `drone-RID-observation`, `contact-list` (mobile forensic extractions), `fbi-most-wanted`, `terminal-output`, `malicious-website`, `exif`, generic `software` / `service` / `container`, generic `physical-object` / `item`, `mfa-auth`.
  - **Schema additions**: new attribute type, `transport` category, sane defaults for `chat-message`, `pcap-metadata` capture-application, packet-filter rule values, etc.
  - **Refactors**: `malware`, `mfa-auth`, `dga`, `yara`, `ais*` reformatted via `jq` for consistent ordering; `chat-message` cleanup.
  - **`uav`**: Flight Controller and firmware-hash attributes added; `ui-priority` typo fixed.
  - **`x509`**: missing certificate fields filled in (issue #88).
  - **`suricata`**: object templates now use the new first-class `suricata` attribute type (instead of `snort`).
- [`misp-warninglists`](https://github.com/MISP/misp-warninglists) — 15 commits
  - April **Network Telescope** update.
  - **microsoft-attack-simulator** update incorporating PR #329.
  - New script to fetch Windows binary hashes and generate a warninglist from them.
  - Phone-generation regex pattern fix; multiple `list.json` refreshes.
  - README clarification on the relationship between warninglists and `misp-feedback`.
- [`misp-taxonomies`](https://github.com/MISP/misp-taxonomies) — 4 commits
  - **New** [`cloud-sovereignty`](https://github.com/MISP/misp-taxonomies/tree/main/cloud-sovereignty) (SoV) taxonomy describing cloud sovereignty.
  - **New** [`ai-computer-assisted`](https://github.com/MISP/misp-taxonomies/tree/main/ai-computer-assisted) taxonomy describing the level of AI assistance and the level of review involved in producing an intelligence package or event.
- [`misp-event-templates`](https://github.com/MISP/misp-event-templates) — **new submodule** (initial integration)
  - Ten starter templates: `ransomware-incident`, `credential-exposure`, `suspicious-domain-triage`, `malware-sample-submission`, `vulnerability-disclosure`, `supply-chain-compromise`, `espionage-case`, `financial-fraud-case`, `uav-observation`, `spearphishing-email`.
  - Schema: `event_report` element type, distribution model rename, `pinned_version` → `minimum_version` rename across schema and templates.

Unchanged since v2.5.36: [`misp-noticelist`](https://github.com/MISP/misp-noticelist), [`misp-decaying-models`](https://github.com/MISP/misp-decaying-models), [`misp-workflow-blueprints`](https://github.com/MISP/misp-workflow-blueprints).

## Deprecations and Removals

- **Legacy templating** — soft-deprecated; menu entry points removed. Controller and views will be removed in 2.5.38.
- **Custom `cti-python-stix2` submodule** — removed in favour of the upstream `stix2` provided via `misp-stix`.

For full details, see the [complete changelog](https://github.com/MISP/MISP/compare/v2.5.36...v2.5.37) on GitHub.
