---
title: MISP 2.4.179 released with a host of improvements a security fix and some new tooling. 
date: 2023-11-26
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/workflow-blue.png
---

MISP 2.4.179 released with a host of improvements a security fix and some new tooling.

## First baby steps taken towards LLM integration

We currently included our first attempt at an LLM integration for report summarisation and extraction. The development is an outcome of our work with @aaronkaplan during hack.lu 2024 and relies on [stochasticCTIExtractor](https://github.com/aaronkaplan/stochasticCTIExtractor) for the extraction and interfacing with LLMs. 

Expect to see more in this space in the near future!

For a sneak peak, head over to our [lightning talk](https://www.youtube.com/watch?v=PzPJc0LdlC4) video on the topic.

## Workflow improvements

As always, @mokaddem is hard at work in his arcane laboratory, improving the workflow tooling. This time, among a host of improvements, he's also concocted up a new IF module that makes decisions based on the number of elements (counts) matching certain criteria. For a full list of changes, have a look at the [Changelog](https://www.misp-project.org/Changelog.txt).

# Performance improvements for large event edits

The edit performance when it comes to large events has been reworked to speed the process up somewhat. In addition a new "fast_update" mode has been added for special cases when no major changes are expected to an event or when additional precautions have been taken (As a main difference, validation of duplicate handling has been removed from this path).

For some benchmarks of what this means in practice for an event, assuming 20.000 attributes with a single tag being added to each and the last seen being altered:

#### MISP 2.4.178
**Time taken**: 171.2364685535431

#### MISP 2.4.179
**Time taken (standard mode)**: 97.22623372077942
**Time taken (fast mode)**: 40.74654579162598

This new method is currently exclusively used by the /events/edit endpoint, so expect it to show up in other endpoints in later releases.

## A new tool for remote delegations

Though more of an edge case, we've seen the need for some communities to be able to cross-instance automatically delegate publications, for example in the case of an ISAC republishing the data of their constituency anonymously, or an organisation providing data produced by a service provider being released under their own umbrella. If you have any such use-cases, head over to the new delegation tool and read up on how it works, what you can do with it - [misp-delegation](https://github.com/MISP/MISP/tree/2.4/tools/misp-delegation)

## Security: XSS fixed in the event timeline

This release also contains a security fix, a stored XSS trigerable via the event timeline widget, as reported by fukusuket(Fukusuke Takahashi). Thanks a lot for the report and we encourage the community at large to update their MISP instances to this release as well as to similarly report all their findings to us based on our [Security](https://www.misp-project.org/security/) policy.

## Other improvements

### MISP Taxonomies

Various improvements and inclusions of [new taxonomies](https://www.misp-project.org/taxonomies.html), such as an update to PAP, a taxonomy used by SRB-CERT as well as a taxonomy for doping-substances. 

The [PAP (Permissible Actions Protocol)](https://www.misp-project.org/taxonomies.html#_pap) has been updated to be inline with TLPv2. Thanks to the [contribution and discussions with ANSSI-FR/CERT-FR about the marking topic](https://www.cert.ssi.gouv.fr/csirt/sharing-policy/).

### MISP Objects 

Various fixes to a host of [object templates](https://www.misp-project.org/objects.html) as well as some new templates such as Crowdstrike Report objects were added in this release.

### MISP Galaxy

- A host of new clusters were added, mostly targeting the threat-actors galaxy library - a huge thanks goes to @Mathieu4141 for all the diligent work. Automatically ingested galaxies, such as the global sigma rule library have also been updated.

The MISP galaxy MITRE ATT&CK has been updated to the version 14. A new NAICS galaxy has been created to support [North American Industry Classification System](https://www.census.gov/naics/).

### MISP warning-lists

- Warning-lists updated to the latest version. Several warninglists have been brought up to the latest release as well as new warninglists such as the findip-host warninglist have been added. 

## For all other changes, please refer to the [Changelog](https://www.misp-project.org/Changelog.txt).

## Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

## MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

