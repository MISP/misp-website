---
title: Latest MISP-STIX release supporting Analyst Data
banner: /img/blog/analyst-data_event.png
author:
 - MISP Project team
date: 2025-02-07
tags: ["MISP", "Threat Intelligence", "STIX"]
layout: post
---

# MISP-STIX released with support for Analyst Data

[MISP-STIX](https://github.com/misp/misp-stix) is the Python library designed to facilitate seamless conversion between the MISP standard and STIX formats. It enables MISP users to import STIX documents into their MISP instance and to convert collections of MISP data into STIX, while preserving the fidelity of the original data to maintain interoperability between formats and CTI platforms wuthout losing important context or analytical insights. The library is maintained to enhance the support for STIX 2.x while preserving a compatibility with STIX 1.x.

With this release, we are delighted to introduce support for Analyst Data, pushing further the mapping coverage between both formats, enabling the conversion of Analyst notes and opinions.

## Feature overview

### Analyst Data support

- **MISP Analyst Notes and Opinions conversion to STIX 2.1**
  - Analyst Data attached to Events, Attributes, Objects, or Event Reports are converted into STIX 2.1 Note or Opinion objects.
  - STIX 2.0 compatibility is maintained through the conversion of Analyst Data into Custom STIX objects.
- **STIX 2.1 Note and Opinion objects conversion to MISP Analyst Data**
  - Notes and Opinions in STIX 2.1 documents are now converted into MISP Analyst Data and attached to the appropriate data layer.
  - Analyst insights, assessments, and additional context provided in STIX documents are preserved and mapped effectively into MISP’s ecosystem.

### Additional features and improvements

As part of our ongoing development roadmap, this release also includes additional features and enhancements:

- New command-line argument to force the conversion of some STIX 2.x SDOs as Galaxy Clusters
  - The default logic for STIX 2.x object parsing ensures accurate mapping to the appropriate MISP layer.
  - Some STIX 2.x producers do not strictly follow specifications, so this option allows users to force the conversion of specific STIX objects into Galaxy Clusters, preventing the pollution of MISP with reusable contextual information.
- A fix has been applied to the command-line feature to clarify the distinction between export and import arguments, eliminating potential confusion.

### Changelog

The full release notes are available [here](https://github.com/MISP/misp-stix/releases/tag/2025.01.09), providing detailed insights into all updates.

## In-depth details

![Event with Analyst Data](/img/blog/analyst-data_event.png "{class='img-responsive'}")

With the recent introduction of the Analyst Data feature in MISP, users can now attach notes or opinions to any data layer or even to other analyst data objects. This provides the ability to annotate and assess shared intelligence with additional insights.

The conversion between MISP Analyst Data and STIX 2.1 Note and Opinion objects is straightforward, as both formats offer clear and structured representations.

The main structural difference to be aware of lies in data organization: while STIX represents data as a flat list of objects referencing each other, MISP Analyst Data is directly attached to its parent data layer object.

### Detailed mapping

![In-depth mapping](/img/blog/analyst_data_json.png "{class='img-responsive'}")

#### STIX 2.1 Note object conversion to MISP Analyst Note

| STIX 2.1 **Note** object | **MISP Analyst Note** | Description |
|:---|:---|:---|
| `content` | `note` | The Note |
| `abstract` | `comment` | An additional comment on the note |
| `authors` | `authors` | Author(s) of the note |
| `lang` | `language` | Language of the note |
| `created` | `created` | Creation timestamp of the note |
| `modified` | `modified` | Last modification timestamp of the note|

#### STIX 2.1 Opinion object conversion to MISP Analyst Opinion

| STIX 2.1 **Opinion** object | **MISP Analyst Opinion** | Description |
|:---|:---|:---|
| `opinion` (Common vocabulary) | `opinion` (score 0-100) | The Opinion |
| `explanation` | `comment` | An explanation or comment on the opinion |
| `authors` | `authors` | Author(s) of the opinion |
| `created` | `created` | Creation timestamp of the opinion |
| `modified` | `modified` | Last modification timestamp of the opinion|
