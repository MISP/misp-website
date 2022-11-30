---
title: MISP 2.4.166 released with many improvements, bugs fixed and security fixes. 
date: 2022-11-30
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.166](https://github.com/MISP/MISP/releases/tag/v2.4.166) with new features and fixes, including two critical security fixes.

# TAXII 2.1 server push integration

With the collaboration of CISA and MITRE, we have included the first version of the [TAXII](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html) integration in MISP, allowing administrators to configure their MISPs to push content to TAXII 2.1 servers. For more informatia new dedicated will be posted soon. On server side, the [taxii2-client Python library](https://pypi.org/project/taxii2-client/) is required to be installed. The conversion is performed by the wonderful and efficient [misp-stix library](https://github.com/MISP/misp-stix).

# Logging rework

The logging of MISP has been severely reworked by Jakub Onderka, including a separate Access log subsystem as well as multiple improvements and cleanups to the system at large. 

# Security fixes

Two critical vulnerabilities have been patched allowing for the tampering with data shared in the community via galaxy clusters and tags. It is **HIGHLY** recommended to update to 2.4.166 as soon as possible to avoid information tampering. We also encourage everyone to consider informing peered MISP instance owners to do the same. CVEs have been requested and are pending for both. Thanks to Jakub Onderka for discovering and fixing the vulnerabilities.

# Allowing for working around the edge cases introduced by TLP v2.0 

Even though [TLP 2.0](https://www.first.org/tlp/) has been supported by MISP for a while, in order to cope with both tools old and new as well as older information sources, we see the need to often attach both TLP:WHITE and TLP:CLEAR to data points. This has however been blocked by the taxonomy exclusivity rules - something that we've now added exceptions for. 

Let's hope that we can avoid similar surprises in the future.

For more [details](https://www.misp-project.org/Changelog.txt) about changes in the MISP core software.

# Other updates and changes

## MISP Objects

- [passport object] Updated to include passport-creation field.

## MISP Galaxy

- MITRE ATT&CK updated and fixing the missing reference
- Many improvements and fixes in all the meta fields
- Tool galaxy updated
- [Ransomware groups](https://www.misp-project.org/galaxy.html#_ransomware) updated

