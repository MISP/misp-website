---
title: MISP 2.4.178 released with many workflow improvements, enhancement and bugs fixed. 
date: 2023-10-30
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/lookyloo-misp.png
---

MISP 2.4.178 released with many workflow improvements, enhancement and bugs fixed.

# Improvements

- [workflow] Added option to provide a custom JSON in the hashpath picker helper.
- [workflow] New action modules (blocklist, warninglist, counter...) to add event in the blocklist.
- [workflow] New trigger event before save.
- [workflow] Various improvements in the quick hashpath filter.
- [workflow] Improved webhook to support HTTP request method, headers, payload. It also now supports self-signed certificates.
- [workflow] Many improvements in debugging and workflow logging.
- [RestClient/OpenAPI] `totp_delete` added in query builder and API documentation.
- [STIX upload] Improved in the galaxies handling including more detailed option while importing STIX 2 and creating galaxies/clusters.

# Changes

- [dashboard-widget:worldmap] Added support of custom scale in widget config.
- [API even:restSearch] Added support of `orgc_id` as valid filter.
- [Auditing] API access time is now stored once per hour by default.
- [API] `includeGranularCorrelations` is now exposed in the event RestSearch.

# Fixes

- [API] Add sharinggroup as an allowed parameter in attribute search.
- [objects:edit] Restored behavior of upgrading object to newer template.
- Many other fixes check the [ChangeLog for detailed changes](https://www.misp-project.org/Changelog.txt).

# Other improvements

## MISP Objects 

- New objects added such as `cryptocurrency-transaction` and many updates to other objects. For detailed changes, [MISP objects changelog](https://www.misp-project.org/Changelog-misp-objects.txt).

## MISP Galaxy

- Many new objects such as `ammunition`, `firearms` and many updates in threat actor, Sigma and many other. For detailed changes, [MISP galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt)

## MISP warning-lists

- Warning-lists updated to the latest version. New warning list with known hostname for lookup source IP of the DNS resolver. [MISP warning-lists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt).

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# Training video

The latest video of MISP Training - Advanced, Developer session, from API to MISP internals is now available [on YouTube](https://www.youtube.com/watch?v=2tmjLsPrQkI).

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
