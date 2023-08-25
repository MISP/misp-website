---
title: MISP to Microsoft Sentinel integration with Upload Indicators API
date: 2023-08-26
layout: post
authors:
- Koen Van Impe
tags: ["sentinel", "microsoft", "integration", "azure", "MISP", "Threat Intelligence"]
categories: []
banner: /img/blog/misp2sentinel_header.png
---

# MISP to Microsoft Sentinel integration

## Introduction

The MISP to Microsoft Sentinel integration allows you to upload indicators from MISP to Microsoft Sentinel. It relies on **PyMISP** to get indicators from MISP and an **Azure App** to connect to Sentinel. 

## Graph API and Upload Indicators API

In April 2023 the [MISP to Azure Sentinel](https://www.misp-project.org/2023/04/03/MISP-Sentinel.html/) integration was covered. This integration used the Microsoft Graph API. Since then, Microsoft [deprecated](https://learn.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview) the Graph API, and preferred new integrations to rely on the [Upload Indicators API](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-upload-api). The new MISP to Microsoft (previously Azure) Sentinel or [misp2sentinel](https://github.com/cudeso/misp2sentinel) does just that, it 
- Supports integration with the old **Graph API**, but most importantly,
- It supports the new, and preferred, **Upload Indicators API**.

To get started you need

- An **Azure App**, with read and write permissions on your Microsoft Sentinel workspace and a threat intelligence **Data Connector**;
- A MISP **API key** to pull data out of MISP;
- The [misp2sentinel](https://github.com/cudeso/misp2sentinel/) code in a Python3 virtual environment or as an Azure Function, with the necessary libraries such as [MISP-STIX](https://github.com/MISP/misp-stix).

## Microsoft Azure Market Place

The [misp2sentinel](https://github.com/cudeso/misp2sentinel) solution is in the Market Place or [Microsoft Sentinel Content Hub](https://portal.azure.com/#create/microsoftsentinelcommunity.azure-sentinel-solution-misp2sentinel) with a corresponding data connector. Note that enabling the solution in Azure isn't sufficient to sync indicators. You still need to setup the *Python environment* or use the *Azure Function*.

![misp2sentinel.png-2](/img/blog/misp2sentinel-2.png)

![misp2sentinel.png-1](/img/blog/misp2sentinel-1.png)

## Python environment

The setup of the Python virtual environment is described in the [README](https://github.com/cudeso/misp2sentinel/blob/main/README.md). Basically you need to clone the repository, setup the Python3 environment, install the necessary libraries and then update the configuration file.

In general this should not take longer than 10 minutes.

## Azure Function

Next to a "traditional" Python environment installation, there is an option to do the integration via an [Azure Function](https://github.com/cudeso/misp2sentinel/tree/main/AzureFunction). The code is contributed by [Infernux](https://github.com/lnfernux) and provides you a great approach to have the integration running directly within Sentinel.

## STIX

 The Upload Indicators API of Microsoft is STIX based. [STIX](https://stixproject.github.io/) is a structured language for describing threat information to make sharing information between systems easier. This integration relies on the [MISP-STIX](https://github.com/MISP/misp-stix) library to handle the conversion between MISP and STIX. 

![misp2sentinel.png](/img/blog/misp2sentinel.png)

 From a functional point of view, all indicators that can be synchronised via the Graph API, can be synchronised via the Upload Indicators API. There are some features missing in the STIX implementation of Sentinel and as a result some context information (identity, attack patterns) is lost. But it is only a matter of time before these are implemented on the Sentinel side, after which you can fully benefit from the STIX conversion.

## Sentinel Workspaces

In addition to the change to STIX, the new API also supports **Sentinel Workspaces**. This means you can send indicators to just one workspace, instead of pushing them globally.

## Configuration changes

If you used the old Graph API version before then it's worth having a look at the new [configuration settings](https://github.com/cudeso/misp2sentinel#what-are-the-configuration-changes-compared-to-the-old-graph-api-version) and [requirements](https://github.com/cudeso/misp2sentinel/blob/main/requirements.txt) before upgrading.

## GitHub repository

The code and documentation is at [https://github.com/cudeso/misp2sentinel](https://github.com/cudeso/misp2sentinel).

## Workflow

The 'workflow' of the integration is outlined in this diagram.

 ![misp2sentinel-workflow.png](/img/blog/misp2sentinel-workflow.png)
