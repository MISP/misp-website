---
title: MISP 2.4.135 released (galaxy 2.0)
date: 2020-12-16
layout: post
banner: /img/blog/galaxy2.0/4.jpeg
---

# MISP 2.4.135 released

Don’t let the minor version number change fool you, this release is a game changer for MISP and information sharing in general. Galaxy 2.0 brings about the ability to customise Galaxy clusters (threat-actors, @MITREattack or any knowledge base element) as well as to extend and share it within your community. This release also includes many new improvements such as a new authkey system to better handle your API keys in MISP.


![](https://www.misp-project.org/img/blog/galaxy2.0/1.jpeg)
![](https://www.misp-project.org/img/blog/galaxy2.0/2.jpeg)
![](https://www.misp-project.org/img/blog/galaxy2.0/3.jpeg)
![](https://www.misp-project.org/img/blog/galaxy2.0/4.jpeg)

The galaxy 2.0 feature is large and provide many new features. For a complete overview, the [following slide deck](https://www.misp-project.org/misp-training/a.10-galaxy-2.0.pdf) provides a good introduction to galaxy 2.0.

# New Advanced API authkeys

Advanced authkeys will allow each user to create and manage a set of authkeys for themselves, each with individual expirations and comments. API keys are stored in a hashed state and can no longer be recovered from MISP. Users will be prompted to note down their key when creating a new authkey. You can generate a new set of API keys for all users on demand in the diagnostics page, or by triggering the advanced upgrade. If you upgrade your MISP, you need to enable this new feature in the security configuration (Security.advanced_authkeys).

# JARM fingerprint format added

MISP (and MISP standard format) now includes the support for [JARM](https://github.com/salesforce/jarm), active Transport Layer Security (TLS) server fingerprinting tool.

# STIX 2 import improvements

- Fixed parsing of objects mapped into galaxies for external STIX.
- For objects from external STIX content that should be mapped as galaxies (such as malware, threat actor, and so on), we do not only test the perfect match with one of the galaxy names in the mapping dictionary, we also test now if the galaxy name is contained in any of the known galaxy names of the dictionary


Additionally, a host of other improvements are documented in the [complete changelog](https://www.misp-project.org/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html)
.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

