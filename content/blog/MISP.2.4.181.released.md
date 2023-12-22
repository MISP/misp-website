---
title: MISP 2.4.181 hot fix release to disable by default the alert on suspicious login plus some minor fixes. 
date: 2023-12-21
layout: post
tags: ["MISP", "Threat Intelligence", "release"]
banner: /img/blog/workflow-blue.png
---

# MISP 2.4.181 hot fix release to disable by default the alert on suspicious login plus some minor fixes.

# Changes

- [tools:misp-delegation] Do not use self-documented expression in
  f-string anymore. [Sami Mokaddem]
- [version] bump. [iglocska]
- [warning-lists] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]
- [tests] search for errors in logs. [Christophe Vandeplas]
- [warning-lists] updated to the latest version. [Alexandre Dulaunoy]
- [misp-galaxy] updated to the latest version. [Alexandre Dulaunoy]

# Fix

- [Alert on suspicious logins] disabled by default. [iglocska]
  - requires logs table to be better indexed currently to not be a bottleneck (user_id and action fields)
  - Will be made default in an upcoming version once the performance issues are resolved
- [tests] fix path in logs_tests.sh. [Christophe Vandeplas]
- [tests] fixes path of logs_tests. [Christophe Vandeplas]
- [userloginprofiles] undefined variable #9424. [Christophe Vandeplas]
- [customauth] missing Class init fixes #9425. [Christophe Vandeplas]


