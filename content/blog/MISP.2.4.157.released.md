---
title: MISP 2.4.157 released including some usability fixes following the large changes of 2.4.156 along with some improvements
date: 2022-03-25
layout: post
banner: /img/signed-sync.png
---

We are pleased to announce the immediate availability of MISP v2.4.157, following a series of bug fixes as a quick follow up to 2.4.156.

As a reminder, MISP v2.4.156 included several critical vulnerability fixes, as such, **we highly encourage everyone to update to this version as soon as possible**. It also brought several new important features that help communities ensure the veracity of their most critical shared data.

# Fixes to the authkey handling

Manage auth keys of your team as an org admin, until now this feature was broken and org admins had to log in as their automation / sync users in order to generate new keys. This is no longer the case, simply view the user you wish to create a new key for and do it directly from the interface or via the API. Keep in mind that org admins can only create keys for non administrator users.

Thank you to @oivindoh for pointing this shortcoming out.

# Fix to a breaking bug with event publishing

Due to a bug introduced by a regression in 2.4.156, publishing events ended up not pushing events with sharing groups to remote instances. This is now resolved and for this in itself we already highly recommend updating to this version. Full instance pushes and pulls were not affected. Neither were events that didn't rely on sharing groups as their distribution model.

Thank you to @treyka for finding the bug.

# New setting introduced to disable event lock checks

Sometimes the addition of certain features, whilst having good intentions, ends up being more annoying that useful. In these cases, unless it's something absolutely hindering, we still do not want to modify the default behaviour of MISP over night. Such is the case with the event lock checks, which provide warnings on the event view that another user is also editing the event, a simple warning to users that their event's state may be outdated. 

This functionality is rather verbose when it comes to logging, gets in the way of debugging and can cause session persistence issues in certain cases. As such we've introduced a new setting to disable the functionality and unless you or your community are especially attached to it, we recommend heading over to the server settings and disabling it via the `MISP.disable_event_locks` setting. 

Thanks to @github-germ and @packet-rat for pointing the annoying nature of this feature out.

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core.

