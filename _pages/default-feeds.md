---
layout: page
title: MISP Default Feeds
permalink: /feeds/
toc: true
---

MISP includes a set of public OSINT feeds in its default configuration. The feeds can
be used as a source of correlation for all your events and attributes without the need to
import the feed into your system. The MISP feed system allows a fast correlation but also
a quick comparison of the feeds among the others.

The feeds can be in three different formats:

- [MISP standardized format](https://github.com/MISP/misp-rfc/blob/master/misp-core-format/raw.md.txt) which is the preferred format to benefit from all the MISP functionalities.
- CSV format where you can select the values you want to be imported.
- freetext format which allows to use the automatic indicators/attributes detection from unstructured texts.

and located in different input transports:

- Network (URL)
- Local (file)

## Default feeds available in MISP

The default feeds are described in a [simple JSON format](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json). The default feeds, the current version of MISP, are the following:

{% include feeds.md %}

To enable a feed in the caching, you just need to check the enabled field and the lookup visible to benefit automatically of the feeds in your local MISP instance.

## Feed overlap analysis matrix

![feed overlap analysis matrix](/assets/images/misp/blog/feed-overlap-analys-matrix.png){:class="img-responsive"}

## How to have my feed published in the default MISP OSINT feed

- Fork the [MISP project](https://github.com/MISP/MISP) on GitHub.
- Update the [default MISP feed](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json) to add your feed(s).
- Make a pull-request with the updated JSON file.

