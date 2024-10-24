---
title: MISP 2.4.83 released (aka attributes-level tag filtering and more)
date: 2017-12-06
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.83](https://github.com/MISP/MISP/tree/v2.4.83) has been released including attribute level tag filtering on synchronisation, full audit logging via ZMQ or Syslog, user email domain restriction at the org level, many more improvements and bug fixes.

Tag filters have been enhanced and filtering is on

- all events containing matching tags on event + attribute level (positive lookup)
- all events not containing matching tags (negative lookup)
- filter attributes within a matched event for blocked attributes (negative lookup)

Tag filtering improved performance for large MISP instances actively when using filtering.

A new functionality has been added to limit the use of certain email domains to an organisation. This extends the granularity of filtering
for specific organisations to avoid out-of-scope users within a specific organisation.

Audit logging has been improved to log all the audit logs in ZMQ and/or Syslog. syslog logging now includes all audit log entries and it's separated into proper severity levels. ZMQ logging and syslog logging are both optional features.

New types were introduced such as mac-address and mac-eui-64 in MISP to allow sharing indicators related to EUI-48 and EUI-64.
Phone type detection is better especially in the free-text import along with the normalisation of the phone attribute type to ensure consistent correlations.

The CSV export has received an overhaul, improving performance and extending the export's flexibility by new filters such as  a "value" filter or the inclusion of attribute level tagging.

ZMQ channel has been improved to support complex software relying on the ZMQ feed such as the recently released [misp-dashboard](https://github.com/MISP/misp-dashboard).

Feed preview enhanced especially for the MISP feed format to allow quick pivoting to the correlating events in a feed from individual attributes.

Many bug fixes and improvement were introduced in this version.

The full change log is available [here](https://www.misp.software/Changelog.txt). [PyMISP change log](https://www.misp.software/PyMISP-Changelog.txt) is also available.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were notably extended by many contributors. These are also included by default in MISP. Don't forget to do a `git submodule update` and update galaxies, objects and taxonomies via the UI.

New MISP trainings are foreseen the 17/01 and 18/01 in Luxembourg including a full-day API and extension hands-on. [For more information and registration](https://www.circl.lu/services/misp-training-materials/).

