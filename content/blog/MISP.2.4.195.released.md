---
title: MISP 2.4.195 - hot summer olympic release 
date: 2024-08-09
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/object-collapse.png
---

## MISP 2.4.195 - hot summer olympic release

We are pleased to announce the immediate availability of MISP v2.4.195, a summer release aiming to introduce new features, fix a long list of reported bugs and deficiencies as well as give your servers a breather in the scorching summer heat by taking a load off your CPUs thanks to a set of impactful performance fixes. 

### Correlation rule system added

With the Olympics being in full swing, we too wanted to break our previous performance records and one of the biggest hurdles to overcome were the data-sets resulting from the ingestion of unerringly overlapping data-sources. This could be coming from daily internal digests from your own tooling all the way to feed providers, data from a single source could often end up being extremely noisy in terms of cross correlations. To combat this, we have added a new system that allows you to create correlation rules (better thought of as de-correlation rules) that instruct MISP to skip any correlations between groups of events.

#### How it works:

A site administrator can add a new de-correlation rule for example telling MISP to disqualify the creation of any correlations between individual events coming from the same organisation, such as a feed vendor or an internal organisation. Simply add a new rule, select the selector type (org_id, orgc_id, event_id, event_info) and add a list of values that shouldn't correlate.

![image](https://github.com/user-attachments/assets/4920cd7c-5869-4bec-b937-e7cc6c2f62d9)

For example, if you wanted to stop the creation of correlation between any event coming from the ACME organisation, simply look up their local user ID and pass it in a JSON list to the correlation rule, such as the example below:

selector_type: `orgc_id`

selector_list:
```
[
    15
]
```

If you wanted to create a list of non-correlating events (for example for events that come from freetext feeds, or from a script that ingests large amounts of data recurringly into the same event, use the following example below:

selector_type: `event_id`

selector_list:
```
[
    1,
    2,
    6,
    7
]
```

The event_info selector is a bit special in that it also allows for sub-string matching, using the % syntax used across the application. A simple example for a daily feed being excluded this way would look as follows:

selector_type: `event_info`

selector_list:
```
[
    "%s] Daily scan results",
    "Weekly scan results week #%"
]
```

Any event that is picked up by the selector will be blocked from creating correlations between one another, but unlike the prior feature of disabling correlations for an event, this will not prevent from said events from correlating with events not matching the selector. So if you do end up working on an incident that contains an indicator found in the daily scans in the example above, all the necessary correlations needed to point you towards the relevant scan results will be created. 


### OpenAPI spec updates

Thanks to Stefano Ortolani's (@ostefano) and Luciano Righetti's (@righel) relay race, digging into the OpenAPI spec, several issues and discrepancies have been resolved, further cementing the reliability of the spec as the de-facto tool for building integrations for MISP. Whilst we are firm believers of the implementation being law, it is absolutely crucial that the documentation reflects the reality of the internals and as such we encourage everyone to keep their eyes peeled for any errors in the spec and to let us know when there's some unsportsmanlike behaviour.

### Performance improvements for the attribute restsearch

As the outcome of a several week long heroic debugging effort with Mitch Germansky (@github_germ), we have managed to get to the bottom of several serious bottlenecks when it comes to the attribute restSearch. This will especially be noticeable for queries that end up returning large data-sets and when paginating the data to be returned. By enabling MISP to internally cluster searches when pagination parameters are provided by the user and by improving the heuristics of such queries, as well as with the switch to a sorted, ID based internal pagination rather than relying on mysql offsets, the search API has truly pulled up its spinnaker. 

We have also added a setting for a legacy restsearch behaviour, that will use joins rather than sub-queries in the attribute restsearch, we have seen this cause a massive performance boost on older mysql versions, so it might be worth experimenting with for anyone running on older database software versions.

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt). Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!

