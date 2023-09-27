---
title: MISP 2.4.177 released with various improvements and bugs fixed. 
date: 2023-09-27
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/lookyloo-misp.png
---

MISP 2.4.177 released with various bugs fixed and improvements. 

# Improvements

- [dev] added a shell script to generate the restsearch parameters.
- [CLI] add command to expire active AuthKeys that do not have an IP allowlist set. 
- [cli] Add command to trigger password change on next login for users with old pw. 
- [Users] add last password change timestamp for users.
- [workflowModules:event_distribution_operation] Added action module.


# Changes

- [tests] testing disabling the timestamp greater as old timestamp for password changes. 
- [tests] make em happy with re-including a filter parameter that worked before, albeit unintentionally.
- [PyMISP] disable some tests. 
- [misp-stix] Bumped latest version.
- [warning-lists] updated. 
- [PyMISP] Keep messing with tests. 
- [warning-lists] updated. 
- Check test files are there.
- [version] bump.
- [escaping] added to event ID. 
- Attempt to fix git clone from the test suite.
- [feeds] change name to Community version.
- [config:customAuth_header] Default to upper case. 

  - See $_SERVER make passed headers upper case
- [console:TrainingShell] Allow overriding existing user data. 
- [Console:trainingShell] Provide correct filters for wiping data. 
- [console:trainingShell] Added wipeUsers and wipeOrgs functions. 
- [posts:crud] Prevent read-only users to create posts. 
- [config:config.default] Disabled warning_for_all by default for new
  install. 

# Fixes

- [misp-stix] Bumped latest version with a fix on the file patterns parsing.
- [tests] added some sleeps to avoid timestamps of follow up tests being within 1 second of the previous test. 
- [API] filter parameters added. 
- [PyMISP/CI] Disavle search logs for now.
- [restsearch] parameters fixed. 
- [taxonomy] enable/disable creating junk taxonomies on invalid ID, fixes #9273.
- [console:trainingShell] More typo in model name.
- [console:trainingShell] Typos in model names.
- [RestSearch] allow filtering on eventinfo for events and attributes.

# Other improvements

- Show object's attributes if they are tagged. 
- Fix event graph tag scope view.
- Fix event hyperlink in discussion view page. 

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# Training video

The latest video of MISP Training - Advanced, Developer session, from API to MISP internals is now available [on YouTube](https://www.youtube.com/watch?v=2tmjLsPrQkI).

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
