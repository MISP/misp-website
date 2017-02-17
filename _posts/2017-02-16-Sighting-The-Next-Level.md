---
title: Sighting the next level
layout: post
featured: /assets/images/misp-small.png
---

Sighting is an [endless topic of discussion](https://lists.oasis-open.org/archives/cti-stix/201508/msg00019.html). This is a required feature especially when information or indicators are regularly shared to gather feedback from users said shared data. Adequate sightings can be an incredible source of information in order to describe the life-time of an indicator, its evolution and especially to ensure the understanding of indicators among a group of users using the information to detect, mitigate or block malicious activities in their infrastructures. The potential is endless, potentially being a significant gain for organised communities of infosec professionals sharing information or even serve as a requirement for advanced algorithms ranging from machine learning to reinforcement learning. But to reach such a state of a feedback loop, you first require a functional model of sighting.   

In early April 2016, MISP introduced the support of [sighting via the API](https://circl.lu/doc/misp/automation/index.html#sightings-api) or the UI. This first step was basically to support the existing description of sighting as described in the STIX standard and allow the support via STIX sighting documents or simplified sightings via MISP JSON attributes. This move in MISP allowed us to test sightings at a large-scale in existing sharing communities such as [the ones operated by CIRCL](https://www.circl.lu/services/misp-malware-information-sharing-platform/). The implementation allowed us to have sightings at different levels (at the attribute level as well as a sighting sum at the event level) whilst also supporting the sightings per organisation or per the MISP instance level. We had engaging discussions about the current limitations of simple counters:

- Positive and negative sightings cannot be interpreted as it's just a positive counter in the existing standards. Many users asked for a direct feedback regarding their false-positive interpretation of a sighting.
- An absence of time-to-live reference that could support advanced expiration models of an indicator.
- Sharing of sightings is also required to support a new model of pseudo-anonymous sharing.

To tackle this, we decided **to remodel and extend the sighting in this new release of MISP**. Now the sighting contains a type (which can be easily extended) to support alternative sets of simple counters. The following types were added:

- Sighting type 0, the default sighting type using the default STIX interpretation of a sighting.
- Sighting type 1, a **false-positive sighting** which means this sighting has been interpreted as a false-positive by the organisation.
- Sighting type 2, an **expiration sighting** which defines when the sighted attributes is to be expired.

In addition to the flexible type format, we added a simple source field which combined with the organisation provides a simple way to scope the sighting (e.g. honeypot networks versus backbone routers where the false-positive interpreation can be significantly different).

# MISP 2.4.66 and Improved Sighting

MISP 2.4.66 has been released including the improved sightings feature. As you can see below:

<div class="myvideo">
   <video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop">
        <source src="{{ site.baseurl }}/assets/images/misp/video/sighting.webm"  type="video/webm"  />
   </video>
</div>

In previous version of MISP, sightings used the basic counter model as described above. In addition to the classical model, MISP 2.4.66 now allows to do negative sighting to track the numbers of false-positives generated.  All the sightings are also tracked per organisation with an additional source. The source allows an organisation to track which equipments or infrastructure generated the sighting.

This new feature allows many new use-cases such as feeding MISP from a ticketing system (for example indicating that an indicator is a false-positive), attributes which have to be expired in 4 days or adding sightings from honeypots or network sensors.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
