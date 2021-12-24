---
title: MISP 2.4.72 released
date: 2017-04-14
layout: post
banner: /img/blog/misp-small.png
---

A new version of MISP [2.4.72](https://github.com/MISP/MISP/tree/v2.4.72) has been released including improvements and important bug fixes.

Improvements have been introduced to better support large MISP instances:

- Added new flag to events/restSearch to disable sharing group loading. The option sgReferenceOnly will only load the sharing_group_id
  not the actual sharing group data. This option helps organisation extensively using sharing groups at attribute level and doesn't use the
  nifty inherit distribution level.

- Minimal flag added to the event index used by the sync, greatly reduces the data fetched / transfered on the initial sync negotiation.

Various bug fixes and small improvements such as:

- Enforce the hide tag directive. Allow to hide tag at instance level by the MISP site admin and remove it from the tag selection from each user. The tag is not lost but just hidden from the user-interface.
- Toggling correlation at attribute level is now completely sane from a user perspective and allow the analyst to safely contact the mother ship while encoding the latest information known from Nation State Actor (There is almost no chance that this MISP release was coordinated with Shadow Brokers estimative-language:likelihood-probability="almost-no-chance").
- A bug in the organisation blacklisting was fixed.
- Fixed an issue where a proposal not having an assigned organisation broke the synchronisation on a pull.
- Multiple fixes and cleanup in the client side JavaScript.
- Other minor fixes [kindly reported by our users](https://github.com/MISP/MISP/issues) via GitHub.

[MISP galaxy](https://github.com/MISP/misp-galaxy) updated to the latest version, including new threat actors, exploit-kits and tool definitions.

There are also two agenda notifications that might be of interest to any MISP users, contributors or developers:

- A [MISP training](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) is foreseen in Luxembourg, the 29th June 2017. [Register](https://www.eventbrite.com/e/misp-training-june-edition-tickets-33663081182) as soon as possible if you want to join us.
- The [Open Source Security Software Hackathon](https://hackathon.hack.lu/) is a 2-days open hackathon to bring people and open source security software/tools together. It will take place 2-3 May 2017 in Luxembourg. The MISP core team will be there and if you want to join us to contribute feedback, ideas, code, documentation or anything that could improve information sharing and MISP.

The full change log is available [here](https://www.misp.software/Changelog.txt).

Don't hesitate to [open an issue](https://github.com/MISP/MISP/issues) if you have any feedback, found a bug or want to propose new features.
