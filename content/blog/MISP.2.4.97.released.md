---
title: MISP 2.4.97 released (aka so many new features)
date: 2018-10-30
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP ([2.4.97](https://github.com/MISP/MISP/tree/v2.4.97)) has been released with new features such as related tags, the sighting restSearch API, a new French localisation along with many improvements to the API and he import/export capabilities, such as improved support for [DHS AIS](https://www.us-cert.gov/ais) STIX 1 files.

![MISP event graph to display an overview of the relationships for a malware infection](/img/blog/eventgraph.png)

The new related tags functionality has been introduced to allow users to view the most commonly used tags for a specific attribute across all events. This can help analysts when deciding to use a specific classification based on previous analyses to reduce the time it takes to contextualise the new information.

![MISP event graph to display an overview of the relationships for a malware infection](/img/blog/related-tags.png)

A new API has been introduced, allowing users to search [MISP sightings](https://www.misp.software/2017/02/16/Sighting-The-Next-Level.html) using a set of filter parameters along with a list of data formats (JSON, CSV or XML). The search is available on an event, attribute or instance level. You can easily search by time ranges (from, to or last) using the standard restSearch API syntax.

At the API level, many changes were introduced such as:

 - [Galaxy](/galaxy.html) API is now exposed and can be browsed via the API.
 - Event index API can now be exported in CSV format in addition to standard JSON format.
 - Log entries are now exposed via the API. The API is documented via the template system/REST client.
 - The Warning-list lookups are now exposed to the API. A value can be quickly tested against the warning-lists enabled on a MISP instance without the need to create any persistent data.

Many fixes were introduced to the STIX 1 and 2 import and export including a better support of AIS markings and specific MISP objects.

The French localisation of the user-interface is now complete (thanks to all the contributors). French is now the second localisation after Japanese to reach full coverage. If you want to contribute and help with the translation project, don't hesitate to [join us on crowdin](https://crowdin.com/project/misp).

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. New object templates were introduced to better support the description of forensic analysis cases and improve their sharing. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

A detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next activities to improve threat intelligence, analytics and automation. We have also two MISP trainings foreseen in Luxembourg Monday 17th December [MISP Training - Threat Intelligence Analyst and Administrators](https://en.xing-events.com/MURFIIQ) and Tuesday 18th December [MISP Training - Developers session - API and Extensions ](https://en.xing-events.com/QDBMTBT.html).
