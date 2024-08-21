---
title: MISP 2.4.196 released with many bugs fixed and improvements.
date: 2024-08-21
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/object-collapse.png
---

## MISP 2.4.196 released with many bugs fixed and improvements.

### New Features
- **Decaying Model:** Introduced a new DecayingModel that leverages true positive and false positive sightings for better decision-making. [Marcel Slotema]
- **Log Search Enhancement:** Added an optional `hh:mm:ss` accuracy to log searches, allowing for more precise time-based queries. This update also includes significant refactoring to improve code quality. [iglocska]
- **User Log Review:** Improved the functionality of the "review user logs" button. It now links directly to logs relevant to the specific user, considering the new audit log system. Future enhancements will include email-based log searches. [iglocska]

### Changes
- **PyMISP Update:** Updated PyMISP to the latest version. [Raphaël Vinot]
- **Decaying Model Formulas:** Enhanced error handling by catching undefined indexes in decaying model formulas. [Sami Mokaddem]
- **Attributes Search:** Added support for sorting by `publish_timestamp` and introduced the `X-Skipped-Elements-Count` header to improve pagination during REST searches. [Benni0]
- **Reverse Proxy Handling:** Fixed issues with base URL handling for reverse proxies, eliminating problematic redirects. Special thanks to Mitch Germansky for the extensive debugging. [iglocska]
- **MISP Components Update:** Updated MISP Object, Galaxy, and STIX components to their latest versions. [Alexandre Dulaunoy, Christian Studer]

### Fixes
- **STIX 2 Import:** Updated the STIX 2 parsers following recent changes in MISP-STIX. [Christian Studer]
- **Base URL Setting:** Adjusted the priority order in `beforeFilter` to avoid redis errors during benchmarking. [iglocska]
- **Image Helper:** Allowed for variable-width organization logos without overlapping text. [iglocska]
- **Workflow Module:** Ensured correct type return if redis fails to load during `workflow:getEnabledModules`. [Sami Mokaddem]
- **Settings Management:** Fixed multiple issues related to changing instance settings, including improvements to CLI checks. [iglocska]
- **Attribute Search Ordering:** Reverted ID-based sliding window ordering due to performance concerns. [iglocska]

### Other
- Merged several development branches to integrate recent changes, updates, and fixes from various contributors. Notably, the branches related to attribute search order, skipped elements count, and environment dependencies were integrated into the main branch. [iglocska, Christian Studer, Sami Mokaddem, Alexandre Dulaunoy, Stefano Ortolani, Andras Iklody]

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt). Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!

