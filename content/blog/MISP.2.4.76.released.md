---
title: MISP 2.4.76 released
date: 2017-06-21
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.76](https://github.com/MISP/MISP/tree/v2.4.76) has been released including bug fixes and a set of performance improvements at the ingestion level.

- A significant issue in older MySQL versions was discovered while entering attributes which significantly improve hampered  the import speed
- CIDR block caching has been added to boost the advanced correlation performance
- Various other improvements to the fetching mechanism have been introduced to speed MISP up

ZMQ publisher has been improved with:
- invocation is now cleaner
- pub-sub redis channel is open once
- discussions at event level are available in the pub-sub channel
- additional context fields added to the discussion related messages being pushed (org name, user email and so on)

A host of new minor functionalities such as triggering of the fetching of feeds via the API, storing of STIX export errors into a log file, correction of valid port numbers for the attribute validation, etc have been added.

This release also includes multiple smaller and larger bug-fixes.

[misp-warninglists](https://github.com/MISP/misp-warninglists) and [misp-galaxy](https://github.com/MISP/misp-galaxy) updated to the latest version.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

We would like to thank all the contributors and users who reported issues or ideas in order to improve MISP.

There are still some seats left [MISP Training - June Edition (29th June)](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182).
