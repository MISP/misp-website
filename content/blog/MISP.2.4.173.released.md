---
title: MISP 2.4.173 released with various bugfixes and improvements 
date: 2023-07-11
layout: post
banner: /img/blog/dashboard-new.png
---

We are pleased to announce the immediate availability of [MISP v2.4.173](https://github.com/MISP/MISP/releases/tag/v2.4.173) with a new password reset feature, along with a host of quality of life improvements and fixes.

# Password reset self-service

We have added a new functionality allowing administrators to enable user self-service for forgotten passwords. When enabled, users will have an additional link below the login screen, allowing them to enter their e-mails and receive a token that can be used to reset their passwords. 

The feature requires the user to have a valid encryption key and the lifetime of the tokens is hard-coded to be 10 minutes. 

![image](https://github.com/MISP/MISP/assets/3668672/9ca9953b-d0a6-4fdb-a262-d6481e698bd7)

# New dashboard widgets

The dashboard has seen another round of improvements, with various fixes and new widgets added. 2.4.173 includes the following new widgets:

- Logarithmic events/org chart (Thanks @vincenzocaputo)
- ATT&CK heatmap widget 

Additionally, you can now download the raw data used to feed each widget.

![image](https://github.com/MISP/MISP/assets/3668672/e91159db-00cd-407d-a302-7a0221f5179f)

# Security fixes

2 vulnerabilities have also been resolved:

## Stored XSS via select page titles

Improper sanitisation of user-controlled data ending up in view titles lead to stored XSS

Huge thanks to Ulaş Deniz İlhan from Zigrin Security (absolute heroes at discovering vulnerabilities in MISP!)

[CVE-2023-37307](https://cve.circl.lu/cve/CVE-2023-37307)

## RCE via uploaded certificates

Malicious administrators could trigger RCE by uploading a well crafted file as an SSL certificate for the sync connection.

[CVE-2023-37306](https://cvepremium.circl.lu/cve/CVE-2023-37306)

Additional information on the vulnerability can be found at the excellent [blog post from synacktiv](https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle)

Huge thanks to @righel for finding and fixing the vulnerability!

# A long list of fixes

As always, we have been diligent with including a long list of fixes, including for issues with server sync certificate handling, url encoding of spaces in search strings, CSRF errors and much more! For a detailed list of fixes, please refer to the [changelog](https://www.misp-project.org/Changelog.txt).


## MISP Objects and Relationships

- Updated relationships to include the ones used by [LookyLoo](https://lookyloo.circl.lu)
- Many improvements following [OASIS STIX TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti) 

For more details, the [misp-object changelog](https://www.misp-project.org/Changelog-misp-objects.txt) is available.

## MISP Galaxy

- Updated threat actor database to include Budapest Convention relation.

For more details, the [misp-galaxy changelog](https://www.misp-project.org/Changelog-misp-galaxy.txt) is available.

## MISP warning-lists

- New warning list digitalSide.IT warninglist added.
- Updated warning-lists for all sources.

For more details, the [misp-warninglists changelog](https://www.misp-project.org/Changelog-misp-warninglists.txt) is available.

## MISP taxonomies

For more details, the [misp-taxonomies changelog](https://www.misp-project.org/Changelog-misp-taxonomies.txt) is available.

# Don't forget to follow us on Mastodon

The MISP projet has its own Mastodon server [misp-community.org](https://misp-community.org/) - don't forget to follow @misp@misp-community.org on the fediverse. Core contributors of MISP can sign-up if they wish to have an account.

# MISP Professional Services

[MISP Professional Services (MPS)](https://www.misp-project.org/professional-services/) is a program handled by the lead developers of MISP Project, in order to offer highly skilled services around MISP and to support the sustainability of the MISP project. This initiative is meant to address the policy requirements of companies/organisations requiring commercial support contracts. Don't hesitate to get in touch with us if you need specific services.
