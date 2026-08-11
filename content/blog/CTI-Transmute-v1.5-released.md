---
title: CTI-Transmute 1.5 released with 16 security fixes and a first-class public API
author:
 - Christian Studer
date: 2026-08-11
tags: ["MISP", "Threat Intelligence", "release", "CTI-Transmute", "STIX"]
layout: post
banner: /img/cti-transmute.png
---

# CTI-Transmute 1.5 released

CTI-Transmute is an open-source service for converting threat intelligence between formats - MISP and STIX today, more to come - with a catalogue on top to store, share, comment on and evaluate the results. It wraps the [misp-stix](https://github.com/MISP/misp-stix) library behind a web UI and a public API.

Version 1.5 is out, and it is dominated by three things: **16 security fixes** identified through multiple reviews, a **first-class public API** for the conversion catalogue, and the **architecture work** that made both possible - a real test suite going from 0 to 516 tests, CI on every push, and a clean separation between the conversion engine, the service layer and persistence.

**All users of 1.4 and earlier should upgrade.** The release also carries a database schema rename and a set of HTTP method changes, so read the [Upgrading section of the release notes](https://github.com/MISP/cti-transmute/releases/tag/v1.5) before deploying.

The instance operated by [CIRCL](https://www.circl.lu) (Computer Incident Response Center Luxembourg) is already running 1.5 - feel free to give it a try, no installation needed:

👉 [https://cti-transmute.org](https://cti-transmute.org)

## Security

This release fixes **16 security issues**, found by an external security review by Jeroen Pinoy and an internal one. Every issue is remediated in this release and ships with a dedicated regression test that pins the fixed behaviour.

All sixteen advisories are published through [vulnerability.circl.lu](https://vulnerability.circl.lu), each with a GCVE and a CVE identifier.

**Four findings are rated High severity**, and they are the reason to upgrade without delay - all four are reachable without authentication or through a simple forged request:

- [GCVE-1-2026-20038](https://vulnerability.circl.lu/vuln/gcve-1-2026-20038) / [CVE-2026-69078](https://www.cve.org/CVERecord?id=CVE-2026-69078) (CVSS 8.8) - **Unauthenticated HTML injection in the evaluation PDF export.** Injected markup reached the PDF renderer, which followed `file://` paths and internal URLs, so an anonymous caller could read local files and probe internal services through the exported document.
- [GCVE-1-2026-20111](https://vulnerability.circl.lu/vuln/gcve-1-2026-20111) / [CVE-2026-69082](https://www.cve.org/CVERecord?id=CVE-2026-69082) (CVSS 8.8) - **CSRF-driven admin user deletion.** The account delete route mutated state over `GET`, so any attacker page an administrator's browser loaded could delete user accounts with a simple `<img src=...>`.
- [GCVE-1-2026-20135](https://vulnerability.circl.lu/vuln/gcve-1-2026-20135) / [CVE-2026-73160](https://www.cve.org/CVERecord?id=CVE-2026-73160) (CVSS 8.7) - **Unauthenticated SSRF on the remote-MISP fetch routes.** The target URL was only checked against internal addresses given as IP literals, so a hostname resolving to an internal IP let an anonymous caller use the instance as a proxy into its own network - and read the responses.
- [GCVE-1-2026-20064](https://vulnerability.circl.lu/vuln/gcve-1-2026-20064) / [CVE-2026-69079](https://www.cve.org/CVERecord?id=CVE-2026-69079) (CVSS 8.7) - **Unauthenticated denial of service on the activity timeline.** The `days` parameter was unbounded, so a single anonymous request could trigger arbitrarily large work.

The remaining twelve findings are rated Medium (one Low). They cluster into stored XSS across several views, private data disclosed by missing authorization checks, and further state-changing `GET` routes:

| Advisory | CVSS | Finding |
|----------|------|---------|
| [GCVE-1-2026-20090](https://vulnerability.circl.lu/vuln/gcve-1-2026-20090) / [CVE-2026-72759](https://www.cve.org/CVERecord?id=CVE-2026-72759) | 6.9 | Private conversion content disclosed via history entries of deleted conversions |
| [GCVE-1-2026-20037](https://vulnerability.circl.lu/vuln/gcve-1-2026-20037) / [CVE-2026-72760](https://www.cve.org/CVERecord?id=CVE-2026-72760) | 5.3 | User e-mail addresses disclosed through the account following list |
| [GCVE-1-2026-20160](https://vulnerability.circl.lu/vuln/gcve-1-2026-20160) / [CVE-2026-73140](https://www.cve.org/CVERecord?id=CVE-2026-73140) | 5.3 | Private evaluation comments disclosed through unauthenticated report exports |
| [GCVE-1-2026-20170](https://vulnerability.circl.lu/vuln/gcve-1-2026-20170) / [CVE-2026-73155](https://www.cve.org/CVERecord?id=CVE-2026-73155) | 5.3 | Missing authorization allows reacting to comments the user cannot see |
| [GCVE-1-2026-20179](https://vulnerability.circl.lu/vuln/gcve-1-2026-20179) / [CVE-2026-73156](https://www.cve.org/CVERecord?id=CVE-2026-73156) | 5.3 | Unauthenticated stored XSS in the conversion sunburst tooltips |
| [GCVE-1-2026-20115](https://vulnerability.circl.lu/vuln/gcve-1-2026-20115) / [CVE-2026-73162](https://www.cve.org/CVERecord?id=CVE-2026-73162) | 5.3 | CSRF on GET: follow and notification routes mutate state over GET |
| [GCVE-1-2026-20109](https://vulnerability.circl.lu/vuln/gcve-1-2026-20109) / [CVE-2026-71502](https://www.cve.org/CVERecord?id=CVE-2026-71502) | 5.1 | Unauthenticated stored client-side template injection executes JavaScript in any viewer's session |
| [GCVE-1-2026-20062](https://vulnerability.circl.lu/vuln/gcve-1-2026-20062) / [CVE-2026-72751](https://www.cve.org/CVERecord?id=CVE-2026-72751) | 5.1 | Unauthenticated stored XSS in the conversion graph view |
| [GCVE-1-2026-20074](https://vulnerability.circl.lu/vuln/gcve-1-2026-20074) / [CVE-2026-73158](https://www.cve.org/CVERecord?id=CVE-2026-73158) | 5.1 | Stored XSS through saved graph configurations |
| [GCVE-1-2026-20164](https://vulnerability.circl.lu/vuln/gcve-1-2026-20164) / [CVE-2026-73159](https://www.cve.org/CVERecord?id=CVE-2026-73159) | 5.1 | Stored XSS via the tag icon field executes in an admin session |
| [GCVE-1-2026-20177](https://vulnerability.circl.lu/vuln/gcve-1-2026-20177) / [CVE-2026-73161](https://www.cve.org/CVERecord?id=CVE-2026-73161) | 5.1 | Stored XSS via the conversion-table search highlight |
| [GCVE-1-2026-20082](https://vulnerability.circl.lu/vuln/gcve-1-2026-20082) / [CVE-2026-73157](https://www.cve.org/CVERecord?id=CVE-2026-73157) | 2.3 | Stored XSS from remote MISP content in the event browser |

Beyond the individual fixes, the defences changed structurally:

- A **Content-Security-Policy with a per-request nonce** - injected markup now raises a CSP violation instead of executing, and every inline event handler in the templates was rewritten to make this possible.
- **Server-rendered values can no longer be executed as front-end template code** - Vue's expression delimiters are neutralised at the template-render boundary, and the set of Vue-mounted page regions is recorded and linted so a regression fails the test suite.
- A **full security header set** and **hardened session cookies** (`Secure`, `SameSite=Lax`).
- The **PDF renderer no longer touches the filesystem or the network** - a custom WeasyPrint URL fetcher refuses `file://` and non-allowlisted hosts.
- The **remote-MISP fetch routes require a login**, and their target URL is vetted against the resolved IP.
- **Routes that mutate state no longer answer GET** - twelve routes now require `POST` or `DELETE` with a CSRF token.

The full table of findings, with CWEs and affected versions, is in the [release notes](https://github.com/MISP/cti-transmute/releases/tag/v1.5).

## A first-class public API

The public API previously exposed only the conversion *action* - the catalogue was reachable only through the web UI's session-authenticated routes. 1.5 closes that gap:

| Endpoint | Description |
|----------|-------------|
| `GET /api/conversions` | Paginated catalogue, access-scoped to the caller. Supports `page`, `q`, `search_scope`, `exact_match`, `tags`, `date_from`/`date_to`, `sort`, `visibility`, `mine`, `type`. |
| `GET /api/conversions/<id>` | One conversion, including its input and output. |
| `GET /api/conversions/<id>/history` | A conversion's accepted re-run history, oldest first. |

Authentication uses an **`X-API-KEY` header**: absent means anonymous (matching a logged-out browser), a key matching a user makes that user the actor, and a key matching nobody is a `403` rather than a silent fall-through to anonymous. Access parity with the browser is exact - anonymous callers see public conversions only, and a conversion the caller cannot see returns `404` rather than `403`, so a private record's existence is never confirmed to a stranger.

The conversion endpoints also gain **`?persist=true`**, which saves the result to the catalogue exactly as a web submission would, returning the record's `url`, `id` and `uuid` in the response.

## Parameters declared once, recorded forever

Converter parameters used to be re-declared by hand at every surface: a parser for the API, a WTForm for the web page, and choices hardcoded a third time in the template. Each Converter now declares its parameters once as a schema, and every surface is generated from it: `GET /api/convert/list` publishes each converter's JSON Schema and description, the conversion pages render their forms from the published schema, and Pydantic validates the parameters on the way in.

Each conversion also **records the typed parameters it ran with**. Re-running a conversion prefills the form from the stored parameters, and the free-form conversion type string is replaced by explicit `source_format` / `target_format` slugs.

## Under the hood

- The conversion engine is now a **registry of Converters**, each declaring its source and target formats, its parameter model, its output format and a description. Supporting a new format is a registry entry, not an edit across every page.
- A cleaner architecture separates the **conversion engine, the service layer and persistence**, making the public API a first-class interface rather than a secondary path around the web application.
- **From 0 to 516 tests**, covering the converters, the API, the service layer, the repositories and the web routes, with CI running Ruff and pytest across Python 3.10 to 3.13 on every push and pull request.

## Interface and graph view

The graph view is completely reworked, powered by **[Pivotick](https://github.com/Pivotick/Pivotick) 1.5** (thanks Sami Mokaddem!) - 409 upstream commits bringing a faceted multi-select sidebar, a type-aware properties panel, image node rendering, note cards and a mode-driven control layout. Pivotick 1.5 was itself hardened as part of the same security review, and the graph view now rests on that.

Also in this release:

- **Public user profiles and a follow system**.
- **Simpler instance management** - database migrations are applied automatically on startup, with new commands for creating an emergency administrator (`manage create_admin`) and accessing the database directly (`manage psql`).
- Timestamps serialize as ISO-8601 UTC and render in the viewer's timezone.
- A **documentation refresh**, with key API and application details pinned by tests so they can no longer silently drift from the code.

## Upgrading

Read the [full release notes](https://github.com/MISP/cti-transmute/releases/tag/v1.5) before deploying. In short:

- **Back up the database first.** Four new migrations run automatically on startup; the `convert` tables are renamed to `conversion` and two migrations rewrite data.
- **Twelve routes no longer accept GET** - any external script or integration calling them must send `POST` or `DELETE` with a CSRF token.
- **Session cookies now default to `Secure`** - instances reached over plain HTTP by IP or hostname must opt out explicitly with `SESSION_COOKIE_SECURE=false`.
- **The CSP is strict** - local customisations adding external origins or inline scripts need the CSP template updated.

## Acknowledgements

Thanks to all contributors and testers! A special thanks to Théo Geffé for the many contributions throughout the release, to Jeroen Pinoy for the thorough security review, and to Sami Mokaddem for Pivotick.

CTI-Transmute is co-funded by CIRCL and by the European Union through the ENSOC project.

- Source code: [https://github.com/MISP/cti-transmute](https://github.com/MISP/cti-transmute)
- Release notes: [https://github.com/MISP/cti-transmute/releases/tag/v1.5](https://github.com/MISP/cti-transmute/releases/tag/v1.5)
- Public instance: [https://cti-transmute.org](https://cti-transmute.org)
