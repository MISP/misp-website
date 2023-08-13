---
title: MISP to Microsoft Sentinel integration with Upload Indicators API
date: 2023-08-13
layout: post
authors:
- Koen Van Impe
tags: ["sentinel", "integration", "azure", "MISP", "Threat Intelligence"]
categories: []
banner: /img/blog/misp2sentinel_header.png
---

# MISP to Microsoft Sentinel integration

## Introduction

In April 2023 the MISP to [Azure Sentinel integration](https://www.misp-project.org/2023/04/03/MISP-Sentinel.html/) was covered. This integration used the Microsoft Graph API. Since then, Microsoft [deprecated](https://learn.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview) the Graph API, and preferred new integrations to rely on the [Upload Indicators API](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-upload-api).

The new MISP to Microsoft (previously Azure) Sentinel or [misp2sentinel](https://github.com/cudeso/misp2sentinel) does just that, it 
- Supports integration with the old **Graph API**, but also
- It supports the new, and preferred, **Upload Indicators API**.

Read the installation and configuration documentation at [misp2sentinel](https://github.com/cudeso/misp2sentinel) for more details.

## Azure App

You stil require an Azure App with the proper permissions to upload the indicators.

## Data connector at Content Hub

The [misp2sentinel](https://github.com/cudeso/misp2sentinel) is available via the Microsoft Sentinel Content Hub at [ADD](ADD)

## STIX

 The Upload Indicators API of Microsoft is STIX based. The integration relies on [MISP-STIX](https://github.com/MISP/misp-stix) to handle the conversion between MISP and STIX format. For reference, [STIX](https://stixproject.github.io/), is a structured language for describing threat information to make sharing information between systems easier.

![base-MISP2Sentinel.png](/img/blog/base-MISP2Sentinel.png)

 From a functional point of view, all indicators that can be synchronised via the Graph API, can also be synchronised via the Upload Indicators API. There are some features missing in the STIX implementation of Sentinel and as a result some context information (identity, attack patterns) is lost. But it is only a matter of time before these are implemented on the Sentinel side, after which you can fully benefit from the STIX conversion.

## Sentinel Workspaces

In addition to the change to STIX, the new API also supports **Sentinel Workspaces**. This means you can send indicators to just one workspace, instead of pushing them globally.

## Configuration changes

If you used the old Graph API version then it's worth having a look at the new [configuration settings](https://github.com/cudeso/misp2sentinel#configuration-changes) and [requirements](https://github.com/cudeso/misp2sentinel/blob/main/requirements.txt).

## Azure Function

Next to a "traditional" MISP installation, there is also an option to do the integration via an [Azure Function](https://github.com/cudeso/misp2sentinel/tree/main/AzureFunction). The code is contributed by [Infernux](https://github.com/lnfernux) and provides you a great approach to have the integration running directly within Sentinel.

## Workflow

For those interested in the underlying code, the 'workflow' of the integration is outlined in this diagram.

 ![base-MISP2Sentinel-workflow.png](/img/blog/base-MISP2Sentinel-workflow.png)