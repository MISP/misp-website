---
title: MISP 2.4.185 released with sighting performance improvements, security and bugs fixes
date: 2024-02-20
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/fin7.png
---

We are happy to announce the immediate availability of MISP 2.4.185. This is mainly a bug fix release resolving several issues as well as tightening the security posture of the org image handling.

## Security fixes

We have moved the organisation images out of the webroot to avoid a rogue administrator from being able to upload a crafted, malicious organisation image and for unsuspecting users to be redirected to a malicious direct link of the image. Whilst this vulnerability is highly unlikely, requiring a compromised/rogue site administrator as a premise, the issue is valid and has been fixed. 

Thanks to Yusuke Nakajima and  Andrei Agape of Teliacompany for both delivering reports of this issue.

## Bugfixes

Various fixes affecting the API, proxy settings, sighting synchronisation. The synchronisation bug in particular could easily bring large, sighting rich instances (such as our own) to its knees when a remote instance tried to synchronise via a pull. 

We would hereby like to again thank for our active community for supplying fixes, bug reports, vulnerability reports and suggestions for the continuous improvement of MISP, the tool definitely wouldn't be what it is today without all your help!

Details changes are available in [Changelog](https://www.misp-project.org/Changelog.txt).

# Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Galaxy

![fin7](https://github.com/MISP/MISP/assets/3309/1fa4b1e0-3edb-44f8-9d71-c0cdee050768)

Major improvement were performed in the MISP galaxy including major updates in the [threat-actor knowledge-base](https://www.misp-galaxy.org/threat-actor/), the [surveillance vendors](https://www.misp-galaxy.org/surveillance-vendor/). Additional updates were done to add the relationships in the [MISP galaxy](https://www.misp-galaxy.org/) public website.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

