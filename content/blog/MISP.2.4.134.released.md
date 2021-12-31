---
title: MISP 2.4.134 released (new import extractor for the event report, various improvements and fixes)
date: 2020-11-10
layout: post
banner: /img/blog/event-reports/report-modal.png
---

# MISP 2.4.134 released

In the previous version of MISP, the new [Event Report functionality](https://www.misp-project.org/2020/10/08/Event-Reports.html) has been introduced to edit, visualise and share reports in Markdown format, which includes the ability to reference elements from within a MISP event.

In the current version, the Event Report has been extended to support the automatic discovery of attributes, galaxies and tags from any website captured.

{{<video src="https://www.misp-project.org/img/blog/event-report-demo-extraction-from-url2.mp4" title="Overview video of the new MISP event report functionality and discover of elements" >}}


This functionality allows the analysts to collect external reports and automatically discover information which can be used in MISP.
The Event Report fetching capabilities require the [misp-modules](https://github.com/MISP/misp-modules) to be activated.

# Optional A/V scanning in MISP

A new feature has been added to automatically scan attachments in MISP. The functionality is completely optional and can be enabled in the global configuration.

# ATT&CK sub-techniques

MISP now includes the ATT&CK sub-techniques as a MISP galaxy.

# Example script for direct STIX ingestion into MISP

A new [Ingest STIX](https://github.com/MISP/MISP/tree/2.4/tools/ingest_stix) script is available to show how to easily ingest STIX 1 and 2 files in MISP while using the parsing functionality of MISP core.


# Security fix - CVE-2020-28043

A security vulnerability [CVE-2020-28043](https://cve.circl.lu/cve/CVE-2020-28043) has been fixed. MISP through 2.4.133 allows SSRF in the REST client via the use_full_path parameter with an arbitrary URL.

- by using the full path parameter in the rest client, users could issue queries to any server
- this becomes especially problematic when the MISP server is able to query other internal servers,
  as external users could trigger those
- new server setting added that allows enabling the full path option, this is now disabled by default
- new server setting added to add an override baseurl for the rest client, removing the need for the full
  path option in the first place (for example for the training VM with its port forwarding)
- Thanks to Heitor Gouvêa for reporting this vulnerability

# Many bugs fixed and small improvements

- Tag index has been improved with a simple view excludes eventtags / attributetags / sightings
- Many UI improvements (thanks to Jakub Onderka for his continuous effort and attention to details)

A host of other improvements are documented in the [complete changelog is available](https://www.misp-project.org/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html)
.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

