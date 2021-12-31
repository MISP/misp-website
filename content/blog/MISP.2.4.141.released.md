---
title: MISP 2.4.141 released (Many improvements from email notification, UI, API and installation scripts)
date: 2021-03-29
layout: post
banner: /img/blog/ss7-example.png
---

# MISP 2.4.141 released

MISP 2.4.141 released including many improvements from email notification, UI, API and installation scripts.

# User-Interface

- [UI] Render galaxy cluster description as markdown.
- [UI] Show threat level icons on event index.
- [eventgraph:viewPicture] Allow access to saved picture from the eventgraph history.
- [eventGraph] Improved object coloring strategy.
- [UI] fix debugon for debug = 1. fix #7131.
- [UI] Show number of items in freetext feed.
- [UI] Make feed event preview nicer.
- [UI] It is 2021! Removed -moz and -webkit specific CSS properties.
- [UI] Make some parts of MISP nicer.
- [UI] Nicer pivots.
- [UI] Simplify keyboard-shortcuts.js.
- [UI] Use Page Visibility API.

and many more updates check the [changelog for details](https://www.misp-project.org/Changelog.txt).

# Email notification

Email notification has been significantly improved and now support HTML emails.

- [email] New setting `MISP.event_alert_metadata_only`.
- [email] Command for testing generated alert email.
- [email] Allow to set email subject from template.
- [email] Back-end support for sending HTML emails.

This release includes many updates in the local and translation of the user-interface.

New default feeds were included in MISP such as the newest [DataPlane.org feeds](dataplane.org).

# Installation scripts and guides

Many improvement in the RHEL7, 7.9 and CentOS8Stream. We thank all the users reporting issues with RHEL.

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html)
.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

