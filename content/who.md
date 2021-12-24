---
layout: page
title: Who
permalink: /who/
toc: true
---

## Who is behind the MISP project?

The core team behind the MISP project is composed of motivated people who think that information sharing can be improved and supported by creating
practical open source tools, open format and practises. The current team is composed of:

* Alexandre Dulaunoy [@adulau](https://twitter.com/adulau)
* Andras Iklody [@Iglocska](https://twitter.com/Iglocska)
* Andrzej Dereszowski [@deresz666](https://twitter.com/deresz666)
* Christian Studer [@chrisred_68](https://twitter.com/chrisred_68)
* Christophe Vandeplas [@cvandeplas](https://twitter.com/cvandeplas)
* David Andre [@elhoim](https://twitter.com/elhoim)
* Deborah Servili [@deltalimasierra](https://twitter.com/deltalimasierra)
* Gerard Wagener
* Raphaël Vinot [@rafi0t](https://twitter.com/rafi0t)
* Sami Mokaddem [@mokaddem_sami](https://twitter.com/mokaddem_sami)
* Sascha Rommelfangen [@rommelfs](https://twitter.com/rommelfs)
* Steve Clement [@SteveClement](https://twitter.com/SteveClement)

and many [contributors](/contributors)! Join us!

### Contact

If you have any enquiries or willing to contribute or support the project, don't hesitate to contact the team at [info@misp-project.org](mailto:info@misp-project.org).

## Integrated Services and Products with MISP

Many third-parties and organizations provide services or software to integrate with MISP via [misp-modules](https://github.com/MISP/misp-modules), [MISP API](https://www.circl.lu/doc/misp/automation/index.html) or [MISP data models]({{ "/datamodels" | prepend: site.baseurl | prepend: site.url }}).

Check out the [tools page]({{  "/tools" | prepend: site.baseurl | prepend: site.url }}).

## Research using MISP and Attribution

If you are writing an academic paper relying or using MISP, you can cite MISP with the following BibTeX entry:

~~~~
@inproceedings{wagner2016misp,
  title={MISP: The Design and Implementation of a Collaborative Threat Intelligence Sharing Platform},
  author={Wagner, Cynthia and Dulaunoy, Alexandre and Wagener, G{\'e}rard and Iklody, Andras},
  booktitle={Proceedings of the 2016 ACM on Workshop on Information Sharing and Collaborative Security},
  pages={49--56},
  year={2016},
  organization={ACM}
}
~~~~

### History

This project started around June 2011 when Christophe Vandeplas had a frustration that way to many IOCs were shared by email, or in pdf documents and were not parseable by automatic machines. So at home he started to play around with CakePHP and made a proof of concept of his idea. He called it CyDefSIG: Cyber Defence Signatures.

Mid July 2011 he presented his personal project at work (Belgian Defence) where the feedback was rather positive. After giving access to CyDefSIG running on his personal server the Belgian Defence started to use CyDefSIG officially starting mid August 2011.
Christophe was then allowed to spend some time on CyDefSIG during his work-hours, while still working on it at home.

At some point NATO heard about this project. On January 2012 a first presentation was done to introduce them in more depth to the project. They looked at other products that the marked offered, but it seemed they deemed the openness of CyDefSIG to be of a great advantage. Andrzej Dereszowski was the first part-time developer from NATO side.

One thing led to another and some months later NATO hired a full-time developer to improve the code and add more features. A collaborative development started from that date.
As with many personal projects the license was not explicitly written yet, it was collaboratively decided that the project would be released publicly under the Affero GPL license. This to share the code with as many people as possible and to protect it from any harm.

The project was then renamed to MISP: Malware Information Sharing Project, a name invented by Alex Vandurme from NATO. Nowadays, MISP is just called MISP as it's a generic platform for storing, sharing and working on intelligence at large.

In January 2013 Andras Iklody became the main full-time developer of MISP, during the day initially hired by NATO and during the evening and week-end contributor to an open source project.

Meanwhile other organisations started to adopt the software and promoted it around the CERT world.  (CERT-EU, CIRCL, and many others ...)

Nowadays, Andras Iklody is the lead developer of the MISP project and works for CIRCL.

As the MISP project expanded, MISP is not only covering the malware indicators but also fraud or vulnerability information. The name is now MISP, threat sharing which includes the core MISP software and a myriad of tools (PyMISP) and format (core format, MISP taxonomies, warning-lists) to support MISP.  **MISP is now a community project lead by a team of volunteers**.

The [full list of contributors](/contributors) is available on the MISP project page.


