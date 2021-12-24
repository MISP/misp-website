---
title: MISP 2.4.152 released with timeline improvements, optional filtering on sync, LinOTP improvements and more.
date: 2021-12-22
layout: post
banner: /img/blog/timeline-improvement.png
---

# MISP 2.4.152 released

MISP 2.4.152 released with timeline improvements, optional filtering on sync, LinOTP improvements and more.

The LinOTP authentication module has been improved to include a mixed mode where both OTP and MISP's usual password authentication can be used together.

The timelining has been improved in several ways, such as the inclusion of images from objects, as well as various improvements in the timeline's sighting view. Several bugs were affecting this feature have also been fixed.

A new optional synchronisation filtering has been added to allow for the removal of specific attribute or object types when syncing. The functionality is meant to be used by the final recipient organisations of a synchronisation chain, in order to filter out specific types of information due to legal or specific internal policies. The filtering feature is disabled by default and needs to be enabled in the general configuration. This feature is for ISACs or consumer organisations, not redistributing information to other MISP communities.

A new STIX 1 and 2 export for attribute restSearch has been added in complement to the existing event export in STIX 1 and 2. The export works just like the other event level STIX export, all you need to do is specify the given STIX format as the return type when querying the attribute restSearch endpoint.

Many internal improvements and bugs fixed.

# MISP Modules

- New [Qintel sentry module](https://misp.github.io/misp-modules/expansion/#qintel_qsentry) added.
- [CIRCL hashlookup expansion](https://circl.lu/services/hashlookup/) SHA-256 support added.

The [MISP modules changelog is available](https://www.misp-project.org/Changelog-misp-modules.txt).

# MISP Taxonomies

- New [political spectrum taxonomy](https://www.misp-project.org/taxonomies.html#_political_spectrum) added.
- Improvement in exercise taxonomy.
- New [deception taxonomy](https://www.misp-project.org/taxonomies.html#_deception) added.

[MISP Taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

# MISP Galaxy

- New matrix [CONCORDIA Mobile Modelling Framework - Attack Pattern](https://www.misp-project.org/galaxy.html#_concordia_mobile_modelling_framework_attack_pattern) added (thanks to [Concordia H2020 project](https://www.concordia-h2020.eu/)).
- Many update in threat actor, RAT and tools galaxy. 

[MISP Galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt)

# MISP Objects

- New Concordia intrusion set object.
- New temporal event object.
- Many improvements in user, person, postal-address, email object.
- New relationships added such as `found-in`, `works-with`, `drives`.

[MISP objects changelog](https://www.misp-project.org/Changelog-misp-objects.txt)

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html)
.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core.

