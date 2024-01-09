---
title: MISP 2.4.183 released with new ECS log feature, improvements and bugs fixed 
date: 2024-01-09
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog//lookyloo-misp.png
---

MISP 2.4.183 released with a new ECS log feature, improvements and bugs fixed.

- MISP now supports Elastic Common Schema (ECS) security logging. A new option has been added `Security.ecs_log` to enable this new functionality. A new `Security.alert_on_suspicious_logins` to security audit has been added. 
- The sync configuration in MISP now supports sharing group blueprints for a simple creation of filter rules based on dynamically updated organisation lists. 
- Major improvement to STIX import handling and especially the [misp-stix library](https://github.com/MISP/misp-stix) such as Parsing PE binary extensions within File observable objects and many more improvements/fixes.
- API add tag functions updated to also work with uuids, rather than just local IDs.
- [event:view] Added option to mass local cluster tag.

Many bugs fixed and minor improvements. Feel free to read the detailed [changelog](https://www.misp-project.org/Changelog.txt)

# MISP project knowledge bases

## MISP Objects

- New [flowintel CM](https://github.com/flowintel/flowintel-cm) object added.

## MISP Galaxy

A [new dedicated website has been developed](https://www.misp-galaxy.org/) to easily reference galaxy outside MISP.

- Improved [Sigma rules galaxy](https://github.com/MISP/misp-galaxy/blob/main/clusters/sigma-rules.json), [threat-actors database](https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json) with many new threat-actors 
- New [disarm](https://www.disarm.foundation/) galaxy is now available. Including [Actor Types](https://www.misp-galaxy.org/disarm-actortypes/), [Countermeasures](https://www.misp-galaxy.org/disarm-countermeasures/), [Detections](https://www.misp-galaxy.org/disarm-detections/) and [Techniques](https://www.misp-galaxy.org/disarm-techniques/). 
- New MITRE Atlas framework added. [MITRE ATLAS Attack Pattern](https://www.misp-galaxy.org/mitre-atlas-attack-pattern/), [MITRE ATLAS Course of Action](https://www.misp-galaxy.org/mitre-atlas-course-of-action/)

## MISP warning-lists

[Warning-lists updated](https://github.com/MISP/misp-warninglists) to the latest version from the different sources.

# Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.


