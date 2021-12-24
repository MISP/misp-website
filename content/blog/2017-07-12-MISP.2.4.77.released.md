---
title: MISP 2.4.77 released
date: 2017-07-12
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.77](https://github.com/MISP/MISP/tree/v2.4.77) has been released including security fixes, bug fixes and various improvements.

This version includes multiple security fixes reported by cert.govt.nz including:

- Some security settings including GnuPG/SMIME passwords for the signing keys used for notifications in MISP and the redis password are now redacted from the server settings accessible via the UI.
- Sanitisation of template uploader view in regards to file names has been tightened.
- Avoid any data leakage through exceptions thrown by the GFI uploader on failed parsing when debug mode is enabled. Replaced by instead giving proper a warnings via flash messages.
- Hashing algorithm updated to bcrypt for new users and updated transparently for existing users at the next login.
- All profile edit pages now require the user's or admin's password to be confirmed to limit the impact on potential session hijacking.

A significant speed improvement on the feed pull has been done for the CSV/freetext import especially for very large feeds. This speed improvement partially carries over to any tasks that add attributes to already large events.

Screenshots are now included in search results to better support users actively sharing image artefacts using MISP.

A host of minor and visual improvements were introduced.

MISP taxonomies, galaxies and PyMISP updated to the latest version. New default feeds (e.g. dataplane.org) have been added.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

We would like to thank all the contributors and users who reported issues or ideas in order to improve MISP. A special thank for the security report
from cert.govt.nz, we always appreciate security analysis of MISP. Don't hesitate to forward any security report (PGP encrypted) to us [via CIRCL](https://www.circl.lu/report/). 

Don't forget our [MISP summit 0x3](https://2017.hack.lu/misp-summit/) before the [hack.lu](https://2017.hack.lu/) 2017 conference which will take place from 14:00 to 18:00, Monday 16 October 2017.
