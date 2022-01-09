---
title: MISP 2.4.118 released (aka the exclusivity tag release and SightingDB support)
layout: post
banner: /img/blog/exclusive/exclusive-example-1.png
date: 2019-11-10
---

# MISP 2.4.118 released

A new version of MISP ([2.4.118](https://github.com/MISP/MISP/tree/v2.4.118)) has been release including a functionality that allows for tag exclusivity within taxonomies, the support for external Sighting sources via SightingDB and many fixes.

# Exclusive taxonomies

![](/img/blog/exclusive/exclusive-example-1.png)
![](/img/blog/exclusive/exclusive-example-2.png)
![](/img/blog/exclusive/exclusive-example-3.png)
![](/img/blog/exclusive/exclusive-example-4.png)

Some time ago, we've introduced the "exclusive" field in the MISP taxonomy format, in order to define rules of exclusivity within a given taxonomy predicate. As of this release, the MISP user-interface shows and enforces inconsistencies of exclusivity between tags assigned at the event and the attribute levels.

# SightingDB support

Over the course of the past years, the MISP Project has worked on improving the sighting capabilities of the platform in various ways when it comes to being able to provide contextualised sightings for information sharing. Most of the use-cases driving this type of sighting reporting were based on a need to encode intelligence gathered during incidents, as part of reporting or encoding the time-based aspects of intelligence. Being able to contextualise the sighting with information on the source, tie its release to the ACL rules governing the sighted data and describing the type of sighting were of a higher priority than performance.
After discussions with users looking for a completely diverging use-case, namely that of bulk, large-scale data/traffic analysis and correlation thereof with the threat information databases of their MISPs. Thanks to our friends at Devo, who have developed an open source system tackling these issues - the [SightingDB server](https://github.com/stricaud/sightingdb) - we had something to integrate into MISP as an alternate sightings system handling lookups against a large-scale sighting system. 

Devo also decided for the standardisation of the SightingDB protocol format and we have decided to host it under the [misp-standard.org](https://www.misp-standard.org/) umbrella.

The SightingDB support includes the following:

 - Added configuration tool
 - Added lookups from the event view
 - Added includeSightingdb flag for the restSearch searches
 - Added SightingDB search tool
 - Added SightingDB connection test tool

# Improved meta search in restSearch

The restSearch now supports the ability to search by creator organisation and also by the meta fields present in the galaxy clusters.

Such requests can now be done on any meta field within a galaxy:

~~~~
/attributes/restsearch/
{
    "galaxy.cfr-suspected-victims": ["China", "Japan"],
    "galaxy.cfr-target-category" : ["Government"]
}
~~~~

along with the various fields of the creator organisation object itself:

~~~~
/events/restsearch/
{
    "galaxy.synonyms": "APT29",
    "orgc.nationality": ["Hungary", "Belgium"]
}
~~~~

# Update module

The database schema model update has been improved in MISP and you can see the current inconsistencies of any past model change or the ongoing upgrade of the database model. This has been introduced because the next version of MISP will include a major improvement to the data model in order to add time references at several layers of the MISP data model. This update, coming in 2.4.119, includes an update of the attributes table which can take a significant amount of time depending of your MISP installation.

# MISP modules - many new modules with objects support

[Many new modules](http://misp.github.io/misp-modules/) were added such as the (event query language) EQL query module, Endgame EQL export module,  OSINT.digitalside.it lookup module and many improvements to existing modules such as the CSV import module, IBM X-Force expansion module and more. Don't forget to update your modules to the latest version.

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. Special thanks to Jakub Onderka for the continuous stream of excellent improvements, Sebastien Tricaud for the joint effort in the SightingDB support, [standard](https://raw.githubusercontent.com/MISP/misp-rfc/master/sightingdb-format/raw.md.txt) and [first implementation](https://github.com/stricaud/sightingdb).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

