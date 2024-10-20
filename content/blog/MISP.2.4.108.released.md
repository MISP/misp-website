---
title: MISP 2.4.108 released (aka copy-paste-and-sync feature)
date: 2019-06-05
layout: post
banner: /img/blog/anothergraph.png
---

A new version of MISP ([2.4.108](https://github.com/MISP/MISP/tree/v2.4.108)) has been released with a host of new features, improvements and bugs fixed. We strongly advise all users to update their MISP installations to this latest version.

# New main features

## A copy-paste-and-sync function

A new tool has been added in MISP to create MISP sync configuration objects in JSON format from the user-interface. This significantly improved the setup of synchronisation links between MISP instances. The synchronisation can now be set up (in addition to the standard setup) in 2 simple steps:

- Use your sync user account on the remote MISP instance to extract the sync config in one click;
- paste the sync config into your own instance as a site-admin user.

That's it, you have the synchronisation configured.

## Improved "paranoid" logging

During the [enforce](https://securitymadein.lu/news/ceis-securitymadein-lu-enforce-project/) training session in Paris, law enforcement officers mentioned the need for LEA to have extensive audit mechanisms in regards to information read and user access in general. A new optional paranoid logging functionality has been added to log any queries from the user-interface and the API of a MISP instance. The feature has two sub-features, allowing administrators to configure their MISPs to log the POST/PUT bodies as well as the ability to force paranoid log entries to skip being stored in the database, instead publish the gathered information exclusively via one of the various pub-sub channels (such as ZMQ, Kafka or ElasticSearch ZMQ, Kafka or ElasticSearch) or via syslog.


## API

- New logical 'AND' for tag filters has been added in restSearch API.
- Added object_relation as a filter for both the event/attribute restSearch functions.
- [restResponse] Added documentation for adding tags on Objects.
- [API] Allow more flexibility on the return content types. [iglocska]

# Various improvements

- [logging] Added verbose logging to the server sync test throwing an unexpected error.
- [bug] A bug in the event graph displayed broken icons to some specific browsers. The bug was fixed by updating font-awesome 5.8.2 and the loading of font-awesome in visjs.
- [event:view] Correctly display title to large by truncating (+ellipsis).
- [diagnostic:view] Improved visibility of the `updateAllJson` update button.
- [object:add] Disable the first select's option when adding a new row.
- [object:add] Added empty option support in select inputs when creating an object.
- [UI] Event lock concatinating quoted empty strings.
- [UI] Double sanitisation of org view fixed, fixes #4704.
- [sync] Further fixes to the deleted flag changes breaking things.
- [authkey] Fixed The authkey variable (Viper should work again) (#4694)
- [sync] Critical bug fixed that blocked attributes from being included in a push. due to the change to the deleted flag that was not reflected in the way we prepare events for the synchronisation
- [UI] Add the create server sync description menu to the server list.
- [sync] whitelist fields that can be added via the JSON config.
- [UI] Invalid redirect fixed.
- [organisation:view] Fixed spinner when viewing events from an org.
- [API] Weird responses from JSON objects fixed when data returned is empty.
- [API]  Wrong JSON output when /events/index returns empty result, fixes #4690.
- [UI] Org index filter fixed.
- [stix2 import] Fixed external domain & x509 patterns import.
- [freetext import] Fixed shadow attribute import.
- [event:view] Correctly support the new `deleted` parameter behavior.
- [UI] Fixed checklocks polluting the top bar.
- [enrichment:popover] Correctly fadeout when clicking on the close button.
- [STIX] STIX upload fixed for API use.
- [galaxy:add] Consider both model names when doing a mass cluster addition.
- [installer] Checksum checker has been fixed and improved.
- [stix import] Fixed email attachments parsing.
- [stix import] Supporting multi attachment attributes for the email object.

# MISP modules

Many new [MISP modules](https://github.com/MISP/misp-modules) were added such as Joe Sandbox integration.

# MISP galaxy, object templates and warning-lists updated

[MISP galaxy](/galaxy.html), [MISP object templates](/objects.html) and [MISP warning-lists](https://github.com/MISP/misp-warninglists/) have been updated to the latest version.

New [default feeds](/feeds/) were added in MISP. Don't hesitate to contact us if you have any idea for new feeds.

We would like to thank all the contributors, reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](http://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.



