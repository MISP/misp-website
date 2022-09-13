---
title: Periodic summaries - Visualize summaries of MISP data
date: 2022-09-12
layout: post
banner: /img/blog/periodic-summary/periodic-summary-1.png
---

# Periodic summaries - Visualize summaries of MISP data

As of version 2.4.162, MISP includes a **periodic summary** feature allowing users to consult a summary based on a requested time-frame for data the user has access to.

Currently, the summaries can be generated for 3 different periods: `daily`, `weekly` and `monthly` and then sent to all users that subscribed to one of these periods.

In addition to allowing users to subscribed, they can also specify filtering options such as tags or distribution level to be applied when generating the report.

![Periodic summary](/img/blog/periodic-summary/periodic-summary-2.png)
![Periodic summary](/img/blog/periodic-summary/periodic-summary-3.png)

## Viewing summaries
There are currently two ways to view a periodic summary:
- In the MISP ui, click on the *View periodic summary* link when browsing events
- Subscribe to one of the available period and receive the summary directly in the user's mailbox

## [admin] Automatic delivery
In order to have MISP send periodic mails, the periodic notification task should be scheduled. One of the easiest way to do it is to use CRON jobs.

For example, this entry could be added
```text
0 6 * * * /var/www/MISP/app/Console/cake Server sendPeriodicSummaryToUsers >/dev/null 2>&1
```

The `sendPeriodicSummaryToUsers` should be called daily and takes care of sending the summaries to every users that subscribed to the `daily` notification.

For the `weekly` and `monthly` periods, they will be sent on Mondays and on the first day of each months respectively.

More details about setting the scheduled task and the CLI tool can be found in the *automation page* (/events/automation).


## [admin] Extending / Overriding

Site administrators of MISP can also extend, replace or remove parts of a periodic summary. 

The notification templates can be found under the `app/View/Emails/html` folder. Each template extend a parametrized common template allowing site-admins to customize the summary to fit theirs needs.

For example, the default `monthly` notification template is configured to only include a subset of the *detailed summary* section.

Options and developer documentation can be found in the `notification_common.ctp` file.
