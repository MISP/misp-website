---
title: "MISP 2.5.48 - Many security fixes, XLSX export feature, misp-modules tags removal and many bugs fixed"
author:
 - MISP Project team
date: 2026-10-01
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

**This is mainly a security release.** It closes a large batch of findings from the autumn
2026 review round, and every instance should be updated. Alongside the security work
it brings a new XLSX export, tag removal from misp-module results, and a set of sync,
ACL and correlation bug fixes.

<img width="1859" height="999" alt="image" src="https://github.com/user-attachments/assets/56b37970-f8c7-420c-b657-b6d6ef7e3a7c" />

## Security

2.5.48 fixes **20 vulnerabilities**, plus **6 further hardening changes** made during
the same review. They cover stored and reflected cross-site scripting, mass-assignment
and record-targeting flaws, event and object access-control gaps, multi-factor
authentication token reuse, and the handling of data received from linked servers.

Individual findings are not detailed here. They are published on the MISP security
page as the advisories go out, and (G)CVE identifiers and severity scores are being
processed by the GCVE team.

### Thanks to the reporters

Our thanks go to everyone who reported to us in this round, for the quality of the
reports and for their patience through a long coordinated-disclosure cycle:

- **Jeroen Pinoy**
- **David André - elhoim** (https://github.com/elhoim)
- **Wenhao Wu**
- **Bastien Bossiroy of NCIA**
- **Célien Desteucq of NCIA**
- **Tanguy Snoeck of NCIA**
- **Jan Verschueren of NCIA**

Several of the findings in this release were reported independently by more than one
of them; joint credit is recorded in the individual advisories.

---

## New features

### XLSX export

Events, attributes and sightings can now be exported directly as an Excel
workbook, available wherever the CSV export is offered (the per-event download list,
the mass export picker and `restSearch`).

Values that Excel would interpret as a formula keep their exact content and are marked
with the `quotePrefix` cell style, so nothing is evaluated on open and no characters
are added to the data. For workflows that re-export the workbook back to CSV,
`escape_formulas_literal:1` switches to the literal apostrophe form instead.

The XLSX entry is now listed above CSV in the export pickers, and the CSV entry is
labelled as not being intended for Excel. Please for the love of Cthulhu, stop sending us reports
about the CSV export being vulnerable to Excel formula inclusion. CSV != Excel, MISP shares IoCs
which we don't want to mangle for the SIEM, detection tool, etc consumers for whom the CSV format is meant.
We hope that with all the warnings in the UI now users will use the native xlsx format now for all
ingestions into excel and similar tools.

### Tag removal from misp-module results

Enrichment and import modules can now return a `remove_tags` list on a result row, and
MISP will strip those tags from the attribute the row points at. When the attribute
already exists in the event, the row changes its tags instead of creating a duplicate.
Removed tags are reported in the resolution screen and in the `EventShell` enrichment
output alongside the ones that were added.

---

## Bug fixes

- **Sync:** objects created without a description were rejected by every instance
  receiving them, silently dropping the object and all of its attributes.
- **Sync:** the local and non-exportable tag filter ran only once per event instead of
  once per event report, so all but one report lost their tags on the remote — and a
  withheld final report made the remote reject the whole event.
- **Proposals:** the proposal ACL accepted any attribute or object carrying one of the
  user's sharing groups regardless of its distribution, and gave the owner organisation
  no access to proposals on its own organisation-only attributes.
- **Attributes:** the permission check on attribute restore was inverted for
  `perm_modify` users.
- **Correlations:** the correlation distribution snapshot was not refreshed when an
  event edit changed its distribution or sharing group, so declassified or broadened
  events failed to re-surface their correlations.
- **Events:** deleting an event left event report tags, event graphs, proposal
  correlations, fuzzy ssdeep chunks and attachment scan results behind as orphans.
- **Enrichment:** a missing-argument error when enriching an object.
- **CRUD:** `correlation_exclusions/add` answered 403 with an empty error list, because
  the add path handed the whole request body to the save rather than the model's own
  block.

---

## Development and testing

- New regression suite, `tests/testregressions.py`, covering fixed security findings.
  Each test builds and tears down its own state under a random identifier so it cannot
  pass on leftovers from an earlier run, and it is now part of the CI pipeline.
- New guide for running MISP from a working copy of the repository on top of the
  `MISP/misp-docker` images: `docs/dev/docker-dev-environment.md`, referenced from
  `CONTRIBUTING.md`.
- New unit tests for the XLSX writer and export, the galaxy icon name validation and
  the module tag-removal path.

---

## Submodules

No submodule pointers moved in this release. The bundled galaxies, taxonomies,
warninglists, noticelists, object templates, event templates, decaying models,
workflow blueprints and PyMISP are unchanged from 2.5.47.

Instances that track these lists through the usual update mechanisms (the feed and
warninglist update tasks, or `git submodule update --remote`) are unaffected by this
and continue to receive upstream content as normal.

---

## Upgrade notes

- No database migration ships with this release; the schema is unchanged from 2.5.47.
- The standard update procedure applies (`git pull` on the 2.5 branch, submodule
  update, `composer install`, and `app/Console/cake Admin runUpdates`).
- Nothing in this release changes an existing API contract or export format. The XLSX
  export is additive, and the CSV export is untouched apart from its label in the
  export pickers.

## Contributors

Thanks to **Luciano Righetti** and **David André - elhoim** for the code contributions in this
release, and to everyone who reported issues, tested fixes and helped triage.

