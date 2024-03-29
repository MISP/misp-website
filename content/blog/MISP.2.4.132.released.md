---
title: MISP 2.4.132 released (security fix CVE-2020-25766 and bugs fixed)
date: 2020-09-21
layout: post
banner: /img/blog/d4_sshd_widget.png
---

# MISP 2.4.132 released

A new version of MISP ([2.4.132](https://github.com/MISP/MISP/tree/v2.4.132)) has been released with several bugs fixed including an important [security](/security/) fix [CVE-2020-25766](https://cve.circl.lu/cve/CVE-2020-25766). 

# Bugs fixed and updates

- [bootstrap-datepicker] Updated to version 1.9.0
- [tag filters] fixed a bug introduced with the previous filter fix, resulting in multiple OR tags being ignored as a valid filter.
- [internal] Correctly handle positive tag filters for non site admins.
- [sightings] anonymise pushed sightings using new Sightings_anonymise_as setting.

# CVE-2020-25766

An issue was discovered in MISP before 2.4.132. This could lead to an unwanted actions (such as an event deletion) being triggered. Thanks to Michael Kerscher for the report.

It was discovered that under certain situations (resource exhaustion when retrieving sessions data for example), a user could incorrectly receive the login page as a response when paginating the event view's attribute list. This in itself should not cause any issues, but due to a bug in the login form's GET/POST exchange, the user actually having a valid session would instead retrieve the event index, on which the first form was submitted (which was an event deletion). In normal situations this is extremely rare and we have only identified a handful of such deletions on our most heavily used community instances.

Version 2.4.133 will include a new diagnostic tool that highlights deletions from the time period when the bug was active along with a recovery functionality.

# Many bugs fixed and small improvements

A host of other improvements are documented in the [complete changelog is available](/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


