---
title: MISP 2.4.166 released with many improvements, bugs fixed and security fixes. 
date: 2022-11-21
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.166](https://github.com/MISP/MISP/releases/tag/v2.4.166) with new features and fixes, including two critical security fixes.

# TAXII 2 server integration

With the collaboration of CISA and Mitre, we have included the first version of the TAXII integration in MISP, allowing administrators to configure their MISPs to push content to TAXII servers. For more information see the dedicated [blog post](https://misp-project.org/blog/taxii2_first_version.md).

# Logging rework

The logging of MISP has been severely reworked by Jakub Onderka, including a separate Access log subsystem as well as multiple improvements and cleanups to the system at large. 

# Security fixes

Two critical vulnerabilities have been patched allowing for the tampering with data shared in the community via galaxy clusters and tags. It is **HIGHLY** recommended to update to 2.4.166 as soon as possible to avoid information tampering. We also encourage everyone to consider informing peered MISP instance owners to do the same. CVEs have been requested and are pending for both. Thanks to Jakub Onderka for discovering and fixing the vulnerabilities.

# Allowing for working around the edge cases introduced by TLP 2.0 

Even though TLP 2.0 has been supported by MISP for a while, in order to cope with both tools old and new as well as older information sources, we see the need to often attach both TLP:WHITE and TLP:CLEAR to data points. This has however been blocked by the taxonomy exclusivity rules - something that we've now added exceptions for. 

Let's hope that we can avoid similar surprises in the future.

For more [details](https://www.misp-project.org/Changelog-misp-objects.txt).


