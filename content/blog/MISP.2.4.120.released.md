---
title: MISP 2.4.120 released (aka the timeline release)
date: 2020-01-21
layout: post
banner: /img/blog/t-misp-overview.png
---

# MISP 2.4.120 released

A new version of MISP ([2.4.120](https://github.com/MISP/MISP/tree/v2.4.120)) has been released, including an extension to the data-model adding the first_seen and last_seen values at the attribute and object levels. The user-interface has been extended with a timeline view/editor per event, allowing users to see all occurrences of attributes and objects based on time. A new quick object edit tool has been added, enabling users to easily add new attributes to already existing objects. A long list of bugs were fixed and various improvements were made in the existing features.

# Update notes

Don't forget to have background workers running before updating, there are some updates to the database which can take time depending on the size of your MISP instance. The
progress of the update can be verified via the interface of your MISP instance using the following endpoint: /servers/updateProgress .

# Timeline feature and improved data-model

{{<video src="/img/blog/timeline-video.mp4" title="Overview of the MISP timeline feature" >}}

[MISP standard format](https://www.misp-standard.org/) has been extended to support first_seen and last_seen on any attribute or object in a MISP instance. This functionality is fully accessible via the restSearch API and via the user-interface of MISP. first_seen and last_seen can be set at the attribute and/or the object levels. A complete timeline viewer and editor has been added to allow users to:

- Quickly see the overall timeline of attributes and objects;
- Zoom in and out in the timeline (alt + mouse wheel);
- Edit and change the first_seen and last_seen by moving the attributes/objects directly on the timeline.

![The representation of spear phishing using the timeline function in MISP](/img/blog/t-misp-overview.png)

As an example above, a spear phishing attack and their respective occurrences are displayed on the timeline. This new feature allows users to describe complex time-based information whilst using existing features such as object relationships.

# New attribute types

- kusto-query attribute type added - Kusto query is the query language for the Kusto services in Microsoft Azure used to search large dataset. It's used in Windows Defender ATP Hunting-Queries as well as Azure Sentinel (Cloud-native SIEM)
- chrome-extension-id attribute type added - This attribute is used by Chrome to uniquely identify extensions. This helps the sharing of information about malicious extensions within a MISP sharing community.

# misp-modules version 2.4.120

MISP modules have been improved and many new modules were added in the following related scopes: [expansion](http://misp.github.io/misp-modules/expansion/), [export](http://misp.github.io/misp-modules/export_mod/) and [import](http://misp.github.io/misp-modules/import_mod/). Don't forget to update the modules to benefit from the improvements and new features.

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

