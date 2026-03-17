---
title: "Have You Ever Thought About Drones in MISP?"
author:
 - MISP Project team
date: 2026-03-10
tags: ["MISP", "Threat Intelligence", "UAV", "Drone" ]
layout: post
banner: /img/blog/uav/4.png
---

# Have You Ever Thought About Drones in MISP?

## The Drone Threat

Unmanned Aerial Vehicles (UAVs), commonly referred to as drones, are increasingly present in civilian, industrial and military environments. While they provide many legitimate capabilities, they also introduce new security risks. In recent years, incidents have illustrated how drones are becoming a recurring operational and security concern across multiple sectors.

This trend has intensified with the war in Ukraine, where UAVs have become a central element of modern warfare. The conflict has accelerated the development, adaptation, and large-scale deployment of drones for reconnaissance, targeting, and strike capabilities. As a result, the proliferation of UAV technologies and tactics is now influencing both military and civilian security landscapes worldwide.

Some recent examples;
* **Airports:** Munich Airport temporarily halted flights after suspected drone sightings; operations resumed on 4 Oct 2025. The airport reported 46 flights cancelled or delayed, affecting about 6,500 passengers. *(Al Jazeera)*
* **Sensitive / critical sites:** Three drones were reported flying over Belgium’s Doel nuclear power plant on 10 Nov 2025. The plant operator confirmed the incident had been reported to authorities. *(Le Parisien)*
* **Military / border context:** A drone crash near Poland’s eastern border (Osiny, Lublin region) on 20 Aug 2025 was assessed by prosecutors as likely involving a military drone. Preliminary findings referenced possible explosive-related damage. *(Polskie Radio)*

