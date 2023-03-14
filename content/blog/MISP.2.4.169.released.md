---
title: MISP 2.4.169 released with various improvements and bug fixes. 
date: 2023-03-14
layout: post
banner: /img/blog/graph-syria.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.169](https://github.com/MISP/MISP/releases/tag/v2.4.169) with various improvements and bug fixes.  

It includes many improvement [release](https://www.misp-project.org/Changelog-misp-stix.txt) of [misp-stix](https://github.com/MISP/misp-stix), the core Python library for importing and exporting STIX (1, 2.0 and 2.1).

# Improvements

- New MISP workflow module to support Splunk HEC export.
- Sighting ReSTsearch reworked to make it faster.
- dashboard-widget:TrendingTags improved with new filtering and over time functionalities.
- New ApacheSecureAuth authentication scheme added.

# Fixes

- TAXII servers invalid baseurl field type fixed.
- Restore bro export (temporary fix until a complete rework of the bro export in ReSTsearch).

A huge thanks to all the contributors and supporters of the MISP project. This release wouldn't be possible without the help of all the organisations and people supporting us to make MISP a reality.

Go to the detailed [changelog](https://www.misp-project.org/Changelog.txt) for more details about the changes to the MISP core software.

# Other updates and changes in the MISP project

## MISP Objects

- A new MISP object `ransomware-group-post` has been created to support [ransomlook.io](https://www.ransomlook.io/).  
- Improved `victim` object.
- A new MISP object `transport-ticket` has been created to share information about transports in MISP.
- Various improvements to `network-connection`, `network-socket`.
- A new MISP object `registry-key-value`

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- A new MISP galaxy `first-dns` matrix describing DNS abuse techniques has been added.
- Various improvements in different galaxy such as `threat-actors`, `sigma`, `stealer`, `tools, ``region`, `360net`, MITRE ATT&CK.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- New `captive-portals` warning list added.
- New `parking` page warning list added.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
