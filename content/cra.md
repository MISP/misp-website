---
layout: page
title: CRA Requests to MISP Project
permalink: /cra-request/
toc: true
---

# CRA and MISP Project

**The first point to clarify is that CRA compliance for your commercial offering is, first and foremost, the responsibility of the economic operator placing that product with digital elements on the market. It is not automatically the responsibility of the upstream open-source project.**

The MISP project does not sell your product, place your MISP-based appliance or bundle on the market, or operate the commercial offering for which you are requesting compliance information.

If your organisation **packages, redistributes, integrates, substantially modifies, or markets MISP as part of a product with digital elements**, you need to assess the CRA obligations applicable to that product and to your role as manufacturer or other economic operator.

We are of course happy to provide the technical information that already exists upstream, but **the MISP project cannot provide a free CRA conformity assessment, compliance package, or technical documentation for a commercial product that another organisation manufactures, integrates or places on the market.**

### Security and vulnerability handling

Nevertheless, **security is a core concern of the MISP project**.

The project has an established Coordinated Vulnerability Disclosure (CVD) process operated by **CIRCL**, the organisation leading MISP development. CIRCL also operates as the CNA/GNA responsible for vulnerability coordination and publication for the open-source project.

This means that vulnerability reporting, coordination, remediation and publication are already part of the upstream project's security processes.

### SBOM and dependency information

If you require an SBOM for the upstream MISP source code, this information can already be generated **free of charge directly from the GitHub repository** using GitHub's dependency graph and SBOM export functionality:

https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/export-dependencies-as-sbom

GitHub can export the dependency information in SPDX format.

**Please keep in mind that an upstream SBOM is not automatically the SBOM of the product you provide to your customers.**

If you package MISP together with additional components, change dependencies, add an operating system, containers, plugins, libraries or other software, or otherwise create your own distribution, **you should review and generate the SBOM corresponding to the product that you actually deliver**.

In other words, we can provide information about **our upstream software**; you remain responsible for documenting **your resulting product**.

### Need specific assistance?

If your organisation needs additional development, integration work, technical documentation or other customised assistance to support its compliance activities, the MISP project also provides **MISP Professional Services (MPS)**:

https://www.misp-project.org/professional-services/

MPS provides professional services and custom development around MISP. **Purchasing professional expertise is distinct from asking the upstream open-source project to assume the CRA compliance obligations of a commercial product built or distributed by another organisation.**

We are therefore very happy to help with MISP itself, its security processes, upstream technical information and, where appropriate, professional services.

**What we cannot do is take responsibility for the CRA compliance of a third party's commercial MISP-based product or provide that compliance work free of charge on their behalf.**

