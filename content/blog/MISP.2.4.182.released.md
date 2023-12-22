---
title: MISP 2.4.182 released with new features, improvements bugs fixed and an important security fix. 
date: 2023-12-22
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/workflow-blue.png
---

MISP 2.4.182 released with new features, improvements bugs fixed and an important security fix.

# MISP Core

## New Features

- [event:view] Added new option `show_server_correlations_for_all_users`
  allowing non-privileged users to view server correlations. [Sami
  Mokaddem]

## Changes

- [Version] bump. [iglocska]
- [misp-objects] updated to the latest version. [Alexandre Dulaunoy]
- [misp-stix] Bumped latest version. [Christian Studer]
- [warning-lists] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [Geo-Open] updated to the latest version. [Alexandre Dulaunoy]
- [PyMISP] Bump. [Raphaël Vinot]
- [CLI] runUpdates updated to purge any pending db lock first.
  [iglocska]
- [event reports] content field size changed to mediumtext. [Andras
  Iklody]
- [logging] fail silently if logging entry can't be saved. [iglocska]

  - can happen when the log change is too large for example
  - no need to roll back / break sync for example if a log entry is too large, just fail silently.
- [events:event-graph] Allow expansion of nodes by double-clicking.
  [Sami Mokaddem]

  In response to significant demand from Terrtia and subsequent evaluation by adulau
- [feed:attachFeedCorrelations] Added comment. [Sami Mokaddem]
- [event:view] Show feed meta-information as popup. [Sami Mokaddem]
- [misp-stix] Bump. [Jakub Onderka]

## Fix

- [db_schema] dump. [iglocska]
- [correlation] exclusion cleaning was broken for noacl correlations,
  fixes #8899. [iglocska]
- [eventReport:editReport] Generate an UUID if new report added from
  pull. [Sami Mokaddem]
- [workflows:editor] Prepend baseurl to url. [Lukasz Rzasik]
- [TOTP] allow deletion of TOTP from edit page. [Christophe Vandeplas]
- [security] new audit logs lack of ACL controls. [iglocska]

  - added proper ACL handling to the new audit logs
  - as reported by fukusuket(Fukusuke Takahashi)
  - Assigned [CVE-2023-50918](https://cvepremium.circl.lu/cve/CVE-2023-50918) for this vulnerability. The new audit log is not enabled by default.
- [case sensitivity] fix. [iglocska]
- [login_history] fixes str_contains  #9433. [Christophe Vandeplas]
- [login_history] fixes str_contains  #9433. [Christophe Vandeplas]
- [password reset] required current password for token based reset.
  [iglocska]
- [diag] diagnostics page loading issue. [Michael Hirt]
- [openapi] add version to match spec. fixes #9058. [Luciano Righetti]
- [caching] remove uuid validation from the feed caching. [iglocska]

  - not really needed and it breaks the entire caching if a single old event has an invalid uuid
- [attribute bulk update] separate out tag deletion as it builds a
  ridiculously large query at times. [iglocska]
- [caching] remove uuid validation from the feed caching. [iglocska]

  - not really needed and it breaks the entire caching if a single old event has an invalid uuid

# MISP project knowledge bases

## MISP Objects

Improved [shadowserver-malware-url-report](https://www.misp-project.org/objects.html#_shadowserver_malware_url_report) and [cs-beacon-config](https://www.misp-project.org/objects.html#_cs_beacon_config) object template. Updates in the [victim object template](https://www.misp-project.org/objects.html#_victim) and [report object template](https://www.misp-project.org/objects.html#_report).

## MISP Galaxy

Improved [Sigma rules galaxy](https://github.com/MISP/misp-galaxy/blob/main/clusters/sigma-rules.json), [threat-actors database](https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json) with many new threat-actors 

## MISP warning-lists

[Warning-lists updated](https://github.com/MISP/misp-warninglists) to the latest version from the different sources.

# Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

