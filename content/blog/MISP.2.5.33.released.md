---
title: "MISP v2.5.33: Performance, Security, and the New Overmind Theme"
author:
 - MISP Project team
date: 2026-03-03
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
banner: /img/blog/uav.png
---

# MISP v2.5.33 Release Notes (2026-02-27)

## 🎨 A Fresh Look: The "Overmind" Evolution
The UI is undergoing its most significant transformation in years. With the introduction of the **Overmind** theme, MISP is transitioning to a modern stack.
* **Bootstrap 5 & Font Awesome 7:** The core views are being migrated to modern CSS frameworks.
* **New Theme System:** Users can now select between different themes (like the new `Overmind` or Chris Horsley's `BetaUI`) if enabled by the site admin.
* **Visual Refinements:** Updates to the login page, navbar, flash alerts, and the footer.
* **Brand Update:** Say hello to the new MISP logo integrated into the Overmind theme.


In order to support the development of multiple future UI concepts, we have added support for themes in MISP. This support currently is limited to beta and in development UIs, allowing users to opt into beta UIs and developers to more smoothly collaborate on the development codebases. To understand the distinction of the UIs and their implementation differences.
* **BetaUI:** Drop in replacement with new concepts brought to the current software stack. Pages are reworked gradually without disrupting the current usage and we encourage users to switch to these and let us know what they think about the changes. 
* **Overmind: Development UI:** Since this includes a full stack change for the front-end, it isn't meant to be a gradual but rather aims to be a one-shot replacement, upon the next major MISP release. Generally we do not encourage day to day users to switch to this UI until it is more established, but for those that want to have their voices heard in regards the future of MISP, we highly encourage you to experiment with it and let us know what you think.

**Important**: In order to enable themes in MISP, administrators will now have to allow MISP to use these functionalities, so make sure that you enable the support for themes if you would like your users to be able to experiment with the new functionalities. To enable themes follow the steps described below

For regular MISP installations:

- `sudo -u www-data /var/www/MISP/app/Console/cake Admin setSetting "MISP.enable_themes" 1`

For Docker installations:

- `docker exec -it -u www-data misp-docker-misp-core-1 /var/www/MISP/app/Console/cake Admin setSetting "MISP.enable_themes" 1`


## ⚡ Sync & Performance: Built for Speed
Synchronizing large instances just got a lot lighter.
* **Fast Caching:** A new client-side caching implementation and endpoint have been added for synchronization. This bypasses the heavy `restSearch` logic, resulting in a smaller memory footprint and faster execution by handling hashing on the database side.
* **Memory Optimizations:** Under-the-hood improvements to base64 encoding (using `simdjson`) and BinaryFileEngine caching significantly reduce memory usage during event processing.
* **Sightings-free Sync:** Events can now be served without sightings during pull requests, preventing "explosive" event sizes that previously caused sync failures.

## 🤖 The "Claude" Refactor
In a bit of technical meta-history, this release features a massive refactoring of core controllers (Warninglists, Galaxies, Taxonomies, etc.) to a standardized **CRUD component**.
* This refactor was heavily assisted by **Claude 4.5**, ensuring consistency across the platform's internal logic while significantly reducing technical debt.
* A `Claude.md` file has been added to the repository to document this collaboration (and save your tokens!).

## 🛡️ Security & Hardening
Several security improvements were implemented, many thanks to reports from the community (notably Maxime ESCOURBIAC):
* **Redirection Protection:** Prevented unauthorized redirects to external websites from dashboard widgets.
* **File Upload Validation:** Fixed inconsistencies in SVG logo uploads for organizations.
* **Authkey Fixes:** Improved the generation and storage of initial user enrollment keys to ensure "new" authkey hashes provide the intended protection.
* **URL Gating:** New settings to enable/disable arbitrary URLs in event reports and workflows.

### Security advisories

- [GCVE-1-2026-0016](https://vulnerability.circl.lu/vuln/gcve-1-2026-0016) < MISP 2.5.33 - Server-Side Request Forgery via Event Report Import From URL in MISP.
- [GCVE-1-2026-0017](https://vulnerability.circl.lu/vuln/gcve-1-2026-0017) < MISP modules 3.0.5 - Improper Neutralization of Raw HTML in MISP modules Markdown-to-PDF Module Leads to HTML Injection.
- [GCVE-1-2026-0018](https://vulnerability.circl.lu/vuln/gcve-1-2026-0018) < MISP 2.5.33 - Improper access control in MISP user contact form allows cross-organisation email targeting.
- [GCVE-1-2026-0019](https://vulnerability.circl.lu/vuln/gcve-1-2026-0019) < MISP 2.5.33 - Improper URL validation in MISP dashboard button widget allows external redirection.

## 🛠️ API & Internal Changes
* **New Endpoint:** Added `/attributes/getAttributeByB64Value` for more efficient attribute lookups.
* **Freetext Improvements:** Added extraction support for Chrome and Edge browser extension IDs.
* **Library Updates:** PyMISP, misp-galaxy, taxonomies, and misp-objects have all been bumped to their latest versions.
* **Workflow Modules:** Enhancements to `threat-level-if` and `aggregate-if`.

**Full Changelog:** For a detailed list of every commit, please see the [official MISP repository](https://www.misp-project.org/Changelog.txt).


