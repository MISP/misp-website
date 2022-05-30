---
title: MISP 2.4.159 released with many improvements including performance 
date: 2022-05-30
layout: post
banner: /img/blog/graph-syria.png 
---

We are pleased to announce the immediate availability of MISP v2.4.159.  This releases includes many improvements, bugs fixing and improvement concerning performance on large dataset.

# Performance Improvements

- [DB] Add MysqlExtended DboSource to support index query hints.
- [Query] Add new setting to disable taxonomy checks when browsing data.
- We discovered that some MISP users are still using slow file-based session handling in PHP. Now, we added in the diagnostic, if session is file based. We recommend everyone to use the Redis session.
- Many additional speed-up and faster functions in the MISP internals.
- Reduce memory usage when generating all correlations.

# Improvements

- [Feed] Allow option to disable correlations for all events coming from a feed. This can be useful when correlation requires to be disabled for an imported feed.
- [UI] Allow to upload MISP event by pasting data to textarea in addition to the file upload.
- An optional feature `clusters:attachMultipleClusters` is now available to allow the mirroring of attribute clusters to event.
- [auditlog] Support for fetch event changes from specific time.
- [UI] Allow to filter attributes from Related Events box.
- [UI] Allow to filter attributes from warninglist box. 
- [UI] Many UI improvements to make the interface easier to read.
- [UI] Disable correlation checkbox for non correlating types.
- [STIX 2 import] Better Galaxies parsing by looking for the ATT&CK technique id.
- [API] Enable sharing group filter for Event controller not just attribute.

# Fixes

- [STIX] Avoiding non RFC-4122 UUIDs to be imported (and therefore skipped)
- [STIX 1 import] Save process network connections.
- [STIX 1 import] Fixed galaxy tag_names fetching from TTP names.

# Knowledge Bases

## MISP Taxonomies

- [dga] First version of the DGA taxonomy based on https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_plohmann.pdf.
- GrayZone of Active Defense, originaly published by Washington University, v2 created and updated by DCG420
- Various fixes to existing taxonomies.

## MISP Objects Template

- A new PaloAlto Threat Event object template has been added.
- A updated security playbook has been added.
- A new ransom negotiation object has been added.
- An improved Passive SSH template object.
- Various fixes and improvements to different object templates such as email, virustotal-submissions and others.

## MISP Galaxy

- Improved Cryptominers galaxy.
- Improved backdoors galaxy.
- Threat Actor galaxy updated and extended with new threat-actors.
- MISP Galaxy updated for MITRE ATT&CK v11.2.

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core. Additional changelogs are available for [misp galaxy](https://www.misp-project.org/Changelog-misp-galaxy.txt), [misp-taxonomies](https://www.misp-project.org/Changelog-misp-taxonomies.txt), [misp-objects](https://www.misp-project.org/Changelog-misp-objects.txt) and [misp-modules](https://www.misp-project.org/Changelog-misp-modules.txt)

