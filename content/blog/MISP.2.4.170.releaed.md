---
title: MISP 2.4.170 released with new features, workflow improvements and bugs fixed 
date: 2023-04-13
layout: post
banner: /img/blog/workflow-2023.png
---

We are pleased to announce the immediate availability of [MISP v2.4.170](https://github.com/MISP/MISP/releases/tag/v2.4.170) with new features, workflow improvements and bugs fixed. 

It includes many improvement [release](https://github.com/MISP/misp-stix/releases/tag/v2.4.170) of [misp-stix](https://github.com/MISP/misp-stix), the core Python library for importing and exporting STIX (1, 2.0 and 2.1).

# Workflow

- A new feature has been added to the "misp-workflow-modules" module. It is an event threat level `if logic` module.
- The "workflow-module:send_mail" module now allows org admins to receive send_log_mail.
- The "workflow-module:send_mail" module now allows all admins to use it.
- The "workflow:tag_if" module now correctly compares cluster tags.
- The "workflow-module:enrich_event" module now does not run enrichment if no filtered elements are found. If a filtering condition was set and no item were matched, the whole event was enriched. Now nothing happens.
- The "workflow-module:tag_if" module now supports galaxy clusters. This fixes issue #8959.
- The data type of the workflows.data column has been changed from TEXT to LONGTEXT in the "db:workflows" module. This should fix issue #8979.
- The "workflows" module now requires misp-modules for email.

# New security features

- Improve security of the API authentication to pin IP in a single click.
- Seen IP addresses per API key added.

# Fixes

- Add support for a `breakOnDuplicate` named parameter on `/attributes/add` endpoint, default value is `true` which keeps the current behavior of throwing an error when the user tries to add duplicate attribute to an event.  When set to `false` the endpoint will work as an upsert, updating the attributes `timestamp` and any other properties provided in the payload, no error logs will be written.
- The "'sharing_group_id' doesn't have a default value error" error when importing an OpenIOC file has been fixed.

# Security fix

- [app/Lib/Tools/CustomPaginationTool.php allows XSS in the community index. ](https://cvepremium.circl.lu/cve/CVE-2023-28884)

A huge thanks to all the contributors and supporters of the MISP project. This release wouldn't be possible without the help of all the organisations and people supporting us to make MISP a reality.

Go to the detailed [changelog](https://www.misp-project.org/Changelog.txt) for more details about the changes to the MISP core software.

# Other updates and changes in the MISP project

## MISP Objects and Relationships

- New [Greynoise](https://www.greynoise.io/)-ip object.
- [network-socket] Added MAC address attributes. 
- New relationships `rewrite` added. 

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Sigma galaxy updated to the latest version.
- Threat actor galaxies updated with new threat actors and improved.
- Ransomware group updated to be inline with [ransomlook.io](https://www.ransomlook.io/).
- Stealer galaxy updated.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- New warning-lists added for Google Bot.
- Updated warning-lists for all sources.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
