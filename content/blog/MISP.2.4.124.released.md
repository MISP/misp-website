---
title: MISP 2.4.124 released (aka the dashboard, auditing improvements)
date: 2020-04-06
layout: post
banner: /img/blog/dashboard.png
---

# MISP 2.4.124 released

A new version of MISP ([2.4.124](https://github.com/MISP/MISP/tree/v2.4.123)) has been released. This version includes various improvements including a new multiline widgets in the dashboard, auditing improvements and many bugs fixed.

# Dashboard and widget improved

The dashboard has been improved along with a host of bugs fixed. A UI for the multiline widget has been introduced.
<img src="/img/blog/2.4.124/multiline-demo.gif" alt="Multiline Demo" width="700"/>
The new interface provides users a simple way to manipulate basic graph components. It includes legends, tooltips, auto-resize, clickable labels and a full support of the 2 most common x-axis: linear and time-based.

You can query the chart to see the delta between two datapoints by selecting the first then the last points. A summary will then be presented.
<img src="/img/blog/2.4.124/multiline-brush-delta.png" alt="Multiline delta between points" width="700"/>


Finally, the widget styling is largely configurable. In addition to the `time_format` and the abscissa type, you can define other parameter influencing how the graph should be presented to the users
<img src="/img/blog/2.4.124/multiline-config.png" alt="Multiline Configuration sample" width="700"/>

# (auditing) Individual user monitoring

- Site admins can set the monitoring flag on a user if the feature is enabled on the instance
- Monitored users will have all requests logged along with POST bodies
- Keep in mind this functionality is quite heavy and intrusive - so use it with care. The idea is that this allows us to track potentially malicious users during an investigation

# New community CogSec Collab disinformation

MISP includes the possibility to advertise your MISP information sharing community, don't hesitate to propose your community to gain some visibility. We added "[The Cognitive Security Collaborative operates as a sharing community dedicated to information operations](/2020/03/26/cogsec-collab-misp-community.html)".

# COVID-19 MISP

COVID-19 MISP is a MISP instance retrofitted for a COVID-19 information sharing community, focusing on two areas of sharing:

- Medical information
- Cyber threats related to / abusing COVID-19

The information sharing community has a low barrier of entry, everyone can contribute and use the data. By default, the information is classified as TLP:WHITE for broader distribution and usefulness. [For more information and joining the COVID-19 MISP community](/covid-19-misp/)

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


