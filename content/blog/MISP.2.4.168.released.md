---
title: MISP 2.4.168 released with bugs fixed, security fixes and major improvements in STIX support. 
date: 2023-02-16
layout: post
banner: /img/blog/graph-syria.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.168](https://github.com/MISP/MISP/releases/tag/v2.4.168) with bugs fixed and various security fixes.

It includes a rather substantial [release](https://www.misp-project.org/Changelog-misp-stix.txt) of [misp-stix](https://github.com/MISP/misp-stix), the core Python library for importing and exporting STIX (1, 2.0 and 2.1).

# Fixes

- Improvements to the indexTable
- allow site admins ability to view event_creator_email for all events in export
- [shadowAttribute:accept] Restored accepting functionality for the proposals
- [feed:edit] Make sure to keep orgc_id to its saved value
- [tags:relationship] Fixed synchronisation of relationship_type

# Security fixes

- [CVE-2023-24070](https://cvepremium.circl.lu/cve/CVE-2023-24070) < MISP 2.4.168 - app/View/AuthKeys/authkey_display.ctp in MISP through 2.4.167 has an XSS in authkey add via a Referer field.
- [CVE-2023-24026](https://cvepremium.circl.lu/cve/CVE-2023-24026) < MISP 2.4.168 - In app/webroot/js/event-graph.js has an XSS vulnerability via an event-graph preview payload.
- [CVE-2023-24027](https://cvepremium.circl.lu/cve/CVE-2023-24027) < MISP 2.4.168 - In app/webroot/js/action_table.js allows XSS via a network history name.
- [CVE-2023-24028](https://cvepremium.circl.lu/cve/CVE-2023-24028) < MISP 2.4.168 - In app/Controller/Component/ACLComponent.php has incorrect access control for the decaying import function.

Thanks to the reporter Cyber Controls from SIX Group and Dawid Czarnecki of Zigrin Security.

A huge thanks to all the contributors and supporters of the MISP project. This release wouldn't be possible without the help of all the organisations and people supporting us to make MISP a reality.

Go to the detailed [changelog](https://www.misp-project.org/Changelog.txt) for more details about the changes to the MISP core software.

# Other updates and changes in the MISP project

## MISP Objects

- A new MISP object has been created for [typosquatting-finder](https://typosquatting-finder.circl.lu/) output.

## MISP Galaxy

- New Sigma Galaxy including all [Sigma rule](https://github.com/MISP/misp-galaxy/blob/main/clusters/sigma-rules.json) and their ATT&CK relationships - [import script](https://github.com/MISP/misp-galaxy/blob/main/tools/sigma/sigma-to-galaxy.py) added
- Many updates to the threat-actor and ransomware MISP galaxy
- Improvements to the country galaxy

## MISP taxonomies

- Improvements to the aviation taxonomy

## MISP warning-lists

- New generator added for the Cached Chrome Top Million Websites
- Improved generator for gzip files source
- VPN list generator fixed

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

