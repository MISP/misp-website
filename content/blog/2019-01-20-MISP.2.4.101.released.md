---
title: MISP 2.4.101 released (aka 3 features for free)
date: 2019-01-20
layout: post
banner: /img/blog/tag-collection-creation.png
---

A new version of MISP ([2.4.101](https://github.com/MISP/MISP/tree/v2.4.101)) has been released with 3 main new features (tag collections, improved tag/galaxy selector and MISP instance caching), along with a host of improvements and bug fixes.

## Tag collections

![](/img/blog/tag-collection-creation.png "{class='img-responsive'}")

Contextualisation in threat intelligence is one of the key activities when performing analysis and when reviewing or processing information from internal or external sources. The task can be rather tedious, but nevertheless, it's a critical step in ensuring the quality and the information's capacity to be used for automatic processing. MISP 2.4.101 introduces a new concept, in an attempt to improve the "time-to-contextualise" information for users using the platform. Tag collections, a new feature in 2.4.101, aim to allow users to predefine re-usable structures consisting of a set of tags (from taxonomies) along with galaxy information attached. Analysts can use these named collections to quickly classify information with all of the contextualisation labels declared in the collection. This functionality enables anyone using MISP to significantly lower the time it takes to classify information and to ensure that all the pre-defined context related information is attached to an event or attribute. This feature is a first step in opening up the sharing of analysisMISP best practices directly via the platform itself.

## Improved tag/galaxy selector

![](/img/blog/tag-collection.png "{class='img-responsive'}")

The success of MISP taxonomies and galaxies since their inception has been suffering from a minor but annoying drawback. When we originally designed the user-interfaces of the tag and galaxy systems in MISP, our immediate intent was to handle a rather small set of taxonomies. Since then we have come a long way and thanks to the many excellent contributions we've received from the community, the ugly side-effect of our original design decisions reared its head: adding multiple tags and galaxies has become a tedious chore, especially when trying to contextualise several aspects of the information to be shared, using multiple tags and galaxies.

In order to solve this issue, a complete new selector-system has been added to ease the process of adding multiple tags and galaxies. The design was based on various issues and the feedback we have received from private organisations, CSIRTs and analysts. Let us know what you think about it and don't hesitate to [open an issue for bugs or feedback on the improved selector](https://github.com/MISP/MISP/issues).

## MISP instance caching

Synchronisation between MISP instances has always been a core functionality of MISP in order to support the sharing of information. This release includes a new feature, allowing administrators to perform MISP remote instance caching without the need to synchronise and pull events. The MISP instance caching feature supports the built-in correlation system of MISP along with the overlap matrix of the feed system. This allows users to see cross-instsance correlations without the need to ingest the data of other instances directly and to include remote instances in the feed correlation system to compare how the information of feeds stacks up to that contained on other instances. This also opens up a host of possible multi-MISP scenarios when it comes to running collection-oriented "junk" MISPs internally and being able to cross correlate them with the operational instances. Keep in mind, in order to benefit from this system, the instance to be cached also has to be on at least version 2.4.101.

## New attribute type

"[HASSH](https://github.com/salesforce/hassh)" is a network fingerprinting standard which can be used to identify specific Client and Server SSH implementations.  The fingerprints can be easily stored, searched and shared in the form of an MD5 fingerprint.

hassh-md5 and hasshserver-md5 types are now part of [MISP standard core format which has been updated](https://tools.ietf.org/html/draft-dulaunoy-misp-core-format-06). If you see a missing types or object template in MISP, don't hesitate to report it back to us.

## Many improvements

- A new unpublish action has been added to simplify the process in the user-interface.
- Disable correlation is now accessible when creating/modifying an attribute.
- New default feed added (from [mirai.security.gives](https://mirai.security.gives)).
- Many improvements in the STIX2 import and export.
- Various bugs fixed.

We would like to thank all the contributors, reporters and users who helped us in the past months to improve MISP and information sharing at large.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

A detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next trainings, talks and activities to improve threat intelligence, analytics and automation.

