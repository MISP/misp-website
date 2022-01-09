---
title: MISP 2.4.109 released (aka cool-attributes-to-object)
date: 2019-06-14
layout: post
banner: /img/blog/attribute-to-object.gif
---

# MISP 2.4.109 released

A new version of MISP ([2.4.109](https://github.com/MISP/MISP/tree/v2.4.109)) has been released with a host of new features, improvements, bug fixes and a minor security fix. We strongly advise all users to update their MISP installations to this latest version.

# New main features

## Encapsulate existing attributes into an object

![](/img/blog/attribute-to-object.gif)

When an analyst inserts information into MISP, it's very common to start with a set of unstructured indicators/attributes. At a later stage, common structures emerge and combining attributes into objects start making more and more sense. However, the effort spent on the process of attribute creation would have to be repeated in prior versions via the object creation interface, something that resulted in analysts deciding to save time and effort and move on, leaving the unstructured data as is. To reduce the workload needed to bring structure to our prior work, we have now introduced a new feature, allowing users to easily select a set of attributes and automatically propose suitable object templates depending on the combination of types of the selected attributes. These in turn, can be gathered and processed into the desired object.

## Improved ATT&CK and ATT&CK-like matrix support

![](/img/blog/attack-new.png)
![](/img/blog/fraud-tactics.png)

We received exhaustive feedback during the FIRST.org CTI conference in London and the [ATT&CK EU community](https://www.attack-community.org/) workshop at Eurocontrol concerning the ATT&CK integration in MISP. The matrix visualisation has been improved by sorting and reorganising the individual techniques based on their aggregate scores. These statistics can now easily be queried based on time-ranges, organisations, tags, along with all other restSearch enabled filters to generate ATT&CK like matrix views.

# Security fix - CVE-2019-12794

An issue was discovered in MISP 2.4.108. Organisation admins could reset credentials for site admins (organization admins have the inherent ability to reset passwords for all of their organization's users) or impersonate them by reusing their API keys. This could be abused in a situation where the host organisation of an instance decides to use organisation admins to further manage their own users. The potential for abuse is limited to situations where the host organisation of an instance creates lower-privilege organisation admins instead of the usual site admins, so whilst it was indeed in the spirit of what the powers of organisation admins are, we agree that this was a bad design decision. [CVE-2019-12794](https://cve.circl.lu/cve/CVE-2019-12794) Thanks to Raymond Schippers for the report.

## API

- [API] added new restSearch filter - date.
  - deprecated to and from
  - date works similarly to timestamp, accepted syntax options:
    - time ranges in the shorthand format (7d or 24h, etc)
    - timestamps
    - fallback parsing for other formats (2019-01-01, "fortnight ago", etc)
    - date ranges using lists [14d, 7d]

# Bugs fixed

- A long-standing bug has been fixed when adding tags or galaxies whilst using Firefox.
- [permissions] Fixed the default sync/user/publisher permissions to include perm_tagger and perm_tag_editor(sync only).
- And many other [fixes](/Changelog.txt).

# MISP galaxy, object templates and warning-lists updated

[MISP galaxy](/galaxy.html), [MISP object templates](/objects.html) and [MISP warning-lists](https://github.com/MISP/misp-warninglists/) have been updated to the latest version.

New [default feeds](/feeds/) were added in MISP. Don't hesitate to contact us if you have any idea for new feeds.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

# Warning: Next release 2.4.110

The next version of MISP will include major changes to the data-model by introducing new functionalities that support forensic capabilities, with a special focus on improving the time representation of MISP attributes and objects. The next release will update various tables in the database as usual, but the automatic update might take longer than usual (on larger instances between 30 and 45 minutes) depending on the number of attributes stored in the instance. During the update procedure, MISP will be unavailable until the update is complete. We will notify our users in advance to prepare their upgrade plan for the next release 2.4.110.

