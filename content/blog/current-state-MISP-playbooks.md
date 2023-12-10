---
title: Current state of the MISP playbooks
date: 2023-12-08
layout: post
authors:
- Koen Van Impe
tags: ["playbooks", "automation", "jupyter", "notebooks", "procedure"]
categories: []
banner: /img/blog/misp-playbook-components.png
---

# Current state of the MISP playbooks

The MISP playbooks at [https://github.com/MISP/misp-playbooks](https://github.com/MISP/misp-playbooks) address common use-cases encountered by SOCs, CSIRTs or CTI teams to detect, react and analyse intelligence received by MISP. The project started early 2023 and as we're now ending the year it's time to look back at its current state and get an early glimpse of the future features. 

But before we do that, maybe it's good to first remind us what the MISP playbooks are about.

## Introduction

A recurring problem with *playbooks*, *standard operation procedures* or *workflows* is that documentation (*why, where, when, who*) and commands (*activities*, the *what*) often reside in different places. Version tracking and sharing playbooks with others can also be a nightmare. That's where [Jupyter notebook](https://jupyter.org/) jump in. Jupyter notebooks are an interactive environment where users can **write** and **execute computer code** and combine the code with **documentation** (in Markdown). For the MISP playbooks we extend this with [PyMISP](https://github.com/MISP/PyMISP), the Python library for MISP. As a user, you only need a **web browser** to interact with these playbooks. The MISP playbooks are also in JSON format so you can store them in a **versioning** system, track their changes and share them with others. 

The [GitHub](https://github.com/MISP/misp-playbooks) repository has [guidelines](https://github.com/MISP/misp-playbooks/blob/main/documentation/MISP%20playbook%20guidelines.md) to help you with building and maintaining your own playbooks and [technical documentation](https://github.com/MISP/misp-playbooks/blob/main/documentation/MISP%20playbook%20technical%20documentation.md) to setup your environment. For those that are impatient: there's a guide to quickly set it up on a [Kali VM](https://github.com/MISP/misp-playbooks/blob/main/documentation/MISP%20playbook%20on%20Kali.md) (or basically any Linux VM).

The structure of the playbooks is also [explained](https://github.com/MISP/misp-playbooks/blob/main/documentation/MISP%20playbook%20structure.md), along with a basic [example](https://github.com/MISP/misp-playbooks/blob/main/documentation/MISP%20playbook.ipynb). There's even a small [slidedeck](https://github.com/MISP/misp-playbooks/blob/main/documentation/FIRST-SIG%20-%20MISP%20Playbooks-20230601.pdf) of a presentation given for the [FIRST Automation SIG](https://www.first.org/global/sigs/automation/).

## Current state

### Commits

Since the start of the project there have been **30 [commits](https://github.com/MISP/misp-playbooks/commits/main)**, resulting in **15 MISP playbooks** and **guidance** and **technical** documentation on how to setup an environment for MISP playbooks.

![misp-playbook-commits.png](/img/blog/misp-playbook-commits.png)

### Issues

The GitHub [issue tracker](https://github.com/MISP/misp-playbooks/issues) is used to track the development of the playbooks. Basically each playbook corresponds with an *issue*. The issue tracker is also your best choice to request a [new playbook](https://github.com/MISP/misp-playbooks/issues/new?assignees=cudeso&labels=playbook%3Astate%3Dproposal%2Cneeds+triage&projects=&template=new-playbook-proposal.yml) (via the **New MISP playbook proposal** template). So far there are **50 issues** created, with 20 issues already closed.

![misp-playbook-issuetracker-new.png](/img/blog/misp-playbook-issuetracker-new.png)

### Playbooks

The current [MISP playbooks](https://github.com/MISP/misp-playbooks/tree/main/misp-playbooks) cover the needs of MISP **users** and MISP **administrators**. For the former there are playbooks to

- Deal with **malware investigations**
  - **Malware** triage with MISP with **static** malware analysis ([2](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_malware_triage-with_output.ipynb))
  - **Malware** triage with MISP with **dynamic** malware analysis ([3](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_malware_triage_upload_sample-with_output.ipynb))
  - Query for **hash** information ([15](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_query_hash_information-with_output.ipynb))
- Do **OSINT investigations**
  - Query for **CVE** information ([25](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_query_cve_information.ipynb))
  - Query for **IP** reputation ([12](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_query_ip_reputation-with_output.ipynb))
  - Query for **domain** reputation ([13](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_query_domain_reputation-with_output.ipynb))
- Use the MISP features to **search** for specific pieces of information
  - Create a custom MISP warninglist ([7](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_create_custom_MISP_warninglist-with_output.ipynb))
  - Do a retroscan with a MISP **warninglist** ([8](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_retroscan_with_MISP_warninglist-with_output.ipynb))
- Become better acquainted with the **MISP features**
  - Create MISP **objects** and relationships ([11](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_create_MISP_objects_and_relationship-with_output.ipynb))
  - Work with the different MISP **timestamps** ([42](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_using_timestamps_in_MISP-with_output.ipynb))
- Use the playbooks to deal with **phishing** incidents
  - Create or update a MISP event with information from a phishing incident with a link ([1](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_create_or_update_a_MISP_event_with_information_from_a_phishing_incident_with_a_link-with_output.ipynb))
- Use MISP for **CTI work**
  - **Threat actor** profiling ([26](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_threat_actor_profiling-with_output.ipynb))


For the MISP administrators there are playbooks to
- Provision **users** and **organisations** ([43](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_provision_users_organisations-with_output.ipynb))
- Do bulk **deletes** of MISP events ([29](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_bulk_delete_events-with_output.ipynb))

There is also a **[skeleton](https://github.com/MISP/misp-playbooks/blob/main/misp-playbooks/pb_skeleton.ipynb)**  playbook that is used to start a new playbook.

### Activities in 2023

If you review the issues you'll notice that most are labelled with **playbook:activity**. This label is used to group the work in different phases of development. In the first year, the focus was on

#### Activity 1 : Creating a first set of playbooks and documentation guidelines
  - Four playbooks are published, in addition to a **skeleton** playbook.
  - Documentation **guidelines** to help users jump on board and start using the playbooks.

#### Activity 2 : A second set of playbooks with technical documentation
  - An additional six playbooks are published, aimed towards MISP **users** and **administrators**. 
  - **Technical** documentation to setup an environment to use the playbooks.

#### Activity 3 : Advanced playbooks
  - Six ([22](https://github.com/MISP/misp-playbooks/issues/22) soon to be published) more **advanced playbooks** are published.

### Moving forward

The GitHub repository also holds the work that is foreseen for 2024. What can you expect for the future?

#### Activity 4: MISP workflow integration, Elasticsearch, MDTI and support for curation

![misp-playbook-workflows.png](/img/blog/misp-playbook-workflows.png)

- First explore the options to integrate the MISP playbooks with **MISP workflows**
    - There are challenges to overcome, but the idea is that documentation for [workflows](https://www.misp-project.org/misp-training/handout/a.12-misp-workflows_handout.pdf) can be stored in the playbooks, and there is a form of *code-interaction* between the two. The exact details are to be defined, if you have ideas or suggestions make sure to add them to issue [46](https://github.com/MISP/misp-playbooks/issues/46)
- Playbooks that query **Elasticsearch** for indicators from MISP. The playbook adds sightings and creates a summary ([5](https://github.com/MISP/misp-playbooks/issues/5))
- Interaction with the Microsoft Defender Threat Intelligence (**MDTI**) API ([44](https://github.com/MISP/misp-playbooks/issues/44))
- Search for JARM fingerprints ([19](https://github.com/MISP/misp-playbooks/issues/19))
- Document the playbooks in JSON ([48](https://github.com/MISP/misp-playbooks/issues/48))
- Support threat intelligence **curation** ([30](https://github.com/MISP/misp-playbooks/issues/30), [23](https://github.com/MISP/misp-playbooks/issues/23) and [21](https://github.com/MISP/misp-playbooks/issues/21))

#### Activity 5: Timesketch, conversions with CACAO and Microsoft Sentinel 

- Following the Elasticsearch playbook, a playbook that has similar features but now with **Timesketch** integration ([6](https://github.com/MISP/misp-playbooks/issues/6))
- Investigate if there can be translations between MISP playbooks and **CACAO** playbooks
  - A [CACAO playbook](https://docs.oasis-open.org/cacao/security-playbooks/v1.0/security-playbooks-v1.0.html) ([v2](https://docs.oasis-open.org/cacao/security-playbooks/v2.0/security-playbooks-v2.0.html)) is a workflow for security orchestration containing a set of steps to be performed based on a logical process. There are overlaps between CACAO and MISP playbooks, so a translation / conversion is only the next logical step ([49](https://github.com/MISP/misp-playbooks/issues/49))
- Following the integration between [MISP and Microsoft Sentinel](https://github.com/cudeso/misp2sentinel), playbooks that create MISP events based on the data in Sentinel incidents ([34](https://github.com/MISP/misp-playbooks/issues/34))
- Additional playbooks to deal with malware and phishing (URLs) ([16](https://github.com/MISP/misp-playbooks/issues/16), [14](https://github.com/MISP/misp-playbooks/issues/14) and [4](https://github.com/MISP/misp-playbooks/issues/4))

#### Activity 6: Scheduled playbooks, timelines, 

- Traditionally playbooks are executed based on a human trigger.
    - In this activity the options are explored to **parametrise** and **schedule** the execution of MISP playbooks ([47](https://github.com/MISP/misp-playbooks/issues/47))
- Create a **timeline** based on different MISP events or search queries ([28](https://github.com/MISP/misp-playbooks/issues/28))
- Additional playbooks to support threat intelligence curation ([24](https://github.com/MISP/misp-playbooks/issues/24) and [50](https://github.com/MISP/misp-playbooks/issues/50))
- Try to integrate the suggestions from "Getting Started with ChatGPT and Jupyter Notebook
" in MISP playbooks ([38](https://github.com/MISP/misp-playbooks/issues/38))
- Playbooks to create filter lists ([18](https://github.com/MISP/misp-playbooks/issues/18)) and do domain pivoting ([17](https://github.com/MISP/misp-playbooks/issues/17))


## Conclusion

As you can observe from the above, there's still quite some work ahead. Important is that the list of playbooks to develop is only a list of suggestions. If you have a good idea for a playbook or if you find yourself doing the same activities over and over again, then document the steps and request a new [MISP playbook](https://github.com/MISP/misp-playbooks/issues/new?assignees=cudeso&labels=playbook%3Astate%3Dproposal%2Cneeds+triage&projects=&template=new-playbook-proposal.yml) to be developped for it.