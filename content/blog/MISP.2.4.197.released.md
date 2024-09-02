---
title: MISP 2.4.197 released with many bugs fixed, a security fix and improvements. 
date: 2024-09-02
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/object-collapse.png
---

# Release Notes - v2.4.197 (2024-09-02)

## New Features

- **Config Option:** Added a new configuration option `user_org_uuid_in_response_header` to include a response header with the requesting user's organization UUID. [Jeroen Pinoy]
- **Build:** Display required STIX dependencies versions during the build process. [Jakub Onderka]
- **Bookmark** now supports comment. 

## Changes

- **Version:** Version bump. [iglocska]
- **Warning List:** Updated the warning list. [Alexandre Dulaunoy]
- **Taxonomies:** Updated to the latest version. [Alexandre Dulaunoy]
- **MISP Galaxy:** Updated to the latest version. [Alexandre Dulaunoy]
- **PyMISP:** Version bump. [Raphaël Vinot]
- **Internal Logging:** Added logging when an event will not be published. [Jakub Onderka]
- **Global Menu - Bookmarks:** Added comment field as the dropdown element's title in the global menu bookmark. [Sami Mokaddem]
- **Database Upgrade - Bookmarks:** Upgraded the database to support bookmark comments. [Sami Mokaddem]
- **Bookmark View:** Added a missing comma for the new comment function and added a field for comments in the bookmark view. [Jan Z.]
- **Bookmark Index:** Added a field to display comments in the bookmarks index. [Jan Z.]
- **Bookmark Add/Edit:** Added a field to add and edit comments for bookmarks. [Jan Z.]
- **MISP Object:** Updated to the latest version. [Alexandre Dulaunoy]

## Fixes

- **UI/Footer:** Improved UI footer to avoid confusion for some users. [Alexandre Dulaunoy]
- **IOC Import:** Added a check to ensure the provided XML is valid. [Jakub Onderka]
- **Schema:** Updated schema version. [Jakub Onderka]
- **UI:** Fixed tag popover to return already parsed data. [Jakub Onderka]
- **Bookmarks - Add:** Lower-cased the comment field. [Sami Mokaddem]
- **Sightings:** Correctly retrieve sightings per the requested event. [Tom King]
- **Bookmarks - Verbose Returns:** Fixed an issue with overly verbose returns from bookmarks when shared with the organization. This fix was reported by Sharad Kumar Dahal of Green Tick Nepal Pvt. Ltd. [iglocska] This fixes a security issue recorded as [CVE-2024-45509](https://vulnerability.circl.lu/vuln/cve-2024-45509). 
- **Feed:** When pulling feeds, events are now checked against specified rules if any rules are provided. [Benni0]

## Other

- Merged pull requests addressing issues with unpublished events logging, tag popover parsing, sightings restSearch performance, and STIX dependencies version display. [Jakub Onderka, Andras Iklody, Andrew Hicks]
- Fixed issues related to sightings restSearch negation of organization ID. [Andrew Hicks]

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt). Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!

