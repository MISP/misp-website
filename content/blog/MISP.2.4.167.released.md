---
title: MISP 2.4.167 released with many improvements, bugs fixed and security fixes. 
date: 2022-12-26
layout: post
banner: /img/blog/time-occurence.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.167](https://github.com/MISP/MISP/releases/tag/v2.4.167) with new features and fixes, bugs fixed and a security fix.

# New features

## Timeline improvements for large events

Timeline is a convenient way to display the different attributes and objects over the time. Events with a large set of attributes or objects (more than 500) cannot display a human readable timeline. 
Nevertheless there are still a lot of valuable information in such event especially concerning the occurences over time. A new feature has been added in 2.4.167 to display the overall occurrences over the time and display the overall sighting trend. 

## Taxonomy highlight

For MISP users and organisations, it's important to show the important contextualised information and especially the [taxonomies](https://www.misp-project.org/taxonomies.html) which are important to your use-case. We introduced a new feature to highlight the important taxonomy in a MISP instance.

The site admin user can select the important taxonomies in the taxonomy list:

![](https://www.misp-project.org/img/blog/highlight.png)

and then the taxonomy namespace will appear in a visible box:

![](https://www.misp-project.org/img/blog/highlight2.png)
![](https://www.misp-project.org/img/blog/highlight3.png)

## Create objects from free-text import

The free-text import in MISP is very nifty for analysts willing to enter quickly new attributes. This functionality was initially used for attributes only. In 2.4.167, MISP objects can be created from the free-text import directly too.

![](https://www.misp-project.org/img/blog/free-text-create.png)

## API

- A new endpoint session kill-switch has been added for the support and integration with MeliCERTes project.

## UI

- Clarify the exclusivity issue in the UI when exclusive tags are used in the TLP namespace.
- [dashboard] sort dashboard widgets.

Many UI improvements and a special thank to Jakub Onderka for the attention to details in the UI.

# Security fix

A security XSS vulnerability has been fixed in this release and tracked under [CVE-2022-47928](https://cvepremium.circl.lu/cve/CVE-2022-47928). We recommend every users to update to the latest version.

A huge thanks to all the contributors and supporters of the MISP project. This release won't be possible by all the organisations and people supporting us to make MISP a reality.

For more [details](https://www.misp-project.org/Changelog.txt) about changes in the MISP core software.

# Other updates and changes

## MISP Objects

- New thaicert-group-cards, Palantir ADS and [persnona](https://itk.mitre.org/toolkit-tools/personas/).
- Invalid UUID object templates fixed including mactim-timeline-analysis and fail2ban. 

## MISP Galaxy

- New threat-actor such as TAG-53, Malteiro and others added.
- RAT group updated.
- [Ransomware groups](https://www.misp-project.org/galaxy.html#_ransomware) updated.

## MISP taxonomies

- A new [aviation](https://www.misp-project.org/taxonomies.html#_aviation) has been added. Thanks to [European Air Traffic Management Computer Emergency Response Team ](https://www.eurocontrol.int/service/european-air-traffic-management-computer-emergency-response-team).

# Don't forget to follow us on Mastodon

MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) and don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if you want an account.

