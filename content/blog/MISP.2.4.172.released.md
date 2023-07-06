---
title: MISP 2.4.172 released with new TOTP/HTOP authentication, many improvements and bugs fixed 
date: 2023-06-13
layout: post
---

We are pleased to announce the immediate availability of [MISP v2.4.172](https://github.com/MISP/MISP/releases/tag/v2.4.172) with new TOTP/HTOP authentication, many improvements and bugs fixed.

# Time-based and Single Use One-time password support (TOTP / HOTP) 

New TOTP support are now included in MISP. This functionality works in two modes:

- (default) optional (T/H)OTP for users (when required libraries are installed)
- (optional) mandatory (T/H)OTP for all users

When logging in the user can enter either the TOTP or the HOTP (one time paper token)
OTP attempts are also limited by the Bruteforce component. So multiple failed attempts will result in a temporary blocking. HTOP is available for recovery and also for security environment where mobile phone or electronic devices are forbidden.

User can generate TOTP through their Profile page:
![image](https://github.com/MISP/MISP/assets/1073662/ceba1dba-694d-4c77-bc08-232766e6dd00)

A QR code is generated and they need to fill in the code once to confirm all is well:
![image](https://github.com/MISP/MISP/assets/1073662/69e5362c-02f5-4707-b429-6797683d9bdf)
Then they get directed to the page containing their next 50 HOTP/paper tokens:
![image](https://github.com/MISP/MISP/assets/1073662/22cd6bdd-5309-4e53-9411-b6cb19ff73c6)

Their profile then shows they have a token, they can also check again what their paper tokens are:
![image](https://github.com/MISP/MISP/assets/1073662/faeb286f-eddb-4e98-ba91-ec315f198b14)
So does the admin page (the phone icon)
![image](https://github.com/MISP/MISP/assets/1073662/0a9af5cd-99cb-467e-af4a-36a8d57438c3)
(org)Admins can delete the secret of a user:
![image](https://github.com/MISP/MISP/assets/1073662/90c5977d-c6e9-445d-bc5f-81e9ac0ed35a)

When they have their TOTP secret, after user/pass window they are prompted to enter the or the HOTP.
![image](https://github.com/MISP/MISP/assets/1073662/4dc4fbc2-ad7b-4b90-a83b-9a6034e9f64f)

Logging is also generated:
![image](https://github.com/MISP/MISP/assets/1073662/4952cf9b-8605-46f3-9aba-bfe2b1a179b5)

The `MISP.totp_required` security setting allows enforcing TOTP for the whole MISP instance.

In this case users are invited to store their TOTP at next login. They cannot access any other page until they validated the TOTP. The server wide parameter has a beforeHook to ensure the required PHP libraries are installed, as otherwise the admin might lock themselves out.

Requires 2 additional PHP libraries to be installed through composer: 
- "spomky-labs/otphp"
- "bacon/bacon-qr-code"

# TAXII preview 

TAXII integration is still in its infancy in MISP, but with the current release we aim to make the process of interacting with a TAXII server more in-depth. Prior to the current release, you could add a taxii server connection, pointing to a collection and initiate a filtered push of your MISP data - however, there was no way to view the contents of the collection nor to see your data reflected after a push.

The current release aims to complete the work on the initial TAXII push functionalities, with a TAXII browser built into the tool along with various fixes to bugs and issues that were reported to the prior implementation.

## Adding a TAXII connection

Simply add a TAXII server via the the TAXII connections interface (sync actions -> List TAXII servers)

![image](https://github.com/MISP/MISP/assets/3668672/7ba0b218-bc3f-49f0-83d5-74e1bcd6abc5)

Make sure that you configure the filters used to decide which of your events should be pushed to the given server. Creating a local tag such as "taxii_push" allows you to manually control and label events to be pushed as in the example above. 

Once the basic server information has been encoded, use the wrench button on top of the `API root` field to populate the dropdown with the valid options found on the TAXII server and once you've selected a root, click the wrench on top of the `collection` field to populate it and select the target colleciton for the connection.

![image](https://github.com/MISP/MISP/assets/3668672/ac855fb5-18ff-48a2-8925-f1e3087879bc)

## Viewing the connection and browsing the contents

Once a connection is established, you can view the connection object and list its collections and the objects in the configured collection on the taxii_servers/view/[id] endpoint, as follows:

![image](https://github.com/MISP/MISP/assets/3668672/dd294504-abf6-4a74-9b8c-ddde16e4c5f9)


You can view individual collections and browse their contents, paginating through all STIX objects (the default collection is shown at the bottom of the page). By clicking view on a STIX object, you can view the STIX 2.1 JSON object in full:

![image](https://github.com/MISP/MISP/assets/3668672/31fa49c9-e1ad-43b8-96e1-b88acaee1fe6)

Simply use the push button on the TAXII server index to initiate a push to the selected collection with the pre-defined filters.

## Dashboard

- [usage data widget] added a global caching for attribute counts.

# Other updates and changes in the MISP project

## Bugs/performance

- [performance] fix for events with large numbers of attributes and
  multiple tags from the same taxonomy. [iglocska]
  - the taxonomy conflict checks were causing multiple issues:
  - non taxonomy tags were counted as a taxonomy with namespace ''
  - once we identified a tag pair that could cause a conflict (same taxonomy) we loaded the taxonomy into redis
    - however, in order to see if we already have the taxonomy loaded, we went to redis to do a GET
    - In the case of 1 million attributes with at least 1 tag pair, at the minimum this means 1 million GETs on reddit with an event
  - Resolution
    - remove the checks for non taxonomy tags
    - store the identified taxonomies temporarily on the model itself in memory
      - only go to redis when the model doesn't have the taxonomy cached in memory
      - still using the old approach when dealing with multiple small events
  - thanks to @github-germ for flagging the issue

## Roles and permission

- [role permission] updated for viewing feed correlations
  - added additional role permission
  - allows hiding feed correlations from users
    - main purpose is with very large instances, to reduce the load on redis


## MISP Objects and Relationships

- New object for [scanning result](https://www.misp-project.org/objects.html#_scan_result) (network and local). 
- New object for [CrowdSec Threat Intelligence - IP CTI search.](https://www.misp-project.org/objects.html#_crowdsec_ip_context).
- New object for [Cobalt Strike Beacon Config](https://www.misp-project.org/objects.html#_cs_beacon_config)

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Updated [attck4fraud](https://github.com/MISP/misp-galaxy/blob/main/clusters/attck4fraud.json) updated with [EAST data](https://www.association-secure-transactions.eu/). 
- Updated [Malpedia](https://github.com/MISP/misp-galaxy/blob/main/clusters/malpedia.json) information.
- Updated [Threat actor](https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json) database.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- Updated warning-lists for all sources.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

## MISP taxonomies

- Updated [workflow taxonomy](https://www.misp-project.org/taxonomies.html#_workflow).
- Added [information-origin](https://www.misp-project.org/taxonomies.html#_information_origin) Taxonomy for tagging information by its origin: human-generated or AI-generated.
- Added [crowdsec](https://www.misp-project.org/taxonomies.html#_crowdsec) - Crowdsec IP address classifications and behaviors taxonomy.

For more details, the [misp-taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
