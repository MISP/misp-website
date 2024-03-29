---
title: MISP 2.4.103 released (aka UI improvements)
date: 2019-03-04
layout: post
banner: /img/blog/filtering.png
---

A new version of MISP ([2.4.103](https://github.com/MISP/MISP/tree/v2.4.103)) has been released with significant UI improvements (including a new flexible attribute filtering tool at the event level), many bug fixes and a fix to a security vulnerability (CVE-2019-9482) which was affecting sighting visibility.

# New features

## Improved attribute filtering tool

A new attribute filtering tool has been added to the event view to replace the previous filtering. Complex filtering rules can be set to easily filter, navigate and paginate over large events with many attributes and objects.

![MISP screenshot - new attribute filtering tool at event level](/img/blog/filtering.png "{class='img-responsive'}")

![MISP screenshot - new attribute filtering tool at event level](/img/blog/filtering2.png "{class='img-responsive'}")

## Improved hover behavior for expansion services.

Thanks to [Wesley Agena](https://github.com/wesleya) from DomainTools for the improvement in the hover placement while using [misp-modules](https://github.com/MISP/misp-modules) expansion services in MISP. The hover improvements include:

- add some logic to choose a better hover placement
- make hover hide on outside click, to allow using the scrollbar to view
  full hover
- add an icon in the hover tooltip to turn it into a popup
- move popup close button to better position
- group attributes for each module in hover UI
- prevent duplicate enrichment API queries once the first one is done

# UI rework

A major project is ongoing to improve the UI accessibility in MISP, UI elements are progressively updated to an adequate templating system to ease the future extension of the UI. This versions already includes a reworked UI for tab UI, index UI, server settings, server preview and much more. The rework is handled in a progressive fashion with the UI being gradually updated to ensure a smooth transition. If you notice any UI specific issues during the transition period, don't hesitate to open an [issue](https://github.com/MISP/MISP/issues) (with a screenshot if possible) to describe the expected behavior.

## Generic matrix-like galaxies are now supported

With the increased use of MITRE ATT&CK and the need of describing similar matrix-like models, generic matrix-like galaxies are now supported.
You can create your own matrix with the associated custom kill chains. A first [new matrix-like galaxy](/galaxy.html#_election_guidelines) has been added to MISP called *Universal Development and Security Guidelines as Applicable to Election Technology* made by the [European Commission](https://www.ria.ee/sites/default/files/content-editors/kuberturve/cyber_security_of_election_technology.pdf) to model the attack model against election processes and technologies.

If you want to create your own matrix-like, [a slide deck called MISP Galaxy](/misp-training/3.2-misp-galaxy.pdf) part of the [MISP training materials](https://github.com/MISP/misp-training#misp-training-materials) explains the basics.

# Security fix (CVE-2019-9482)

In MISP 2.4.102, an authenticated user could view sightings that they should not be eligible for. Exploiting this requires access to the event that has received the sighting in addition to certain conditions aligning - the issue affects instances with restrictive sighting settings (event only / sighting reported only). This vulnerability got has received the designation [CVE-2019-9482](https://cve.circl.lu/cve/CVE-2019-9482). Thanks to Tyler McLellan of CanCyber.org for reporting the vulnerability. We are eager to receive security reports and/or analyses about the MISP project, [don't hesitate to contact us](https://github.com/MISP/MISP/blob/2.4/CONTRIBUTING.md#reporting-security-vulnerabilities).

## Enhancements

- Kerberos authentication has been updated to include ldapEmailField to specify additional location of where email addresses can be found (thanks to [iwitz](https://github.com/iwitz))
- [API] change_pw is now exposed to the API.
- The event view now includes the number of objects included in an event.
- Additional url setting to add a complementary baseurl especially when a MISP is accessible via different means and an url is required for the sharing groups. The objective is to decouple the baseurl (used to prepend links) from the announce baseurl (for sharing groups / emailing).
- Add CORS setting for external integration (thanks to [Hannah Ward](https://github.com/FloatingGhost)).
- A major rework on the [auto installer script for MISP](https://misp.github.io/MISP/INSTALL.ubuntu1804/) to transform the installation process into a pleasant journey.
- [CLI] DB updates can now be executed via the CLI. This mimics what he is done what the automatic update does when login for the first time after an update.
- [API] New tag search API to search for tags.
  - simply pass the value you want to search for. Use % for wildcards
  - taxonomy and galaxy metadata returned with tag
- [API] The log search API now supports time ranges.
- Event view now includes a sparkline to track changes on the event over time.
- Many docs and installer guides have been improved.

A host of bugs were squashed and various small improvements were implemented.

MISP [galaxy](/galaxy.pdf), [objects](/objects.pdf) and [taxonomies](/taxonomies.pdf) were extended by many contributors, which are also included by default in MISP. Don't forget to run a `git submodule update` and update galaxies, objects and taxonomies via the UI.

[MISP modules](https://github.com/MISP/misp-modules) were also significantly improved especially on the PDF export which includes a complete export of MISP events as a clean and concise PDF report.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

Don't hesitate to have a look at our [events page](http://www.misp-project.org/events/) to see our next trainings, talks and activities to improve threat intelligence, analytics and automation.

