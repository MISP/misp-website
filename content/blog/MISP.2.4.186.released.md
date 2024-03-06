---
title: MISP 2.4.186 released with analyst data feature including analyst notes, opinions and relationships. 
date: 2024-03-06
layout: post
tags: ["MISP", "Threat Intelligence", "release", "analyst notes", "analyst opinions"]
banner: /img/blog/fin7.png
---

We are pleased to announce the immediate release of MISP 2.4.186, which includes two major new feature called "Analyst Data" and "Collections" along with an extension to the MISP standard format.

# Analyst Data Feature

The Analyst Data feature is an extended and shareable set of capabilities that allows analysts to share and add their own analysis to any MISP event.

The Analyst Data feature comprises three main new features:

- Adding an Analyst Note to any element in MISP, such as Event, Event Report, Object, Attribute, or Galaxy Cluster.
- Adding an Analyst Opinion with a rating (between 0 and 100) to any element in MISP, such as Event, Event Report, Object, Attribute, Galaxy Cluster, or Analyst Note.
- Adding an Analyst Relationship from/to any element in MISP with a specified relationship type.

This enhancement provides highly flexible capabilities for analysts to describe information about specific details. Analyst Data, similarly to Events and Galaxy clusters, are first class citizens, respecting ownership and distribution mechanisms as well as being synchronisable between MISP instances.

For a quick overview, the below screencast can give you an idea of the analyst data feature in action:

{{<video src="/img/blog/analyst-data/analyst-data-note.mp4" title="Analyst data note" >}}

{{<video src="/img/blog/analyst-data/analyst-data-opinion.mp4" title="Analyst data opinion" >}}

{{<video src="/img/blog/analyst-data/analyst-data-relationship.mp4" title="Analyst data relationship" >}}

# Collections Feature

The new collection feature allows users to create collections for organising data shared by the community. These collections can be categorised based on commonalities or as part of the research process. Collections are treated as first-class citizens and adhere to the same sharing rules as, for example, events do. You can create your own collection and share it with your partners on the same MISP instance.

# Other fixes

Details changes are available in [Changelog](https://www.misp-project.org/Changelog.txt).

# Don't forget to follow us on Mastodon

The MISP project has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Galaxy

Major improvement were performed in the MISP galaxy including major updates in the [threat-actor knowledge-base](https://www.misp-galaxy.org/threat-actor/), the [surveillance vendors](https://www.misp-galaxy.org/surveillance-vendor/). Additional updates were done to add the relationships in the [MISP galaxy](https://www.misp-galaxy.org/) public website.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.

