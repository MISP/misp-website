---
title: MISP 2.4.98 released (aka usability improvements and SleuthKit mactime import)
date: 2018-11-26
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP ([2.4.98](https://github.com/MISP/MISP/tree/v2.4.98)) has been released with new features such as improved UI consistency (such as attributes search output), improved validation error messages, a new built-in experimental SleuthKit mactime import, new small features and many bugs fixed.

The user interface has been significantly improved in regards to the reporting of validation errors occuring whilst attempting to save attributes. The user can now view the attributes not properly imported and the
reason for the validation failing. A user can view the failed/succeeded saves resulting from batch imports via the UI. Additionally a host of small fixes for the flash message system have been implemented.

The output of the search interface is now consistent with standard attributes view in MISP. The user can now add sighting, tags, galaxies directly in the search results.

A new experimental import functionality has been included to import SleuthKit mactime timelines from MISP directly. The user can import one or more mactime timelines in MISP, which will be included as a mactime object to describe forensic activities on an analysed file system. The import is a two-step process where the user can cherry pick the forensic events which took place and select the meaningful activity to be added in a MISP event.

![SleuthKit mactime import in MISP](/img/blog/mactime1.png)
![SleuthKit mactime imported in MISP as objects](/img/blog/mactime2.png)

The API has been improved with many new features such as:

- The result counts to restsearch API are now visible via the x-result-count header
- The option includeProposals is now functional at attribute level restSearch
- The event controller readability has been improved
- Fixed a bug blocking malware samples from being added using /events/add when the encrypt=1 flag was set for raw sample inclusion
- Sighting restSearch API documentation has been fixed
- Better handling when trying to edit an attribute without adequate permissions
- Throw a proper error when trying to edit an event without access to doing so
- Fixed non exportable tags being included in the attribute level restSearch.

In the CSV export functionality, the ignore flag is restored to the old behaviour:

- If not set, only return published events / to_ids flagged events by default
- Setting ignore:0 will result in the default behaviour
- Setting ignore:1 will result in unpublished events and non to_ids attributes being filtered out
- Fixed a bug that broke the CSV api if ignore:0 was passed

Many long-standing bugs were fixed based on the feedback from various users and organisations.

In STIX 1 import, AIS marking is now included in import as MISP event tag. Many improvement in STIX 1 and STIX 2 import/export, check the changelog for the complete changes.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. New object templates were introduced to improve the support for the description of forensic analysis cases and improve their sharing. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

A detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next activities to improve threat intelligence, analytics and automation.

