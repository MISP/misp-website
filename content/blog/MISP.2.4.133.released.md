---
title: MISP 2.4.133 released (major improvements such as the markdown report feature and many UI improvements)
date: 2020-10-16
layout: post
banner: /img/blog/event-reports/report-modal.png
---

# MISP 2.4.133 released with major improvements such as the markdown report feature and many UI improvements.

# Unstructured/semi-structured report feature

MISP is widely known as a powerful tool to gather, correlate and share information. As a response to the growing information-sharing maturity of the community, more features have been introduced over the past few years to meet analyst skills and requirements.

MISP has evolved to support a richer data structure allowing analysts and operators to describe and visualize complex scenarios. Data stored in MISP can be adjusted and linked in a comprehensive manner turning them into explorable graphs or timelines representing their activity or events.

However, in the current threat intelligence scene, information is often explained and shared in the form of article and using MISP’s raw text comments is far from ergonomic and appealing. Consequently, a crucial piece of data structure was missing and had to be supported: Reports.

In MISP 2.4.133, the report feature has been introduced including a complete Markdown editor to edit one or more report(s) attach to an event. The report feature including
a complete editor to allow an interactive method to add structured information from the MISP event including attributes, objects, galaxies or tags into the report.

![Editor hints](https://www.misp-project.org/img/blog/event-reports/cm-hints.gif)
![Editor hints tags](https://www.misp-project.org/img/blog/event-reports/cm-hints-tag.gif)

The report editor provides features such as:

- Markdown syntax shortcuts
- Auto-completion
- Synchronized scrolling between the text editor and the markdown viewer
- Automatic markdown rendering when typing
- Fullscreen and resizable interface
- Time since last edit & quick save

![Event editor full](https://www.misp-project.org/img/blog/event-reports/editor-full.png)

Event reports have all the standard properties regarding information sharing available MISP such as distribution level, sharing communities. A report can be shared to specific groups while structured information can be shared to a wider audience as an example.

*Event reports* also offer a wide range of new possibilities that were not doable efficiently before. For example, Counter analysis on cases can be explained, resolution steps and recommendations can be supplied, and complete articles can be included inside an *event*.

For more details, check out our blog post: [Event Report: A convenient mechanism to edit, visualize and share reports](https://www.misp-project.org/2020/10/08/Event-Reports.html).

# New features

## UI

- Add icons for threat levels.
- Show organisation nationality flag.
- Use flag icons from Twemoji.
- Go directly to object reference when referenced object is on the same page.
- Major improvements in the misp-modules view especially for the enrichment output.
- Many more improvements. Thanks to Jakub Onderka for his continuous attention to the details.

## Recovery of deleted events

- A new feature has been added to recover deleted events available in the diagnostics page. The feature uses the event history.

# New attribute types and changes

- `filename-pattern` filename-pattern to describe a filename based on a pattern (to avoid ambiguity from the filename attribute).
- `cpe` attribute to share and describe [CPE - Common Platform Enumeration](https://nvd.nist.gov/products/cpe) - and associated object like [cpe-asset](https://github.com/MISP/misp-objects/blob/main/objects/cpe-asset/definition.json)
- `telfhash` attribute type added and associate file object updated. For more details about [telfhash](https://github.com/trendmicro/telfhash).
- Normalize `AS` type to asplain notation.

# Speedup and optimisation

- Speedup sending module results.
- Sighting saving optimisation.
- [warninglist] Use faster method for fetching data from Redis.
- [complextype] Speedup hash parsing from CSVs and freetexts.

# Many bugs fixed and small improvements

A host of other improvements are documented in the [complete changelog is available](https://www.misp-project.org/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html)
.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

