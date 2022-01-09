---
title: MISP 2.4.126 released (Spring release edition)
date: 2020-06-04
layout: post
banner: /img/blog/dashboard.png
---

# MISP 2.4.126 released

A new version of MISP ([2.4.126](https://github.com/MISP/MISP/tree/v2.4.126)) has been released a while ago, though we have forgotten to publish a blog post about it - thanks to @coolacid for the reminder. This version includes a security fix and various quality of life improvements.

# Security fix - fixed XSS

[Fixed a persistent XSS](https://cve.circl.lu/cve/CVE-2020-13153) (CVE-2020-13153) that could be triggered by correlating an attribute via the freetext import tool with an attribute that contains a javascript payload in the comment field. By hovering over the correlation, the analyst encoding the information would have the exploit triggered.

Thanks to @JakubOnderka for reporting it!

# Tool to generate the communities webpage

Being able to find the right communities is key when utilising MISP. Thanks to @cvandeplas for implementing this!

# experimental CLI only force pull method added

It allows an administrator to issue a special kind of pull via the API that overwrites the local data with that on the remote, no matter which one is newer. No additional data gets deleted, but modifications will get reverted to the remote's state. This tool is meant as a last resort if things have gone awry with unwanted local modifications.

# A host of quality of life fixes

A long list of improvements, fixes and new functionalities have been added, make sure to check out the changelog for an exhaustive list!

# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html).

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.


