---
title: MISP 2.4.174 released with major workflows enhancement, new features and fixes
date: 2023-07-31
layout: post
banner: /img/blog/2.4.174/blueprint-falsepositive-warninglist.png
---

We are thrilled to announce the immediate availability of [MISP v2.4.174](https://github.com/MISP/MISP/releases/tag/v2.4.174) with significant workflow improvements, accompanied by a host of quality-of-life enhancements and bug fixes.

## General Improvements

- [Authkeys] We have added a new setting that allows the mandate of IP allowlist for advanced authkeys, providing an extra layer of security.
- [event:publishSightingsRouter] We have changed this from prio worker to default, resulting in better performance and reliability.

## Sync Fixes and Improvements

- [proposal] Sync fixes have been implemented, including the option to disable correlation/proposal to delete fields in the proposal index. This change ensures that the fields are included during pulls, preventing any discrepancies.
- [proposal accept] The issue related to deletions has been fixed, ensuring smooth proposal acceptance.
- [sightings] Now, sightings are only pushed via full push to avoid congestion, optimizing the syncing process.

## Bug Fixes

- [stix export] We have resolved issues related to empty inputs during STIX export, ensuring accurate and consistent results.
- [taxii_push] The `taxii_push` script now correctly passes the standard MISP JSON format to misp-stix, avoiding any format-related problems.
- [security] We now reset otp_secret on logout, enhancing security measures.
- [authkeys] The admin read-only key is now allowed to access audit logs (#9191), improving access control.

These updates and fixes mark a significant step forward for MISP, delivering a more efficient, secure, and reliable experience for our users. We encourage everyone to upgrade to the latest version to take advantage of these improvements. For more details and to access the release, please visit [MISP v2.4.174](https://github.com/MISP/MISP/releases/tag/v2.4.174). Thank you for your continued support and feedback, which has been instrumental in making MISP better with each release. For a more detailed overview of the MISP workflows and various MISP submodules/projects improvement check below:

# MISP Workflows improvements overview

We had the pleasure of being invited to participate in [GeekWeek](https://www.cyber.gc.ca/en/geekweek/geekweek-8) with the main objective of streamlining the identification of false positives and simplifying the process of building workflows. We developed new modules for both the enrichment and the workflow systems and introduced self-contained blueprints acting as building block to make the creation of complexe IoC curation pipeline feels like a breeze.
In addition, this release includes numerous little UI/UX treats for the workflow system hoping to provide a more efficient and user-friendly experience.

Overall, the following work was carried out:
- 5 new workflows modules related to tagging enrichment & curation
- 3 new [enrichment modules](https://github.com/MISP/misp-modules/) to improve false-positive detection from different services
    - Many thanks to (TinyHouseHippos)[https://github.com/TinyHouseHippos] for adding support of [Google Safe Browsing](https://safebrowsing.google.com/) and [AbuseIPDB](https://www.abuseipdb.com/)!
- 9 new workflow-blueprints using the above module to make the curation of incoming data a simple task
- Many quality of life improvements for the workflow editor interface

## Curation blueprints

To give an idea of what these blueprints look like, let's have a look at `Flag false-positive tripping over warninglists`.

![Blueprint `Flag false-positive tripping over warninglists`](/img/blog/2.4.174/blueprint-falsepositive-warninglist.png)

In few words, here what's going on:
1. The system integrates warninglist hits in the data
2. Attributes having a hit on a warninglist of type `false_positive` are kept, the others are filtered out
3. Depending on the configuration, the `to_ids` flag will be disabled or kept as is
4. Tags are attached accordingly marking matching IoCs as false-positive

It should be noted that every curation blueprints are configurable in the sense that they might execute differently based on the tags (coming from the [`misp-workflow` taxonomy](https://github.com/MISP/misp-taxonomies/blob/59ec473a5f7a44755a6098890a1ee290487bfc53/misp-workflow/machinetag.json)) attached to the event. For example, if the tag `misp-workflow:mutability="allowed"`is set on the event, the workflow will modify existing data. This can be very useful for servers acting as a clearing hub or forwarding vetted data to other instances. While if the tag isn't present, data won't be touched and only `local` tags will be applied if needed.

Should you be interested to check the 9 new blueprints out, the complete list can be found here: https://github.com/MISP/misp-workflow-blueprints#curation-blueprints.


## Workflow editor improvements

Now let's have a quick look at the changes that have been integrated to speed up edition, simplify complex tasks and make things a little more intuitive.

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
UI feature to enable framing node that achieve a specific actions. Especially useful when using blueprints.
![](/img/blog/2.4.174/wf-frame-node.gif)


## MISP Objects and Relationships

- New object to support [hhhash format](https://github.com/adulau/HHHash).
- Improved [scan-results](https://www.misp-project.org/objects.html#_scan_result) object.
- Improved [ja3s](https://www.misp-project.org/objects.html#_ja3s) object. 
- [relationships] Added some relationships defined in STIX 2.1 & updated some opposite relationships in consequence.
- New object templates to support [STIX 2.1 incident extension](https://github.com/MISP/misp-objects/pull/396).
- New object template for [AbuseIPDB](https://www.misp-project.org/objects.html#_abuseipdb).
- new object template for [Google Safe Browsing](https://www.misp-project.org/objects.html#_google_safe_browsing).

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Various updates in the [threat actor MISP galaxy](https://www.misp-project.org/galaxy.html#_threat_actor).
- Various automatic updates from Sigma galaxy.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- Improvement in the [CRL generation list](https://github.com/MISP/misp-warninglists/blob/main/tools/generate-crl-ip-domains.py).
- All the lists have been updated.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

## MISP taxonomies

- Minor improvements in the [cryptocurrency threat](https://www.misp-project.org/taxonomies.html#_cryptocurrency_threat) taxonomy and workflow taxonomy to support the new workflow features.

For more details, the [misp-taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

## MISP-stix

MISP-stix includes multiple improvements and bugs fixed.

For more details, the [misp-stix changelog](https://www.misp-project.org/Changelog-misp-stix.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
