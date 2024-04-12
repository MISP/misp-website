---
title: MISP 2.4.189 released with bug fixes, performance improvements and a new blocklist feature. 
date: 2024-04-12
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

We are pleased to announce the immediate release of MISP 2.4.189, released with bug fixes, performance improvements and a new blocklist feature.

### New Features

#### Sighting blocklists

Sightings were something initially intended as a system of pinpointing the continued prevalence of indicators as seen by our communities, but as it happens with ever growing, interconnected communities, new use-cases do emerge. Some of those use-cases involve the collection of "bulk sightings" - for example by directly using a SIEM or IDS to feed your sighting collection. 

Whilst this has many potential applications, especially for internal use-cases, it can easily get out of hand when such massive data amounts are shared across larger communities, easily going into the billions of sightings rather rapidly.

We have therefore introduced a new blocklist system that allows MISP administrators to filter out organisations with such use cases from their sighting sync use-cases. Make sure to use the new subsystem if you feel overwhelmed by such sighting strategies.

When synchronising with peers running MISP 2.4.189+, the filtering already happens during the negotiation phase, drastically reducing the time it takes to synchronise instances.

This development is an outcome of the JTAN (Joint Threat Analysis Network) project hackathon and workshop organised in Luxembourg. 

#### Analyst data relationship improvement

Analyst data is still a very fresh feature, allowing the community to further elaborate on, share their points of view on or to interlink the various data points in MISP. Especially the latter pillar of the new system had, as pointed out by some community members, a pretty massive flaw in the first implementation. Users could create and quantify relationships between data points, but the relationships would only be visible unidirectionally on the source object. This has now been resolved and data-points being referenced by others are now properly highlighted.

#### New attribute type, integer

In hindsight, this seems like a massive oversight, but better late than never: We now have an "integer" attribute type, something that we until recently used the "count" type for, though it always felt like ramming a round peg through a square hole. If you are using your own object templates, make sure you revise them for the next iteration - whilst "count" is often the right choice, a generic integer may be more accurate in some of those cases.

### Performance improvements

This is yet another rapid release for a set of planned performance improvements, expect more frequent releases in the next few weeks as we resolve bottlenecks.

### A long list of bug fixes

Please refer to the full [changelog](https://www.misp-project.org/Changelog.txt) for a full list of fixes and improvements. Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!
