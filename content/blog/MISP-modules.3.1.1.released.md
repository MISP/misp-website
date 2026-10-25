---
title: "MISP Modules v3.1.1: 33 New Expansion Modules and More Ways to Turn Threat Intelligence into Action"
author:
 - MISP Project team
date: 2026-10-25
tags: ["MISP", "Threat Intelligence", "release", "modules" ]
layout: post
banner: /img/blog/mod1.png
---

The MISP project is pleased to announce **misp-modules v3.1.1**, one of our largest recent expansions of the module ecosystem. This release brings **33 new expansion [modules](https://misp-project.org/modules/)**, new integrations for security controls and automation, and a broad set of fixes to existing connectors.

The timing is deliberate. With **MISP 3.0 now available in Early Access**, we are not only improving the interface through which analysts explore threat intelligence. We are also expanding the range of data sources, investigation pivots, and operational tools they can use. MISP 3.0 makes it easier to navigate and connect intelligence; misp-modules v3.1.1 makes more intelligence and more actions available along the way.

<img width="1689" height="925" alt="Screenshot from 2026-10-25 15-38-12" src="https://github.com/user-attachments/assets/a23435b4-d6cd-4ad8-aa2e-32fcac38a32d" />
<img width="1713" height="1061" alt="Screenshot from 2026-10-25 15-39-48" src="https://github.com/user-attachments/assets/28d854b8-359a-4a34-aeef-362b610abbd2" />
<img width="1713" height="1061" alt="Screenshot from 2026-10-25 15-40-11" src="https://github.com/user-attachments/assets/21668833-dcd2-40c7-9cf3-6e210573c3a2" />

## 33 new expansion modules: more sources, more pivots

An indicator is rarely the end of an investigation. An IP address leads to a host, a domain leads to historical DNS records, a file hash leads to malware analysis, and a vulnerability identifier leads to affected products. This release adds a substantial number of ways to follow those connections from MISP.

### Infrastructure, DNS, and open-source intelligence

New integrations make it easier to explore Internet-facing infrastructure, historical context, and relationships around suspicious indicators:

- **Team Cymru Scout** and **Team Cymru Scout Search** for additional infrastructure intelligence and search capabilities.
- **Silent Push Enrichment**, **ShadowTrackr**, and **Shodan InternetDB** for new infrastructure and exposure pivots.
- **IVRE** and **Host.io** to broaden network and domain investigations.
- **Zetalytics Passive DNS** for historical DNS observations.
- **OSINT Industries** and **LastInfoSec** for additional OSINT enrichment sources.
- **Wayback Machine webarchive** to add archived web content to investigations.

Together, these integrations help analysts move beyond a single observable and investigate the infrastructure and history around it.

### Threat intelligence services and malware context

The release significantly broadens the selection of commercial and community intelligence sources available through misp-modules:

- **Kaspersky Threat Intelligence Portal**
- **Intel 471 Hunter**
- **Proofpoint ET Intelligence**
- **Orange Cyberdefense Datalake**
- **Metras Enrichment**
- **MalBeacon**
- **Orion Malware**
- **PolySwarm Enrichment**
- **ReversingLabs Malware Presence**
- **ReversingLabs Spectra Intelligence Submission**

Different sources answer different questions. Having more of them accessible from MISP helps teams corroborate findings, add context, and select the pivots that fit their investigative workflows.

### Sandboxes, malware analysis, and sample retrieval

Seven new modules extend the malware investigation toolbox:

- **Intezer Sandbox**
- **Hybrid Analysis Sandbox**
- **PolySwarm Sandbox**
- **Palo Alto WildFire**
- **VMRay Analyzer Lookup**
- **UnpacMe Lookup**
- **VirusTotal Sample Downloader**

These modules expand the available paths from a suspicious hash or sample to analysis results and related evidence, including sample retrieval where the connected service supports it.

### Vulnerabilities, product context, and intelligence hygiene

Not every important pivot starts with an IP address or a hash. We have also added:

- **GCVE CPE**, bringing additional product-identification context into vulnerability investigations.
- **Qualys CVE Enrichment**, extending vulnerability-related lookups.
- **Import External Reference**, for enriching investigations with external references.
- **Hygiene Warninglist Check**, offering another way to check intelligence against warninglist data.

These modules reinforce an important principle: useful threat intelligence needs context, and the quality of an indicator matters as much as its presence.

### Cryptocurrency investigations: SoChain

The new **SoChain** expansion supports **BTC, LTC, DOGE, and ZEC** addresses. It can return balances, transaction counts, activity windows, recent counterparties, and potential address-poisoning lookalikes as MISP coin-address objects. It works without an API key, with optional authenticated access.

This is a useful addition for investigations involving cryptocurrency infrastructure and financial traces.

## Beyond enrichment: getting intelligence into operational tools

Enrichment is only part of the story. MISP is also valuable when intelligence can be translated into detection, filtering, and response workflows. Version 3.1.1 adds several integrations in that direction:

- **Firewall ACL exporters** for **PAN-OS, Junos, FortiOS, Cisco ASA, and RouterOS**, providing additional vendor-specific ways to translate MISP indicators into access-control lists.
- **Wazuh CDB export and publishing modules** for typed indicator lists, together with improvements to size limits and `analysisd` reload handling.
- **OWASP Core Rule Set (CRS) export** for HTTP indicators marked for IDS use.
- **Squid proxy export** for IDS-filtered indicators.
- **osquery pack publishing**, alongside updates to pack formatting and case-insensitive DNS indicator matching.
- **Matrix workflow action**, allowing MISP workflows to send messages to Matrix rooms.

These additions help bridge the gap between discovering intelligence and making it useful in an operational environment. As always, exported indicators and rules should be reviewed and tested in the context of the receiving security control.

## Reliability and security matter too

A large integration ecosystem is only useful when its modules behave predictably. Alongside the new modules, v3.1.1 includes a substantial round of corrective work:

- **CSV import** now correctly handles custom delimiters and quoting, tolerates empty fields, and imports `attribute_tag` values.
- **Microsoft Defender Endpoint export** now matches SHA-256 hashes against the correct `InitiatingProcessSHA256` field.
- **ONYPHE enrichment** has been aligned with its OpenAPI CTI and ASM models, including improvements to certificate serial-number handling.
- **ANY.RUN integrations** gain proxy settings and a report-handling fix.
- **CEF export** receives serialization and standards-compliance corrections.
- **Team Cymru Scout** preserves usable intelligence when only part of a response can be converted.
- **Palo Alto WildFire** supports appliance CA bundles while retaining TLS verification.
- Numerous connectors receive updates for API endpoints, pagination, authentication, timeouts, timestamps, and structured responses.
- HTTP dependencies have been updated to address **emSign and Brotli security issues**.

These details may be less visible than a brand-new module, but they are essential to trustworthy automation and repeatable investigations.

## Built to complement MISP 3.0

[MISP 3.0 Early Access](https://www.misp-project.org/2026/10/16/misp.3.0-early-access.html) introduces a redesigned analyst experience, including new ways to explore values, relationships, and graphs. That experience becomes much more useful when analysts have more sources to consult and more ways to act on what they find.

**[misp-modules](https://misp-project.org/modules/) v3.1.1 complements that direction:** broader enrichment helps analysts add context; expanded export and publishing capabilities help operational teams use the resulting intelligence; and the fixes in this release make both paths more reliable.

Importantly, this evolution is not limited to MISP 3.0. The MISP 3.0 Early Access retains compatibility with the established API, and the module ecosystem continues to serve existing MISP deployments. 

## Get involved

The strength of misp-modules comes from the range of services it connects and from the people who keep those connections working. Thank you to all contributors, including **Andrei Bacescu**, **Badger**, and **Atif Nazir**, as well as the wider MISP community, for the fixes, integrations, reviews, and testing behind this release.

If you maintain a useful threat intelligence service, have an interesting OSINT pivot, or need a new export format, contributions are welcome. **The more interoperable our tooling becomes, the more useful shared threat intelligence is for everyone.**

**Resources:**

- **Source code and contributions:** https://github.com/MISP/misp-modules
- **MISP 3.0 Early Access announcement:** https://www.misp-project.org/2026/10/16/misp.3.0-early-access.html

**MISP Modules v3.1.1 is another step toward a richer, more connected, and more operational threat intelligence ecosystem—just as we open the next chapter with MISP 3.0.**
