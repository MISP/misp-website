---
title: MISP 2.4.91 released (aka distribution visualisation, galaxy at attribute level and privacy notice list)
date: 2018-05-16
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.91](https://github.com/MISP/MISP/tree/v2.4.91) has been released including new major features, improvements and bug fixes.

### Distribution and sharing visualisation

MISP 2.4.91 has a new visual aid in order to simply view the distribution and sharing model of all the attributes within an event. As events can
become quite larger, with long lists of objects and attributes, analysts need to verify whether the proper distributions are applied. The new visualisation
allows them to view the items per distribution level including the associated sharing groups. The visualisation is dynamic and can be used to
filter the given attributes matching a specific distribution setting within the event.

![Visualisation of a MISP event and how the sharing of attributes will take place](/img/blog/sharing.png "{class='img-responsive'}")

### Galaxy at attribute level

[MISP Galaxy](/galaxy.html) includes a large number of libraries to assist in classifying events based on threat actors, kill chains or actor techniques such as described in the [MITRE ATT&CK](https://attack.mitre.org/wiki/Main_Page) galaxy. Initially, MISP galaxies were limited to be attached to MISP events alone. As many users developed new galaxy cluster to map their own model, MISP 2.4.91 is now capable of attaching MISP clusters at the attribute level. In the example below, a vulnerability attribute can be then easily linked to the respective MITRE ATT&CK adversary technique supporting analysts trying to search for and pivot on techniques, but also supporting various more advanced automation scenarios.


![An example of a MISP galaxy such as MITRE ATT&CK attached to a specific attribute in MISP](/img/blog/exploitation.png "{class='img-responsive'}")

### Privacy notice list and GDPR

The MISP Project is actively involved when it comes to questions of compliance, as of lately with a special focus on [information sharing and legal compliance](/compliance). In the scope of the CEF-TC-2016-3 - Cyber Security co-funding helped us to improve the various aspects of compliance while keeping a strong focus on the information sharing aspect.

In MISP 2.4.91, we introduced the [MISP notice system](https://github.com/MISP/misp-noticelist) to inform MISP users of the legal, privacy, policy or even technical implications of using specific attributes, categories or objects. The feature was originally designed to support the Directive 95/46/EC (General Data Protection Regulation - GDPR) by notifying the analyst about the potential risks while entering specific information. The notice feature is a flexible solution to allow for a wide variety of notice systems (expressed in a simple JSON format) to be included in MISP, based on the category or type entered in the system.

We expect to see organisations using MISP to enable, disable or extend the notice lists to fit their specific policies, legal frameworks or local regulation frameworks.

![GDPR notice about a specific category](/img/blog/not1.png "{class='img-responsive'}") 

and notice lists are easily configurable:

![Notice lists are configurable](/img/blog/not2.png "{class='img-responsive'}") 

### API

[Feed](/feeds) management, in 2.4.91, can be also be done via the API such as add/edit/delete feeds. API documentation is directly accessible via the API if a GET request is performed instead of a POST.

ZMQ feed has been extended to include base64 encoded attachments in order to improve the integration with the CSP platform (MeliCERTes) and other application relying on the ZMQ feed (3169 fixed).

### Miscellaneous Improvements

Event enrichment (via misp-modules) can now be easily triggered from the event menu to automatically enrich all the attributes in event. This enrichment is also globally accessible via the API and exposed via the command-line too.

The legacy STIX 1 import has been improved to support CustomObjects, socket address objects, CIQ targets, DNS records object and many others.

Many bugs were fixed with special note to issues 3245, 3240, 3202 and 3201.

MISP 2.4.91 has been updated to the latest version of CakePHP 2.10 series.

The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

PyMISP has been also updated, boasting a more clever approach to timestamp handling while updating MISP JSON files. The PyMISP documentation has been updated [PDF](https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf).

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI. To get the MISP notice list, don't forget to perform a `git submodule init; git submodule update` to initialise the new external dependency.

Don't forget that the MISP Threat Intelligence Summit 0x4 will take place the Monday 15th October 2018 before hack.lu 2018. A [Call-for-Papers is open](https://cfp.hack.lu/misp0x4/) for the MISP Threat Intelligence Summit 0x4. We would be glad to see users, contributors or organisations actively using MISP or/and threat intelligence to share their experiences and presentation to the CfP.
