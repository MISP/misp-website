---
title: MISP 2.4.57 released
date: 2016-12-19
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.57](https://github.com/MISP/MISP/tree/v2.4.57) has been released, including bug fixes and improvements.

Two major new features were introduced in 2.4.57. One of them is the addition of new attribute types and categories
to support the new use-cases in MISP, including the ```Person```, ```Social network``` and ```Support tool``` categories. The
new attribute types include additional email header types along with attributes describing a natural person and even an attribute type for describing mobile application identifiers.
For a complete overview of the new types, you can have a look at the [wiki page "New Attributes"](https://github.com/MISP/MISP/wiki/NewAttributes).

The second feature is the ability to enforce the [warning-lists](https://github.com/MISP/misp-warninglists) via the API. 
The warning lists are integrated in MISP to display an info/warning box at the event and attribute level if any of the attributes have a hit in one of the lists.
With the new feature in 2.4.57, you can now enforce the list at the API level too and remove all attributes having a hit in a warning list. A flag called ```enforceWarninglist``` is available to enforce it.

The release includes various improvements such as:

- Add a way to disable certain tags from the UI and especially a setting to set new tags as hidden.
- [Galaxy] bug fixes and improvement to the UI based on users feedback.
- Latest taxonomies updated.
- Some minor bug fixes and updates.

A big thank to all the users who gave feedback to help us improve MISP.

The full change log is available [here](http://www.misp-project.org/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
