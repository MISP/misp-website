---
title: MISP 2.4.73 released
date: 2017-05-09
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.73](https://github.com/MISP/MISP/tree/v2.4.73) has been released including new features, improvements and bug fixes.

A new module type Cortex has been introduced allowing for easy integration of MISP and Cortex. [Cortex](https://github.com/CERT-BDF/Cortex) is the analysis engine part of the [TheHive Project](https://thehive-project.org/) which supports expansion services from Cortex within MISP. A new setting has been added to support Cortex similarly to MISP expansion modules where you set the remote Cortex instance. MISP includes a new Cortex attribute type to allow for the raw analysis to be stored along with the event for subsequent analysis.

![feed overlap analysis matrix](/img/blog/feed-overlap-analys-matrix.png "{class='img-responsive'}")

The MISP feed handling was reworked to expand the functionality and avoid the past limitation:

- feeds can now be fetched and compared with events without being imported as MISP events. This is a significant improvement to allow for fast lookups of feed indicator values against any event. A new column has been introduced in the event view to add a correlation counter linking to the cached feeds.

- As the feed indicators are now cached in Redis, MISP is now offering the capability to compare the similarities between feeds. An overview matrix is available, showing the overall overlap of indicators among the different feeds. The table is
there to support analysts and aid them in better understanding the different levels of coverage provided by their feed collections.

The feed management and information is only accessible to the MISP site admin by default.
An option has been added to allow other users of an instance to benefit from the feed correlation data but this needs to be explicitly set by the site admin while creating a new feed. This allows users to benefit from a feed without sharing the configuration details or even the existance of a feed source.

Multiple updates have been done to the API:

- freeTextImport is now accessible via the API to allow the import from unstructured text similar to the functionality in the user-interface. As there is no

- JSON based extension formats can now be updated via the API (warninglists, taxonomies, galaxy-clusters)

[MISP galaxy](https://github.com/MISP/misp-galaxy) and [MISP taxonomies](https://github.com/MISP/misp-taxonomies) updated to the latest version, including new threat actors, ransomware and tool definitions.

There is also an upcoming MISP training that might be of interest to MISP users, contributors or developers:

- A [MISP training](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) is foreseen in Luxembourg, the 29th June 2017. [Register](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) as soon as possible if you want to join us.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.

We would like to thank all the contributors and especially the participants of the [hackathon organised](https://hackathon.hack.lu/) in Luxembourg.
