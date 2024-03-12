---
title: Introducing Standalone Functionality to MISP Modules - A New Era of Flexibility and Efficiency 
date: 2024-03-12
layout: post
tags: ["MISP", "Threat Intelligence", "misp-modules", "modules"]
banner: /img/blog/all-modules.png
---

# Introducing Standalone Functionality to MISP Modules: A New Era of Flexibility and Efficiency

In the ever-evolving landscape of information security, the need for adaptable and efficient tools has never been greater. The MISP  project, known for facilitating the sharing of structured threat information, has taken a significant leap forward. We're excited to announce a pivotal enhancement to the misp-modules, a collection of modules for MISP, extending their functionality to operate not only as an integral part of MISP but also as a standalone web application. 

## What Are MISP Modules?

Before delving into the new features, let's recap what [MISP modules](https://github.com/MISP/misp-modules) are. MISP modules are a set of tools and functionalities designed to improve and extend the capabilities of the MISP platform. These modules (more than 200 modules) enable functions like importing data from external sources, exporting data in various formats, and conducting enrichment on existing data. Until now, these modules were primarily designed to be used within the MISP platform.

## The New Standalone Capability

Our latest update brings a groundbreaking change: [misp-modules](https://github.com/MISP/misp-modules) can now function independently of the MISP platform. This development means users can leverage the powerful features of misp-modules in a variety of new environments and scenarios, without the need for a full MISP installation.

## Benefits of Standalone misp-modules for analysts

- Flexibility and Versatility: Organizations can now utilize specific modules relevant to their needs, without using the entire MISP platform.
- Ease of Integration: Standalone modules can easily be integrated into other systems or workflows, making it a versatile choice for different analyst environments.
- Resource Efficiency: For users who require only specific functionalities, running misp-modules standalone saves system resources and simplifies operations.

## How Does It Work? 

The standalone version of misp-modules functions much like its integrated counterpart but without the need to interact with a MISP server. Users can directly interact with the modules through a user-friendly API, allowing a fast and easy access to the full range of capabilities from MISP modules.

The installation process is streamlined and can be done in less than 5 minutes as described in the [README file](https://github.com/MISP/misp-modules/tree/main/website) to ensure a smooth transition to the standalone functionality.

The existing integration with MISP modules and MISP is not affected and continues to work as expected.

### Overview

The default web interface show a common interface where you can perform queries on any modules exposed in misp-modules

![Home page](/img/blog/modules/1.png)

In the result view, multiple tabs can be used to see the results in different formats, such as structured MISP objects, raw JSON, or even Markdown output.

![Result page](/img/blog/modules/2.png)

Each query is saved in the database back-end, and a structured hierarchy is provided to enhance navigation and analysis. This hierarchy facilitates 'pivoting,' a process where analysts systematically explore related data points. Pivoting enables analysts to move seamlessly from one piece of data to another related piece, thereby uncovering hidden patterns and connections within the data. This approach is particularly useful in complex data environments, as it allows for a more thorough and efficient analysis by linking different pieces of information together in a meaningful way.

![History page](/img/blog/modules/3.png)

## Use-Cases

- **Threat Intelligence Analysis**: Analysts can use specific enrichment modules to augment their datasets without needing full access to a MISP instance.
- **Accessing Untrusted Third-party Services**: MISP-modules can be utilized to access untrusted third-party expansion services without the necessity of directly connecting to a cyber threat intelligence infrastructure.
- **Development of MISP modules**: Developer can easily test and develop their own modules without installing a complete MISP instance. 

## Conclusion

This extension of misp-modules to operate as standalone applications marks a significant advancement in the flexibility and utility of the MISP ecosystem. It also facilitates the use of the framework with other services and the creation of new extensions for the MISP modules.

# Acknowledgement 

This extension has been developed for JTAN (Joint Threat Analysis Network) project and co-funded by the European Union CEF program and CIRCL. Next to that project, David Cruciani developed [a framework to facilitate the development of Flask application](https://github.com/DavidCruciani/ptit-crolle). 

