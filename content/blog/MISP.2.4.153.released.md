---
title: MISP 2.4.153 released with improvements and bugs fixes
date: 2022-02-04
layout: post
banner: /img/blog/timeline-improvement.png
---

# MISP 2.4.153 released

- MISP UI translation in Thai added.
- Improved the debugging of the synchronisation, including more meaningful messages in debug logs.
- Significant improvements in the [misp-stix library](https://github.com/MISP/misp-stix), to support additional import coverage of files along with improvements to the STIX export.
- Improved debugging in the TLS handshake for synchronisation.
- Additional CLI tests for security.
- Markdown-IT library updated to the latest version, including security fixes to version 12.3.2.
- Improvements in the various MISP install scripts.

Many internal improvements and bug fixes.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements in MISP core.

# MISP Modules

- New [VirusTotal collection export](https://misp.github.io/misp-modules/export_mod/#virustotal_collections) module added.
- Improved i[Crowdstrike falcon expansion](https://misp.github.io/misp-modules/expansion/#crowdstrike_falcon) module.
- [Censys enrich module](https://misp.github.io/misp-modules/expansion/#censys_enrich) updated for the new API of Censys.
- [New MWDB push module](https://misp.github.io/misp-modules/expansion/#mwdb) for malware sample in MISP.
- Various fixes to existing modules.

The [MISP modules changelog is available](/Changelog-misp-modules.txt).

# MISP Taxonomies

- New [State responsibility taxonomy](https://www.misp-project.org/taxonomies.html#_state_responsibility) added.
- [Workflow taxonomy](https://www.misp-project.org/taxonomies.html#_workflow) improved.
- [runtime-packers](https://www.misp-project.org/taxonomies.html#_runtime_packer) taxonomy improved.
- New [Unified Kill Chain taxonomy](https://www.misp-project.org/taxonomies.html#_unified_kill_chain) added.

[MISP Taxonomies changelog](/Changelog-misp-taxonomies.txt) is available.

# MISP Galaxy

- New surveillance group added "Cytrox".
- New [threat-actor](https://www.misp-project.org/galaxy.html#_threat_actor) such as SideCopy, AQUATIC PANDA and others.
- Many updates.

[MISP Galaxy changelog](/Changelog-misp-galaxy.txt)

# MISP Objects

- New social and personal relationships for MISP objects based on [FOAF relationships](https://www.perceive.net/schemas/20020722/relationship/).
- [Probabilistic data structure object](https://www.misp-project.org/objects.html#_probabilistic_data_structure) added and describes a space-efficient data structure such as Bloom filter or similar structure.
- Many improvements in GTP, diameter and SS7 attack template objects.
- New STIX 2.1 objects such artifact and identity available as MISP template object.
- Many improvements to different MISP object templates.

[MISP objects changelog](/Changelog-misp-objects.txt)

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html)
.


