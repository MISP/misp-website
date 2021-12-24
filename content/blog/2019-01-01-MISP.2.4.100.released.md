---
title: MISP 2.4.100 released (aka happy new year release)
date: 2019-01-01
layout: post
banner: /img/blog/restsearchbuilder.png
---

Happy new year! We are so proud of our community which has supported us for the past year and we hope to do even better for 2019. Thanks a lot.

A new version of MISP ([2.4.100](https://github.com/MISP/MISP/tree/v2.4.100)) has been released with improvements to the UI, API, import and export along with the addition of a new query builder.

![](/img/blog/restsearchbuilder.png)

Considering the criticality of being able to accurately define how we query MISP instances in order to feed and integrate with network security devices, endpoint security devices or monitoring tools, we have tried to improve the life of the users tasked with the above duties via a new query builder, available through the REST client interface (REST client below the Event Actions). The query builder provides a simple interface to create your JSON queries used to get
the information you truly are interested in back for ingestion in your devices and tools easily.

Instead of going through the sometimes headache inducing task of trying to manually craft JSON objects, you can now construct complex queries via a series of simple clicks. The query builder is intelligent in a sense that it attempts to provide the exact values that are supported as options and provide you with dynamic contextual information for each of the query filters. You can subsequently test your queries and grab the code generated based on your filter choices in Python or curl format to support your integration.

UI usability has been improved with the following fixes (based on various feedbacks during the MISP trainings):

- Quickedit (double-click on value) on the event view has been replaced by a more obvious edit icon to ease cutting and pasting values the attribute list. This change has also made for the category, type and IDS fields.
- Hover functionality has been improved to avoid glitchy popovers and a scrollbar was added along with multiple bugs that were fixed.
- Clarification of the old hide tag functionality to clarify it's intended effect (being a non-selectable tag via the interface for the given instance).

Two new attribute types were introduced in MISP (thanks to the contributors):

- cdhash - Code Signing which is the canonical hash of the program’s CodeDirectory resource on Apple OS ref:[Code Signing Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/RequirementLang/RequirementLang.html). Thanks to [Daniel Roethlisberger](https://github.com/droe) for the contribution.
- ja3-fingerprint-md5 - is a hash for creating SSL client fingerprints in an easy to produce and shareable way. A tool to extract ja3 from pcap and generate ja3 object in MISP called [ja3toMISP](https://github.com/eCrimeLabs/ja3toMISP) has been developed by [eCrimelabs](https://www.ecrimelabs.com/blog/2018/12/30/ja3-to-misp-tool-released).

The types are also part of [MISP standard core format which has been updated](https://tools.ietf.org/html/draft-dulaunoy-misp-core-format-06). If you see a missing types or object template in MISP, don't hesitate to report it back to us.

Multiple bugs were fixed, such as a synchronisation bug causing certain events not getting synced via a pull due to an overzealous protection mechanism.

MISP submodule for STIX 2.x now relies on our [fork of the STIX 2 library](https://github.com/MISP/cti-python-stix2) to support import STIX 2.x files (which time-based UUIDs) produced by some vendors and tools. If you have any issue while updating the submodule, don't forget to run a `git submodule sync` before running a `git submodule update` on existing MISP instances. STIX 1 and 2 import/export has been significantly improved based on the numerous sample files received. If you have specific issues with certain STIX files, feel free to send these to us.

We would like to thank all the contributors, reporters and users who helped us in the past months to improve MISP and information sharing at large.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

A detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

We also released the [complete source code of the MISP training materials](https://github.com/MISP/misp-training) and we hope to see many improvements such as translation, new materials or ideas from the training materials.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next activities to improve threat intelligence, analytics and automation.

