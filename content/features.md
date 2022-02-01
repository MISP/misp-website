
---
title: MISP features and functionalities
aliases:
    - /features.html
---
## Features of MISP, the open source threat sharing platform. 
A threat intelligence platform for sharing, storing and correlating Indicators of Compromise of targeted attacks, threat intelligence, financial fraud information, vulnerability information or even counter-terrorism information. Discover how MISP is used today in multiple organisations. Not only to store, share, collaborate on cyber security indicators, malware analysis, but also to use the IoCs and information to detect and prevent attacks, frauds or threats against ICT infrastructures, organisations or people.</header>

![](/img/banner.jpg "{ class='img-responsive'}") 
* An **efficient IoC and indicators** database allowing to store technical and non-technical information about malware samples, incidents, attackers and intelligence. 
* Automatic **correlation** finding relationships between attributes and indicators from malware, attacks campaigns or analysis. Correlation engine includes correlation between attributes and more advanced correlations like Fuzzy hashing correlation (e.g. ssdeep) or CIDR block matching. Correlation can be also enabled or event disabled per attribute. 
* A flexible data model where complex [objects](/objects.html) can be expressed and [linked together](/objects.html#_relationships) to express threat intelligence, incidents or connected elements. 
* Built-in **sharing functionality** to ease data sharing using different model of distributions. MISP can synchronize automatically events and attributes among different MISP. Advanced filtering functionalities can be used to meet each organization sharing policy including a **flexible sharing group** capacity and an attribute level distribution mechanisms.
* An **intuitive user-interface** for end-users to create, update and collaborate on events and attributes/indicators. A **graphical interface** to navigate seamlessly between events and their correlations. An **event graph** functionality to create and view relationships between objects and attributes. Advanced filtering functionalities and [warning list](https://github.com/MISP/misp-warninglists) to help the analysts to contribute events and attributes.
* **storing data** in a structured format (allowing automated use of the database for various purposes) with an extensive support of cyber security indicators along fraud indicators as in the financial sector.
* **export**: generating IDS (Suricata, Snort and Bro are supported by default), OpenIOC, plain text, CSV, MISP XML or JSON output to integrate with other systems (network IDS, host IDS, custom [tools](/tools)
* **import**: bulk-import, batch-import, free-text import, import from OpenIOC, GFI sandbox, ThreatConnect CSV or MISP format.
* Flexible **free text import** tool to ease the integration of unstructured reports into MISP.
* A gentle system to **collaborate** on events and attributes allowing MISP users to propose changes or updates to attributes/indicators.
* **data-sharing**: automatically exchange and synchronization with other parties and trust-groups using MISP.
* **feed import**: flexible tool to import and integrate MISP [feed](/feeds/) and any threatintel or OSINT feed from third parties. Many [default feeds](/feeds/) are included in standard MISP installation.
* **delegating of sharing**: allows a simple pseudo-anonymous mechanism to delegate publication of event/indicators to another organization.
* Flexible **API** to integrate MISP with your own solutions. MISP is bundled with [PyMISP](https://github.com/MISP/PyMISP) which is a flexible Python Library to fetch, add or update events attributes, handle malware samples or search for attributes.
* **adjustable taxonomy** to classify and tag events following your own classification schemes or [existing taxonomies](https://github.com/MISP/misp-taxonomies). The taxonomy can be local to your MISP but also shareable among MISP instances. MISP comes with a default set of well-known [taxonomies and classification schemes](/taxonomies.html) to support standard classification as used by ENISA, Europol, DHS, CSIRTs or many other organisations.
* **intelligence vocabularies** called MISP galaxy and bundled with existing [threat actors, malware, RAT, ransomware or MITRE ATT&CK](galaxy.html) which can be easily linked with events in MISP.
* **[expansion modules](https://misp.github.io/misp-modules/) in Python** to expand MISP with your own services or activate already available [misp-modules](https://github.com/MISP/misp-modules).
* **sighting support** to get observations from organizations concerning shared indicators and attributes. Sighting [can be contributed](https://www.circl.lu/doc/misp/automation/index.html#sightings-api) via MISP user-interface, API as MISP document or STIX sighting documents. Starting with MISP 2.4.66, [Sighting has been extended](/2017/02/16/Sighting-The-Next-Level.html) to support false-negative sighting or expiration sighting.
* **STIX support**: export data in the STIX format (XML and JSON) including export/import in STIX 2.0 format.
* **integrated encryption and signing of the notifications** via PGP and/or S/MIME depending of the user preferences.
* **Real-time publish-subscribe channel** within MISP to automatically get all changes (e.g. new events, indicators, sightings or tagging) in ZMQ (e.g. [misp-dashboard](https://github.com/MISP/misp-dashboard)) or Kafka. 
### Sharing with humans 
Data you store is immediately available to your **colleagues** and **partners**. Store the event id in your ticketing system or be informed by the signed and encrypted email notifications. 
### Sharing with machines 
By generating **Snort/Suricata/Bro/Zeek IDS rules, STIX, OpenIOC**, text or csv exports MISP allows you to **automatically** import data in your detection systems resulting in **better and faster detection** of intrusions. Importing data can also be done in various ways: **free-text import, OpenIOC, batch import**, sandbox result import or using the preconfigured or **custom templates**. If you run MISP internally, data can also be uploaded and downloaded automagically **from and to externally hosted MISP instances**. Thanks to this automation and the effort of others you are now in possession of valuable indicators of compromise with no additional work. 

### Collaborative sharing of analysis and correlation 
How often has your team analyzed to realise at the end that a **colleague had already worked on another, similar, threat**? Or that an external report has already been made? When new data is added MISP will immediately show **relations with other observables and indicators**. This results in more efficient analysis, but also allows you to have a better picture of the TTPs, related campaigns and attribution. The **discussion** feature will also enable conversations between multiple analysts resulting in **win-win** for everyone. ![](/img/blog/automation-icon.png "{class='img-responsive'}")
