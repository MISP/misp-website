---
title: MISP 2.4.150 released (The "Bloody PKI again" hotfix release)
date: 2021-10-12
layout: post
banner: /img/blog/letsencrypt-logo-horizontal.png
---

# MISP 2.4.150 released

MISP 2.4.150 released, including a new CA bundle to combat the issues with the Letsencrypt root CA expiration. This is a follow-up release to 2.4.149 and has no other major changes besides pointing to our own repository of the framework that includes the new CA bundle.

# Sync issues due to the expiration of a Letsencrypt root CA

As described in their [blog post](https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/#:~:text=On%20September%2030%202021%2C%20there,accept%20your%20Let's%20Encrypt%20certificate), Letsencrpyt had to retire an old Root CA, meaning that that SSL connections when synchronising MISP with other instances would fail if the remote side used letsencrypt. This update includes a new CA bundle that should help you avoid any issues with this.# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html)
.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

