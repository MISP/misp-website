---
title: MISP 2.4.115 released (aka CVE-2019-16202 and sync speed improvement)
date: 2019-09-10
layout: post
banner: /img/blog/community-view.png
---

# MISP 2.4.115 released

A new version of MISP ([2.4.115](https://github.com/MISP/MISP/tree/v2.4.115)) with a major security fix (CVE-2019-16202) and various small improvements has been released. We strongly recommend all MISP users update to this version.

## Fixed major performance blocker in sync

- fix based on the insights of @RichieB2B, the hero we need, not the one we deserve
- added orgc_uuid to the minimal event index
- added handlers for it on the pull side
- when pulling from old instances the new functionality is skipped, resulting in the behaviour we had pre-patch
- instances on both sides of the sync are encouraged to update, especially if the slow pulls are causing issues

## API and export

- [export] Add a proper filename to the event restsearch API's output to make downloading events a bit more convenient, fixes #4905.
- [stix2 import] Dealing with the case of named pipe attribute being imported from custom object.
- [stix2 export] Avoid fails with named pipe export as custom object.  

## Many fixes and error handling improvement

Thanks to Jakub Onderka for the tireless review of the code and all the fixes. For a complete overview, check the [complete changelog is available](https://www.misp-project.org/Changelog.txt).

## CVE-2019-16202 - Vulnerability in MISP version <= 2.4.114

### Conditions to be vulnerable

Any MISP instance version 2.4.114 or below with sync users or organisation administrators allowing incoming synchronisation connections are affected.

### Details

By requesting the /servers/index endpoint via the API, authenticated sync and org admin users have access to all synchronisation servers configured, including the API keys used.

The vulnerability was caused by a combination of 3 separate issues:

- The decision to allow sync users and org admins to have access to the server index was flawed, the idea was that they could assist with finding misconfigurations towards their home instance
- The API and the UI code paths handled the query that fetched the server list differently, with the restriction for org admins / sync users missing on the API side
- The API keys were included in the output via the API, not taking into the account that users besides site admins could have access to the functionality

This allows these users to pivot to the remote instances and authenticate using the acquired sync user keys.

### Mitigation

If patching immediately is not an option, whitelisting the IPs of incoming sync accounts to their respective MISP instance IPs avoids any abuse with the obtained keys, though for large sharing communities, this mitigation is not recommended.

### Fix

Upgrade to a version of MISP that has tightened the access control for the vulnerable endpoint (>= 2.4.115). This remedies any future attempts to abuse the vulnerability.

The 2.4.115 release version also introduces tools that ease the purging of the potentially exposed keys, along with logging attempts to access the vulnerable functionality.

The fix itself removes the access of all users besides the site admin to the /servers/index end-point and thus removes the necessity to deal with issue 2 or 3 identified in the details.

Site administrators are encouraged to reset all org admin / sync user API keys via the new reset functionality found at the top of the /admin/users/index page, or by POSTing an empty request to /users/resetAllSyncAuthKeys as a site administrator or executing the reset via the CLI command: `/var/www/MISP/app/Console/cake resetSyncAuthkeys [sync_user_id]`

Administrators are also encouraged to remotely reset their API keys on instances where the above is not executed by the administrators, by navigating to /servers/index on their own instance and issuing a remote reset for their API keys. This will conveniently issue a reset on the remote instance and store the new key in the sync connection.

### Credits

Guenaëlle De Julis and Céline Massompierre from CERT-XLM of Excellium Services.

### Timeline

- 2019-09-06 16:25:47: Vulnerability report received from CERT-XLM
- 2019-09-06 20:25:02 [TLP:amber]: MISP Project confirmed vulnerability to CERT-XLM along with notifying them of an internal fix being ready for co-ordinated publication, scheduled for 2019-09-09 13:00
- 2019-09-09 13:07:00 [TLP:green]: Co-ordinated limited release, patch released and tagged to GitHub and all known MISP community users notified and encouraged to notify their constituents
- 2019-09-10 [TLP:white]: CVE ID assignment, publication of tagged version, publishing of this advisory, release of blog post describing the vulnerability

# Acknowledgement

We would like to reiterate the importance of continuous security testing and the reporting of findings. Without the diligent work of security professionals in our community, we would have an infinitely harder time of squashing potential vulnerabilities. Thanks again to everyone that has helped us make MISP more secure.

If you have found a vulnerability in MISP and would like to get in touch with us, please read our [vulnerability disclosure notice](https://www.misp-project.org/security/).

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements.

