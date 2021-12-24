---
title: MISP 2.4.128 released (STIX import/export refactored release edition)
date: 2020-06-24
layout: post
banner: /img/blog/d4_sshd_widget.png
---

# MISP 2.4.128 released

A new version of MISP ([2.4.128](https://github.com/MISP/MISP/tree/v2.4.128)) has been released with a significant refactoring of the STIX import/export along with many improvements and bugs fixed.

# STIX 2 and 1 major refactoring and improvements

A major refactoring of the STIX (version 1 and version 2) import/export has been performed by Christian Studer. We invite you to read the [Changelog](https://www.misp-project.org/Changelog.txt) for the complete set of changes and improvements. The most significant change is the import of threat-actors, tools and alike. As of this version on, the import process automatically maps the data-points to existing galaxies. As an example, if a synonym of a threat-actor is found in the original STIX file, the import process will attach the existing threat-actor from the MISP galaxy library. It also works with tags.

# Security fix

- [CVE-2020-14969](https://cve.circl.lu/cve/CVE-2020-14969) <= MISP 2.4.128 - app/Model/Attribute.php in MISP 2.4.127 lacks an ACL lookup on attribute correlations. This occurs when querying the attribute restsearch API, revealing metadata about a correlating but unreachable attribute.

# New features

- [correlations] Enable CIDR correlations for ip-src|port and ip-dst|port types
- [widget]  Authentication failure widget added to provide a dashboard from [D4 project](https://www.d4-project.org/).

Many other improvements are documented in the [complete changelog is available](https://www.misp-project.org/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.


