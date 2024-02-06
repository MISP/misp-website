---
title: MISP 2.4.184 released with performance improvements, security and bugs fixes. 
date: 2024-02-06
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/lookyloo-misp.png
---

MISP 2.4.184 released with performance improvements, security and bugs fixes.

## Improvements

- Speed up improvements in ssdeep correlation and many other parts of MISP. Thanks to Jakub Onderka for the work on this.
- [objects] restsearch first/last seen filters added. 
- [event:publication] Added new setting to block event publication if the publishing user is the creator.
- [events:export] Make setting `MISP.disable_cached_exports` enabled by default. Since the /events/export has been marked deprecated for a years, we are starting the process to phase it out by first disabling the endpoint by default. The [MISP ReST search API](https://www.misp-project.org/openapi/) is the API to be used in the future if you still have very old scripts relying on export. We recommend to start making plans to rework those scripts.
- [organisation:orgMerge] Added missing models for organisation handover

## Security fixes

A series of security fixes were done in this release, the vulnerabilities are accessible to authenticated users, especially those with specific privileges like Org admin. We urge users to update to this version especially if you have different organisations having access to your instances.

- [security] Improved security checks for organisation logo upload. (low)
- [security] New auditlogs's fullChange lack of ACL controls. (medium)
- [security] Enforce usage of POST to start an export generation process. (low)

CVE assignments are pending and will be published on the [security page](https://www.misp-project.org/security).

## Bugs fixed

- [GalaxyClusters] fix tag_name restsearch filter (#9512).
- Various UI fixes.

Many bugs fixed and minor improvements. Feel free to read the detailed [changelog](https://www.misp-project.org/Changelog.txt)

## PyMISP

Many improvements in PyMISP including faster JSON parsing with orjson. Feel free to read the detailed [changelog](https://www.misp-project.org/Changelog-PyMISP.txt)

# MISP project knowledge bases

## MISP Objects

- [artifact] Changed the `payload_bin` attribute to attachment type.
- [flowintel-task] add case-uuid.
- [process] Environment variables attribute.

## MISP Galaxy

A [new dedicated website has been developed](https://www.misp-galaxy.org/) to easily reference galaxy outside MISP.

- Improved [Sigma rules galaxy](https://github.com/MISP/misp-galaxy/blob/main/clusters/sigma-rules.json), [threat-actors database](https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json) with many new [threat-actors](https://www.misp-galaxy.org/threat-actor/). A huge thanks to all the regular contributors.
- MITRE Data Sources and Data Components are now included in MITRE ATT&CK.
- Stealer galaxy updated.

## MISP warning-lists

[Warning-lists updated](https://github.com/MISP/misp-warninglists) to the latest version from the different sources.

# Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.


