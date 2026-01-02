---
title: "NGSOTI: Building an Integrated Threat-Intelligence and Information Sharing Ecosystem for the Next Generation of SOC Analysts"
banner: /img/blog/urban.jpg
author:
 - MISP Project team
date: 2026-01-02
tags: ["MISP", "Threat Intelligence", "soc", "training", "ngsoti" ]
layout: post
---

The **[Next Generation Security Operator Training Infrastructure (NGSOTI)](https://github.com/ngsoti/)** initiative was created to address a growing gap in cybersecurity education: the need to train analysts not only on tools, but on *real-world workflows, collaboration models, and operational constraints*. Rather than focusing on isolated technologies, NGSOTI brings together a coherent ecosystem of open-source projects designed to reflect how modern Security Operations Centers (SOCs) actually function.

At the core of this initiative is a strong emphasis on **human-centric security operations**, where analysts learn how to detect, investigate, contextualize, and respond to threats using realistic data, tooling, and processes. This approach is made possible through close collaboration between academic institutions and operational partners, including **[CIRCL](https://www.circl.lu/)**, **[Restena](https://restena.lu/)**, **[Tenzir](https://tenzir.com/)**, and the **[University of Luxembourg](https://www.uni.lu/en/)**.

## A Shared Operational Backbone

The various projects developed or integrated within NGSOTI are not standalone tools. They are designed to interoperate and reinforce one another, forming a cohesive training and experimentation platform that mirrors real SOC environments.

At the center of this ecosystem is **[MISP](https://misp-project.org/)**, which acts as the backbone for threat intelligence sharing and contextual enrichment. MISP enables trainees to work with structured threat intelligence, indicators, and contextual data while understanding lifecycle management, information sharing policies, and trust models.

Around this core, several complementary projects extend the operational realism of the platform.

### Vulnerability-Lookup: From Disclosure to Context

[Vulnerability-Lookup](https://github.com/cve-search/vulnerability-lookup) plays a key role in connecting vulnerability intelligence with operational workflows. It allows analysts to correlate vulnerability information from multiple sources, independently of traditional identifiers such as CVE IDs or new distributed publication such as [GCVE](https://gcve.eu/).

Within NGSOTI scenarios, Vulnerability-Lookup is used to:
- Enrich incidents and alerts with vulnerability context,
- Explore Coordinated Vulnerability Disclosure (CVD) workflows,
- Understand how incomplete or evolving vulnerability information impacts decision-making.

This directly complements MISP by strengthening the bridge between threat intelligence and vulnerability management. 

Integration with [MISP and vulnerability-sighting sighting](https://github.com/vulnerability-lookup/MISPSight) has been developed to provide direct intelligence from MISP communities back to vulnerability monitoring. A new [MISP module expansion](https://misp.github.io/misp-modules/expansion/#vulnerability-lookup) has been developed to support intelligence analysts in vulnerability management. 


### Poppy: Efficient Data Structures for High-Volume Intelligence

[Poppy](https://www.misp-project.org/2024/03/25/Poppy-a-new-bloom-filter-format-and-project.html) introduces an efficient Bloom filter implementation that is particularly useful when dealing with large-scale datasets and constrained environments.

Within NGSOTI, Poppy is used to:
- Demonstrate scalable filtering techniques,
- Teach students how to pre-filter large indicator sets before deeper analysis,
- Enable performance-aware design choices in detection and enrichment pipelines.

It highlights an often-overlooked aspect of SOC operations: performance engineering and data reduction. This is a fundamental library to support further lookup capabilities in MISP including correlation tables or feed management.

### Kunai: Endpoint Visibility and Detection Engineering

[Kunai](https://github.com/kunai-project/kunai) provides deep visibility into Linux systems and serves as a practical foundation for detection engineering exercises. Acting as a Linux-native counterpart to Sysmon, Kunai allows trainees to design, test, and validate detection logic based on real system telemetry.

Within NGSOTI, Kunai integrates naturally with:
- Rule-based detection workflows,
- Threat hunting exercises,
- MISP-driven intelligence enrichment.

This enables students to move from abstract detection concepts to hands-on engineering and validation. A [sandboxing environment](https://sandbox.kunai.rocks/) has been developed using Kunai to enable the analysis of potentially malicious software. It includes native integration with MISP, allowing analysis results to be exported and shared seamlessly.


### Rulezet: Collaborative Detection Engineering

[Rulezet](https://rulezet.org/) adds a collaborative layer to the ecosystem by enabling the creation, review, and improvement of detection rules such as Sigma, YARA, or Suricata signatures.

In the NGSOTI context, Rulezet supports:
- Peer review of detection logic,
- Quality assessment of rules before operational deployment,
- A shared knowledge base for detection engineering best practices.

This mirrors real-world SOC workflows, where detection content evolves through collaboration and continuous improvement. An integration with MISP is directly accessible in Rulezet, allowing any user to reuse rules across the MISP ecosystem.


### SkillAegis: Training, Scenarios, and Evaluation

[SkillAegis](https://github.com/MISP/SkillAegis) ties the entire ecosystem together by providing a structured environment for exercises, simulations, and assessment. It enables instructors to design realistic scenarios involving MISP, Kunai, vulnerability data, and detection rules, while tracking participant progress and skill development.

Through gamification and scenario-based learning, SkillAegis transforms technical tooling into an engaging training experience aligned with operational reality.

## A Cohesive Training and Research Ecosystem

What makes NGSOTI unique is not just the individual tools, but how they interoperate to form a realistic, modular, and extensible SOC environment. From vulnerability disclosure and threat intelligence to detection engineering and incident response, the platform allows learners and practitioners to experience the full lifecycle of modern cybersecurity operations.

By combining open-source technologies, real-world workflows, and strong collaboration between academia and operational teams, NGSOTI provides a blueprint for how future SOC training environments can be designed—grounded in reality, adaptable to evolving threats, and built around the people who operate them.

