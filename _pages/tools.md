---
layout: page
title: Tools
permalink: /tools/
toc: true
---

## Software and Tools

Many open source and proprietary tools integrate MISP support (MISP format or API) in order to extend their tools
or MISP itself. A series of additional software are supported and handled by the [MISP project](https://www.github.com/MISP).
The additional software supported by the MISP project allow the community to rely on additional tools to support their day-to-day operations. The objective
is also to explore new ideas, concepts or functionality which can be integrated in MISP core software later on.

### Software within the MISP project


* [misp-modules](https://github.com/MISP/misp-modules) - Modules for expansion services in MISP

#### Expansion modules

* [ASN History](https://github.com/MISP/misp-modules/modules/expansion/asn_history.py) - a hover and expansion module to expand an AS number with the ASN description and its history.
* [CIRCL Passive DNS](https://github.com/MISP/misp-modules/modules/expansion/circl_passivedns.py) - a hover and expansion module to expand hostname and IP addresses with passive DNS information.
* [CIRCL Passive SSL](https://github.com/MISP/misp_modules/modules/expansion/circl_passivessl.py) - a hover and expansion module to expand IP addresses with the X.509 certificate seen.
* [countrycode](https://github.com/MISP/misp_modules/modules/expansion/countrycode.py) - a hover module to tell you what country a URL belongs to.
* [CrowdStrike Falcon](https://github.com/MISP/misp_modules/modules/expansion/crowdstrike_falcon.py) - an expansion module to expand using CrowdStrike Falcon Intel Indicator API.
* [CVE](https://github.com/MISP/misp_modules/modules/expansion/cve.py) - a hover module to give more information about a vulnerability (CVE).
* [DNS](https://github.com/MISP/misp_modules/modules/expansion/dns.py) - a simple module to resolve MISP attributes like hostname and domain to expand IP addresses attributes.
* [DomainTools](https://github.com/MISP/misp_modules/modules/expansion/domaintools.py) - a hover and expansion module to get information from [DomainTools](http://www.domaintools.com/) whois.
* [EUPI](https://github.com/MISP/misp_modules/modules/expansion/eupi.py) - a hover and expansion module to get information about an URL from the [Phishing Initiative project](https://phishing-initiative.eu/?lang=en).
* [Farsight DNSDB Passive DNS](https://github.com/MISP/misp_modules/modules/expansion/farsight_passivedns.py) - a hover and expansion module to expand hostname and IP addresses with passive DNS information.
* [GeoIP](https://github.com/MISP/misp_modules/modules/expansion/geoip_country.py) - a hover and expansion module to get GeoIP information from geolite/maxmind.
* [IPASN](https://github.com/MISP/misp_modules/modules/expansion/ipasn.py) - a hover and expansion to get the BGP ASN of an IP address.
* [iprep](https://github.com/MISP/misp-modules/modules/expansion/iprep.py) - an expansion module to get IP reputation from packetmail.net.
* [OTX](https://github.com/MISP/misp_modules/modules/expansion/otx.py) - an expansion module for [OTX](https://otx.alienvault.com/).
* [passivetotal](https://github.com/MISP/misp_modules/modules/expansion/passivetotal.py) - a [passivetotal](https://www.passivetotal.org/) module that queries a number of different PassiveTotal datasets.
* [rbl](https://github.com/MISP/misp_modules/modules/expansion/rbl.py) - a module to get RBL (Real-Time Blackhost List) values from an attribute.
* [shodan](https://github.com/MISP/misp_modules/modules/expansion/shodan.py) - a minimal [shodan](https://www.shodan.io/) expansion module.
* [sourcecache](https://github.com/MISP/misp_modules/modules/expansion/sourcecache.py) - a module to cache a specific link from a MISP instance.
* [ThreatCrowd](https://github.com/MISP/misp_modules/modules/expansion/threatcrowd.py) - an expansion module for [ThreatCrowd](https://www.threatcrowd.org/).
* [threatminer](https://github.com/MISP/misp_modules/modules/expansion/threatminer.py) - an expansion module to expand from [ThreatMiner](https://www.threatminer.org/).
* [virustotal](https://github.com/MISP/misp_modules/modules/expansion/virustotal.py) - an expansion module to pull known resolutions and malware samples related with an IP/Domain from virusTotal (this modules require a VirusTotal private API key)
* [wikidata](https://github.com/MISP/misp_modules/modules/expansion/wiki.py) - a [wikidata](https://www.wikidata.org) expansion module.
* [xforce](https://github.com/MISP/misp_modules/modules/expansion/xforceexchange.py) - an IBM X-Force Exchange expansion module.
* [YARA syntax validator](https://github.com/MISP/misp_modules/modules/expansion/yara_syntax_validator.py) - YARA syntax validator.

#### Export modules

* [CEF](https://github.com/MISP/misp_modules/modules/export_mod/cef_export.py) module to export Common Event Format (CEF).
* [GoAML export](https://github.com/MISP/misp_modules/modules/export_mod/goamlexport.py) module to export in GoAML format.
* [Lite Export](https://github.com/MISP/misp_modules/modules/export_mod/liteexport.py) module to export a lite event.
* [Simple PDF export](https://github.com/MISP/misp_modules/modules/export_mod/pdfexport.py) module to export in PDF (required: asciidoctor-pdf).
* [ThreatConnect](https://github.com/MISP/misp_modules/modules/export_mod/threat_connect_export.py) module to export in ThreatConnect CSV format.
* [ThreatStream](https://github.com/MISP/misp_modules/modules/export_mod/threatStream_misp_export.py) module to export in ThreatStream format.

#### Import modules

* [CSV import](https://github.com/MISP/misp_modules/modules/import_mod/csvimport.py) Customizable CSV import module.
* [Cuckoo JSON](https://github.com/MISP/misp_modules/modules/import_mod/cuckooimport.py) Cuckoo JSON import.
* [Email Import](https://github.com/MISP/misp_modules/modules/import_mod/email_import.py) Email import module for MISP to import basic metadata.
* [OCR](https://github.com/MISP/misp_modules/modules/import_mod/ocr.py) Optical Character Recognition (OCR) module for MISP to import attributes from images, scan or faxes.
* [OpenIOC](https://github.com/MISP/misp_modules/modules/import_mod/openiocimport.py) OpenIOC import based on PyMISP library.
* [stiximport](https://github.com/MISP/misp_modules/modules/import_mod/stiximport.py) - An import module to process STIX xml/json.
* [ThreatAnalyzer](https://github.com/MISP/misp_modules/modules/import_mod/threatanalyzer_import.py) - An import module to process ThreatAnalyzer archive.zip/analysis.json sandbox exports.
* [VMRay](https://github.com/MISP/misp_modules/modules/import_mod/vmray_import.py) - An import module to process VMRay export.

* [misp-workbench](https://github.com/MISP/misp-workbench) - Tools to export data out of the MISP MySQL database and use and abuse them outside of this platform.
* [MISpego](https://github.com/MISP/MISPego) - Maltego Transform to put entities into MISP events.
* [MISP-maltego](https://github.com/MISP/MISP-maltego) - Set of Maltego transforms to inferface with a MISP instance.
* [PyMISP](https://github.com/CIRCL/PyMISP) - Python library using the MISP Rest API. This is the official library for MISP and can also generate offline MISP events.
* [MISP-STIX-Converter](https://github.com/MISP/MISP-STIX-Converter) -  An utility repo to assist with converting between MISP and STIX formats.
* [MISP-Taxii-Server](https://github.com/MISP/MISP-Taxii-Server) - An OpenTAXII Configuration for MISP with automatic TAXII to MISP sync.
* [mail_to_misp](https://github.com/MISP/mail_to_misp) - Connect your mail client/infrastructure to MISP in order to create events based on the information contained within mails.

For the additional software created by the MISP project, check our [MISP project organization](https://github.com/MISP/).

### Software or Services with MISP support or Extending MISP functionalities

* [Viper](http://www.viper.li/) - is a binary management and analysis framework dedicated to malware and exploit researchers including a MISP module.
* [cve-search](https://github.com/cve-search) - a tool to perform local searches for known vulnerabilities include a [MISP plug-in](https://github.com/cve-search/Plugins/tree/master/plugins/plugins/MISP).
* [Cuckoo modified](https://github.com/spender-sandbox/cuckoo-modified) - heavily modified version of Cuckoo Sandbox including a [MISP reporting module](https://github.com/spender-sandbox/cuckoo-modified/blob/master/modules/reporting/misp.py) to put the information into a MISP instance.
* [Hybrid analysis](https://www.hybrid-analysis.com/) exports in MISP format.
* [Joe Sanbox](https://www.joesecurity.org/) outputs analysis in MISP format.
* [Loki - Simple IOC Scanner](https://github.com/Neo23x0/Loki) includes a MISP receiver.
* [MISP-Extractor](https://github.com/PidgeyL/MISP-Extractor) extracts information from MISP via the API and automate some tasks.
* [IntelMQ](https://github.com/certtools/intelmq) support MISP to retrieve events and update tags.
* [misp-to-autofocus](https://github.com/PaloAltoNetworks/misp-to-autofocus) - script for pulling events from a MISP database and converting them to Autofocus queries.
* [otx_misp](https://github.com/gcrahay/otx_misp/) imports Alienvault OTX pulses to a MISP instance.
* [FireMISP](https://github.com/deralexxx/FireMISP) FireEye Alert json files to MISP Malware information sharing platform (Alpha).
* [cti-toolkit](https://github.com/certau/cti-toolkit)  CERT Australia Cyber Threat Intelligence (CTI) Toolkit includes a transform to MISP from STIX.
* [MISP-IOC-Validator](https://github.com/tom8941/MISP-IOC-Validator/) validates the format of the different IOC from MISP and to remove false positive by comparing these IOC to existing known false positive.
* [TheHive](https://thehive-project.org/) A 3-in-1 Security Incident Response Platform has an extensive MISP support.
* [yara-exporter](https://github.com/BSI-CERT-Bund/yara-exporter) - Exporting MISP event attributes to yara rules usable with Thor apt scanner.
* [tie2misp](https://github.com/DCSO/tie2misp) - Import DCSO TIE IOCs as MISP events.
* [misp-takedown](https://github.com/rommelfs/misp-takedown) - A curses-style interface for automatic takedown notification based on MISP events.
* [OpenDXL-ATD-MISP](https://github.com/mohl1/OpenDXL-ATD-MISP) - Automated threat intelligence collection with McAfee ATD, OpenDXL and MISP.
* [OpenDXL-MISP-IntelMQ-Output](https://github.com/mohl1/OpenDXL-MISP-IntelMQ-Output) - This use case is focusing on the automated real-time threat sharing with MISP (Malware Intelligence Sharing Platform), orchestration tool (IntelMQ) and OpenDXL. IntelMQ is used to collect data from the Malware Intelligence Sharing Platform (MISP), to parse and push intelligence via OpenDXL.
* [BTG](https://github.com/conix-security/BTG) - BTG's purpose is to make fast and efficient search on IOC  including a MISP crawler and collector.
* [ThreatPinchLookup](https://github.com/cloudtracer/ThreatPinchLookup)  - ThreatPinch Lookup creates informational tooltips when hovering oven an item of interest on any website and contains a MISP connector.
* [Automated Payload Test Controller](https://github.com/jymcheong/aptc) - A set of scripts using PyMISP to extend MISP for automated payload testing.
* [MISP Golang](https://github.com/0xrawsec/golang-misp) - Golang Library to interact with your MISP instance.
* [misp-bulk-tag](https://github.com/morallo/misp-bulk-tag) - this script performs bulk tagging operations over MISP.
* [polarity MISP integration](https://github.com/polarityio/misp) - The Polarity MISP integration allows Polarity to search your instance of MISP to return valid information about domains, IPS, and hashes.
* [AIL framework - Framework for Analysis of Information Leaks](https://github.com/CIRCL/AIL-framework) - AIL framework - Framework for Analysis of Information Leaks use MISP to share  found leaks within a threat intelligence platform using MISP standard (objects).
* [Splunk integration with MISP](https://github.com/stricaud/TA-misp) - This TA allows to check if objects/attributes in your MISP instance matches your data in Splunk.
* [pymisp-suricata_search](https://github.com/raw-data/pymisp-suricata_search) - Multi-threaded Suricata search module for MISP.
* [misp42splunk](https://github.com/remg427/misp42splunk) - A Splunk app to use MISP in background.
* [Integration between MISP platform and McAfee Active Response](https://github.com/mohlcyber/MISP-MAR) - McAfee Active Response integration with MISP.


