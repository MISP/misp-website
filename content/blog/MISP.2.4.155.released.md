---
title: MISP 2.4.155 - quick bugfix release 
date: 2022-03-03
layout: post
banner: /img/sharing-group-blueprints.png
---

This release is a rapid follow up to v2.4.154, addressing several rather annoying issues

# Bugfixes 

- Various bugfixes to the sharing group blueprint system (especially to it being more restrictive than intended)
- Updating the DB schema to avoid the diagnostics complaining
- Fixed an issue with organisation meta fields defaulting to null rather than '' (causing the blueprint issue mentioned above)
- Rework of the DB schema dumper
- Fixes to the Kali Linux installer

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core.
