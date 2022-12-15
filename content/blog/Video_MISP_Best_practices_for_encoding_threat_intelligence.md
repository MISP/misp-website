---
title: Training Video - MISP Best Practices for Encoding Threat Intelligence
date: 2022-12-15
layout: post
banner: /img/blog/workflow.png 
---

# MISP Training Video December Edition - Best Practices for Encoding Threat Intelligence and Leveraging the information in MISP to Make Threat Landscape Report

{{< youtube JIeiwzY7Fvs >}}

## Content of Training Session

- [MISP data model introduction](https://github.com/MISP/misp-training/blob/main/complementary/other-slides/a.11.a-misp-data-model-overview.pdf)
- [Best practices - from evidences to actionable evidences](https://github.com/MISP/misp-training/blob/main/complementary/other-slides/MISP%208%20Commandments%20-%20Recommendations%20and%20Best%20Practices%20when%20encoding%20data.pdf)
- Leveraging the information in MISP to Make Threat Landscape Report

## Leverage the information in MISP to make threat landscape report

### Most often questions asked to generate a threat landscape report

MISP can be a great source for generating a threat landscape report. There often many questions asked by various stakeholders which can be used as basis to scope what kind of information is required or needed.

- What are the most common vulnerabilities?
- What are the most common threats?
- What are the most common techniques used by adversaries?
- What are the priorities or remediation to limit specific risks?
- What are the most common countries targeted?
- What are the most common malware families?

MISP itself can be also a source of interesting insight such as

- Who are the most active organisations?
- How active a sharing community is?
- What are the capabilities of an organisation?

MISP is not replacing an analyst to produce a report but it's an easy way to produce threat intelligence report without too much tedious or repetitive work.

### Tools in MISP that can help to generate threat-landscape report

#### From easiest to hardest - From UI to scripting
- Automatic event report generation
    - Create an event dedicated to threat-landscape
    - Build the event report automatically
    - Caveat: Time consuming to create, need to perform the aggregation manually

- MISP Periodic report
    - How to view it
    - How to set up automatic reporting by mail
    - How to configure in order to aggregate only for a filtered set of events

- MISP builtin-dashboard
    - How it works
        - Each user can have their own & templates can be shared
        - Drag & Drop widgets + configure the dashboard

- Extracting data from MISP
    - Get API key
    - Index VS RestSearch
    - Useful queries & parameters

- Toolsets to generate your report
    - Pandoc

~~~~bash
pandoc misp-event-report.md -o misp-event-report.pdf --from markdown --template eisvogel --listings
~~~~

### References

 - TIBER-EU [Guidance for Target Threat Intelligence Report](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/shared/pdf/Final_TIBER-EU_Guidance_for_Target_Threat_Intelligence_July_2020.pdf)
 - [A pandoc LaTeX template to convert markdown files to PDF or LaTeX.](https://github.com/Wandmalfarbe/pandoc-latex-template)
 - [Cybersecurity Threat Landscape Luxembourg 2021-2022](https://api.cybersecurity.lu/public/get_public_document/RAPPORT%20CTL_pages.pdf)

## Resources

### Cheatsheets

- [Cheatsheet: Concepts & Data model](https://www.misp-project.org/misp-training/cheatsheet.pdf)
- [Synchronisation logic](https://github.com/MISP/MISP/tree/2.4/docs/generic/Synchronisation)
- [Authentication logic](https://github.com/MISP/MISP/blob/2.4/docs/generic/Authentication%20Diagram/MISP%20Authentication%20Diagram.pdf)
- For your lawyers or if you are interested in legal docs: [MISP legal compliance (such as GDPR and alike)](https://www.misp-project.org/compliance/)

### Training materials

- Virtual machines (VirtualBox and VMWare format): [https://vm.misp-project.org/](https://vm.misp-project.org)
- All Slide Deck (source file and compiled): [https://github.com/MISP/misp-training](https://github.com/MISP/misp-training)
- PyMISP: [https://github.com/MISP/PyMISP/](https://github.com/MISP/PyMISP/)
- OpenAPI documentation: [https://www.misp-project.org/documentation/openapi.html](https://www.misp-project.org/documentation/openapi.html)
- [misp-stix](https://github.com/MISP/misp-stix/) a generic library for MISP standard format to STIX (1.1, 1.2, 2.0 and 2.1): [documentation](https://github.com/MISP/misp-stix/tree/main/documentation)


### Other ressources

- [MISP Mastodon](https://misp-community.org/@misp) - @misp@misp-community.org
- [MISP Twitter](https://twitter.com/MISPProject) - Follow to get latest news
- [Gitter MISP Support chat](https://gitter.im/MISP/Support)
- [Benefits of running your own MISP instance](https://www.misp-project.org/2019/09/25/hostev-vs-own-misp.html/)

### Acknowledgement

A huge thanks to all the participants for their active participation. The training is also part of the MeliCERTes project.

![](https://www.cerebrate-project.org/assets/images/logo/melicertes.png)
