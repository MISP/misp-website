---
title: "MISP 2.5.46 released -  security hardening, major performance gains, knowledge-base updates and Overmind moving forward"
author:
 - MISP Project team
date: 2026-09-10
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/new-correlation2.jpeg
---

MISP 2.5.46 is out, and the project continues to move at a **very active development pace**.

This release brings together a large security review, significant performance improvements, major updates to the MISP knowledge bases and submodules, many fixes contributed by the community, and another substantial round of work on **Overmind**, the evolving MISP user interface.

The volume and diversity of changes in this release also reflect the current activity around MISP: development, security reviews, performance work, knowledge-base maintenance, UI improvements and external contributions are all happening continuously across the project.

<img width="1919" height="942" alt="Screenshot from 2026-09-10 10-10-18" src="https://github.com/user-attachments/assets/40fcbbd0-5b12-49af-9e20-e2b31464c36d" />


## Major security hardening

A large part of this release is dedicated to improving MISP's security posture.

A new shared **`UrlEgressValidator`** introduces a common policy for outbound URL requests, validating schemes and resolved addresses and blocking loopback, link-local and private destinations where appropriate.

`CurlClient` has also been extended with:

* host pinning;
* controlled and validated redirects;
* response size limits;
* TLS peer verification enabled by default.

These changes provide the foundation for securing the different places where MISP retrieves remote resources.

Several concrete SSRF-related issues have consequently been addressed, including:

* event report URL imports;
* feed redirects;
* TAXII discovery;
* credential forwarding during redirects;
* access to internal or private network destinations.

The security review also resulted in a broad range of additional fixes:

* rejection of empty and non-string LDAP and LinOTP credentials;
* session ID rotation after `CustomAuth` authentication;
* brute-force protection for email OTP verification;
* improved CSRF protection across user settings and dashboard actions;
* conversion of numerous state-changing GET requests to POST;
* stricter sharing-group authorisation;
* enforcement of `perm_modify` when deleting attributes;
* access-control enforcement in the OnDemand correlation engine;
* ACL checks for collection objects, graph references, feeds and cryptographic keys;
* SVG sandboxing for inline-served organisation logos and report pictures;
* prevention of stored and reflected XSS through URL and event filtering parameters;
* protection against path manipulation in server-side file deletion;
* redaction of information that should not be exposed to insufficiently privileged users;
* improved authentication-failure logging and throttling.

Many of these issues were identified during the extensive review performed with the **Scottish Government – National Cyber Team**, by **elhoim (David André)**, and through additional internal review.

A big thank you to everyone involved in this work.

## Significant performance improvements

This release also contains some important performance work.

### Event report counts

Event report counts on event indexes previously resulted in one count query per event. The new implementation performs grouped queries instead.

For a default page containing 60 events, this reduces roughly **60 database round trips to one or two queries** depending on the user context.

Benchmarks with a real MariaDB instance showed improvements in the range of roughly **19× to 35×** for this operation.

### Sightings retrieval

Sightings attached during `MispAttribute::fetchAttributes()` are now fetched in batches rather than individually for every attribute.

Previously, a 50,000-attribute batch could potentially trigger a huge number of database queries. The new implementation groups the work into chunked queries while preserving the existing sightings policies and ACL behaviour.

In the benchmark used during development, the sighting attachment step went from:

**8.109 seconds / 10,661 queries**

to:

**0.149 seconds / 6 queries**

for a 5,000-attribute test case — more than a **50× reduction for that part of the processing path**.

This should particularly benefit large instances and high-volume export or REST API workloads.

## Major updates to MISP galaxies, warning lists and knowledge bases

MISP 2.5.46 is also accompanied by significant updates to the data and knowledge bases shipped through the MISP submodules. These repositories are increasingly important parts of the MISP ecosystem in their own right and are under continuous development alongside the core software.

### `misp-galaxy`

The **MISP Galaxy** knowledge base received another major refresh, with substantial improvements across threat actors, ransomware, tools, frameworks and other structured threat-intelligence datasets.

In particular, the **MITRE ATT&CK galaxies have received major updates and improvements**, keeping the MISP representation closely aligned with recent ATT&CK developments. The updated representation includes improvements around tactics, techniques and sub-techniques as well as newer ATT&CK concepts such as **Detection Strategies** and **Analytics**, making ATT&CK information richer and more directly usable when modelling, correlating and exchanging threat intelligence in MISP.

The wider `misp-galaxy` repository is also seeing sustained development, including new and updated threat actors, ransomware information, specialised frameworks, tooling and improvements to relationships and metadata. This continuous maintenance is important: galaxies are not static lookup tables, but evolving knowledge bases used by MISP communities and many other threat-intelligence tools.

