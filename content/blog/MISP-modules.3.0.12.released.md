---
title: "MISP Modules v3.0.12 Released - richer threat intelligence enrichment, improved interoperability with MISP objects, new enrichment capabilities, and increased reliability across existing modules."
author:
 - MISP Project team
date: 2026-10-14
tags: ["MISP", "Threat Intelligence", "release", "modules" ]
layout: post
banner: /img/blog/mod1.png
banner_alt: "MISP server settings showing the enrichment module catalogue and configuration options."
banner_caption: "Manage enrichment modules from MISP server settings."
---

# MISP Modules v3.0.12 Released

**Release date:** 14 October 2026

We are pleased to announce **MISP Modules v3.0.12**, a significant release focusing on richer threat intelligence enrichment, improved interoperability with MISP objects, new enrichment capabilities, and increased reliability across existing modules.

One of the most important improvements in this release is the extensive transition from flat text-based enrichment results to **structured MISP objects**. This allows analysts to better understand relationships between indicators, infrastructure, vulnerabilities, reputation assessments, and other contextual information.

The release also introduces several new expansion and hover modules, improves vulnerability intelligence integration, and extends infrastructure analysis capabilities.

![MISP module selector listing enrichment modules for an indicator.](/img/blog/mod2.png "Choose an enrichment module directly from an indicator in MISP.")

## Highlights

### A major step towards structured enrichment

A large number of existing enrichment modules have been updated to return structured MISP objects instead of simple text attributes. This is critical for the MISP 3.0 version and the value intelligence view.

This improves the quality of enriched events by preserving relationships, metadata, and contextual information that would otherwise be lost.

Some notable improvements include:

- **urlscan.io**: Now returns interconnected `url`, `domain-ip`, `geolocation`, `asn`, `x509`, `image`, and `reputation` objects, preserving relationships between scanned infrastructure, certificates, screenshots, and reputation assessments.
- **SecurityTrails**: Enrichment now produces `passive-dns`, `whois`, and `domain-ip` objects, including historical observations and timestamps.
- **Vulners**: Vulnerability intelligence is represented through `vulnerability`, `exploit`, and `reputation` objects, preserving CVSS scores, references, and exploit information.
- **GeoIP**: Geographic and ASN enrichment now produces dedicated `geolocation` and `asn` objects, including additional location information where available.
- **DNS and Reverse DNS**: Results are now represented as `dns-record` objects, preserving multiple records instead of returning only the first result.
- **Have I Been Pwned and XposedOrNot**: Breach intelligence now uses structured `breach` objects, providing dates, affected records, exposed data classes, and additional metadata.
- **Bitcoin enrichment**: The `btc_steroids` module now creates `btc-wallet` and `btc-transaction` objects, including transaction details and counterparty addresses.
- **SocialScan**: Account discovery now produces `user-account` objects for identified accounts.
- **Reputation modules**: `extuno`, `rbl`, `dbl_spamhaus`, and `btc_scam_check` now return structured `reputation` objects with explicit classifications and supporting information.
- **SourceCache**: Captured web pages are now represented as `page-capture` objects, preserving the original URL, captured content, domain, and capture timestamp.

These changes make enrichment results more useful for correlation, investigation, automation, and downstream threat intelligence processing.

### New enrichment modules

Several new modules have been introduced to extend the enrichment capabilities available to MISP users.

#### MODAT Magnify infrastructure enrichment

