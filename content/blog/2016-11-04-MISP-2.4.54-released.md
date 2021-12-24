---
title: MISP 2.4.54 released
date: 2016-11-04
layout: post
banner: /img/blog/misp-small.png
---

A new version [2.4.54](https://github.com/MISP/MISP/tree/v2.4.54) of MISP including new features, bug and security fixes.

We strongly recommend to update to this latest version.

The release includes various improvements including:

- A new feature to block attributes from IDS export based on the pending proposal. The feature can be enabled in the MISP settings (MISP.proposals_block_attributes). This allows to benefit from pending proposals in your MISP even if the initial contributor didn't approve the proposals. This affects the following export OpenIOC, HIDS, NIDS text and RPZ zone exports.
- A new API to admin users has been introduced to manage users via the API. [Documentation](https://www.circl.lu/doc/misp/automation/index.html#user-management) - PyMISP added two examples [add_user.py](https://github.com/MISP/PyMISP/blob/master/examples/add_user.py) [add_user_json.py](https://github.com/MISP/PyMISP/blob/master/examples/add_user_json.py) on how to use the admin users API.
- TLDs from the warninglists are now used in the free-text import.
- Improvement in the statistics pages including a treemap for the tags used, an overview of the organisations including their contributions.
- Many bug fixes in the modules part (enrichment and import).
- Multiple fixes and improvement in the UI.

We thank all contributors.

The full [change log is available](http://www.misp-project.org/Changelog.txt) at the following location:

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