### `misp-warninglists`

The **MISP Warning Lists** have also received a major update, with many existing lists refreshed and numerous sources added or improved.

The warning-list collection now covers an increasingly broad range of infrastructure that can otherwise generate false positives during threat-intelligence processing, including known scanners and research infrastructure, cloud and service-provider ranges, public services, crawlers, benign software hashes and other commonly encountered Internet infrastructure.

Recent additions and updates include data for network and security scanners, Network Telescope-derived scanner ranges, Cortex/Xpanse infrastructure, Telegram-related infrastructure and many other regularly changing sources.

These updates are especially valuable as the volume of observable data handled by MISP installations continues to increase. Warning lists provide an important layer for **contextualising indicators, reducing false positives and helping analysts distinguish expected Internet infrastructure from potentially actionable indicators**.

Both `misp-galaxy` and `misp-warninglists` are standalone open-source projects as well as MISP submodules, and contributions to these knowledge bases directly benefit the broader threat-intelligence community.

## Overmind continues to evolve

Development of **Overmind**, the evolving MISP user interface, remains very active.

This release brings another large set of improvements, including:

* card views for additional indexes;
* server-specific card views;
* improved Galaxy card views;
* multiple cards per row;
* smoother switching between table and card views;
* improved Event view;
* filtering improvements;
* warning-list filtering in correlation graphs;
* responsive correlation graph timelines;
* correlated events collapsed by default;
* improved role display;
* improved publication confirmation dialogs;
* unified confirmation modals;
* improved modal sizing;
* Galaxy support inside Tag Collections;
* expanded quick actions for events;
* improved Galaxy actions and icons;
* additional filtering for attributes;
* the first version of the **MISP Tutorial**.

The Event quick-action cards now expose additional operations such as:

* merge attributes;
* enrich event;
* contact reporter;
* delegate publishing;
* execute ad-hoc workflows;
* recorrelate events.

Overmind is progressing rapidly and continues to cover more and more of the existing MISP workflows.

## 🛠️ Fixes and usability improvements

As usual, the release contains many smaller fixes across MISP.

Among them:

* focus URLs now correctly reach attributes outside the first page of large events;
* application-log quick filters persist across pagination;
* analyst-data synchronization uses POST for UUID lists, avoiding HTTP 414 errors;
* feed correlation settings are handled more safely;
* taxonomy attachment from the Tags index has been corrected;
* Galaxy search no longer fails when joined tables introduce ambiguous column names;
* event report counts now exclude soft-deleted reports;
* event reports belonging to events from other organisations are counted correctly according to ACLs;
* picture references in event reports are counted using both aliases and filenames;
* dashboard CSV exports are now properly formed;
* CLI audit records correctly identify CLI activity and impersonated users;
* tests have been updated for Python 3.12 and recently hardened POST-only endpoints.

PyMISP, MISP taxonomies, warning lists and MISP galaxies have also been updated.

## Community contributions

This release again shows how active the MISP development community is.

Alongside the core development team, fixes and improvements were contributed or reported by several community members, including:

* **Scottish Government – National Cyber Team**
* **elhoim / David André**
* **skraft9**
* **Dmitry Rantovov**
* **Thomas Lacroix**
* and many others contributing code, knowledge bases, testing, reviews and feedback.

The project is currently seeing sustained work across **security, performance, user experience, threat-intelligence knowledge bases, information-sharing workflows, APIs and large-scale deployments**.

This is exactly what keeps an open-source project such as MISP healthy: continuous review, continuous improvement and contributions coming from its users and community.

## An active development model

The development and release workflow has also been documented more explicitly.

Normal development takes place on the `develop` branch, feature branches are merged back into `develop`, and `develop` is merged into the `2.5` branch for releases. Direct commits to `2.5` are reserved for urgent hotfixes.

This release is therefore not an isolated batch of changes: **MISP development is continuous**, and work toward the next release is already happening as soon as a release is published.

The same applies to the wider MISP ecosystem. Projects such as **misp-galaxy, misp-warninglists, PyMISP, MISP taxonomies and the other MISP libraries and knowledge bases evolve continuously**, often independently of the core release cycle.

## Updating

Given the number of security, performance, data-quality and reliability improvements included in this release, we recommend MISP administrators update their instances to the latest version.

As always, thank you to everyone who develops, reviews, tests, reports issues, contributes patches, maintains integrations, improves knowledge bases, and runs MISP in production.
