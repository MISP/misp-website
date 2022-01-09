---
title: MISP 2.4.138 released (Many improvements including CISA.gov AIS dynamic marking functionality, RSIT galaxy added)
date: 2021-02-10
layout: post
banner: /img/blog/rsit-3.png
---

# MISP 2.4.138 released

We have released 2.4.138, the latest release for MISP along with an update of the JSON libraries.

Besides that, several usability and performance issues have been resolved along with a host of small improvements, additional API improvements, etc. Make sure that you read the [detailed changelog](/Changelog.txt) to see all the improvements. Improvements include the use of the threat level for the alert filtering, many bugs fixed in the event graph and many others.

# Nested Galaxy Element generator

We have a new tool that allows you to take nested JSON documents and convert it to galaxy cluster elements using a dot delimited format. If you ever want to quickly encoding existing nested data for your custom galaxies, this should make your life easier. This functionality was integrated for the support of the [Automated Indicator Sharing (AIS) from DHS/CISA.gov](https://www.cisa.gov/sites/default/files/publications/AIS%20Brokering%20Between%20the%20Non-Federal%20Entities%20Sharing%20Community%20and%20the%20Federal%20Entities%20Sharing%20Community.pdf) to include dynamic marking. The functionality can be reused for many different use-cases.

![](https://raw.githubusercontent.com/MISP/misp-training/main/a.10-galaxy-2.0/pics/json-view.png)
![](https://raw.githubusercontent.com/MISP/misp-training/main/a.10-galaxy-2.0/pics/tabular-view.png)

# RSIT galaxy added with MITRE ATT&CK 

[Reference Security Incident Taxonomy Working Group](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force), is a joint initiative for CSIRTs to produce a reference taxonomy for the CSIRT community. A new version of RIST has been integrated into MISP along with a complete set of relationships with MITRE ATT&CK, thanks to the [galaxy 2.0 feature](/2020/12/16/MISP.2.4.135.released.html) in MISP. Thanks to [Koen Van Impe](https://www.cudeso.be/) for this new updated galaxy.

![](/img/blog/rsit-3.png)
![](/img/blog/rsit-3.png)
![](/img/blog/rsit-3.png)


# Acknowledgement

We would like to thank all the [contributors](/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](/objects.html), [misp-taxonomies](/taxonomies.html) and [misp-galaxy](/galaxy.html)
.

As always, a detailed and [complete changelog is available](/Changelog.txt) with all the fixes, changes and improvements.

