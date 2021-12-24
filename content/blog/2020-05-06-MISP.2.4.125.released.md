---
title: MISP 2.4.125 released (aka self-registration feature and feed improvements release)
date: 2020-05-06
layout: post
banner: /img/blog/timeline-sight.png
---

# MISP 2.4.125 released

A new version of MISP ([2.4.125](https://github.com/MISP/MISP/tree/v2.4.125)) has been released. This version includes various improvements including a major refactoring of the feed system, the addition of OTP, a new inbox system to allow for self-registration, sightings in the timeline visualisation and many more improvements.

# new inbox system and self-registration feature

If you operate a large community such as an ISAC, the creation of new users can be a tedious task. The new self-registration feature allows organisations to receive and review registration before creating the real user in MISP.

- if the feature is enabled, users can unauthenticated send a registration request to MISP
  - request includes information on desired org and some privileges (sync / org admin / publisher)
- requests land in the inbox, admins can inspect the registration requests
  - they can accept/discard them individually or en masse
  - users will be notified of their credentials automatically
  - quick user creation if the user asks for an org that doesn't exist yet
  
# E-mail based OTP

To add a second layer of security, OTP has been made available thanks to the contribution of @Golbark. If you would like to use this feature, please enable it via your security settings. Users will receive tokens via e-mail that they need to provide each time they authenticate and start a new session with MISP.

# Feeds index refactoring and new features

- added the ability to select an orgc ID for CSV/freetext feeds
  - all events created from this feed will carry the selected orgc_id

- Refactored the index fully
  - using the factories
  - better warnings against the dangerous new feed each pull setting
  - event index search added
  - several settings cleaned up / made more clear

- auto reload of default feed configuration disabled, fixes #2542, fixes #5789
  - added a button / endpoint to handle that instead to allow for the deleted default feeds to stay delete


# Debugging improvement

- [database] New MySQL data source added for debugging.
  - MySQLObserver datasource added - prepends all queries with the requested controller/action and user ID for better debugging

May improvements were done in this MISP release, for a complete overview, you can have a look at the [complete changelog](https://www.misp-project.org/Changelog.txt).

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.


