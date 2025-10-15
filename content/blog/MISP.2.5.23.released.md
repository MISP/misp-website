---
title: MISP 2.5.23 Released with Enhanced Benchmarking, Many Bug Fixes, and Documentation Updates 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-10-15
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP 2.5.23 Release Notes - (2025-10-15)

We're rolling out MISP 2.5.23! This release is another step in our continuous effort to keep MISP running smoothly and effectively for the entire threat intelligence community. We know how crucial it is to have a reliable platform for sharing and analyzing threat data, and we're committed to delivering regular updates that bring you solid improvements and quick fixes.

Think of it this way: the cyber world doesn't stand still, and neither do we. Our regular releases, like this one, are all about making sure you have the best tools to keep up. We're not just adding new shiny things; we're also fine-tuning what's already there and squashing those annoying bugs. This means less headache for you and more focus on what matters – tackling those threats. So, dive into 2.5.23.

### New
*   `[first publication]` added to events.
*   `[benchmarks]` slow query log endpoint now accepts additional flags.
    *   Simple add `/{param}` to the `/benchmarks/sqlMetrics` endpoint's URL, with the following parameters currently implemented:
        *   `/explain` runs EXPLAIN on the SQL query
        *   `/analyze` runs ANALYZE on the SQL query (careful, this can be demanding, especially for unfiltered `/benchmarks/sqlMetrics` calls as it will iterate and execute analyze on each hit)
*   `[doc]` Added sharing group blueprints OpenAPI documentation.
*   `[preRelease]` function added to admin shell.
    *   Currently only has two functionalities:
        *   dump the current DB schema
        *   dump describeTypes.json
    *   Usage: `/var/www/MISP/app/Console/cake Admin preRelease`

### Changes
*   `[querystring]` bump.
*   `[version]` bump.
*   `[doc]` add sharing group blueprints viewOrgs OpenAPI documentation.
*   `[warning-lists]` updated.
*   `[misp-galaxy]` updated.
*   `[taxonomies]` updated to the latest version.
*   `[misp-stix]` Bumped latest version.
*   `[restsearch limits]` tuned for events / objects scopes.
    *   use some basic heuristics to get sane limits for the given endpoints
    *   fixed DB update
*   `[schema]` update.
*   Enable Test Pull Rules without pull rules set, change wording.
*   `[typo reintroduced]` for backwards compatibility.
*   `[user edit]` move the unsetting of the password field earlier.
    *   will help avoid screw ups later on, the change was introduced in the previous commit

### Fix
*   Workflow 'add tag' fails on events without existing tags.
    *   When pulling events from remote servers, the workflow's 'add tag' function could fail if the incoming event JSON lacked an existing 'Tag' array. This resulted in `array_merge()` receiving `null` instead of an array, causing a fatal error during event synchronization.
    *   This commit modifies `WorkflowBaseModule.php` to ensure that `$rData['Event']['Tag']` is always treated as an array (or an empty array if null), preventing `array_merge()` errors and ensuring workflow jobs complete successfully for events without pre-existing tags.
*   `[schema]` fix.
*   `[galaxy cluster restsearch]` don't barf back all results if an elements filter yields no results.
*   Revert.
*   `[object reverse join]` fixed if no contain parameters are provided.
*   `[reverse join fix]` for objects.
*   `[benchmark controller]` typo fix.
*   `[TagCollections]` correct permission check in removeTag().
*   `[tag index link]` fixed when clicking on tagged attributes.
    *   it redirected to `/attributes/search/tags:{id}` rather than `/attributes/index/tags:{id}`
*   `[user edit]` don't load related models when retrieving the user for editing via the GUI.
    *   it lead to fetching all related event meta information, which can be a memory hog
*   `[user edit]` don't load related models when retrieving the user for editing via the GUI, fixes #10509.
    *   it lead to fetching all related event meta information, which can be a memory hog
*   `[galaxy timestamps]` fixed when they are zeroed out.
    *   helps with tighter SQL modes
*   `[tag-collection:removeTag]` Reverted permission to allow deletion.
*   `[sharing group blueprints]` viewOrgs fixed for the API.
*   `[galaxy cluster restsearch]` improvements, fixes #3644.
    *   allow value/type searches again
    *   allow for substring searches (by using `%`) and multiple values
    *   Example:
        ```json
        {
            "value": ["%Sofacy%", "%APT-29%"]
        }
        ```
*   `[galaxy cluster restsearch]` fixes #3644.
    *   correctly use the elements parameter
    *   allow for substring searches
    *   allow for lists of values (that are ORed) within each element parameter such as:
        ```json
        "elements": {
            "foo": ["ba%", "xyz"]
        }
        ```
*   `[db settings]` fallback for cli_only settings when db_settings are enabled, fixes #10504.
    *   not ideal, but at least we'll be able to save those settings using the config file rather than not having any way to enforce them
    *   Keep in mind, this solution means that the setting will have to be set across all instances in a load balanced setup

### Other

*   Merge branch 'develop' into 2.5.
*   Merge branch '10423' into develop.
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge pull request #10508 from Wachizungu/add-sharing-group-blueprints-vieworgs-openapi.
    *   chg: `[doc]` add sharing group blueprints viewOrgs OpenAPI documentation
*   Merge branch '2.5' into develop.
*   Merge pull request #10510 from jsoref/update-pr-template-branch-to-2.5.
    *   chore: Update current release branch
*   Chore: Update current release branch.
*   Merge pull request #10512 from jsoref/update-issue-templates-branch-to-2.5.
    *   chore: Update code of conduct link for current release
*   Chore: Update code of conduct link for current release.
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge branch '10518' into develop.
*   General spelling corrections across the codebase for various terms and phrases.
*   Merge branch '10517' into develop.
*   Merge branch '10516' into develop.
*   Merge branch '10511' into develop.
*   Merge branch '10515' into develop.
*   Merge branch '10514' into develop.
*   Replace deprecated apt-key.
*   Merge branch '10513' into develop.
*   Updated various links including STIX format, old MISP automation page, OpenAPI spec of the MISP Automation API, start page, feed data, mkdocs site, MISP/MISP issues, and installation instructions for Ubuntu and RHEL/CentOS distributions.
*   Merge pull request #10431 from Frisb7/fix/removeTagPermission.
    *   fix: `[TagCollections]` correct permission check in removeTag()
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge branch '10506' into develop.
*   Added Debian 13 installer and minor fix to Debian 12 installer.
*   Merge branch 'develop' of github.com:MISP/MISP into develop.
*   Merge pull request #10505 from Wachizungu/add-sharing-group-blueprints-openapi-doc.
    *   new: `[doc]` Added sharing group blueprints OpenAPI documentation

### Authors
*   iglocska
*   Jeroen Pinoy
*   Alexandre Dulaunoy
*   Christian Studer
*   Luciano Righetti
*   Giacomo Guerzoni
*   frisb7
*   Sami Mokaddem
*   Andras Iklody
*   Josh Soref
*   alk4lo1d
