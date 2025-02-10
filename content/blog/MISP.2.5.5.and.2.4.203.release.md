---
title: MISP 2.4.203 and 2.5.5 released including new features, improvements and many security improvements. 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2025-01-12
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

# MISP Software Release: Combined Updates for v2.4.203 and v2.5.5

## Introduction

We are thrilled to announce the release of **MISP v2.4.203** and **MISP v2.5.5**, bringing a range of new features, improvements, and fixes to enhance the platform's performance, usability, and security. These updates reflect our ongoing commitment to providing a robust and reliable open-source threat intelligence platform for the community.

This release introduces significant changes, including reworked log search capabilities, enhanced password management, and important security fixes. Below, you'll find an overview of the updates in this combined release.

## Highlights of v2.5.5

### 🚀 New Features
- Added support for `misp_stix_converter` in `stixtest.py` for improved STIX testing.

### 🐞 Fixes
- Improved the password change process with a new approach and additional restrictions for blocked site admins.
- Fixed various issues related to analyst data processing and nesting validations.
- Debug functionality removed to streamline performance.

### 📂 Other Improvements
- Merged several branches (`develop`, `2.4-develop`, `2.5`) to unify the codebase.
- Resolved issues in `misp-stix` version management and integrated updates from contributors.

## Highlights of v2.4.203

### 🚀 New Features
- Reworked **Log Search**:
  - Introduced a modernized internal system for log searches.
  - Enhanced pagination and filter persistence.
  - Improved user interface with additional field information.

### 🛠️ Changes
- Added more `cli_only` flags for fine-grained control of settings.
- Updated `SECURITY.md` with a direct link to security advisories for easier access.

### 🐞 Fixes
- Addressed multiple security issues, including:
  - Sanitization of user objects during edits.
  - Improved sanitization of logs to protect API keys.
  - Redacted sensitive headers in feeds.
- Tightened ACLs for collections and reports, ensuring stricter permissions.
- Backported relevant setting changes from `2.5` for consistency.

### 📂 Other Improvements
- Integrated a new UI feature: a checkbox for selecting object attributes directly from the event view.

## Acknowledgments

We extend our gratitude to all contributors who provided valuable feedback, reported issues, and shared patches for these releases.

## Feedback and Support

If you encounter issues or have suggestions, please feel free to open a ticket on our [GitHub repository](https://github.com/MISP/MISP/issues). Your feedback is invaluable to us!


## Stay Connected

Follow us on [Fediverse/Mastodon](https://misp-community.org/@misp) and join our community on [Gitter](https://gitter.im/MISP/) for the latest updates and discussions.

Thank you for your continued support of the MISP project. Together, we make threat intelligence sharing more effective and secure!

**Happy sharing!**

