---
title: MISP 2.4.121 released (aka the security release)
date: 2020-02-12
layout: post
banner: /img/blog/t-misp-overview.png
---

# MISP 2.4.121 released

A new version of MISP ([2.4.121](https://github.com/MISP/MISP/tree/v2.4.121)) has been released. This version is a security/bug fix release and users are highly encouraged to update as soon as possible. Besides that several issues were resolved and some new functionalities were added.

# Security issues

The new version includes fixes to a set of vulnerabilities, kindly reported by Dawid Czarnecki. For details, see the attached CVE information.

- A reflected XSS in the galaxy view [CVE-2020-8893](https://cve.circl.lu/cve/CVE-2020-8893)
- ACL wasn't always correctly adhered to for the discussion threads [CVE-2020-8894](https://cve.circl.lu/cve/CVE-2020-8894)
- Potential time skew between web server and database would cause the brute force protection not to fire.[CVE-2020-8890](https://cve.circl.lu/cve/CVE-2020-8890)

Whilst investigating the above, we have identified and resolved other issues with the brute force protection:

- Missing canonicalisation of the usernames before issuing the bruteforce entry.[CVE-2020-8891](https://cve.circl.lu/cve/CVE-2020-8891)
- PUT requests for the login were skipping the protection. [CVE-2020-8892](https://cve.circl.lu/cve/CVE-2020-8892)

Whilst the issues identified are not deemed critical, it is highly suggested to update and inform your peers to follow suit.

# Additional sync pull filters

One of the most annoying side-effects of the synchronisation mechanism was the potential unfiltered flow of massive amounts of aged-out data when first pulling from a newly connected community. We have added a simple filter option when configuring sync connections to pass event index filters along with the sync requests. An example would be to limit the publish age of pulled data to the desired time frame (for example: Only fetch data that is at maximum 2 months old).

# New background worker configuration loading

Background workers were loading the server wide configurations on startup, meaning that changes to server settings would not be reflected by any background processed job unless the workers were restarted. A new helper resolves this and loads the configuration on each job execution (Thanks to @RichieB2B for reporting the issue).

# Memory envelope improvements

When fetching data from MISP, it tries to cluster the data into smaller chunks and fetch it piece by piece to avoid memory exhaustion and to be able to serve the data anyway. The new release improves on the estimation, avoiding potential memory exhaustions with larger data-sets. Potential issues are also logged from here on.

# SQL schema check improvements

Various improvements to both better inform administrators about potential issues along with remediation scripts

# A host of other improvements

A massive list of improvements to the usability of MISP, with a special thank you to Jakub Onderka again for his endless stream of improvements.

# MISP Objects templates

We received a significant number of [new object templates](/objects.html) to describe specific additional use cases including disinformation, media and also improved HTTP representation.

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


