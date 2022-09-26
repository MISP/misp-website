---
title: MISP 2.4.163 released with improved periodic notification system and many improvements
date: 2022-09-26
layout: post
banner: /img/blog/periodic-summary/periodic-summary-2.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.163](https://github.com/MISP/MISP/releases/tag/v2.4.163) with an updated [periodic notification system](https://www.misp-project.org/2022/09/12/2022-09-12_periodic_notifications.html/) 
and many improvements. 


# Updated periodic notification system

- A new option has been added to set the number of days for the trending calculation.
- New correlation are now showed in the periodic notification.
- Only the top 10 MITRE ATT&CK techniques are displayed and sorted by number of occurrences.
- Layout has been improved in the UI and also in the static email rendering.
- Only show data in the chart for tags having changes over time.

For more information, check out the [Periodic summaries - Visualize summaries of MISP data](https://www.misp-project.org/2022/09/12/2022-09-12_periodic_notifications.html/) blog.

# Fixes

- MISP [OpenAPI description file](https://www.misp-project.org/openapi/) has been improved.
- [community] Clarification concerning the NATO process.
- [ssdeep] Check if the ssdeep contains newline characters.
- Many code clean-up and speed-up included.
- Improvements and bugs fixed in the correlation engine.
- Many bugs fixed.

Thanks to all the contributors and users reporting bugs to make the software better.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core. 

# misp-stix v.2.4.163

misp-stix has been released too and now in-line with the MISP release schedule. The full [changelog is available](https://www.misp-project.org/Changelog-misp-stix.txt).

Many improvements in the MISP galaxy and especially the threat-actor galaxy, [360.net Threat Actors](https://www.misp-project.org/galaxy.html#_360_net_threat_actors) added. There is a detailed [changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt).

New `financial` taxonomy and many other taxonomies. There is a detailed [changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt).

Multiple objects were updated and added, for [more details](https://www.misp-project.org/Changelog-misp-objects.txt).

Various fixes in [misp-modules](https://misp.github.io/misp-modules/) for more [details](https://www.misp-project.org/Changelog-misp-modules.txt).


