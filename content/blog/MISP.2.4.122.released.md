---
title: MISP 2.4.122 released (aka the bug fix release)
date: 2020-02-18
layout: post
banner: /img/blog/t-misp-overview.png
---

# MISP 2.4.122 released

A new version of MISP ([2.4.122](https://github.com/MISP/MISP/tree/v2.4.122)) has been released. This version includes various fixes, minor new features and improvements.

# Log user IP addresses on login

A new logging optional feature has been added to log user IPs on login.

The feature logs on successful login logs the associated user ID for a given IP (with a 30 day retention). It also logs the IP for the associated user ID (indefinite retention).

Two new command lines were added:

    - Get IPs For User ID: `MISP/app/Console/cake Admin UserIP [user_id]`
    - Get User ID For User IP: `MISP/app/Console/cake Admin IPUser [ip]`

# New Danish community added

We have a flexible system to announce information sharing communities directly in MISP - in 2.4.122, we have added a Danish MISP user-group community. If you would like to have your community added and announced to all MISP users, don't hesitate to edit the [community JSON file](https://github.com/MISP/MISP/blob/2.4/app/files/community-metadata/defaults.json) and perform a pull-request.

# Correlation bug fixed

A bug fix solves an issue where attribute edits could purge correlations. The bug was introduced by a merge gone wrong. The attribute edits that modify fields that do not affect the correlations (such as to_ids, comment, etc) would cause correlations to be purged

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.


