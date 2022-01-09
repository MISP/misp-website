---
title: MISP 2.4.82 released (aka improved pub-sub ZMQ)
date: 2017-11-10
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.82](https://github.com/MISP/MISP/tree/v2.4.82) has been released including an improved publish-subscribe ZMQ format, improvements in the feeds system, sightings are now ingested and synchronised among MISP instances, many bug fixes and export improvements.

MISP includes a nifty real-time publish-subscribe system to notify subscribers on any updates on a MISP instance. 2.4.82 introduced new channels and expanded format
to deliver additional information to the subscribers. The system can be used to feed stream processing automation systems (e.g. IntelMQ), real-time SIEM interaction , monitoring or custom applications. As an example, we developed a complete dashboard application called [misp-dashboard](https://www.github.com/MISP/misp-dashboard) which solely relies on the publish-subscribe ZMQ feature to allow for a geolocalised view, historical searches of geographical information and a contributor dashboard which is the first version of the gamification project in MISP to promote information sharing (a separate post will come soon).

{{<video src="/img/video/misp-zmq-dashboard-integration.mp4" >}}

MISP ZMQ has new channels especially related to MISP objects in addition to events and attributes.

CSV export has been improved to allow the selection of columns to be included in the export. 
CSV is still the most commonly exported format used and we had feedback from various organisations 
relying on CSV requesting enhancements to the export format.

The old legacy CSV export will work as before like exporting all attributes:

~~~~
GET https://<misp-instance>/events/csv/download/<event-id>
~~~~

The new export format allows to select more columns using the following query format:

~~~~
GET https://<misp-instance>/events/csv/download/<event-id>?attributes=timestamp,type,uuid,value
~~~~

The order of columns will be honoured including those related to object level information.

To select object level columns, simply pre-pend the given object column's name by object_, such as:

~~~~
GET https://<misp-instance>/events/csv/download/<event-id>?attributes=timestamp,type,uuid,value&object_attributes=uuid,name
~~~~

The following columns will be returned (all columns related to objects will be prefixed with object_):

`timestamp,type,uuid,value,object_uuid,object_name`

includeContext option includes the tags for the event for each line.

The STIX 2.0 export has been improved to include custom objects, Person object included in Identity SDO, tool SDO now includes [exploit-kit from MISP galaxy](/galaxy.html#_exploit_kit) and all the [galaxy which can be mapped](/galaxy.html), course-of-action SDO added. Export code has been improved to cope with the utter complex mess of STIX patterning standard.

The STIX 1.x export now includes reporter in STIX incident and producer in STIX indicator and MISP TLP Marking as STIX tlpMarking. File objects are now included in STIX 1.x export.

The MISP feed format has been improved to include objects, attribute tags and object references. The format has been also significantly improved with a quick-hash-list to perform fast lookups and improve the MISP caching mechanisms for large feeds. If you rely on the feed generator in PyMISP, [feed-generator has been updated](https://github.com/MISP/PyMISP/commit/195cd6d7fc305ac6628ed8f2ff762b3f69a9b6ca).

The feed preview in MISP has been improved to include the objects and support the new feed format.

The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

For the MISP users joining the [Borderless Cyber Conference and Technical Symposium / 6-8 Dec 2017 / Prague](https://eu17.first-oasis-conference.org/en/), we will do a MISP training on the 8th December.
