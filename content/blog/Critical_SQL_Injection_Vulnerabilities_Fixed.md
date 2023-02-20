---
title: Critical SQL injection vulnerabilities in MISP (fixed in v2.4.166 and v2.4.167) 
date: 2023-02-20
layout: post
---

# Critical SQL injection vulnerabilities in MISP (fixed in v2.4.166 and v2.4.167)

## Introduction

As of the past 2 months, we've received two separate reports of two unrelated SQLi vector vulnerabilities in MISP that can lead to any authenticated user being able to execute arbitrary SQL queries in MISP.

We consider this to be a critical vulnerability and chose to follow a **silent fix procedure** working with the reporters. We normally only do this in extreme cases where we want to ensure that the community has plenty of time to update once the vulnerability is patched and before we would publicly announce it. We also wanted to make sure that we have a way to urge the community to update, so we have been elevating the criticality of other minor vulnerabilities that were reported in the same time-frame.

### The method we chose for the fix was simple: 

- fix the vulnerability, disguise it as a refactor / minor fix
- fix another security issue/vulnerability that is unrelated
- release a critical bug fix, overplaying the importance of the minor secondary issues resolved
    - blogging / tweeting / tooting / contacting groups / organisations to upgrade on the basis of the latter

The two SQLi vulnerabilities in question were as follows.

## 1. Vulnerability in the order parameter used in several indexes

As reported by Jakub Onderka. Besides being the hero that we all know him to be for bringing the code base up to snuff, he also found one of the most obnoxious vulnerabilities with this one that shows our misunderstanding of a standard framework function's provided protections. Kudos to him for finding it!

### Description:

Basically, we allowed users to provide custom field ordering for certain endpoints such as RestSearch. These were set using url parameters in the format of /order:field_name. However, contrary to our belief, the "order" parameter of the CakePHP find() function is not SQLi safe and thus we've introduced field allow-listing for any occurrence of custom order fields. Any sorting relying on /sort:field_name/direction:asc|desc is unaffected and safe. 


#### Reported:
2022/11/25 by Jakub Onderka

#### Fixed:
2022/11/28 - release version: v2.4.166

#### Fixed via:

- [https://github.com/MISP/MISP/commit/afbe08d256d609eee5195c5b0003cfb723ae7af1](https://github.com/MISP/MISP/commit/afbe08d256d609eee5195c5b0003cfb723ae7af1)
- [https://github.com/MISP/MISP/commit/a73c1c461bc6f8a048eae92b5e99823afd892d1e](https://github.com/MISP/MISP/commit/a73c1c461bc6f8a048eae92b5e99823afd892d1e)

#### CVE ID: [CVE-2022-48329](https://cvepremium.circl.lu/cve/CVE-2022-48329)

## 2. Vulnerability in the search parameters of any index using the CRUD component

As reported by Dawid Czarnecki of Zigrin Security on behalf of the Luxembourgish army. Dawid has been reporting findings continuously for a long period of time now, with Zigrin Security developing their own tooling for detecting vulnerabilities that we quite frankly would never have caught ourselves.

Massive thanks to Dawid and his team!

### Description:
The CRUD component would allow for custom search parameters to be passed - and whilst the lookup values are SQLi safe and properly sanitised, the field names themselves are not. With some clever forged requests, these can be abused. We have moved to allow-listing these field names. 

#### Reported:
2022/12/12 by Dawid Czarnecki

#### Fixed:
2022/12/22 - release version: v2.4.167

#### Fixed via:

- https://github.com/MISP/MISP/commit/1edbc2569989f844799261a5f90edfa433d7dbcc
- https://github.com/MISP/MISP/commit/206f540f0275af2dd2a86275abc199df41e72a21

#### CVE ID: [CVE-2022-48328](https://cvepremium.circl.lu/cve/CVE-2022-48328)

## General note on software vulnerabilities

As always, we always welcome and highly encourage MISP users to run their own vulnerability assessments, code review and penetrating testing of MISP codebase and to let us know about the outcomes so that we can make MISP as secure as it can be. Thanks again to all that have reported vulnerabilities in the past. 

For information on how to submit your findings, please refer to [https://misp-project.org/security/](https://misp-project.org/security/)
