---
title: MISP 2.4.65 released
date: 2017-02-09
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.65](https://github.com/MISP/MISP/tree/v2.4.65) (and 2.4.64) has been released, including bug fixes and new features.

API access added to the MISP statistics providing [additional statistics](https://www.circl.lu/doc/misp/automation/index.html#additional-statistics) regarding information on contributions by organisation, attributes used and tags. The API can be also used by monitoring tools to monitor the state of a MISP instance.

Mass tagging of attributes is now available at the event view level.

An advanced correlation mechanic has been added to support new extended correlations. The new experimental feature can be enabled to correlate on CIDR network blocks.

An option (which can be enabled server-wide) has been added to allow the sanitisation of fields (category, type, value, comment, to_ids) on delete.

Bugs were fixed, especially on the database indexing level (significant improvement in the indexer algorithm) as well as various other improvements that were included.

[MISP galaxy](https://github.com/MISP/misp-galaxy) has been updated to the latest version.

A big thanks to all the users who gave feedback and contributors who helped us improve MISP.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
