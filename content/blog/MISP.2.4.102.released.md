---
title: MISP 2.4.102 released (aka bug fixes and FOSDEM release)
date: 2019-02-02
layout: post
banner: /img/blog/anon-graph.png
---

A new version of MISP ([2.4.102](https://github.com/MISP/MISP/tree/v2.4.102)) has been released with several fixes, various UI improvements, new types and a praise to the open source community.

## New types

### Anonymisation

Sharing and exchanging information encompasses a lot of different models, communities or practices, with the MISP project being involved in various discussions and projects centered around building sharing and information exchange communities. A complex topic comes up regularly, namely the anonymisation of the information exchanged. Sharing anonymised information often aims to simply share the existence of knowledge about information. We introduced a new attribute type in MISP called "anonymised", which can be combined with a newly introduced object called [anonymisation](/objects.html#_anonymisation).

![](/img/blog/anon-graph.png "{class='img-responsive'}")
![](/img/blog/anon2.png "{class='img-responsive'}")
![](/img/blog/anonymisation.png "{class='img-responsive'}")

The design is flexible and can be extended with new anonymisation techniques and/or approaches. We are standing on the shoulders of giants, for example open source tools such as [Crypto-PAn](https://www.cc.gatech.edu/computing/Networking/projects/cryptopan/), [ipsumpdump](https://github.com/kohler/ipsumdump) or [arx](https://arx.deidentifier.org/).

### Bro -> Zeek

The open source NIDS [Bro project was renamed Zeek](https://blog.zeek.org/2018/10/renaming-bro-project_11.html) in late 2018. Bro has a growing community and NIDSs are important in ensuring the detection and enforcement of threat intelligence information shared within various communities at the network level. We added a new MISP type called zeek which can be used in exactly the same fashion as the bro type (which will remain in place to ensure backwards compatibility). As diversity is of utmost importance when it comes to information security and also to open source NIDS options, the MISP standard core format supports [Suricata](https://suricata-ids.org/), [Snort](https://www.snort.org/) and [Zeek](https://www.zeek.org/).


## Sighting

![](/img/blog/sighting-UI.png "{class='img-responsive'}")

- MISP UI has been improved to allow sighting at the attribute level or at the global level.
- Various improvements to the sighting hover such as a generic hovering support.
- ReST API for sighting improved.
- ReST API bug fixes where sightings were added to every single attributes when addSighting failed.
- Search results now include sighting results too.

## Enhancements

- Server settings have been refactored and streamlined with the UI server settings.
- [Installation documentation](https://misp.github.io/MISP/) has been improved with a generic Debian installer script.
- restSearch APIs improved in regards to better support for URL parameters.
- Feed correlation is no longer visible when attributes have correlation disabled.
- Translations of the UI were improved and new languages were added (Updated: Czech 4%, Danish 53%, German 21%, French 95%, Italian 39%, Japanese 95%, Korean 3%, Brazilian Portuguese 6%, Spanish 3% new: [i18n] Hungarian, Russian, Ukrainian, Simplified Chinese.)
- STIX 1 and 2 exports are now using the restSearch API instead of the old download interface.
- Major improvements in the handling of malware samples in STIX 1 and 2 format.

Many bugs were fixed and various small improvements were performed. A significant fix to improve performance for older versions of MySQL were implemented to avoid incorrect indexes being preferred for some specific queries.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large. As this is the FOSDEM release, we would like to praise all the open source software and their respective authors who have helped us to make the MISP project a reality, including (in no particular order and this is in no ways meant to be exhaustive) [Redis](https://redis.io/), [PHP](http://php.net/), [Python](https://www.python.org/), [TheHive Project](https://thehive-project.org/), [LIEF - Library to Instrument Executable Formats](https://lief.quarkslab.com/), [MariaDB](https://mariadb.org/), [vis.js](http://visjs.org/index.html), [ZMQ](http://zeromq.org/) ...

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next trainings, talks and activities to improve threat intelligence, analytics and automation.

