---
title: MISP 2.4.129 released (merge event improved, event block rule system, security fixes and many bugs fixed)
date: 2020-07-28
layout: post
banner: /img/blog/d4_sshd_widget.png
---

# MISP 2.4.129 released

A new version of MISP ([2.4.129](https://github.com/MISP/MISP/tree/v2.4.129)) has been released with an improved merge functionality, a new event block rule system, many security fixes and bugs fixed.

# Merge functionality improved

- handle objects, tags, etc via @chrisr3d's module result parsing
- handle sharing groups correctly
- using standardised fetchers internally
- API enabled (which will directly merge all contents of the source event into the target event)

# event block rule system added.

- add simple tag filters to block events from being added.
- it will not stop a manual creation of an event with subsequent adding of the tag in a later stage
- it will however block synced events

# Many bugs fixed and small improvements

Many other improvements are documented in the [complete changelog is available](/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


