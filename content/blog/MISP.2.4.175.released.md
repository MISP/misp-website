---
title: MISP 2.4.175 released with various bugs fixed, improvements and security fixes. 
date: 2023-08-24
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/sigint.png
---

MISP 2.4.175 released with various bugs fixed, improvements and security fixes. 

# Improvements

- Added support of `start_date` and `end_date` options in the MISP dashboard widgets.
- In the user periodic reporting, allow users to set the number of days to include in the reporting (UI).
- In the MISP dashboard org Widget, added support for `first_half_year` and `second_half_year` timeframe. 
- New enrich object functionality added, in order to allow for the enrichment of a complete MISP object. Used by the [SigMF module](https://www.misp-project.org/2023/08/23/MISP_now_supports_Signal_Metadata_Format_Specification_SigMF.html/) but this can be used with any expansion modules supporting objects.
- New feeds added.
- Improve the diagnostics when an instance does not have internet access or does not use the self-update feature

# Bugs fixed

- Update the CA bundle of the CakePHP submodule maintained by the MISP project.
- IndexFilter: correct index page filtering is now fixed for ReST requets.
- Prevent `push_rules` from being required in API requests to the `/server/edit` endpoint.
- The annoying MISP event import bug from JSON has been fixed, you can now import MISP JSON events without the `Event` key.
- Various fixes in the MISP dashboard interface.
- Fix 

# Security fixes

- [CVE-2023-40224](https://cvepremium.circl.lu/cve/CVE-2023-40224) <= MISP 2.4.174 - allows XSS in app/View/Events/index.ctp. (reported by BeDisruptive OSS Team)
- [CVE-2023-41098](https://cvepremium.circl.lu/cve/CVE-2023-41098) <= MISP 2.4.174 - In app/Controller/DashboardsController.php, a reflected XSS issue exists via the id parameter upon a dashboard edit. 

Thanks to BeDisruptive OSS Team and Centre for Cyber Security Belgium (CCB) for the reporting.

Also a huge thanks to all the contributors, reporters and helpers supporting the MISP project.

## MISP Objects and Relationships

- A new generic `x-header` object template has been created to add custom HTTP or SMTP headers easily.
- [SigMF object templates](https://www.misp-project.org/2023/08/23/MISP_now_supports_Signal_Metadata_Format_Specification_SigMF.html/) added.
- Updated `artifact` object to better support [STIX 2.1](https://github.com/MISP/misp-stix).
- New `malware` and `malware-analysis` objects to better support [STIX 2.1](https://github.com/MISP/misp-stix). 

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Various updates in the [threat actor MISP galaxy](https://www.misp-project.org/galaxy.html#_threat_actor) and tool cluster.
- Various automatic updates to the Sigma galaxy.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- New [Zscaler IP address generator](https://github.com/MISP/misp-warninglists/blob/main/tools/generate-zscaler.py) added.
- New OpenAI chatgpt crawler IP sources added.
- All the lists have been updated.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

## MISP taxonomies

For more details, the [misp-taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

## MISP-stix

MISP-stix includes multiple improvements and bugs fixed.

For more details, the [misp-stix changelog](https://www.misp-project.org/Changelog-misp-stix.txt) is available.

## PyMISP

- Bug fix for updating sharing group.
- Improved msg-extract function.

For more details, the [PyMISP changelog](https://www.misp-project.org/Changelog-PyMISP.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
