---
layout: page
title: MISP Default Feeds
permalink: /feeds/
toc: true
---

{{< feed-intro >}}

<!-- BEGIN GENERATED MISP FEEDS -->
{{< feed-catalog >}}
<!-- END GENERATED MISP FEEDS -->

## Using feeds in your MISP instance

- **Cache for correlation:** turn on **Caching enabled** for your selected feeds, then run a cache action from the Feeds screen. Caching prepares indicator lookups without creating local events.
- **Share lookups:** enable **Lookup visible** so other users on your instance can see feed correlations.
- **Import when needed:** enable the feed and use a fetch action to store its data locally.

See the [feed management guide](https://www.circl.lu/doc/misp/managing-feeds/) for configuration steps and the site administrator permissions required to manage feeds.

## Feed overlap analysis matrix

![feed overlap analysis matrix](/img/blog/feed-overlap-analys-matrix.png)

## How to have my feed published in the default MISP OSINT feed

- Fork the [MISP project](https://github.com/MISP/MISP) on GitHub.
- Update the [default MISP feed](https://github.com/MISP/MISP/blob/2.5/app/files/feed-metadata/defaults.json) to add your feed(s).
- Make a pull-request with the updated JSON file.
