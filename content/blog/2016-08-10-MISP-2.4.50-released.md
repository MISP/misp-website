---
title: MISP 2.4.50 released including new features, security and bug fixes.
banner: /img/blog/misp-small.png
date: 2016-08-10
layout: post
---

<p>A version of MISP has been released: 2.4.50 including many bug fixes, updates and improvements.</p>

* New export and import MISP module framework in MISP. You can now write your own Python modules for
import and export without touching the MISP core software. Samples modules are available in [misp-modules
repository](https://github.com/MISP/misp-modules/tree/master/misp_modules/modules).
* A XSS vulnerability has been fixed into the handling of the external feed.
* New feature to view the public attributes of an event.
* Multiple fixes in the caching exports (useful for large exports).
* New SSO plug-in Shibboleth based.
* Many other fixes.

Thanks to all the contributors and especially the new ones who joined us at our first hackathon.

For more details check the [Changelog](http://www.misp-project.org/Changelog.txt).

