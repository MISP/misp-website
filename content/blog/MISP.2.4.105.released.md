---
title: MISP 2.4.105 released (aka security fix for CVE-2019-10254)
date: 2019-03-28
layout: post
banner: /img/blog/distribution-graph.png
---

A new version of MISP ([2.4.105](https://github.com/MISP/MISP/tree/v2.4.105)) has been released to fix a security vulnerability ([CVE-2019-10254](https://cve.circl.lu/cve/CVE-2019-10254)) in addition to some minor improvements and a fix for the STIX 1.1 import, enabling the import of files with additional namespaces (such as [CISCP](https://www.dhs.gov/cisa/cyber-information-sharing-and-collaboration-program-ciscp)).

This release includes a security fix for a reflected XSS ([CVE-2019-10254](https://cve.circl.lu/cve/CVE-2019-10254)) vulnerability in the default layout template as reported by Tuscany Internet eXchange - Misp Team - TIX CyberSecurity (Thanks to them!). We strongly recommend that everyone update their MISPs to the latest version.

The STIX 1.1 import can now import STIX files using additional, non-standard namespaces (such as [CISCP](https://www.dhs.gov/cisa/cyber-information-sharing-and-collaboration-program-ciscp)).

# Improvements

- A new diagnostic to display the status of all the git sub-modules.
- Replaced the old non-cached export page with improved restSearch.
- Multiple improvements in the UI.
- Russian translation of the UI added.
- STIX 1.1 export fixed to set the adequate TLP marking.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next trainings, talks and activities to improve threat intelligence, analytics and automati
on.


