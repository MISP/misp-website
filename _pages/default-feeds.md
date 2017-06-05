---
layout: page
title: MISP Default Feeds
permalink: /feeds/
toc: true
---

MISP includes a set of public OSINT feeds in its default configuration. The feeds can
be used as a source of correlations for all of your events and attributes without the need to
import them directly into your system. The MISP feed system allows for fast correlation but also
a for quick comparisons of the feeds against one another.

The feeds can be in three different formats:

- [MISP standardized format](https://github.com/MISP/misp-rfc/blob/master/misp-core-format/raw.md.txt) which is the preferred format to benefit from all the MISP functionalities.
- CSV format, allowing you to pick the columns that are to be imported.
- freetext format which allows automatic ingestion and detection of indicator/attribute by parsing any unstructured text.

and located in different input transports:

- Network (URL)
- Local (file)

## Default feeds available in MISP

The default feeds are described in a [simple JSON format](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json). The default feeds and the current version of MISP are the following:

{% include feeds.md %}

To enable a feed for caching, you just need to check the enabled field to benefit automatically of the feeds in your local MISP instance. To allow other users of your MISP instance to benefit from this functionality, simply check the "lookup visible" checkbox.

## Feed overlap analysis matrix

![feed overlap analysis matrix](/assets/images/misp/blog/feed-overlap-analys-matrix.png){:class="img-responsive"}

## How to have my feed published in the default MISP OSINT feed

- Fork the [MISP project](https://github.com/MISP/MISP) on GitHub.
- Update the [default MISP feed](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json) to add your feed(s).
- Make a pull-request with the updated JSON file.

