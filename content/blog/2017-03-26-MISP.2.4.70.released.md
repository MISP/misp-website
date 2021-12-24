---
title: MISP 2.4.70 released
date: 2017-03-26
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.70](https://github.com/MISP/MISP/tree/v2.4.70) has been released including new features, improvements and important bug fixes.

- A significant improvement has been introduced to the MISP user-interface to make it [more accessible](https://github.com/MISP/MISP/issues/2038) especially for visually impaired users.
- API improvements introduced to allow adding several attributes in one go.
- API extended to support the functionality of adding and editing MISP servers.
- A simple update feature from the user-interface was introduced to ease the update process of MISP.
- New attribute types (hex, sigma and impfuzzy) have been introduced for new misp-objects and to improve the support of the new [sigma format](https://github.com/Neo23x0/sigma). Sigma is a generic signature format for SIEM Systems. This new attribute type will help the development of a sigma converter via misp-modules.
- Test and diagnostic for the MISP server synchronisation has been significantly improved. The old legacy and mangle sync for very old MISP instances (2.3x) has been removed in an effort to make the code cleaner and improve the synchronisation process with recent MISP instances.

Many other bugs fixed and minor features added.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
