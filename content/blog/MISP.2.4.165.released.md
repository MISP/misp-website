---
title: MISP 2.4.165 released with many improvements, bugs fixed and security fixes. 
date: 2022-11-21
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.165](https://github.com/MISP/MISP/releases/tag/v2.4.165) with many improvements to the workflow subsystem along with various performance improvements.

# Improvements

- [workflow] Module to toggle/remove the to_ids flag
- [workflow] Added generic module to support attribute edition
- [workflow] [triggers:event_after_save_new] Added 2 new triggers for new events and new events from pull.
- [workflow:execute_module] Allow to ignore format conversion before executing module.
- [workflows:triggers] Added filtering capability on the index
- [CLI] Feed management added
- [CLI] Pretty and JSON output added in list and view feeds
- [Auth] OpenID connect improved
- [freetext] Fetch security vendor domains from [warninglist](https://github.com/MISP/misp-warninglists)
- [UI] Allow to disable PGP key fetching
- [UI] Show warning if user don't have permission to use API
- [tool:evengraph] Include relationships when using pivot key
- [UI] Show servers where event will be pushed

# Performance improvements

- [feed] Store freetext feed compressed in cache
- [internal] Store some data in Redis compressed to save memory
- [correlation] Do not correlate over correlating value again for full correlation
- [internal] Add support for [simdjson](https://github.com/simdjson/simdjson) extension
- [warninglist] Load warninglist from Redis for TLDs and security vendors

# Bugs fixed

- [tags] not passing name, filter, search all together would lead to the search not working

# Security issues

- [security] Permission for tag collections
- [security] Check user permission when attaching clusters

We strongly recommend MISP administrators to update to this latest version.

For a more detailed changelog, please see the online [Changelog](https://www.misp-project.org/Changelog.txt).

# New workflow blueprints available

New [workflow blueprints](https://github.com/MISP/misp-workflow-blueprints/) were added to support new use-cases.

- [Attach `tlp:clear` on `tlp:white`](./blueprints/blueprint_attach-tlp_clear-on-tlp_white_1661328256.json) - Attach the `tlp:clear` tag on elements having the `tlp:white` tag.
- [`PAP:RED` and `tlp:red` Blocking](./blueprints/blueprint_pap_red-and-tlp_red-blocking_1661328258.json) - Block actions if any attributes have the `PAP:RED` or `tlp:red` tag.
- [Remote `to_ids` flag if the indicator appears in known file list](https://github.com/MISP/misp-workflow-blueprints/blob/main/blueprints/blueprint_disable-to_ids-flag-for-existing-hash-in-hashlookup_1667228944.json) - Disable to_ids flag for existing hash in [hashlookup](https://www.hashlookup.io/).
- [Set tag based on BGP Ranking maliciousness level](https://github.com/MISP/misp-workflow-blueprints/blob/main/blueprints/blueprint_set-tag-based-on-bgp-ranking-maliciousness-level_1668498668.json) - Set tag based on [BGP Ranking](https://bgpranking.circl.lu) maliciousness level.

# New MISP modules

- [expansion] Added extract_url_components module to create an object from an URL attribute. 
- [expansion] New [crowdsec](https://www.crowdsec.net/) expansion module added.
- [expansion] New [VARIoT IoT exploits database](https://www.variotdbs.pl/exploits/) expansion module added.
- [expansion] Updates on hyasinsight expansion module.

# MISP taxonomies

- new misp-workflow taxonomy to have a consistent tag message for the MISP workflow.
- Taxonomy in support of integrating MISP with Sentinel. Sentinel indicator threat types added.

For more [details](https://www.misp-project.org/Changelog-misp-taxonomies.txt).

# MISP galaxy

- Many updates to the threat actor database.
- Update to the MITRE ATT&CK framework to version 12.0.

For more [details](https://www.misp-project.org/Changelog-misp-galaxy.txt).

# MISP objects

- New object to describe Telegram bots.
- Updated exploit object.

For more [details](https://www.misp-project.org/Changelog-misp-objects.txt).


