---
title: MISP 2.4.174  
date: 2023-07-31
layout: post
banner: /img/blog/dash-new.png
---

# MISP Workflows

We had the pleasure of being invited to participate in [GeekWeek](https://www.cyber.gc.ca/en/geekweek/geekweek-8) with the main objective of streamlining the identification of false positives and simplifying the process of building workflows. We developed new modules for both the enrichment and the workflow systems and introduced self-contained blueprints acting as building block to make the creation of complexe IoC curation pipeline feels like a breeze.
In addition, this release includes numerous little UI/UX treats for the workflow system hoping to provide a more efficient and user-friendly experience.

Overall, the following work was carried out:
- 5 new workflows modules related to tagging enrichment & curation
- 3 new enrichment modules to improve false-positive detection from different services
    - Many thanks to (TinyHouseHippos)[https://github.com/TinyHouseHippos] for adding support of [Google Safe Browsing](https://safebrowsing.google.com/) and [AbuseIPDB](https://www.abuseipdb.com/)!
- 9 new workflow-blueprints using the above module to make the curation of incoming data a simple task
- Many quality of life improvements for the workflow editor interface

## Curation blueprints

To give an idea of what these blueprints look like, let's have a look at `Flag false-positive tripping over warninglists`.

![Blueprint `Flag false-positive tripping over warninglists`](/img/blog/2.4.174/blueprint-falsepositive-warninglist.png)

In few words, here what's going on:
1. The system integrates warninglist hits in the data
2. Attributes having a hit on a warninlist of type `false_positive` are kept, the others are filtered out
3. Depending on the configuration, the `to_ids` flag will be disabled or kept as is
4. Tags are attached accordingly marking matching IoCs as false-positive

It should be noted that every curation blueprints are configurable in the sense that they might execute differently based on the tags (coming from the [`misp-workflow` taxonomy](https://github.com/MISP/misp-taxonomies/blob/59ec473a5f7a44755a6098890a1ee290487bfc53/misp-workflow/machinetag.json)) attached to the event. For example, if the tag `misp-workflow:mutability="allowed"`is set on the event, the workflow will modify existing data. This can be very usefull for servers acting as a clearing hub or forwarding vetted data to other instances. While if the tag isn't present, data won't be touched and only `local` tags will be applied if needed.

Should you be interested to check the 9 new blueprints out, the complete list can be found here: https://github.com/MISP/misp-workflow-blueprints#curation-blueprints.



## Workflow editor improvements

Now let's have a quick look at the changes that have been integrated to speed up edition, simpifly complex tasks and make things a little more intuitive.

##### Multiple values in filtering
Added support of two new operators `Any value` and `Any values from`, allowing `OR` condition in logic blocks.
![](/img/blog/2.4.174/wf-multiple-values.gif)

##### Quick insert on existing links
UX improvement to help users to quickly insert blocks on existing connections.
![](/img/blog/2.4.174/wf-quick-insert.gif)

##### Collapsible sidebar
UX improvement to support smaller screens.
![](/img/blog/2.4.174/wf-collapsible-sidebar.gif)

##### Hash-path picker
UX improvement and helper tool to facilitate crafting complex hash path.
![](/img/blog/2.4.174/wf-hashpath-picker.gif)

##### Frame nodes
UI feature to enable framing node that achieve a specific actions. Especially usefull when using blueprints.
![](/img/blog/2.4.174/wf-frame-node.gif)


## MISP Objects and Relationships

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Updated threat actor database to include Budapest Convention relation.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

## MISP taxonomies

For more details, the [misp-taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
