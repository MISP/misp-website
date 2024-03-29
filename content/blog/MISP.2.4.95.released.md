---
title: MISP 2.4.95 released (aka API search improvement)
date: 2018-09-06
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP ([2.4.95](https://github.com/MISP/MISP/tree/v2.4.95)) has been released with the first stage of a complete rework and refactoring of the API exports, allowing for more flexibility, improved search capabilities, performance and extendability.

The search API in MISP has been refactored to streamline and simplify the code's logic and to bring consistency among the various export formats (MISP JSON, MISP XML, OpenIOC, Suricata, Snort and the text export) especially in regards to filtering. The filter system now assumes exact string matches by default and allows users to insert wild-card characters for substring searches across all filters. This provides both performance boosts along with more accurate results when substring matching is not needed along with the flexibility of setting search terms such as starts with or endswith. The API is also backwards compatible with previous versions and existing tools (let us know if you have [any issue](https://www.github/MISP/MISP)).

With the new API, building search queries has become more natural and simple to build programmatically. For example, exporting all attributes of types ip-src and ip-dst that have a TLP marking and are not marked tlp:red, can be achieved with the query below. String searches are by default exact lookups, but you can use SQL style "%" wildcards to do substring searches.

~~~~
{
    "returnFormat": "json",
    "type": {
        "OR": [
            "ip-src",
            "ip-dst"
        ]
    },
    "tags": {
        "NOT": [
            "tlp:red"
        ],
        "OR": [
            "tlp:%"
        ]
    }
}
~~~~

All old parameter syntaxes are still supported, though passing ordered parameters via the URL has been deprecated. We are also currently in the process of baking all existing export APIs into the standard API search functionality - simply pass your usual standardised list of parameters as described in the API and choose the return format. Make sure you query the correct scope (/events/restSearch for all events matching a query and /attributes/restSearch for all attributes matching a query). 

A complete ReST client has been added in the MISP interface to easily query the API from your MISP. A templating system has been included to assist users to create their ReST queries against the API. The ReST client includes the API enumeration documentation based on the API exposed description. Use this tool to build and test queries that you would like to use via other tools and applications.

A debug functionality has been added in any API query to quickly show the SQL queries performed by appending `/sql:1` to any query via the API (debugging mode must be set to "debug with SQL dump" - option 2).

Many new [MISP modules](https://www.github.com/MISP/misp-modules) were included and we extend MISP to better support enrichment modules with large output (such as the Sigma to search queries converter). In this version, a new on-demand pop-up has been introduced to have a sticky hover to ease cut-and-paste or selection.

![A sigma export to SIEM rules via the misp-modules export](/img/blog/sigma.png "{class='img-responsive'}")

A bro NIDS type has been added in MISP to support the exchange of raw bro NIDS signature within MISP communities.

For a complete overview of all the changes, the full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

Enhancements to the STIX2 export and import were undertaken to improve the scope coverage of the [MISP open standard](https://github.com/MISP/misp-rfc) and the mapping thereof to the STIX2 JSON format. Relationships between SDOs have been improved in the export to map the MISP relationships with the fixed relationships described in STIX2. valid_until has been mapped in the STIX2 export based on the expiration date used in the expiration sightings available in MISP.

Several new translations were included in MISP for the user-interface localisation. The Japanese translation has been completed, French, Danish and Italian have been improved drastically and many other translations (such as German, Spanish and Korean) are on the way. 

A huge thanks to all the [contributors](/contributors) who have tirelessly helped us improve the software and also all the participants in the MISP trainings giving us a bunch of interesting feedback for ideas for improvements.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

Don't forget that the MISP Threat Intelligence Summit 0x4 will take place the Monday 15th October 2018 before hack.lu 2018. Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next activities to improve threat intelligence, analytics and automation.
