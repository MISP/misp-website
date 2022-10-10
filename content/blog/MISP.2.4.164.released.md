---
title: MISP 2.4.164 released with new tag relationship feature, improvements and a security fix 
date: 2022-10-10
layout: post
banner: /img/blog/periodic-summary/periodic-summary-2.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.164](https://github.com/MISP/MISP/releases/tag/v2.4.164) with a new tag relationship features, many improvements and a security fix.

# New tag relationship feature

Relationship can now be added to any attribute tag or event tag. This works with tags and galaxy clusters. The new feature is available in event view. 

The tag relationship feature is also exposed in the API under the endpoint `/tags/modifyTagRelationship/[scope]/[id]` where `scope` is the attribute/event and `id` is the id of the EventTag / AttributeTag object.

# Improvements and bug fixes

- [periodic_report] Added security recommendations section showing course of actions related to attack techniques.
- [workflow] add support for `local` and `relationship` in workflow.
- [API/galaxyCluster/restSearch] Allow multiple filtering conditions to be used at once. 
- [EventGraph] Added entity comment in the graph as tooltip and support of comment in searches.
- [UI] Many improvements and optimisation.

# CVE-2022-42724 

This release fix a security vulnerabilities ([CVE-2022-42724](https://cvepremium.circl.lu/cve/CVE-2022-42724)) which allows org admin to discover role names which should have been restricted to site admin.

We strongly recommend MISP administrator to update to this latest version.

For a more detailed changelog, please see the online [Changelog](https://www.misp-project.org/Changelog.txt).

