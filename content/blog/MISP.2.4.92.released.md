---
title: MISP 2.4.92 released (aka performance improvement)
date: 2018-06-07
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.92](https://github.com/MISP/MISP/tree/v2.4.92) has been released including aggressive performance boosts, various improvements and bug fixes.

We received feedback from various users about the negative impact on performance when the [MISP warning-lists](http://www.github.com/MISP/misp-warninglists/) are enabled (a feature allowing the detection and filtering of false positive attributes in MISP).  The performance hit incurred by enabling warning-lists has been reduced to such an extend that enabling them will barely have any impact on performance when viewing or browsing events. We hope this performance gain will increase the overall adoption of the warning-lists.

A benchmarking tool has been added to the AppModel allowing us to easily spot performance issues across the application. Aggregate execution time, number of iterations and peaked memory usage can be easily spotted in order to facilitate rapid and accurate profiling of the performance across the various functionalities of MISP.

The API has been improved to allow objects to be added by template UUID and version in addition to the local ID.

A new role permission to publish to the ZMQ pub-sub channel has been added (as kindly requested by our favorite user, who regularly motivates us by sending decapitated horse heads if we slack). This role allows administrators to enable or disable ZMQ publishing per user.

The flash message system has been rewritten from scratch, providing a cleaner approach that relies on bootstrap's internal flash messaging look and feel, along with 3 different levels of notifications.

Allow hard deleting of attributes that were never published in order to avoid the leaking of sensitive information via soft deleted attributes.

Two security vulnerabilities were fixed: [CVE-2018-11245](https://cve.circl.lu/cve/CVE-2018-11245) and [CVE-2018-11562](https://cve.circl.lu/cve/CVE-2018-11562).  Thanks to the reporters Jarek Kozluk from zbp.pl and Dawid Czarnecki. Don't hesitate to contact us for [reporting vulnerabilities](https://github.com/MISP/MISP/blob/2.4/CONTRIBUTING.md#reporting-security-vulnerabilities), we love those contributions.

The STIX 1 and STIX 2 exports and imports were migrated to Python 3 (don't forget to update the dependencies). The STIX 1 export has been improved to include additional objects such X.509 certificate and MISP objects. The STIX 1 import has been improved for email, whois, and artifact objects along with tags via journal entries. The STIX 2 export has improved regkey object parsing, along with ip|port and custom object export.

The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

A huge thanks to all the [contributors](/contributors) who helped us to improve the software and also all the participants in MISP training which always give intere
PyMISP has been also updated, boasting a more clever approach to timestamp handling while updating MISP JSON files. The PyMISP documentation has been updated [PDF](https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf). [MISP standard Internet-Drafts](https://github.com/MISP/misp-rfc) have been updated and published.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

Don't forget that the MISP Threat Intelligence Summit 0x4 will take place the Monday 15th October 2018 before hack.lu 2018. A [Call-for-Papers is open](https://cfp.hack.lu/misp0x4/) for the MISP Threat Intelligence Summit 0x4. We would be glad to see users, contributors or organisations actively using MISP or/and threat intelligence to share their experiences and presentation to the CfP.
