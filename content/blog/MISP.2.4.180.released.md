---
title: MISP 2.4.180 released with a new security user login profile feature, bugs fixed and many improvements. 
date: 2023-12-20
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/workflow-blue.png
---

MISP 2.4.180 released with a new security user login profile feature, bugs fixed and many improvements.

# New

- [api] added X-MISP-AUTH as an alternative header to Authorization,
  fixes #9418. [iglocska]

# Changes

- [VERSION] bump. [iglocska]
- [workflows] restored 7.2 and 7.3. [iglocska]
- [user login profile] old version compatibility. [iglocska]
- [event index] hover over ID will show the info field, generally more
  useful than the threat level. [iglocska]

# Fix

- [login] fixes bad fix and catches first login after update.
  [Christophe Vandeplas]
- [revert] dumb check. [iglocska]
- [compatibility] make the ancient gods happy. [iglocska]
- [user login profile] skip checks for ancient php versions. [iglocska]
- [Attribute:EditPostProcessing] Make sure the ID is set. [Sami
  Mokaddem]
- [attribute:editPostProcessing] Fixed typo in condition preventing tags
  to be detached. [Sami Mokaddem]
- [attributes] type field added to editable fields. [iglocska]
- [RPZ] export custom parameters ingored, fixes #9420. [iglocska]
- [Attribute:editPostProcessing] Fixed sighting capture. [Sami Mokaddem]
- [Attribute:EditPostProcessing] Make sure the ID is set. [Sami
  Mokaddem]
- [attribute:validation] Typo in function name. [Sami Mokaddem]
- [attribute:editPostProcessing] Fixed typo in condition preventing tags
  to be detached. [Sami Mokaddem]

# Other

- Merge remote-tracking branch 'origin/develop' into 2.4. [Christophe
  Vandeplas]
- Merge branch 'develop' into 2.4. [iglocska]
- Merge branch '2.4' into develop. [iglocska]
- Merge branch 'develop' into 2.4. [iglocska]
- Revert "chg: [workflows] restored 7.2 and 7.3" [iglocska]

  This reverts commit 206d2af439ae22c35a41568b4dc79562f2cb29e4.
- Merge branch '2.4' into develop. [iglocska]
- Merge branch '2.4' of github.com:MISP/MISP into develop. [Sami
  Mokaddem]
- Merge remote-tracking branch 'origin/2.4' into develop. [Sami
  Mokaddem]
- Merge branch '2.4' of github.com:MISP/MISP into develop. [Sami
  Mokaddem]
- Merge branch 'develop' of github.com:MISP/MISP into develop.
  [iglocska]
- Merge branch 'develop' of github.com:MISP/MISP into develop. [Sami
  Mokaddem]
- Feature/user login profiles2 (#9379) [Christophe Vandeplas, iglocska]

  * new: [userloginprofiles] start over with previous code

  * fix: [user_login_profiles] fixes catching up the backlog

  * chg: [userloginprofile] email to org_admin for suspicious login

  * chg: [userloginprofile] only inform new device

  * chg: [userloginprofiles] view_login_history instead of view_auth_history

  * chg: [userloginprofile] make login history visually better

  * chg: [userloginprofile] inform admins of malicious report

  * fix: [userloginprofile] cleanup

  * fix: [userloginprofile] fixes Attribute include in Console

  * fix: [userloginprofile] db schema and changes

  * chg: [CI] log emails

  * chg: [PyMISP] branch change

  * chg: [test] test

  * fix: [userloginprofile] unique rows

  * fix: [userloginprofile] unique rows

  * chg: [cleanup]

  * Revert "chg: [PyMISP] branch change"

  This reverts commit 3f6fb46fee9745437998fc013a97af874679c87b.

  * fix: [userloginprofile] fix worksers with monolog=1.25 browcap=5.1

  * fix: [db] dump schema version

  * fix: [CI] newer php versions

  * fix: [composer] php version

  * fix: [php] revert to normal php7.4 tests

  ---------
- Merge branch '2.4' into develop. [iglocska]

