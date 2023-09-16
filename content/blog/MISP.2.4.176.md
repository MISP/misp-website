---
title: MISP 2.4.176 released with various improvements and bugs fixed. 
date: 2023-09-15
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/lookyloo-misp.png
---

MISP 2.4.176 released with various improvements and bugs fixed. This version also includes major improvements in the [misp-stix](https://github.com/MISP/misp-stix/releases/tag/v2.4.176) library especially on the storing relationships and the description of relationships in the MISP standard format.

# Improvements

- [logs] add time based filter. Quite useful when you have a large set of logs.
- [audit] add last password change timestamp for users. 
- [UI] show which attributes/objects are new and awaiting publication
  still.
-  [console:TrainingShell] Added deleteAllSyncs function. 
- [feeds] add Ellio threat list.

# Bugs fixed

- [internal] improved parameter parsing.
- Properly filter out query parameters.
- Method call on null.
- Fixed invalid ordering errors.
- Do not require jobId for AdminShell jobGenerateCorrelation, create a new job if jobId is null. fixes #9206.
- [dashboard:organisationMapWidget] Do not require the config to have start and end date. 
- [restSearch] exact match for values starting with %, fixes #9258.
- Unable to enrich individual shadow attribute.
- Unable to enrich individual attribute, fixes #9267. 
- [stix2 import] Fixed debugging message for errors and warnings when the `debug` option is set. 
- Unable to enrich individual shadow attribute.
- Unable to enrich individual attribute, fixes #9267. 
- Disable submodule update section when MISP.self_update is disabled, to allow not carrying git dependencies in docker.

# misp-objects updates

- Various fixes to MISP objects such as [email](https://www.misp-project.org/objects.html#_email), [virustotal-report](https://www.misp-project.org/objects.html#_virustotal_report) and [relationships](https://www.misp-project.org/objects.html#_relationships). 

# misp-galaxy updates

- Update of target sectors in threat-actor database. This now includes the known target sectors as meta. 
- Various updates to the threat-actor database.

# misp-warning-lists updates

- [Cisco umbrella block pages](https://github.com/MISP/misp-warninglists/blob/main/lists/umbrella-blockpage-hostname/list.json) added to the MISP warning-lists.
- [Censys scanning IP address space](https://github.com/MISP/misp-warninglists/blob/main/lists/censys-scanning/list.json) added. 
- Various improvements to the generation tools.

# misp-modules

- Fix the url of the VirusTotal collection in the VirusTotal expansion module.

# PyMISP

- Various bugs fixed where fixed in PyMISP.  For more details, [PyMISP changelog](https://www.misp-project.org/Changelog-PyMISP.txt).

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# Training video

The latest video of MISP Training - Advanced, Developer session, from API to MISP internals is now available [on YouTube](https://www.youtube.com/watch?v=2tmjLsPrQkI).

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
