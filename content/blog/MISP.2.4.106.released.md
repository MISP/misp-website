---
title: MISP 2.4.106 released (aka Too many improvements)
date: 2019-04-25
layout: post
banner: /img/blog/graph-thumb.png
---

A new version of MISP ([2.4.106](https://github.com/MISP/MISP/tree/v2.4.106)) has been released with a host of improvements, including new features such as a feed cache search, CLI tools to manage your MISP instance along with improved diagnostics.

# New features

- [API] Improved API to update warning-lists, object templates, the galaxy library, taxonomies and notice lists.
- Searching the feed caches is now possible via both the UI and the API. This allows users to rapidly find out whether a provided value exists in any of the cached sources (feeds [feeds](/feeds/) and MISP servers alike).
- [CLI] Worker management is now exposed via the CLI. The listing, starting, restarting and killing of workers can now be simply accomplished via the CLI.
- [CLI] reset/set a user's API key via the CLI. Overriding a password is now also possible without the need to force a password reset on login.
- [Auth] [LinOTP](https://www.linotp.org/) authentication module added in MISP.
- A [training deployment script](https://github.com/MISP/MISP/blob/2.4/app/Console/Command/TrainingShell.php) has been added to support the deployment of configurable networked MISP training topologies. The script has been created in order to support the NATO locked shields 2019 exercise, especially in regards to the deployment of a large number of connected player-team instances.

# Improvements

- Image resizing of attachments has been improved including a local thumbnail cache.
- [UI] Thumbnails are now included in the event graph visualisation.
- Exports in all formats are now enabled by default even for non-published events.
- Refanging of attributes are now done before saving attributes in the UI (refanging algorithms are the ones from the free-text import).
- [UI] Refactor of the tag picker to improve performance and re-introduce the custom tags.
- [UI] Performance improvements for events with large numbers of attributes and objects.
- [doc] Installation scripts and documentation were significantly improved. [MISP Install Documentation ](https://misp.github.io/MISP/)
- [UI/translation] Improvements to the various UI translations including the Russian translation.
- Improvement of various MySQL queries for outdated and buggy MySQL versions.
- Many new [MISP objects template](https://github.com/MISP/misp-objects/) were included. Don’t forget to run a git submodule update and update galaxies, objects and taxonomies via the UI.
- Many improvements in the accessibility of MISP user-interface especially for [Accessible Rich Internet Applications (ARIA)](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA).
- Many reported bugs were fixed.

# MISP modules

Many new [MISP modules](https://github.com/MISP/misp-modules) were added such as a QR code extractor, OCR hover module, Cuckoo sandbox submission and Cisco FireSight manager.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.



