---
title: MISP 2.4.90 released (aka Extended Events release)
date: 2018-04-20
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.90](https://github.com/MISP/MISP/tree/v2.4.90) has been released including the new extended events feature along with many updates in improvements in the API, user-interface (including many improvement in the graph editor) and many bug fixes.

The extended event feature has been added in MISP to allow users to extend events without modifying the original events. For more information about the extended event feature, the blog post [Introducing The New Extended Events Feature in MISP](/2018/04/19/Extended-Events-Feature.html) includes many details and use-cases explaining how it can support organisations in their management of threat information.

The graph editor has been significantly improved including filtering on tag/type of attributes, making the physics engine of the graph configurable, along with providing support for the extended MISP events directly in the graph tool.

A new functionality has been added to control the server settings via the command line directly.

- /var/www/MISP/app/Console/cake Admin getSetting [setting]
  - setting is optional, if none set "all" is assumed
  - returns all or a specific setting's current value and metadata

- /var/www/MISP/app/Console/cake Admin setSetting [setting] [value]
  - set a given server setting by full setting name
  - for example the following will enable the import services:
  -  /var/www/MISP/app/Console/cake Admin setSetting "Plugin.Import_services_enable" 1

Tasks from MISP can be triggered from the command line and an example of cron entry has been added in the UI.

Some improvement in the [Cortex integration](https://github.com/TheHive-Project/Cortex) and settings, to allow the configuration of TLS options and ensuring Cortex 2 compatibility.

A clarification has been introduced in the UI to clearly separate the caching of feeds and enable feeds for full import.

User roles have gained a new setting, allowing administrators to set the maximum memory usage and execution time per role (e.g. useful to differentiate between regular and API roles that are expected to be more resource intensive).

The STIX 2 export has been refactored and supports more features of the MISP standard format and the performance was improved too.

To ensure data portability of users (GDPR), a new export button has been added to allow users to get their information in addition to the existing API for user management. Regarding GDPR compliance, the MISP project [released a document about GDPR and information sharing](/compliance/gdpr/) on the topic, which can help operators and users of MISP communities understand what the exact impacts of the regulation are, along with why information sharing is critical in information security.

MISP default feeds updated including the (URLhaus)[http://urlhaus.abuse.ch] feed.

We would like to thank all of the contributors who have been fixing bugs, contributing new features or supporting us for this release.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MIS
P. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.
