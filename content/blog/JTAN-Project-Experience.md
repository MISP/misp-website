---
title: Collaborative Threat Intelligence Sharing and Automated Information Exchange - Insights from the JTAN Project Experience 
banner: /img/blog/2.4.174/blueprint-falsepositive-warninglist.png
author:
 - Alexandre Dulaunoy 
date: 2024-07-01
layout: post
---

The JTAN (Joint Threat Analysis Network) Project, co-funded by the European Union's CEF program, addresses the critical need for efficient and effective threat intelligence sharing among cybersecurity teams. As cyber threats grow in complexity and scale, the ability to quickly exchange and analyze threat data across organizations has become essential for maintaining robust security.

This document outlines the practical methods and tools developed and tested by the JTAN Project to facilitate this exchange. These include MISP Synchronization for real-time data sharing, REST APIs for automated integration with other systems, and real-time streaming solutions for immediate response scenarios. Additionally, advanced techniques like privacy-aware caching using PSS and Bloom Filters are explored to enhance data sharing while maintaining confidentiality.

The strategies and tools detailed here are designed to be reusable and adaptable, particularly for networks of CSIRTs (Computer Security Incident Response Teams), SOCs (Security Operations Centers), and other dispersed groups involved in cybersecurity operations. By implementing these approaches, organizations can improve their collective situational awareness and better defend against emerging cyber threats.

## Data Exchange Mechanisms and Strategies

By reviewing various open data exchange mechanisms and strategies, the JTAN project has tested and established a robust and versatile framework for sharing threat intelligence. This framework effectively caters to a diverse range of needs and scenarios in the field of cybersecurity. Additionally, these strategies are reusable and particularly beneficial for networks of CSIRTs, SOCs, or any dispersed group involved in operational security.

### (Push/Pull) MISP Synchronization

This method involves the synchronization of threat intelligence information across multiple MISP (Threat Intelligence Sharing Platform) instances. It allows various organizations to share and collaborate on cyber threat data in real-time, ensuring that the latest threat intelligence is available across all synchronized MISPs.

### (Pull cache) MISP Caching Synchronization

As an extension of MISP Synchronization, this strategy involves caching shared data to enhance the performance and reliability of data exchange. This approach is particularly beneficial in scenarios where MISP instances or caching sources are too large or out-of-context for direct and complete ingestion into MISP. Caching enables the correlation and availability of references, allowing users to determine if an indicator has been observed elsewhere without needing access to the entire dataset.

### (OpenAPI) MISP REST API

Utilizing the RESTful API provided by MISP, this strategy allows for programmatic access to the MISP platform. It enables automated data exchange and integration with other systems or tools, enhancing the flexibility and scalability of threat intelligence sharing.

### (Stream) Streaming using CocktailParty or N6

This approach is more dynamic, featuring real-time data streaming. Tools such as CocktailParty and N6 facilitate the streaming of threat intelligence, thus providing a continuous flow of information. This method is crucial in scenarios that demand an immediate response to evolving threats or the processing of a continuous data stream.

### (Privacy-aware cache) PSS and Bloom Filter for Sharing and Data Exchange

PSS and Bloom Filters represent advanced techniques utilized for efficient data sharing and exchange. PSS enables scalable and decentralized data searching, while Bloom Filters offer space-efficient probabilistic data representation. This combination ensures the sharing and searching of large volumes of threat data with minimal resource consumption. Additionally, a notable aspect is the capability to share information while maintaining the confidentiality of the actual data.

# API Documentation References

