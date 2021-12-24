---
title: MISP 2.4.107 released (aka similar objects review, yara native export)
date: 2019-05-13
layout: post
banner: /img/blog/similar-objects.png
---

A new version of MISP ([2.4.107](https://github.com/MISP/MISP/tree/v2.4.107)) has been released with a host of new features, improvements and security fixes. We strongly advise all users to update their MISP installation to this latest version.

# New main features

## Similar objects and an easy to use tool to merge them

MISP objects are now a cornerstone of describing complex data-structure along with other aspects of threat intelligence. We have seen a regular process of analysts to add new objects and having similar objects in their analysis. In MISP 2.4.107 shows similar objects (with common attributes) and proposes merging strategies into existing objects. The user-interface is easy to use and part of the standard project.

## Native yara and yara-json export

For a very long time, MISP supported the sharing of pre-crafted [YARA](https://virustotal.github.io/yara/) attributes and objects. As of 2.4.107, we've introduced the ability to export YARA rules generated from any existing attributes in MISP, via the yara and yara-json exports. Existing YARA rules will remain intact similar to the state before the current release and will be included together with the native YARA rules stored in MISP. The export depends on the [Python plyara module](https://github.com/plyara/plyara).

## API

- New includeWarninglistHits option interested for the attribute and event search APIs, enabling users to query any subset of they're misp repositories using the usual search filters to reveal potential false positives or other warnings.
- Added new export format (attack) for restSearch, opening up the usual search filters to the [ATT&CK](https://attack.mitre.org/) integration. The new export format returns the ATT&CK matrix data as HTML via the API and is therefore directly viewable via the REST client. The export was designed during the [EU ATT&CK community](https://www.attack-community.org/) workshop organised at eurocontrol.


# Various other changes

- New update process included in MISP (to prepare the merge of the "zoidberg" branch and improve the migration process).
- Installer updated and improved (MISP now works on OpenBSD 6.5 and Debian 9.9).
- Module selection improved (sorted and improved the look and feel).
- STIX export fixed for email attachments.
- RPZ export improved, including new RPZ policy actions (based on [IETF draft](https://tools.ietf.org/html/draft-vixie-dnsop-dns-rpz-00)).
- New button to quickly extend a MISP event added in the event view.
- Many bugs squashed.

# Security fixes

Thanks to João Lucas Melo Brasio from [Elytron Security S.A.](https://elytronsecurity.com) who reported the following security vulnerabilities which are now fixed in MISP 2.4.107.

- [CVE-2019-11812](https://cve.circl.lu/cve/CVE-2019-11812) A persistent XSS issue was discovered in app/View/Helper/CommandHelper.php in MISP before 2.4.107. JavaScript can be included in the discussion interface, and can be triggered by clicking on the link.
- [CVE-2019-11813](https://cve.circl.lu/cve/CVE-2019-11813) An issue was discovered in app/View/Elements/Events/View/value_field.ctp in MISP before 2.4.107. There is persistent XSS via link type attributes with javascript:// links.
- [CVE-2019-11814](https://cve.circl.lu/cve/CVE-2019-11814) An issue was discovered in app/webroot/js/misp.js in MISP before 2.4.107. There is persistent XSS via image names in titles, as demonstrated by a screenshot.:

# MISP modules

Many new [MISP modules](https://github.com/MISP/misp-modules) were added such as PDF, PPT, DOCX and XLS importer along with VMRay sandboxes analysis import.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.