A new integration with **[MODAT Magnify](https://modat.io/)** provides additional infrastructure enrichment capabilities.

The module supports infrastructure observations and related contextual information, with specific improvements for handling multiple observations, certificate information, classification metadata, and partial results when subscription permissions restrict certain endpoints.

#### ipapi.is enrichment

A new `ipapi.is` lookup module provides an additional source of IP address intelligence and enrichment.

####  [Phishunt](https://phishunt.io/) phishing intelligence

A new Phishunt expansion and hover module enriches domains, hostnames, and URLs using the [Phishunt](https://phishunt.io/) API.

The integration provides:

- Phishing detection information represented as structured `phishing` objects.
- Targeted brands and associated infrastructure.
- First-seen information and detection references.
- Additional context about hosting, TLS certificates, and other detection sources.
- Read-only lookups without submitting indicators for additional analysis.

The module uses exact hostname matching to avoid unrelated results and includes rate-limit handling.

#### PTR classification enrichment

A new [ptrclassify](github.com/adulau/ptrclassify) hover and expansion module provides classification of reverse DNS information.

The module returns structured classification and DNS record objects while preserving the associated IP address context.

#### URL DNS and ASN expansion

A new URL enrichment capability resolves URLs into associated infrastructure information.

The module produces structured `ip-port` and IPv4 `asn` objects, making it easier to connect URLs to their underlying network infrastructure.

### Extended Vulnerability-Lookup integration

The [vulnerability_lookup](https://www.vulnerability-lookup.org/) module receives additional capabilities to support vulnerability intelligence enrichment.

Improvements include:

- Expanded read-only API enrichment.
- Additional CPE lookup capabilities.
- Improved handling of optional configuration settings.
- More precise matching of Known Exploited Vulnerability (KEV) assertions to vulnerability identifiers.
- Adjustments to attachment correlation and object template synchronization.

These improvements strengthen the integration between MISP and [[Vulnerability-Lookup](https://vulnerability.circl.lu/)](https://vulnerability.circl.lu/), helping analysts connect vulnerability intelligence with threat intelligence workflows.

### Reliability and data quality improvements

This release also contains numerous fixes aimed at improving the consistency and reliability of enrichment results.

**DNS and infrastructure enrichment**
- DNS resolution now supports both IPv4 (`A`) and IPv6 (`AAAA`) records.
- Reverse DNS enrichment correctly handles multiple PTR records.
- Multicast IPv4 addresses are excluded from inappropriate ASN enrichment.
- Improved handling of multiple certificate and DNS observations.

**Reputation and vulnerability intelligence**
- Improved distinction between negative reputation results and lookup failures.
- Better handling of unknown Spamhaus response codes.
- Reputation classifications now distinguish suspicious activity from malicious activity where appropriate.
- Vulners enrichment no longer generates artificial exploit content when only an exploit title or reference is available.

**Module robustness**
- Improved handling of empty responses and API errors in HIBP.
- Fixed WHOIS configuration validation and error handling.
- Improved handling of unavailable external services.
- Fixed optional configuration defaults in several modules.
- Improved preservation of comments and lookup source information in `onion_lookup`.
- Improved handling of partial enrichment results returned by MODAT.

### Improved debugging capabilities

The release introduces improvements to **outbound HTTP debugging**.

These changes preserve HTTP debugging information and improve attribution of requests to nested module workers, helping developers and administrators troubleshoot enrichment issues more effectively.

### Better alignment with MISP object templates

An important objective of this release is to improve consistency with the MISP object model.

Several modules have been updated to respect object relation cardinality, attribute types, and template requirements.

The result is more predictable enrichment output and better preservation of structured information.

The traditional WHOIS module intentionally retains its free-text output, allowing MISP's free-text importer to extract useful indicators. Users looking for structured registration information can also use the RDAP module.

## Contributors

A big thank you to everyone who contributed to this release through development, testing, reviews, and improvements.

Special thanks to:

- **Alexandre Dulaunoy**
- **Sami Mokaddem**
- **Nikolai Tschacher**
- **Daniel López**

This release also includes contributions developed with the assistance of AI coding tools, particularly in the extensive conversion of enrichment modules to structured MISP objects.

We greatly appreciate the continued involvement of the MISP community in improving the quality and interoperability of threat intelligence enrichment.

## Upgrade and feedback

We encourage all MISP Modules users to upgrade to **v3.0.12** to benefit from these new capabilities, improvements, and fixes.

As several modules now return structured MISP objects instead of flat attributes, users with custom integrations or automated workflows should review any dependencies on previous output formats.

Feedback, bug reports, and contributions are always welcome.

- **Source code:** https://github.com/MISP/misp-modules
- **Release:** https://github.com/MISP/misp-modules/releases/tag/v3.0.12
- **Issues and feedback:** https://github.com/MISP/misp-modules/issues

**Thank you to the MISP community for your continued support!**
