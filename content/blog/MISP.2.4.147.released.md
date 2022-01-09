---
title: MISP 2.4.147 released (improvements and bug fixes release)
date: 2021-07-27
layout: post
banner: /img/blog/misp-openapi.png
---

# MISP 2.4.147 released

MISP 2.4.147 released including a massive number of small improvements, bug and security fixes. We strongly recommend all MISP users to upgrade as soon as possible. This release fixes [CVE-2021-37534](https://cvepremium.circl.lu/cve/CVE-2021-37534).

# Sync improvements

Many improvements were done in the synchronisation such as:

- When saving sightings, only push the new sightings.
- Filter out existing sightings if remote sever supports that method.
- Check if event exists before pushing.
- Check event existence before pushing sightings.
- Optimise event filtering.

# API/CLI

Many improvements in the API and CLI.

This release also includes refactoring of various forms to support future major improvements in MISP.

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html)
.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

