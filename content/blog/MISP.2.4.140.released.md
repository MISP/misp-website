---
title: MISP 2.4.140 released (OpenID support, cross object references in extended events and many improvements)
date: 2021-03-10
layout: post
banner: /img/blog/ss7-example.png
---

# MISP 2.4.140 released

We have released 2.4.140, the latest release for MISP, introducing a host of new features, including integrations with various authentication systems, various improvements to the handling of objects, CLI improvements as well as a package containing general bug fixes, along with the usual update of the JSON libraries.

# Manage my identity!

MISP already had a host of integration options with various IDPs, but this release will give you some additional options, in the shape of [OpenID Connect authentication](https://github.com/MISP/MISP/tree/2.4/app/Plugin/OidcAuth) and [Azure Active Directory Authentication](https://github.com/MISP/MISP/tree/2.4/app/Plugin/AadAuth) integrations. Have a look at the various authentication plugins' configuration in the MISP/app/Plugin directory.

# Built in security report of your MISP instance

As of this release, you can get some guidance on the security posture and potential security impacting misconfigurations and best practices via the new security audit tool, locate in the diagnostics section of the server settings. Make sure you go through the tools findings and make any changes you find appropriate from the suggestions offered. When in doubt, feel free to start a discussion on the [support chat](https://gitter.im/MISP/Support) hosted on gitter.

The audit also gives you a sanity check over your CSP posture, used in junction with the new settings and tightened security measures.

Massive kudos to @JakubOnderka for all this work!

# Cross referencing objects across extended events

Whilst extended events were the most flexible way of creating counter analyses in MISP as well as being able to provide additional information to a report, we were always lacking a crucial component to make this feature truly shine: The ability to build connected graphs of the data points contained in a set of events extending one another. This has now been added to MISP as of 2.4.140.

# CLI improvements

We want to make scripting and using the CLI in general a bit more straight-forward. Since the phasing out of the build in task scheduler, we find that there has been a massive uptick in the usage of these tools so expect more improvements in the future. For now, we have added tools to list the connect servers directly from the CLI, to be able to automate the sync process per connected server. 

Additionally, a new set of CLI tools is being built for developers, to ease our lives when trying to modify MISP. The first tool for this toolkit allows us to massage the direct feed description dumps to the expected format for easier modification.

# New types added in MISP

New full-name, dkim and dkim-signature attribute types were added to MISP. Associated to [DKIM objects](/objects.html#_dkim) were included to support tools such as Farsight Security dnsdb to add DKIM information in your investigations.

# Security Vulnerability

An issue was discovered in app/Model/SharingGroupServer.php in MISP 2.4.139. In the implementation of Sharing Groups, the "all org" flag sometimes provided view access to unintended actors. Thanks to Jeroen Pinoy for the report. The vulnerability has [CVE-2021-27904](https://cvepremium.circl.lu/cve/CVE-2021-27904) assigned.

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html)
.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

