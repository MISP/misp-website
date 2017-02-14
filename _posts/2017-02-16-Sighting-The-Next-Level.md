---
title: Sighting the next level
layout: post
featured: /assets/images/misp-small.png
---

Sighting is an [endless topic of discussion](https://lists.oasis-open.org/archives/cti-stix/201508/msg00019.html). This is a required feature especially when information or indicators are regularly shared to gather feedback from users of the shared information. Adequate sightings can be an incredible source of information in order to describe the life-time of an indicators, its evolution and especially to ensure the understanding among a group of users using the information to detect, mitigate or block in their infrastructures malicious activities. The potential is huge and can be a significant gain for organised communities of infosec professionals sharing information or even a requirement for any advanced algorithms ranging from machine learning or reinforcement learning. But to reach such state of feedback loop, you require a functional model of sighting.   

In early April 2016, MISP introduced the support of [sighting via the API](https://circl.lu/doc/misp/automation/index.html#sightings-api) or the UI. This first step was basically to support the existing description of sighting as described in the STIX standard and allow the support via STIX sighting documents or simplified sighting via MISP JSON attributes. This move in MISP allowed us to test sighting at large-scale in existing sharing communities like [the ones operated by CIRCL](https://www.circl.lu/services/misp-malware-information-sharing-platform/). The implementation allowed to have sightings at different levels (events or attributes) with a support of sighting per organisation or per MISP instance level. We had engaging discussions about the current limitation of simple counters:

- Positive and negative sightings cannot be interpreted as it's just a positive counter in the existing standards. Many users asked for a direct feedback regarding their false-positive interpretation of a sighting.
- An absence of time-to-live reference time that could support advanced expiration model of an indicator.
- Sharing of sightings alone is also required to support new model of pseudo-anonymous sharing.

To tackle this, we decided **to remodel and extend the sighting in this new release of MISP**. Now the sighting contains a type (which can be easily extended) to support alternative issue of simple counters. The following types were added:

- Sighting type 0, a default sighting type using the default STIX interpretation of sighting.
- Sighting type 1, a **false-positive sighting** which means this sighting has been interpreted as a false-positive by the organisation.
- Sighting type 2, an **expiration sighting** which defines when the sighted attributes is expired.

In addition to the flexible type format, we added a simple source field which combined with the organisation provides simple way to scope the sighting (e.g. honeypot networks versus backbone routers where the false-positive interpreation can be significantly different).