**Sources:** [aljazeera.com](https://www.aljazeera.com/news/2025/10/4/munich-airport-resumes-operations-after-more-drone-sightings-halted-flights) (04/10/2025), [leparisien.fr](https://www.leparisien.fr/international/une-centrale-nucleaire-belge-survolee-par-trois-drones-dans-un-contexte-de-recrudescence-dincidents-10-11-2025-PFDQSY5JGFEXFPUDE7YHZKW6NQ.php) (10/11/2025), [polskieradio.pl](https://www.polskieradio.pl/395/7784/artykul/3567856,drone-that-exploded-in-eastern-poland-was-russian-defence-minister-says) (20/08/2025)

These incidents highlight a growing challenge: how to **document, share, correlate, and improve analysis of drone-related security events**.

Several operational needs are emerging:

* Development of standardized incident response procedures adapted to drone threats.
* Improved attribution methods, combining forensic analysis, intelligence sharing, and correlation.
* Integration of threat intelligence platforms to detect recurring patterns and anticipate incidents.
* Increased need for reliable drone detection capabilities, including both knowledge and detection systems.

To address some of these challenges, a structured information sharing becomes essential.

## What is MISP?

MISP (MISP Is a Sharing Platform) is an open-source platform designed to **collect, store, share, and correlate threat intelligence** among trusted communities (https://www.misp-project.org/).

It allows analysts, security teams, and organizations to exchange structured information about threats and incidents. Using standardized objects, taxonomies, and relationships, MISP helps transform isolated observations into actionable intelligence.

Although MISP was initially widely adopted for **cyber threat intelligence**, its flexible data model allows it to be extended to many other domains, including physical security and hybrid threats. Drone incidents are a good example of such cross-domain threats: they combine elements of cyber, physical, and geopolitical intelligence.

## How MISP Was Improved for UAV Threat Intelligence

To better support the documentation and analysis of drone-related incidents, several new resources have been integrated into MISP. We have integrated new objects, one galaxy and three new taxonomies. 

### UAV and Controller Objects and Relationships

Dedicated **UAV objects** and **controller objects** were added to allow analysts to describe drones and their associated control devices in a structured manner.

The object supports technical and operational fields such as the manufacturer, model, variant, serial number, registration ID, MAC address, fly path, firmware version/hash, etc… and many other related informations. This structured modeling makes it easier to normalize incident data and correlate sightings, recovered devices, or recurring platforms across multiple events. [https://www.misp-project.org/objects.html#_uav](https://www.misp-project.org/objects.html#_uav)

A series of [new relationships](https://www.misp-project.org/objects.html#_relationships) related to drone activity (such as `crashed-at`, `jammed-by`, `identified-by`, and `intercepted-by`) were added to describe the different possible interactions.

### UAV Model Galaxy

A dedicated [**MISP Galaxy**](https://misp-galaxy.org/uavs/) containing more than **680 UAV models** was introduced.

![UAV's Galaxy](/img/blog/uav/1.png)

Each entry includes general description, detailed technical and manufacturer specifications, as well as reference links. This database is maintained by CIRCL team and is **fully open source**. The information it contains is based on **OSINT sources** and is also enriched with data collected through our **dark web monitoring plateform ([AIL](https://ail-project.org))**, which enables tracking of **Telegram channels** where UAV-related information may appear. This allows analysts to quickly identify and update specific drone informations.

### Drone-Specific Taxonomies

Three taxonomies were introduced to classify UAVs and enrich incident data:

* **[ce-uas-classification](https://github.com/MISP/misp-taxonomies/blob/main/ce-uas-classification/machinetag.json)** — To cover European Union (EASA) drone classification system. The EASA drone classification system defines standardized drone classes from C0 to C6. The categorisation is mainly done by weight, capabilities, and risk level and it is used to regulate safety, technical requirements, and operational limits for unmanned aircraft in Europe. 

* **[nato-uas-classification](https://github.com/MISP/misp-taxonomies/blob/main/nato-uas-classification/machinetag.json)** — NATO classification framework used to categorize UAS platforms by weight, altitude, and operational capabilities.

* **[uas-additional-classification](https://github.com/MISP/misp-taxonomies/blob/main/uas-additionnal-classification/machinetag.json)** — Additional tags used to qualify drone usage, configuration, or specific model characteristics. For example it adds tags capability of VTOL (Vertical Take off and Landing), LM (Loitering Munition) etc..

These taxonomies help to standardize how drone-related information is described across different organizations and communities.

## Now What Can We Do?

With these new resources integrated into MISP, analysts can now structure and correlate drone-related intelligence more effectively. Instead of treating drone incidents as isolated events, they can now be modeled using consistent objects, enriched with standardized taxonomies, and linked to known UAV models here an example of a standardised drone incident.

### Case 1 – A Drone in a Field

On the night of **19–20 August 2025**, a **Shahed-type UAV** [reportedly](https://polanddaily24.com/services-have-recordings-of-the-polish-sky-a-fast-moving-object-can-be-seen/poland-today/59302) crashed near **Osiny in the Lublin region of eastern Poland**, close to the border area. The drone detonated on impact, causing minor material damage such as shattered windows and scattering debris across nearby agricultural fields. Authorities opened an investigation. This type of incident can be encoded and documented in **MISP**.

![](/img/blog/uav/3.png)

In this case, **MISP** allows storing detailed information about the incident, including geolocation data and pictures of the scene. This enables investigators to track evidence, document the event, and enrich the dataset with additional technical information about the involved UAV.

### Case 2 - A Drone in the City

Another common incident (here fictional) is where drones are discovered, either or not in a no fly zone. From forensic data could be extracted, it may sometimes be possible to discover juicy information like sync uid, waypoints. Also many informations that could be now be registerend in misp. In addition, you still benefit from MISP’s ability to correlate attributes across different events, which can, for example, allow correlating a remote control with a drone firmware. 

Another common incident (fictional in this case) occurs when a drone is discovered in an urban area, sometimes within a no-fly zone. Through digital forensics, investigators may extract valuable data such as Sync UID, waypoints, firmware information, or device informations.

These artifacts can then be registered in MISP in object within events. This allows analysts to leverage MISP’s correlation capabilities, for example linking a remote controller to a specific drone firmware, identifying reused components across incidents, or connecting multiple drone-related events together.

![](/img/blog/uav/4.png)


## To get further

If you would like to learn more about Drones, how they operate, knowns security bypass techniques, and forensic data extraction from FPV drones, CIRCL will be present at the FIRST [2026 Cyber Threat Intelligence Conference](https://www.first.org/conference/firstcti26/program#pDrone-Threat-Intelligence-Workshop), in Munich, Germany, on April 21, 2026. We will do a workshop dedicated on these topics, covering drone-related threat intelligence and forensic analysis.

## Links

- MISP: [https://www.misp-project.org/](https://www.misp-project.org/)
- AIL: [https://ail-project.org/](https://ail-project.org/)
- UAV's MISP Galaxy: [https://misp-galaxy.org/uavs/](https://misp-galaxy.org/uavs/)
- UAV's Related Objects:
  - [https://www.misp-project.org/objects.html#_uav](https://www.misp-project.org/objects.html#_uav)
  - [https://www.misp-project.org/objects.html#_remote_controller](https://www.misp-project.org/objects.html#_remote_controller)
- UAV's Related Taxonomy
  - ce-uas-classification: [https://www.misp-project.org/taxonomies.html#_ce_uas_classification](https://www.misp-project.org/taxonomies.html#_ce_uas_classification)
  - nato-uas-classification: [https://www.misp-project.org/taxonomies.html#_nato-uas-classification/machinetag.json](https://www.misp-project.org/taxonomies.html#_nato-uas-classification/machinetag.json)
  - uas-additional-classification: [https://www.misp-project.org/taxonomies.html#_uas_additionnal_classification](https://www.misp-project.org/taxonomies.html#_uas_additionnal_classification)
