---
title: MISP 2.4.162 released with a new periodic notification system, workflow updates and many improvements
date: 2022-09-13
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.162](https://github.com/MISP/MISP/releases/tag/v2.4.162) with a new periodic notification system, workflow updates
and many improvements. 

In addition to the MISP v2.4.162 release, [misp-guard](https://github.com/MISP/misp-guard) has been released which is a [mitmproxy](https://mitmproxy.org/) addon that inspects the events that MISP is attempting to synchronize with external MISP instances via `PUSH` or `PULL` and applies a set of customizable rules defined in a JSON file. This is a complementary tool to support MISP users having to interconnect MISP instances between highly sensitive networks.

# Periodic notification system

As of version 2.4.162, MISP includes a **periodic summary** feature allowing users to consult a summary based on a requested time-frame for data the user has access to.

Currently, the summaries can be generated for 3 different periods: `daily`, `weekly` and `monthly` and then sent to all users that subscribed to one of these periods.

In addition to letting users subscribe to a period, they can also specify filtering options such as tags or distribution levels to be applied when generating the report.
The summary can then be sent via email or viewed in the MISP User-Interface.

![Periodic summary](/img/blog/periodic-summary/periodic-summary-2.png)
![Periodic summary](/img/blog/periodic-summary/periodic-summary-3.png)

For more information, check out the [Periodic summaries - Visualize summaries of MISP data](/2022/09/12/2022-09-12_periodic_notifications.html/) blog.

# Workflow improvements

- Added diagnostic support and support of arbitrary URL for webhook module.
- New Microsoft teams module based on the webhook module. 
- New email notification module to send email to a list of MISP users including [Jinja templating](https://jinja.palletsprojects.com/en/3.1.x/).
- Tag name can now be used in workflows.

For more details about MISP Workflow, check out the [training materials](https://www.misp-project.org/misp-training/a.12-misp-workflows.pdf).

# MISP core improvements

- Allow option to delete tags on event sync prior to soft-delete tag implementation.
- API/[Event:restSearch] Added option `event_tags` to filter for eventTag only. 
- API/RestSearch - Added support of `static` parameter to produce a static HTML output.
- Syslog/logging  for certain log entries vital information was omitted by the syslog. If no custom message is specifically set for the log entry, the change field is included.
- Enforce UUIDs uniqueness on MISP data back-end.

# Bugs fixed

- [correlations] save the distribution state of the event before/after saving it, fixes #8528.
- [attribute tags] removal broken, fixes #8567. 
- Class 'Folder' not found #8544. 
- Create unique SIDs for email attributes in NIDS export.

Thanks to all the contributors and users reporting bugs to make the software better.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core. 

Many improvements in the MISP galaxy and especially the threat-actor galaxy. There is a detailed [changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt).

Improvement in the `false-positive` taxonomy and many other taxonomies. There is a detailed [changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt).

Multiple objects were updated and added, for [more details](https://www.misp-project.org/Changelog-misp-objects.txt).



