---
title: MISP 2.4.116 released (aka the new decaying feature)
date: 2019-09-17
layout: post
banner: /img/blog/decay.png
---

# MISP 2.4.116 released

A new version of MISP ([2.4.116](https://github.com/MISP/MISP/tree/v2.4.116)) has been release, including a long awaited major new feature that deals with decaying indicators in addition to a new ATT&CK sightings export and a new sync priority capability.

## Major new feature - decaying indicators

After several years of gathering requirements, doing [research](https://arxiv.org/abs/1803.11052) and various implementation attempts, MISP 2.4.116 finally includes [a new extensive feature for Decaying Indicators](/2019/09/12/Decaying-Of-Indicators.html) using an advanced model to expire indicators based on custom and shareable models.

The feature allows MISP users to have a simple yet customisable system to automatically (or in some cases semi-manually) mark an Indicator Of Compromise (or more generally, an Attribute) as expired. The expiration system allows for the overlaying of computed scores on all attributes in real-time, based on the configured mappings via a decay model. The feature has been designed not to change the attributes per se, but rather to extend the meta information available about the attributes. As with everything in MISP, this new feature is accessible via both the user-interface and also via the API, in order to allow for the filtering of attributes based on a decay model.

<img src="/img/blog/decaying/dm-event.png" alt="Decay Model index" width="700"/>

The feature is exhaustive and we highly recommend to read the [blog post and watch the video showing all aspects of the new feature](/2019/09/12/Decaying-Of-Indicators.html) or [the slides from the MISP training](/misp-training/a.5-decaying-indicators.pdf). As usual, MISP comes with a set of default decay models which can be extended locally or contributed back to the community at large.

## ATT&CK sighting

More and more users and communities are using the ATT&CK framework to contextualise information shared within MISP. The fine team of [ATT&CK recently created a format to share the sightings](https://attack.mitre.org/resources/sightings/) associated with the techniques. MISP 2.4.116 now has a new output format available which allows users to export the sightings in the Mitre ATT&CK sightings format and share it back to the community or with MITRE directly. This allows the sharing of insights about the various techniques and their frequency of usage.

## New sync priority

When having a lot of MISP server to sync with, you might want to prioritise the sync for specific communities or MISP instance. In 2.4.116, we introduced the ability to order the priority of the sync between MISP instances.

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

