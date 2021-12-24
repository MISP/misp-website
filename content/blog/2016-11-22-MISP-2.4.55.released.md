---
title: MISP 2.4.55 released
date: 2016-11-22
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.55](https://github.com/MISP/MISP/tree/v2.4.55) has just been released, including bug fixes and improvements.

This release is a transient release before the galaxy release (TTP-like support) coming up soon.

The release includes various improvements such as:

- Sightings are now a default enabled feature. Multiple UI improvements added to the sighting system.
- The NIDS API export has been improved allowing the passing of filter parameters via JSON/XML payloads. The attribute type can now be also filtered on.
- Bug fixes in the add user API.
- Various bug fixes in the NIDS export including the addition of the missing domain|ip attribute type.
- Multiple bug fixes.

We thank all contributors.

The full change log is available [here](http://www.misp-project.org/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
