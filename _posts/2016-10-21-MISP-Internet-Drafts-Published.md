---
title: MISP Internet Drafts Published
layout: post
featured: /assets/images/misp-small.png
---

We recently released two Internet-Drafts describing the MISP format:

 - [misp-core-format]() - the core JSON format of MISP which describes the Event format including meta-information, attributes, shadow
 attributes. In addition, the Manifest format which bundles MISP events is described.
 - [misp-taxonomy-format]() - The MISP taxonomy JSON format describes how to define a machine tag namespace in a parseable format.

The [misp-rfc](https://www.github.com/MISP/misp-rfc) project was started to better document and describe MISP formats. The specifications are
based from the real implementation cases (**code is law**). As we received many requests of vendors or software developers willing to integrate MISP.
The specifications were designed to support organizations willing to use and integrate MISP formats in their product or software.

The MISP standard specifications were not designed before implementation. The process to write the specifications from the current implementations
in the MISP projects (e.g. MISP core, PyMISP, PyTaxonomies and misp-taxonomies). We strongly believe that having implementation in parallel helps
to refine the MISP standards and reducing the potential overload of unused specifications.

The current specifications are published in [misp-rfc](https://www.github.com/MISP/misp-rfc) repository.
We welcome contributions and especially any issues regarding the interpretation of specification.

Additional specification documents will be published later like the misp-galaxy-format, misp-modules-protocol and misp-collaborative-voting-format.
