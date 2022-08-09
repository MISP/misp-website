---
title: MISP 2.4.160 released with new workflow feature, new correlation engines and many major improvements 
date: 2022-08-08
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of MISP v2.4.160. With the August summer-holiday season kicking into high gear, we have a very special release for you all, containing a long list of major new features, improvements and general quality of life improvements.

Unlike we do normally, this time around we're preparing separate blog posts for some of those major features, so follow the links below to read up on in-depth descriptions of each.

# Workflows

Something that has been in the works for quite some time now is finally hitting a release version of MISP, as of 2.4.160, we have the first release of the built in workflow system released.

This system allows you to use an easy to use, yet extremely powerful graphical interface to modify how MISP handles certain tasks such as event publishing, user enrollment, synchronisation, etc., by adding additional logical steps in their respective executions, utilising a module system similar to what was already common to MISP from enrichment subsystems, exports as well as imports.

This is merely the first step (or leap rather) towards customising and sharing custom workflows, stay tuned for new features, improvements as well as triggers and modules in the near future.

Head over to the [README](https://github.com/MISP/misp-workflow-blueprints/blob/main/README.md) as well as a nifty [slide deck](https://www.misp-project.org/misp-training/a.12-misp-workflows.pdf), to find out what this incredibly powerful can do for you and your community. If you would like to see a video demonstration of how it works, narrated by @mokaddem's soothing voice, head over to the [vlog entry](https://www.youtube.com/watch?v=XSvUwwu1Ku0) over at youtube.

{{< youtube XSvUwwu1Ku0 >}}

# New correlation engine

One of the biggest pain points as of recently has been our dated and rather bloated correlation engine, which could easily bring a long running MISP instance to its knees when certain highly correlated data sources were synchronised.

As of 2.4.160, we now have 2 brand new correlation engines at your disposal, with the old engine being retired immediately. Please be aware that upgrading to the current version will regenerate your correlations using the new engine, something that can take quite a long time (on our largest instance it took a whopping 40 hours!). With that said, we can assure you it's well worth the wait and should resolve several long standing performance bottlenecks as well as heavily cut down on the space requirements for your data.

For more information, on the new engines, their differences, the various new support tools as well as what benefits you should expect, head over to the [dedicated blog post](https://github.com/MISP/MISP/blob/2.4/docs/correlations.rework.md).

# STIX 2 library reworks

There has been a massive amount of work going into the STIX 2.x library rework, bringing us closer and closer to having a full mapping of everything expressable. We're collaborating with CISA and Mitre to ensure that MISP can both express and understand STIX to its fullest extent.

For more information, head over to the [release notes](https://github.com/MISP/misp-stix/releases/tag/v2.4.160) over on the MISP STIX library's repo.

# Mermaid support for Event reports added

![A screenshot in MISP in the event report to add mermaid diagrams](/img/blog/mermaid-misp.png)

Writing custom reports has become more and more popular, but one annoyance has been the lack of a way to depict graphs and flow charts without relying on external tools to create those (and share them as images for example). Using [Mermaid](https://mermaid-js.github.io), you now have a nifty tool to build graphs out of simple markdown directly in the event report editor.

# Various other improvements

A long list of other improvements, affecting the performance and stability of the platform as well as improvements to existing features. Head over to the changelog for a detailed list of changes. 

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core. Additional changelogs are available for [misp galaxy](https://www.misp-project.org/Changelog-misp-galaxy.txt), [misp-taxonomies](https://www.misp-project.org/Changelog-misp-taxonomies.txt), [misp-objects](https://www.misp-project.org/Changelog-misp-objects.txt) and [misp-modules](https://www.misp-project.org/Changelog-misp-modules.txt)

