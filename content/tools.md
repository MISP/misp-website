---
layout: page
title: Tools
permalink: /tools/
toc: true
---

## Software and tools

MISP's ecosystem includes applications, libraries, shared data models, and integrations for collecting, analysing, sharing, and using threat intelligence. This directory lists the [MISP project's software](https://github.com/MISP) first, followed by [CIRCL projects](https://circl.lu/projects/) and third-party integrations.

Choose tools for your use case and check their installation instructions, supported MISP versions, and required service subscriptions. Inclusion here describes functionality; it does not imply that every project has the same maintenance or support policy.

### Software within the MISP project

#### Core, enrichment, and conversion

| Project | Purpose |
| --- | --- |
| [MISP](https://github.com/MISP/MISP) | The core threat intelligence platform for sharing, correlating, and managing events, indicators, sightings, and contextual information. |
| [PyMISP](https://github.com/MISP/PyMISP) | The official Python client for the MISP REST API; also creates and manipulates MISP events and objects offline. |
| [misp-modules](https://github.com/MISP/misp-modules) | Enrichment, expansion, import, export, and workflow modules. Can also run independently of MISP through its API and web interface. |
| [misp-modules-cli](https://github.com/MISP/misp-modules-cli) | Command-line access to misp-modules. |
| [misp-stix](https://github.com/MISP/misp-stix) | The current Python library and command-line tools for conversion between MISP and STIX formats. |
| [cti-transmute](https://github.com/MISP/cti-transmute) | Web service for converting threat intelligence formats using misp-stix. |
| [MISP-Taxii-Server](https://github.com/MISP/MISP-Taxii-Server) | OpenTAXII configuration and supporting tools for exchanging MISP data through TAXII. Check the repository's supported protocol and dependencies before deployment. |
| [mail_to_misp](https://github.com/MISP/mail_to_misp) | Creates MISP events from email, principally through mail-server workflows such as Postfix. The older desktop mail-client integrations are unmaintained. |
| [misp-workbench](https://github.com/MISP/misp-workbench) | A standalone MISP-compatible analysis stack for ingesting feeds, searching indicators, and generating correlations, with a Python API and Vue frontend. |

#### Data models, validation, and knowledge bases

These resources can also be used by tools that do not run a MISP instance.

| Project | Purpose |
| --- | --- |
| [misp-taxonomies](https://github.com/MISP/misp-taxonomies) | Machine-readable taxonomies for classifying intelligence and applying consistent tags. |
| [misp-galaxy](https://github.com/MISP/misp-galaxy) | Contextual knowledge about threat actors, malware, techniques, tools, and other related entities. |
| [misp-objects](https://github.com/MISP/misp-objects) | Object templates and relationship definitions for structured intelligence. |
| [misp-warninglists](https://github.com/MISP/misp-warninglists) | Lists of common infrastructure and other values that help identify potential false positives. |
| [misp-noticelist](https://github.com/MISP/misp-noticelist) | Notices about legal, privacy, policy, and technical implications of particular attributes or objects. |
| [misp-decaying-models](https://github.com/MISP/misp-decaying-models) | Default models for decaying indicator relevance over time. |
| [misp-event-templates](https://github.com/MISP/misp-event-templates) | Reusable event templates for collecting consistently structured intelligence. |
| [misp-workflow-blueprints](https://github.com/MISP/misp-workflow-blueprints) | Reusable blueprints for MISP's built-in workflow engine. |
| [misp-feedback](https://github.com/MISP/misp-feedback) | Warninglist lookup engine with a daemon, HTTP/Unix-socket access, and command-line client. |
| [misp-validation](https://github.com/MISP/misp-validation) | Prototype rule format and runtimes for language-independent attribute normalization and validation. |
| [misp-engineering-bay](https://github.com/MISP/misp-engineering-bay) | Editors and supporting utilities for creating and validating MISP content and data structures. |
| [misp-global-search](https://github.com/MISP/misp-global-search) | Full-text search across MISP galaxies, objects, and taxonomies. |
| [threat-intelligence-browser](https://github.com/MISP/threat-intelligence-browser) | Browser for the MISP Galaxy threat intelligence knowledge base. |
| [threat-actor-intelligence-server](https://github.com/MISP/threat-actor-intelligence-server) | REST lookup of threat actors by name, synonym, or UUID using MISP Galaxy data. |

#### Libraries and MCP interfaces

| Project | Purpose |
| --- | --- |
| [RustMISP](https://github.com/MISP/RustMISP) | Rust client library for the MISP REST API. |
| [LuaMISP](https://github.com/MISP/LuaMISP) | Lua library for creating and manipulating MISP entities. |
| [PyTaxonomies](https://github.com/MISP/PyTaxonomies) | Python access to MISP taxonomies. |
| [PyMISPGalaxies](https://github.com/MISP/PyMISPGalaxies) | Python access to MISP Galaxy data. |
| [PyMISPWarningLists](https://github.com/MISP/PyMISPWarningLists) | Python access to MISP warninglists. |
| [PyMISPObjectTemplates](https://github.com/MISP/PyMISPObjectTemplates) | Python API for creating and updating MISP object templates. |
| [PyIntel471](https://github.com/MISP/PyIntel471) | Python client for Intel 471's API. |
| [misp-mcp](https://github.com/MISP/misp-mcp) | Model Context Protocol server providing read-only access to MISP events, attributes, objects, and reference data. |
| [misp-galaxy-mcp](https://github.com/MISP/misp-galaxy-mcp) | Model Context Protocol server for searching the MISP Galaxy knowledge base. |
| [ai-connector](https://github.com/MISP/ai-connector) | MISP AI module for event/report summarisation and related assistance; check its documentation for the required MISP feature branch and available use cases. |

#### Investigation, detection, and reporting

| Project | Purpose |
| --- | --- |
| [MISP-maltego](https://github.com/MISP/MISP-maltego) | Maltego transforms for MISP and exploration of MITRE ATT&CK data. |
| [misp-wireshark](https://github.com/MISP/misp-wireshark) | Wireshark plugin that exports selected packet data in MISP format. |
| [misp-ghidra](https://github.com/MISP/misp-ghidra) | Integration between Ghidra and MISP for reverse engineering workflows. |
| [bsimvis](https://github.com/MISP/bsimvis) | Binary similarity analysis and visualisation using Ghidra analyzers and BSim. |
| [evtx-toolkit](https://github.com/MISP/evtx-toolkit) | Reads Windows EVTX/Sysmon records and converts them to JSON, MISP objects, and graph data. |
| [misp-sighting-tools](https://github.com/MISP/misp-sighting-tools) | Generates sightings from sources such as network packet captures. |
| [misp-sighting-server](https://github.com/MISP/misp-sighting-server) | Standalone service for storing and looking up indicator sightings. |
| [wazuh-integration](https://github.com/MISP/wazuh-integration) | Wazuh rules and scripts for checking file hashes against MISP and optionally reporting sightings. |
| [misp-expansion](https://github.com/MISP/misp-expansion) | Firefox/Chrome extension for looking up selected text or page URLs in MISP. |
| [misp-dashboard](https://github.com/MISP/misp-dashboard) | Live overview of activity and intelligence from MISP instances. |
| [misp-grafana](https://github.com/MISP/misp-grafana) | Grafana dashboards using the MISP ZeroMQ stream and InfluxDB. |
| [widget-collection](https://github.com/MISP/widget-collection) | Additional widgets for MISP's built-in dashboards. |
| [misp-pandoc-filter](https://github.com/MISP/misp-pandoc-filter) | Work-in-progress Pandoc filter for turning MISP event reports into PDF documents. |
| [misp-playbooks](https://github.com/MISP/misp-playbooks) | Jupyter-based operational playbooks using PyMISP for analysis, enrichment, and response. |
| [matrix-misp-bot](https://github.com/MISP/matrix-misp-bot) | Basic MISP bot for Matrix. |
| [misp-opendata](https://github.com/MISP/misp-opendata) | Publishes and manages metadata for MISP-backed datasets on open-data portals. |
| [misp-takedown](https://github.com/MISP/misp-takedown) | Generates takedown notifications through RT/RTIR from MISP events. |
| [yara-misp](https://github.com/MISP/yara-misp) | Exports MISP attributes as YARA rules. |
| [yara-exporter](https://github.com/MISP/yara-exporter) | MISP-hosted fork of the YARA exporter for THOR-compatible scanning rules. |

#### Deployment, administration, and testing

| Project | Purpose |
| --- | --- |
| [misp-docker](https://github.com/MISP/misp-docker) | Official Docker deployment for MISP and its associated services. |
| [MISP-RPM](https://github.com/MISP/MISP-RPM) | RPM packaging for MISP. |
| [misp-airgap](https://github.com/MISP/misp-airgap) | Deployment and maintenance in air-gapped environments using LXD. |
| [MISP-Fleet-Commander](https://github.com/MISP/MISP-Fleet-Commander) | Web application for managing MISP instances and communities. |
| [MISP-Fleet-Commander-Browser-Extension](https://github.com/MISP/MISP-Fleet-Commander-Browser-Extension) | Registers MISP instances in Fleet Commander from the browser. |
| [misp-guard](https://github.com/MISP/misp-guard) | Proxy addon for applying rules to MISP synchronisation traffic. |
| [misp-bump](https://github.com/MISP/misp-bump) | Exchanges MISP synchronisation setup information using encrypted QR codes. |
| [misp-monitoring](https://github.com/MISP/misp-monitoring) | Monitoring utilities and operational documentation for MISP servers. |
| [misp-usage-statistics](https://github.com/MISP/misp-usage-statistics) | Collects and visualises MISP usage statistics. |
| [MISP-sizer](https://github.com/MISP/MISP-sizer) | Hardware sizing calculator for MISP deployments. |
| [ansible](https://github.com/MISP/ansible) | Ansible installation scripts; review supported operating systems and MISP versions. |
| [misp-packer](https://github.com/MISP/misp-packer) | Packer-based virtual machine image builder; its documented image targets Ubuntu 18.04. |
| [misp-cloud](https://github.com/MISP/misp-cloud) | Cloud image generation, with AWS support documented in the repository. |
| [misp-vagrant](https://github.com/MISP/misp-vagrant) | Vagrant deployment definitions for MISP project software. |
| [misp-synchronisation](https://github.com/MISP/misp-synchronisation) | Deploys multiple instances and tests their synchronisation behaviour. |
| [misp_dockerized_testing](https://github.com/MISP/misp_dockerized_testing) | Earlier Docker-based infrastructure for testing MISP instances. |
| [misp-stix-tests](https://github.com/MISP/misp-stix-tests) | STIX fixtures for testing conversion libraries. |
| [dockerized_training_environment](https://github.com/MISP/dockerized_training_environment) | Container-based MISP training environment. |
| [mail_to_misp_test](https://github.com/MISP/mail_to_misp_test) | Email fixtures for testing mail_to_misp. |
| [pCraft](https://github.com/MISP/pCraft) | Generates PCAPs from scripted scenarios for testing and exercises. |
| [cexf](https://github.com/MISP/cexf) | Common Exercise Format for describing exercise injects and scenarios. |
| [Synthetic-Exercise-World-Format](https://github.com/MISP/Synthetic-Exercise-World-Format) | Structured fictional countries, organisations, sectors, and threat actors for neutral exercises and CTI examples. |

#### Experimental and historical tools

These repositories document earlier implementations or research approaches. Review their dependencies and compatibility before using them with a current MISP deployment.

| Project | Purpose and context |
| --- | --- |
| [vintage-misp-workbench](https://github.com/MISP/vintage-misp-workbench) | Original database export and correlation workbench. The current standalone analysis application is [misp-workbench](https://github.com/MISP/misp-workbench). |
| [MISP-STIX-Converter](https://github.com/MISP/MISP-STIX-Converter) | Earlier MISP/STIX synchronisation implementation. Use [misp-stix](https://github.com/MISP/misp-stix) for the current conversion library. |
| [MISPego](https://github.com/MISP/MISPego) | Earlier Maltego transforms for adding entities to MISP events; also see MISP-maltego above. |
| [docker-misp](https://github.com/MISP/docker-misp) | Archived Docker implementation; its README directs users to misp-docker. |
| [x_old_misp_docker](https://github.com/MISP/x_old_misp_docker) | Older Docker implementation retained separately from misp-docker. |
| [misp-graph](https://github.com/MISP/misp-graph) | Graphviz/GEXF export from MISP XML, with legacy Python dependencies. |
| [data-processing](https://github.com/MISP/data-processing) | Scripts for extracting and correlating intelligence from MISP data exports. |
| [misp-search](https://github.com/MISP/misp-search) | Command-line MISP search implementation hosted as a fork. |
| [misp-bloomfilter](https://github.com/MISP/misp-bloomfilter) | Builds Bloom filters from MISP XML exports; consult its documented limitations on indicator confidentiality. |
| [misp-privacy-aware-exchange](https://github.com/MISP/misp-privacy-aware-exchange) and [pypraware](https://github.com/MISP/pypraware) | Research implementation and Python support for privacy-aware indicator exchange. |
| [sacti](https://github.com/MISP/sacti) | MISP-hosted fork for securely aggregating and reporting sightings. |
| [misp-darwin](https://github.com/MISP/misp-darwin) | Work-in-progress rules for translating structured MISP intelligence into human-readable reports. |

#### Specifications, training, and supporting repositories

| Resource | Purpose |
| --- | --- |
| [misp-rfc](https://github.com/MISP/misp-rfc) and [misp-standard.org](https://github.com/MISP/misp-standard.org) | MISP format specifications and the standards website. |
| [misp-book](https://github.com/MISP/misp-book) | User and administrator guide. |
| [misp-training](https://github.com/MISP/misp-training) and [misp-training-lea](https://github.com/MISP/misp-training-lea) | General training and material for law enforcement/CSIRT information sharing. |
| [MISP-presentations](https://github.com/MISP/MISP-presentations) | Presentations about MISP. |
| [best-practices-in-threat-intelligence](https://github.com/MISP/best-practices-in-threat-intelligence) | Guidance for threat intelligence operations. |
| [misp-compliance](https://github.com/MISP/misp-compliance) | Legal, policy, and procedural templates for operating sharing communities. |
| [misp-iconify](https://github.com/MISP/misp-iconify) and [intelligence-icons](https://github.com/MISP/intelligence-icons) | Icons and visual material for intelligence sharing. |
| [misp-website](https://github.com/MISP/misp-website) | Source of this website. |
| [cakephp](https://github.com/MISP/cakephp), [sachertortephp](https://github.com/MISP/sachertortephp), and [Cake-Resque](https://github.com/MISP/Cake-Resque) | Framework and background-job dependencies used by MISP. |
| [cti-python-stix2](https://github.com/MISP/cti-python-stix2) | MISP's fork of the Python STIX 2 library. |
| [cti-toolkit](https://github.com/MISP/cti-toolkit) | MISP-hosted fork of the CERT Australia CTI Toolkit. |
| [nginx-proxy](https://github.com/MISP/nginx-proxy) | MISP-hosted fork of a Docker reverse proxy. |
| [SimpleQueue](https://github.com/MISP/SimpleQueue) | Experimental multiprocessing queue implementation extracted from AIL. |
| [pdf_fonts](https://github.com/MISP/pdf_fonts) | Fonts for PyMISP PDF export. |
| [SwiftCodes](https://github.com/MISP/SwiftCodes) | MISP-hosted fork of a bank identifier dataset. |

The [MISP organisation's repository directory](https://github.com/orgs/MISP/repositories) is the authoritative inventory for new projects and repository status.

### CIRCL projects and services

CIRCL develops MISP and a wider set of security tools and services. Projects have their own requirements; some integrate directly with MISP, while others support investigation, enrichment, or incident response alongside it. MISP projects are listed above to avoid duplicating them here.

| Project or service | Purpose and relationship to MISP |
| --- | --- |
| [AIL](https://github.com/ail-project/ail-framework) | Analysis of information leaks, with MISP event/object export. The current project is in the ail-project organisation. |
| [Flowintel](https://github.com/Flowintel/flowintel) | Investigation and case management with MISP taxonomies/galaxies, enrichment through misp-modules, and MISP export. |
| [Lookyloo](https://github.com/Lookyloo/lookyloo) | Captures websites and visualises their relationships; can look up indicators in MISP and export captures as MISP events. |
| [Lacus](https://github.com/ail-project/lacus) | Browser capture service using Playwright, usable by other analysis applications. |
| [Pandora](https://github.com/pandora-analysis/pandora) | Document and file analysis platform for examining suspicious submissions. |
| [Vulnerability-Lookup](https://github.com/vulnerability-lookup/vulnerability-lookup) | Aggregates vulnerability information and community observations. MISPSight transfers vulnerability sightings from MISP. |
| [cve-search](https://github.com/cve-search/cve-search) | Local vulnerability search and API, accessible through MISP enrichment modules. |
| [hashlookup](https://github.com/hashlookup/hashlookup-server) | Known-file hash lookup for identifying legitimate files and reducing noise during investigations. |
| [D4](https://github.com/D4-project/d4-core) | Distributed sensor and analysis framework for collecting security observations. |
| [BGP Ranking](https://github.com/D4-project/BGP-Ranking) | Ranks autonomous systems using observed malicious activity. |
| [IPASN History](https://github.com/D4-project/IPASN-History) | Historical IP-to-ASN lookup for investigating network infrastructure. |
| [CIRCL Passive DNS](https://circl.lu/services/passive-dns/) | Historical DNS observations for domains and IP addresses; available through misp-modules and [PyPDNS](https://github.com/CIRCL/PyPDNS). |
| [CIRCL Passive SSL](https://circl.lu/services/passive-ssl/) | Observed TLS certificates and associated infrastructure, with MISP enrichment support. |
| [CIRCLean](https://github.com/CIRCL/Circlean) | USB document sanitisation, with the [PyCIRCLean](https://github.com/CIRCL/PyCIRCLean) library and [image builder](https://github.com/CIRCL/circlean-pi-gen). |
| [URL Abuse](https://github.com/CIRCL/url-abuse) | URL review, investigation, and abuse reporting; also used by misp-takedown. |
| [Email Abuse](https://github.com/CIRCL/email-abuse) | Email review and abuse reporting. |
| [Douglas-Quaid](https://github.com/CIRCL/douglas-quaid) | Image similarity, correlation, and analysis; [Carl-Hauser](https://github.com/CIRCL/carl-hauser) provides a related testing framework. |
| [Drone Forensic](https://github.com/CIRCL/Drone-Forensic) | Digital forensic resources and tooling for drones and UAVs. |
| [CIRCL forensic tools](https://github.com/CIRCL/forensic-tools) | Utilities for system forensic investigations. |
| [Factual Rules Generator](https://github.com/CIRCL/factual-rules-generator) and [Factual Rules](https://github.com/CIRCL/factual-rules) | Generates and publishes YARA rules for identifying legitimate installed software in forensic acquisitions. |
| [ELF Insight](https://github.com/CIRCL/elfinsight) | Collects and aggregates information about ELF binaries. |
| [ASN Description History](https://github.com/CIRCL/ASN-Description-History) | Tracks changes in autonomous-system descriptions. |
| [CIRCL threat intelligence workshop](https://github.com/CIRCL/circl-threat-intel-workshop) | Hands-on notebooks for learning to use CIRCL tools and services. |

See the [CIRCL projects directory](https://circl.lu/projects/) and [CIRCL repositories](https://github.com/CIRCL) for project documentation and related utilities. Access conditions for hosted services are documented on their service pages.

### MISP enrichment, import, and export modules

The [misp-modules documentation](https://misp.github.io/misp-modules/) and [repository](https://github.com/MISP/misp-modules) provide the module catalog, configuration, and dependencies. Consult that catalog instead of relying on a fixed list of individual Python files, which changes as integrations evolve.

* **Enrichment and expansion:** passive DNS/SSL, vulnerability lookup, hash reputation, sandbox results, geolocation, and other contextual sources.
* **Import:** external intelligence formats, email, documents, and analysis reports.
* **Export:** supported intelligence and reporting formats.
* **Workflow actions:** modules used by MISP's automation workflows.

Some modules require a separate account, API key, paid service plan, or local dependency. Enable the modules appropriate to your deployment.

### Third-party integrations

These tools are developed by their respective communities or vendors. Check upstream documentation for the current integration, supported API, and product licensing.

#### Incident response, threat intelligence, and automation

| Tool | MISP integration |
| --- | --- |
| [TheHive](https://docs.strangebee.com/) | Incident response platform with MISP integration. Current versions are distributed by StrangeBee; the former public TheHive 3/4 repositories are no longer maintained or distributed. |
| [Cortex MISP analyzer](https://github.com/TheHive-Project/Cortex-Analyzers/tree/master/analyzers/MISP) | Looks up observables in MISP from Cortex analysis workflows. |
| [OpenCTI MISP connector](https://github.com/OpenCTI-Platform/connectors/tree/master/external-import/misp) | Imports MISP threat intelligence into OpenCTI. |
| [IntelMQ](https://github.com/certtools/intelmq) | Collects, processes, and exchanges security feeds, including MISP input/output bots. |
| [Rapid7 InsightConnect](https://github.com/rapid7/insightconnect-plugins/tree/master/plugins/misp) | MISP actions and triggers for automation workflows. |
| [RTIR MISP extension](https://github.com/bestpractical/rtir-extension-misp) | Connects RTIR incident handling with MISP. |
| [EclecticIQ](https://www.eclecticiq.com/) | Threat intelligence platform; consult the vendor's current MISP connector documentation. |
| [Hybrid Analysis](https://www.hybrid-analysis.com/) | Analysis reports and intelligence export in MISP format. |
| [Joe Sandbox](https://www.joesecurity.org/) | Sandbox analysis with MISP-format output and integration. |

#### SIEM, detection, and hunting

| Tool | MISP integration |
| --- | --- |
| [Elastic MISP integration](https://github.com/elastic/integrations/tree/main/packages/ti_misp) | Ingests threat intelligence through Elastic Agent. This is the current integration rather than the former standalone Filebeat MISP module. |
| [misp42splunk](https://github.com/remg427/misp42splunk) | Retrieves MISP intelligence in Splunk and sends data back through alert actions. Also available on [Splunkbase](https://splunkbase.splunk.com/app/4335/). |
| [TA-misp](https://github.com/stricaud/TA-misp) | Splunk technology add-on for matching local data against MISP objects/attributes. |
| [misp2sentinel](https://github.com/cudeso/misp2sentinel) | Exports indicators to Microsoft Sentinel using the STIX objects Upload Indicators API. The repository's older Microsoft Graph approach is deprecated. |
| [Dovehawk](https://github.com/tylabs/dovehawk) | Zeek intelligence integration that retrieves indicators from MISP and reports sightings. |
| [misp_to_zeek](https://github.com/cudeso/misp_to_zeek) | Exports MISP indicators to Zeek's intelligence framework. |
| [surimisp](https://github.com/StamusNetworks/surimisp) | Matches MISP indicators against Suricata events. |
| [pymisp-suricata_search](https://github.com/raw-data/pymisp-suricata_search) | Retrieves MISP attributes and generates Suricata rules. |
| [sigmai](https://github.com/0xThiebaut/sigmai) | Generates Sigma rules from MISP indicators. For storing and exchanging existing Sigma rules, MISP also has native Sigma support. |
| [MISP2CbR](https://github.com/eCrimeLabs/MISP2CbR) | Converts MISP intelligence into a Carbon Black Response threat feed. Check compatibility with your product version. |
| [MISP CrowdStrike scripts](https://github.com/aacgood/MISP-Integrations) | Scripts for exporting MISP indicators to CrowdStrike; review the supported CrowdStrike API before use. |

#### Collection and analyst utilities

| Tool | MISP integration |
| --- | --- |
| [misp-scraper](https://github.com/cudeso/misp-scraper) | Creates MISP events and reports from web pages; also used by the zsazsa CTI platform. |
| [phish2MISP](https://github.com/eCrimeLabs/phish2MISP) | Collects information about phishing URLs and adds it to MISP. |
| [vt2misp](https://github.com/eCrimeLabs/vt2misp) | Adds VirusTotal results to MISP events as objects. |
| [ja3toMISP](https://github.com/eCrimeLabs/ja3toMISP) | Extracts JA3 fingerprints from PCAPs and adds them as MISP objects. |
| [misp_btc](https://github.com/rommelfs/misp_btc) | Retrieves Bitcoin addresses from MISP and enriches them with transaction information. |
| [misp-bulk-tag](https://github.com/morallo/misp-bulk-tag) | Applies tags in bulk through the MISP API. |
| [MISP-PurgeEvents](https://github.com/eCrimeLabs/MISP-PurgeEvents) | Administration script for deleting selected events. Review its cleanup instructions before use. |
| [MISP-IOC-Validator](https://github.com/tom8941/MISP-IOC-Validator) | Validates indicator formats and compares values with known false positives. |
| [MISP-Extractor](https://github.com/PidgeyL/MISP-Extractor) | Retrieves intelligence and automates operations through the MISP API. |
| [misp-extractor](https://github.com/00gxd14g/misp-extractor) | Exports selected attribute types to separate files. |
| [BTG](https://github.com/conix-security/BTG) | IOC search tool with MISP collection support. |
| [threatingestor](https://pypi.org/project/threatingestor/) | Extracts and aggregates indicators from feeds, including MISP output support. |
| [ThreatPinchLookup](https://github.com/cloudtracer/ThreatPinchLookup) | Browser-based indicator lookup with a MISP connector; check browser compatibility. |

#### Other API libraries

Use [PyMISP](https://github.com/MISP/PyMISP) for the official Python API client. Alternative clients expose different subsets of the MISP API.

| Library | Language and scope |
| --- | --- |
| [golang-misp](https://github.com/0xrawsec/golang-misp) | Go library focused on MISP search. |
| [mispex](https://github.com/FloatingGhost/mispex) | Elixir wrapper for the MISP HTTP API. |
| [mispy](https://github.com/airbus-cert/mispy) | Alternative Python interface to MISP. |

#### Archived integrations and older examples

These links are retained for users maintaining existing integrations. Archived projects do not receive upstream updates; older examples can depend on historical MISP or vendor APIs.

| Integration | Status or compatibility context |
| --- | --- |
| [misp-rb](https://github.com/ninoseki/misp-rb) | Archived Ruby API wrapper. |
| [DCSO tie2misp](https://github.com/DCSO/tie2misp) | Archived importer for DCSO TIE intelligence. |
| [otx_misp](https://github.com/gcrahay/otx_misp) | Archived OTX importer; also consult the OTX module in misp-modules. |
| [CERT Australia CTI Toolkit](https://github.com/Cosive/cti-toolkit) | Archived toolkit containing STIX/MISP conversion tools. |
| [CERT-Bund yara-exporter](https://github.com/CERT-Bund/yara-exporter) | Archived upstream YARA exporter; a MISP-hosted fork is listed above. |
| [LOKI](https://github.com/Neo23x0/Loki) | The Python scanner and its MISP receiver are deprecated upstream. Follow the repository's successor guidance; do not assume identical MISP integration in the successor. |
| [Cuckoo modified](https://github.com/spender-sandbox/cuckoo-modified) | Earlier sandbox fork with a MISP reporting module. Review its runtime requirements before using it. |
| [Automated Payload Test Controller](https://github.com/jymcheong/aptc) | Earlier PyMISP-based payload testing scripts with version-specific installation instructions. |
| [FireMISP](https://github.com/jaegeral/FireMISP) | FireEye alert import scripts, moved from the former deralexxx repository. |
| [PySight2MISP](https://github.com/jaegeral/PySight2MISP) | Historical FireEye/iSight API integration. |
| [misp-to-autofocus](https://github.com/PaloAltoNetworks/misp-to-autofocus) | Converts MISP intelligence to Autofocus queries; check availability of the target service. |
| [MISP-MVISION-EDR](https://github.com/mohlcyber/MISP-MVISION-EDR) | Older McAfee MVISION EDR/OpenDXL integration, formerly linked as MISP-MAR. |
| [OpenDXL-ATD-MISP](https://github.com/mohlcyber/OpenDXL-ATD-MISP) | Older McAfee ATD/OpenDXL collection workflow. |
| [OpenDXL-MISP-IntelMQ-Output](https://github.com/mohlcyber/OpenDXL-MISP-IntelMQ-Output) | Earlier IntelMQ/OpenDXL bridge for MISP intelligence. |
| [misp-to-sentinel Azure Function](https://github.com/zolderio/misp-to-sentinel) | Earlier integration based on Microsoft's Graph security API. For the STIX objects Upload Indicators API, see misp2sentinel above. |

### Keeping this directory current

The [MISP repositories](https://github.com/orgs/MISP/repositories), [CIRCL projects](https://circl.lu/projects/), and [misp-modules catalog](https://github.com/MISP/misp-modules) are the primary sources for this directory. Check those sources and each integration's upstream documentation when choosing a tool or contributing an update.