| Tool | API Reference(s) |
|:----|:---|
| [MISP](https://www.misp-project.org/) | [MISP OpenAPI Documentation](https://www.misp-project.org/openapi/)<br />[MISP Playbooks](https://github.com/MISP/misp-playbooks) |
| [N6](https://github.com/CERT-Polska/n6) | [N6 Stream API](https://n6.readthedocs.io/usage/streamapi/) |
| [IntelMQ](https://github.com/certtools/intelmq) | [IntelMQ API](https://intelmq.readthedocs.io/en/latest/user/intelmq-api.html) |
| [AIL](https://www.ail-project.org/) | [AIL API](https://github.com/ail-project/ail-framework/blob/master/doc/api.md) |
| [FlowIntel](https://flowintel.github.io/) | [FlowIntel API](https://flowintel.github.io/flowintel-doc/#/docs/api) |
| [PSS](https://github.com/hashlookup/private-search-set) | [PSS Metaformat](https://github.com/hashlookup/private-search-set?tab=readme-ov-file#meta-format) |
| [Graphoscope](https://github.com/cert-lv/graphoscope) | [Graphoscope API Usage](https://github.com/cert-lv/graphoscope?tab=readme-ov-file#api-usage-demo) |
| [Taranis-NG](https://github.com/SK-CERT/Taranis-NG) | [Taranis-NG Core ReST API](https://github.com/SK-CERT/Taranis-NG/tree/main/src/core/api) |
| [CocktailParty](https://github.com/flowintel/cocktailparty) | [CocktailParty](https://github.com/flowintel/cocktailparty/tree/stomp) |
| [MWDB](https://github.com/CERT-Polska/mwdb-core) | [MWDB REST API and MWDBLIB](https://mwdb.readthedocs.io/en/latest/user-guide/8-REST-and-mwdblib.html) |

# Interoperability Review via MISP

The existing API integrations were tested to ensure that the tools commonly used in JTAN and the CSIRT community are interoperable with the MISP standard REST API. If the tools did not support a REST API, evaluations were performed on available compatible streaming protocols within JTAN, such as STOMP.

| Tool | API Reference(s) |
|:----|:---|
| [MISP](https://www.misp-project.org/) | ✔️ Core testing protocol via REST API acting as a reference for the other tools |
| [N6](https://github.com/CERT-Polska/n6) | ✔️ [N6 Stream API](https://n6.readthedocs.io/usage/streamapi/) relies on STOMP and can interconnect with IntelMQ and CocktailParty. |
| [IntelMQ](https://github.com/certtools/intelmq) | ✔️ The different IntelMQ models (Expert bot, API collector, API output, Expert) [are supported](https://intelmq.readthedocs.io/en/develop/user/MISP-Integrations.html) to connect to MISP. Acting as a streaming tool, IntelMQ integrates [N6 support](https://intelmq.readthedocs.io/en/develop/user/n6-integrations.html). |
| [AIL](https://www.ail-project.org/) | ✔️ Can push to MISP any investigation or item in AIL. MISP galaxies and taxonomies are also supported. |
| [FlowIntel](https://flowintel.github.io/) | ✔️ Via FlowIntel Connector or Analyzer, data can be pushed to MISP and use the MISP modules as an analyzer. MISP galaxies and taxonomies are also supported. |
| [PSS](https://github.com/hashlookup/private-search-set) | ✔️ [PSS Metaformat](https://github.com/hashlookup/private-search-set?tab=readme-ov-file#meta-format) is compatible with MISP standard feed format. |
| [Graphoscope](https://github.com/cert-lv/graphoscope) | ✔️ MISP REST API accessible via [MISP plugins](https://github.com/cert-lv/graphoscope/tree/master/plugins/src/misp) |
| [Taranis-NG](https://github.com/SK-CERT/Taranis-NG) | ✔️ `Presenter` can create MISP standard JSON format and `Publisher` can create MISP events. |
| [CocktailParty](https://github.com/flowintel/cocktailparty) | ✔️ Streaming via STOMP compatible with N6 [CocktailParty](https://github.com/flowintel/cocktailparty/tree/stomp) |
| [MWDB](https://github.com/CERT-Polska/mwdb-core) | ✔️ via [karton-misp-pusher](https://github.com/CERT-Polska/karton-misp-pusher) |

# JTAN Project

The JTAN Project is co-funded by the European Union's CEF program.

The Action will establish a Joint Threat Analysis Network, an open collaboration group of European computer security incident response teams (CSIRTs) focused on collecting, sharing, and analyzing technical, operational, and strategic threat intelligence. The purpose of this collaboration is to combine the unique advantages of different teams to obtain comprehensive situational awareness and actionable information to effectively defend constituencies in each Member State, from critical infrastructure operators targeted by state-sponsored actors to individual citizens affected by cybercrime. The main part of the Action addresses gaps in the Cyber Threat Intelligence (CTI) tooling that is currently used by national-level CSIRTs in Europe. By strengthening individual tools and interconnecting them, the beneficiaries will achieve a new level of common situational awareness and benefit from shared knowledge and tooling.

## JTAN References

- Video [JTAN - Building a Data Sharing Network Using Open Source Tools](https://www.youtube.com/watch?v=lcSO6O-9YRk) - FIRST.org - FIRSTCON24 - Fukuoka, Japan

