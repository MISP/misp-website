---
title: MISP 2.4.60 released
date: 2017-01-17
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.60](https://github.com/MISP/MISP/tree/v2.4.60) has been released, including bug fixes and the long awaited attribute-level tagging feature.

![MISP attribute level tagging](/img/blog/attribute-level.png "{class='img-responsive'}")

All tags (local or from taxonomies) can now be also applied at the attribute level. This allows analysts or users to easily classify attributes
within an event. Many of the taxonomies have useful properties that can be applied to provide additional contextual information to attributes.
The attribute level tagging feature introduces many new potential use-cases where MISP can be used to better the day-to-day tasks of incident handlers, analysts
or security engineers.

The release includes further improvements such as:

- Request encryption of samples via the event ReST api is now supported.
- Allow disabling/enabling publishing of events imported via the UI.
- [taxonomies and galaxy] updated to the latest version.
- Clarification of session.timeout description.
- Some UI improvements especially in the tag selection.
- Disable correlation via the API is now supported.

A big thanks to all the users who gave feedback and contributors who helped us improve MISP with special thanks to Andreas Ziegler for the attribute-level contribution.

The full change log is available [here](https://www.misp.software/Changelog.txt).

A [MISP training is organized the 7th February 2017 in Luxembourg](https://www.eventbrite.com/e/misp-training-tickets-30484201066) followed by a [hackathon the 8th February 2017](https://www.eventbrite.com/e/misp-hackathon-3-tickets-30488596212).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
