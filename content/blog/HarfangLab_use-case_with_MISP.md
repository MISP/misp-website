---
title: HarfangLab Use-Case with MISP 
date: 2024-02-26
layout: post
authors:
- Rémi Pointel
tags: ["HarfangLab", "MISP", "EDR"]
categories: []
banner: /img/blog/hf-image001.png
---

## EDR Use-Cases with MISP 

Historically, teams shared indicators of compromise (IOCs) via email in documents that were often difficult to analyze and challenging to automate for processing.

Simultaneously, the sharing of information between operational teams across different entities, via their CSIRTs and SOCs, has become increasingly industrialized.

This trend led to the inception of the MISP project in 2011, which aims to share information in a [standard](https://www.misp-standard.org/), automatable format within trusted circles.

Today, MISP is utilized by numerous CSIRTs and SOCs, either for community information-sharing projects or for internal IOC management.

Given its widespread adoption, it's easy to find libraries and tools for integrating MISP into existing ecosystems.

Having introduced MISP, let's delve into the YARA and Sigma formats, well-known to cyber experts and used by EDR [HarfangLab](https://harfanglab.io/en/).

## Cyber Threat Detection: What Are YARA and Sigma?

### YARA: Definition

[YARA](https://github.com/VirusTotal/yara) is a tool aimed at assisting malware analysts and researchers in identifying and classifying malware samples. It enables the creation of descriptions for malware families based on textual or binary patterns and is an open format embraced by the cyber community.

### Sigma: Definition

Sigma, another standard tool extensively used by the community, facilitates the writing of detection rules. It allows for the definition of these rules independent of the security product’s format.

It also supports converting from Sigma to the query language used by the security tool.

We use these standard formats in our EDR, offering full access to detection rules in a transparent, white-box manner.

Adopting standard formats like YARA and Sigma offers several benefits:

- Ease of use for users.
- Familiarity among analysts.
- Opportunity to leverage existing knowledge of these formats, which are prevalent in other market security solutions.
- Easy integration with the existing ecosystem.
- Rule transparency, with the option for modification if needed.

Beyond YARA and Sigma, how does HarfangLab handle Threat Intelligence? We explain next.

## Cyber Threat Intelligence (CTI) at HarfangLab

Our CTI team is constantly monitoring for new threats, utilizing both open sources (publications) and private channels (telemetry, communities, etc.).

They ensure the timely updating of detection rules in MISP.

## How HarfangLab Integrates MISP

All detection rules are centralized and managed in MISP.

The goal is to centrally provide our detection rules to customer stacks via a dedicated tool, facilitating information sharing in all configurations (SaaS and On-Premise).

Our management console, through a native MISP connector, links to HarfangLab MISP and retrieves the latest detection rules.

![](/img/blog/hf-image001.png)

We've discussed the YARA and Sigma rules and their integration and updates in MISP to enhance our EDR detection engines. But how do these engines function?

## HarfangLab EDR: 5 Complementary Detection Engines

![](/img/blog/hf-image002.png)

HarfangLab's EDR comprises 5 detection engines:

- **IOC**: This engine allows users to define indicators deemed malicious.
- **YARA**: A signature-based detection engine, applying rules to binaries during execution and various process stages. Depending on security policy settings, it detects and possibly blocks the concerned process.
- **Sigma**: A behavioral detection engine, applying rules to system events.
- **HL-AI**: An AI-based engine, identifying unknown threats. It evaluates binaries at process creation, predicting their nature (goodware or malware), and can block execution.
- **Ransomguard**: Dedicated to detecting and blocking ransomware threats.

What about whitelist management?

## MISP and Whitelists

System administration utilities or certain application behaviors, mistaken for attacks, can lead to false alerts. Thus, it's crucial for analysts to manage alert relevance via whitelists in MISP.

When an analyst deems a security event a false positive, two actions are possible:

- Creating or modifying a whitelist specific to the customer's information system.
- The CTI team amends the rule, independent of the customer's system, benefiting all solution users.

### Rule Deployment Cycle

Upon rule modification or addition by the CTI team, it undergoes a CI/CD cycle. After consistency and validity tests, it's deployed to the HarfangLab MISP, available to all customer stacks.

As mentioned earlier, MISP centralizes detection rules and seamlessly integrates into existing ecosystems. Users maintain full control over rules, with the flexibility to activate, deactivate, modify, or add them.

Furthermore, users with existing MISPs can link them to HarfangLab MISP, gaining access to our rules in addition to their own.

In conclusion, MISP offers:

- Centralized detection rules.
- Native integration with existing IS tools.
- Automated rule updates.
- Facilitated information sharing.

