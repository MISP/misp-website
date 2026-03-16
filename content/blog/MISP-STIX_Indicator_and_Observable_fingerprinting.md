---
title: MISP-STIX 2026.3.13 Released
date: 2026-03-16
layout: post
authors:
- Christian Studer
tags: ["MISP", "STIX", "Threat Intelligence", "CTI"]
banner: /img/blog/misp-stix_conversion_features.png
---

# MISP-STIX v2026.3.13: Improved Indicator-Observable Matching and Expanded STIX Coverage

## Introduction

[misp-stix](https://github.com/MISP/misp-stix) is the Python library powering bidirectional conversion between MISP and STIX (versions 1.x, 2.0, and 2.1).  
It is used by MISP core software, available as `misp-stix` on PyPI, and also available directly as a conversion service on [cti-transmute.org](https://cti-transmute.org).

The headline features are a new indicator-observable fingerprinting system, dual indicator + observed data export, expanded MISP object support, and ACS marking definition handling.

## What This Release Means for the MISP Community

### Better Round-Trip Fidelity

The biggest challenge in MISP-to-STIX conversion has always been preserving meaning across format boundaries. When a MISP attribute has `to_ids=True`, that flag carries operational significance: it tells analysts this indicator should be used for detection. Previously, this information could be lost or ambiguous during round-trip conversion. With this release, the library now intelligently matches STIX Indicators against Observable objects and restores the `to_ids` flag when importing back into MISP, dramatically improving round-trip fidelity as well as conversion accuracy for STIX data generated from third-party sources.

### More Object Types, Fewer Gaps

Every unsupported object type is a gap where threat intelligence gets dropped during conversion. This release closes several of those gaps: `artifact` objects (with `payload_bin` support), `malware` and `malware-analysis` SDOs, and `http-request` objects from network traffic observables. Combined with the expanded indicator pattern parsing (covering x509 certificates, registry keys, email messages, PE extensions, and more), significantly more of your MISP data now survives the journey to and from STIX.

### ACS Marking Support

For organisations working with Access Control Specification (ACS) markings, this release adds full round-trip support. ACS marking extension definitions in STIX 2.1 are converted to MISP Galaxy Clusters on import, and those clusters are converted back to proper STIX 2.1 Marking Definitions on export. This is particularly relevant for government and defence sector users who rely on ACS markings for information sharing policies.

### Cleaner, More Reliable Output

Several quality-of-life improvements make the exported STIX content cleaner: the `to_ids` label has been removed from STIX objects (since it no longer makes sense to include it on a MISP object exported to STIX when the attributes with `to_ids=True` are already described in the Indicator pattern), relationship deduplication prevents redundant links, and deterministic UUID generation ensures consistent output across runs.

## Feature Deep-Dives

### Indicator-Observable Fingerprinting

The core innovation in this release is a fingerprinting system that links STIX Indicators with their corresponding Observable objects. The problem it solves: when a STIX bundle contains both an Indicator (with a pattern like `[file:hashes.'SHA-256' = 'abc123...']`) and a separate File observable with the same hash, these represent the same piece of intelligence — but nothing in the STIX format explicitly connects them in a way that maps back to MISP's `to_ids` concept.

The fingerprinting system compares pattern values from Indicators against field values in Observable objects. When a match is found, the resulting MISP attribute gets `to_ids=True` and the Indicator ID is stored in the attribute's comment for traceability.

This works differently for internal vs external STIX content:
- **Internal** (MISP-generated STIX): The library can reconstruct the original MISP structure with high fidelity
- **External** (third-party STIX): The library uses pattern matching heuristics to infer the indicator-observable relationship

### Dual Export: Indicator + Observed Data

Previously, a MISP attribute with `to_ids=True` was exported as either an Indicator or an Observed Data object. Now it generates **both**, connected by a STIX Relationship. This better represents the dual nature of the data: what was seen versus the detection pattern.

This is especially relevant for MISP objects with multiple attributes set to `to_ids=True` (e.g., a file object with multiple hashes and filename attributes). All attributes are now represented as STIX Observable objects, while an Indicator object describes the detection pattern.

The export pipeline also now:
- Applies default `to_ids` values per attribute type (so attributes without an explicit flag get a sensible default)
- Deduplicates relationships (if an Observed Data object already has a relationship to another object, the corresponding Indicator won't create a duplicate)
- Generates deterministic relationship IDs for reproducible output

### New Object Types Supported

**Artifact**: Full round-trip support for STIX Artifact objects, including `payload_bin` field handling. On import, Artifact observables and indicators are converted to MISP `artifact` objects. On export, the reverse conversion produces valid STIX Artifacts.

**Malware & Malware Analysis**: MISP `malware` objects now export to STIX 2.x Malware SDOs, and `malware-analysis` objects export to STIX 2.1 MalwareAnalysis SDOs with proper kill chain handling.

**HTTP Request**: External `network-traffic` observables with HTTP request extensions are now imported as MISP `http-request` objects, preserving request method, URI, headers, and other HTTP-specific fields.

### ACS Marking Definition Support

ACS (Access Control Specification) markings define sharing policies for classified or sensitive information. This release adds:

- **Import**: STIX 2.1 ACS marking extension definitions are converted to MISP Galaxy Clusters, grouped under a single Galaxy. Multiple `further_sharing` rules are now properly handled. Marking definitions referenced in Report or Grouping `object_refs` are correctly resolved.
- **Export**: Custom ACS marking Galaxy Clusters are converted back to STIX 2.1 Marking Definitions with the proper extension structure. For STIX 2.0, they are exported as custom marking definition objects.

### Pattern Parsing Improvements

The STIX pattern parser has been significantly improved to handle complex patterns across a wide range of observable types:

- **x509 certificates**: Improved handling of hash properties within certificate patterns
- **Processes**: Proper attribute extraction from process patterns
- **Registry keys**: Fixed value parsing for patterns with list indexes describing embedded values
- **Email messages**: Correct conversion of email patterns to MISP `email` objects
- **Domain-name + IP**: Proper differentiation between `domain-ip` objects and simple `domain` attributes
- **Autonomous systems**: Fixed AS name and number extraction
- **Socket extensions**: Correct parsing of `socket-ext` patterns
- **Network traffic**: Unified handling of network connection and network traffic patterns
- **MAC addresses**: New indicator-to-attribute conversion support
- **Mutex objects**: Improved pattern parsing
- **PE extensions**: Better extraction of PE header and section data from file indicators
- **Artifact `payload_bin`**: Proper base64 payload extraction from artifact patterns

## Release at a Glance

- Almost **350 commits** across **120 files changed**
- **~89,000 lines added**, **~48,000 lines removed**
- New `AbstractParser` base class unifying error/warning handling across all parsers
- Deterministic v5 UUID generation for reproducible conversions
- Default MISP event validation before conversion and export to STIX

For the full mapping documentation, see the [documentation/mapping/](https://github.com/MISP/misp-stix/tree/main/documentation/mapping) directory.
