---
title: MISP 2.4.131 released (improvements, bug fixes and major update to JavaScript dependencies)
date: 2020-09-08
layout: post
banner: /img/blog/d4_sshd_widget.png
---

# MISP 2.4.131 released

A new version of MISP ([2.4.131](https://github.com/MISP/MISP/tree/v2.4.131)) has been released with improvements, bug fixes and a major update to JavaScript libraries.

# Improvements

- New types pgp-public-key/pgp-private-key/email/sha3 added.
- Export format for Bro, Snort, OpenIOC updated to support new email type (in addition to the legacy email-src/email-dst attribute type)
- A new filter "type" added for the internal fetcher which appends email as a type if email-src/email-dst are found.
- [types] email added as a new type, affects #6281.
- [diagnostic] Check if database index is unique.
- New API export: added "count" returnFormat for the REST API which simply counts the number of attributes/events found (on each respective scope).
- The ACL has been extended to allow host org users to block events. Also added a new special permission for the ACL system host_org_user - which will evaluate whether the user is in the org configured in the MISP.host_org_id directive
- Major upgrade to jQuery (Bumped jQuery to version 3.5.1.) and related dependencies.
- STIX 1 Importing test mechanisms from indicators as yara rules (as used by CISA).
- The API GET requests on restsearch with no parameters are no longer allowed.  warn the user of the use of GET queries with posted JSON bodies
- STIX 2 import - Fixed external pattern types parsing.
- Logging -  Add the ability to customize the IP header field when logging.
- New dasbhoard widget - Feature/achievements widget adding gamification to the information sharing.
- New MISP-SNMP Monitor script.
- Various fixes for accessibility for users of screen readers such as ARIA labels.

# Many bugs fixed and small improvements

A host of other improvements are documented in the [complete changelog is available](/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


