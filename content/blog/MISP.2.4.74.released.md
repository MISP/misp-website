---
title: MISP 2.4.74 released
date: 2017-05-30
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.74](https://github.com/MISP/MISP/tree/v2.4.74) has been released including new features, improvements and bug fixes.

The ZeroMQ pub-sub feature has been significantly improved in MISP to allow for a complete flexible notification scheme for a host of actions which
take place within a MISP instance, such as:

- Event publishing
- Attribute creation and update
- Sighting creation
- User creation or modification

[Documentation of the ZeroMQ pub-sub](https://www.circl.lu/doc/misp/misp-zmq/) feature is available in [misp-book](https://github.com/MISP/misp-book).

A [persistent default feed list](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json) has been added including free and open feeds like:

- CIRCL
- Botvrij.eu
- InThreat
- Binary Defense Systems
- abuse.ch (multiple feeds)
- rules.emergingthreats.net
- malwaredomainlist
- TOR Node List from dan.me.uk
- cybercrime-tracker.net
- phishtank
- dns-bh.sagadc.org
- labs.snort.org
- longtail.it.marist.edu
- pan-unit42
- malwaremustdie
- booterblacklist.com
- openbl.org
- home.nuug.no
- hosts-file.net
- openphish.com
- iplists.firehol.org

which can be enabled as a feed cache to do automatic correlation within MISP without the need of importing the full data-set.

Filtering is now available via the tag index (fixing a famous request during one of the MISP training sessions ;-).

There is also an upcoming MISP training that might be of interest to MISP users, contributors or developers:

- A [MISP training](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) is foreseen in Luxembourg, the 29th June 2017. [Register](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) as soon as possible if you want to join us.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

We would like to thank all the contributors and especially the participants of the [hackathon organised](https://hackathon.hack.lu/) in Luxembourg.
