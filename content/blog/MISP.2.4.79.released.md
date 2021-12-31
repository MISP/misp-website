---
title: MISP 2.4.79 released
date: 2017-08-25
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.79](https://github.com/MISP/MISP/tree/v2.4.79) has been released including an important security fix (persistent XSS on comment field), multiple bug fixes and new functionalities.

All the taxonomies actions (including index, view, enable, disable) are now accessible via the API.

The feed previews are now exposed to the API in addition to the graphical user-interface.

Additional command line tool such as enabling/disabling misp or changing baseurl can be done from command line (e.g. easing the automation and deployment of MISP instances at large scales).

Set the current password confirmation requirement for any user profile edits as optional (off by default).

Feeds (caching and updates) can now be updated via the scheduler.

[CVE-2017-13671](https://www.circl.lu/advisory/CVE-2017-13671/) was fixed. A MISP user having access to a MISP instance can inject JavaScript in a discussion comment field, aka XSS.  The comment field is not part of the MISP synchronisation and only impacts the users of the same instance. Thanks to Jurgen Jans and Cedric Van Bockhaven from Deloitte for the security report. 

MISP taxonomies, galaxies (including the MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK™)) and PyMISP updated to the latest version.

Multiple annoying bugs were fixed in the UI and API including [#2394](https://github.com/MISP/MISP/issues/2394), [#2387](https://github.com/MISP/MISP/issues/2387), [#2381](https://github.com/MISP/MISP/issues/2381).

The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

Don't forget our [MISP summit 0x3](https://2017.hack.lu/misp-summit/) before the [hack.lu](https://2017.hack.lu/) 2017 conference which will take place from 14:00 to 18:00, Monday 16 October 2017. The core team of MISP will also join the [hack.lu open source security software hackathon 0x2 ](https://hackathon.hack.lu/) which will take place 19-20 October 2017.

A new MISP training will take place in Luxembourg the 21st November 2017, [registration is now open](https://www.eventbrite.com/e/misp-training-november-edition-tickets-36347289722).
