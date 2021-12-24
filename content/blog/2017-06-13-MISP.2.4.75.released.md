---
title: MISP 2.4.75 released
date: 2017-06-13
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.75](https://github.com/MISP/MISP/tree/v2.4.75) has been released including bug fixes and a set of performance improvements.

In this release the most important improvement is performance tuning to improve the day-to-day life of the users. The performance improvements are most explicitly on:

- Pagination on events with a lot of attributes has been significantly improved.
- Warning-lists are now stored in the Redis data store which improves the warning-list lookup notably.
- Memory usage of the search API has been drastically reduces

New features were introduced, such as the mass-delete feature in the user-interface on the event index as well as at the API level where a list of event IDs to be deleted can now be posted to the appropriate API.

Multiple improvements in the ZMQ publisher script to support Python 3 including a bug fix to avoid the tearing down of the ZMQ socket for each message published.

Galaxies updated to the latest version including a complete new galaxy for [RAT (Remote Access Trojan) definitions](https://www.circl.lu/doc/misp-galaxy/index.html#_rat).

This release also includes bug fixes to the STIX exports where some installations using different versions of the Python libraries would be unable to export events in STIX format.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

We would like to thank all the contributors and users who reported issues or ideas in order to improve MISP. 
