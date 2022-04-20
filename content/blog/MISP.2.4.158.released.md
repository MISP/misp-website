---
title: MISP 2.4.158 security fix and general improvement release
date: 2022-04-20
layout: post
banner: /img/blog/graph-syria.png 
---

We are pleased to announce the immediate availability of MISP v2.4.158. This release includes a series of security fixes and as such **we highly encourage everyone to update to this version as soon as possible**.

Thanks to Dawid Czarnecki of Zigrin Security for the in-depth penetration test and its findings and thanks to the Luxembourg Army for financing the penetration test. This is the follow up to the Cerebrate penetration test also conducted by Zigrin Security on behalf of the Luxembourg Army, as described [here](https://www.cerebrate-project.org/2022/01/27/Cerebate-version-1.4-released.html).

# Security fixes

Several security issues have been resolved, head over to [the security page](https://www.misp-project.org/security/) for a detailed break-down of the advisories including the associated CVEs. Whilst most of the vulnerabilities listed are mitigated by requiring compromised high privilege accounts, we nevertheless advise all users to update their instances as soon as possible.

- Phar deserialisation
  - [Global fix](https://github.com/MISP/MISP/commit/0108f1bde2117ac5c1e28d124128f60c8bb09a8e)
  - [Individual additional mitigations](https://github.com/MISP/MISP/commit/93821c0de6a7dd32262ce62212773f43136ca66e)
- [XSS in LinOTP login](https://github.com/MISP/MISP/commit/9623de2f5cca011afc581d55cfa5ce87682894fd)
- [XSS in Galaxy clusters](https://github.com/MISP/MISP/commit/107e271d78c255d658ce998285fe6f6c4f291b41)
- [XSS in organisation fetchSGOrgRow](https://github.com/MISP/MISP/commit/ce6bc88e330f5ef50666b149d86c0d94f545f24e)
- [XSS in Event graph via tags](https://github.com/MISP/MISP/commit/bb3b7a7e91862742cae228c43b3091bad476dcc0)
- [XSS in Cerebrate view](https://github.com/MISP/MISP/commit/60c85b80e3ab05c3ef015bca5630e95eddbb1436)
- [Password confirmation bypass](https://github.com/MISP/MISP/commit/01120163a6b4d905029d416e7305575df31df8af)

## Announcement of a silent fix of phar deserialisation RCE in a previous release (v2.4.156)

As of the previous security release (v2.4.156), based on the pentest conducted by Ianis BERNARD of the NATO Cyber Security Centre, a high criticality vulnerability was also identiefied. We have opted for a silent fix to the critical vulnerability whilst upgrading the announced criticality of the other security fixes included in the release.

This is an extreme measure that we take whenever we want to ensure that the community is both aware that they do need to update as soon as possible whilst not drawing attention to the actual critical vulnerability. If you have followed our guidance over the past month to update you are already safe - if you are running a MISP instance below 2.4.156 **we highly encourage you to update to the latest version as soon as possible**. 

- [Phar deserialisation silent fix](https://github.com/MISP/MISP/commit/8eff854fce1fea1521f33fffc2440df5b7e5c410)

# Custom email templates

Added the ability to override some of the standard e-mail templates with custom ones, just drop the templates mirroring the naming convention of the existing ones in `/var/www/MISP/app/View/Email/text` and `/var/www/MISP/app/View/Email/html` into `/var/www/MISP/app/View/Email/text/Custom/` and `/var/www/MISP/app/View/Email/html/Custom/`. Currently supported templates: alert, password_reset.

# RestSearch improvements

Fixing a baffling oversight on our side, thanks to Tom King we can now search by sharing groups besides just distribution levels. 

# A long list of refactors and bugfixes

Massive thanks to Jakub Onderka for the continuous refactoring, simplifying and cleaning up of the code-base. For a full list of all the improvements that are part of this herculean effort, refer to the [changelog](https://www.misp-project.org/Changelog.txt)

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core.

