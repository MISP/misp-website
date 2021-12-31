---
title: MISP 2.4.87 released (aka translate everything, improvements everywhere and more)
date: 2018-01-28
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.87](https://github.com/MISP/MISP/tree/v2.4.87) has been released including a massive contribution enabling support for internationalisation and localisation in the MISP UI (a huge thank to Steve Clement of CIRCL for the tedious work), as well as a host of improvements to the UI, feed and APIs, including bug fixes and speed improvements.

The feed system now supports the ability to add any arbitrary HTTP headers which can be used to cache and get feeds from feed providers with authentication. A basic authentication widget has been added to easily generate the appropriate
authentication header for a feed. Feed providers are more than welcome to contact us, if they would like to have their feed metadata added to the default MISP installation.

The MISP ZMQ publish-subscribe channel has been extended with a new specific channel for all activities related to [tags](https://www.misp-project.org/taxonomies.html).

[Warning-list](https://github.com/MISP/misp-warninglists) can now support a regular expressions in addition to the string, substring, hostname and CIDR parsing algorithms. This allows the creation of a new type of versatile of warning-lists, which can be used to filter false-positives at the API level (using the `enforcewarninglist` option in the API) and to limit the export of false-positives.

The MISP automatic upgrade model has been improved to decouple DB changes from MISP version number allowing a more flexible upgrade model.

Free-text import improved to support automatic category switching based on currently selected types making it more adaptable for corner cases and easing the life of users taking advantage of this functionality in general.

Speed-up of the event history and tag views, expect massive speed boosts.

Many bug fixes and improvement were introduced in this version. The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

PyMISP has been improved with additional tests. The PyMISP documentation has been updated [PDF](https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf).

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

We have many trainings and events foreseen in the next weeks, feel free to have a look at [our events page](/events/).
