---
title: MISP 2.4.194 released with new functionalities and various bugs fixed 
date: 2024-06-21
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/object-collapse.png
---

MISP 2.4.194 released with new functionalities and various bugs fixed.

{{<video src="/img/blog/bookmark.webm)"  >}}

### New Features
- **Bookmark Functionality**:
  - Users can now create bookmarks.
  - Bookmarks can be shared with all users in the same organization.
- **Heartbeat Endpoint**:
  - New `/users/heartbeat` endpoint.
  - Accessible without authentication; returns a 200 response to indicate the instance is operational.
  - Designed for quick checks to see if the instance is up and running.
- **Skip OTP Requirement**:
  - New role permission to exclude certain roles from OTP requirements.
  - Useful for filtered, local service accounts.
- **Users API Update**:
  - Added a new boolean field indicating whether TOTP is set up for the user.
  - Applicable to `/users/view`, `/admin/users/view`, `/admin/users/index` endpoints.

### Changes
- **Various Version Bumps**:
  - Updates for misp-stix, schema, PyMISP, warning-lists, misp-galaxy, and misp-objects.
- **Bookmark Improvements**:
  - Added title documentation for the `exposed_to_org` field.
  - Enhanced quick search support for bookmarks.
- **ACL and Schema Updates**:
  - Heartbeat added to the ACL component.
  - Updates to schema and `mysql.sql`.

### Fixes
- **Default Roles and Permissions**:
  - Added delegation permission for sync user and publisher roles.
  - Readded default roles.
  - Fixed issues with PyMISP tests, default roles, and various editor and ingestion bugs.
- **UI and Functional Fixes**:
  - Corrected event report markdown editor to display tags.
  - Included user agent in feed ingestion to address issues with specific feeds.
  - Fixed editing view for galaxycluster blocklist.
  - Readded missing org logo in the decaying model.
  - Corrected JSON response handling in the decaying tool.
  - Fixed object reference links for proper view refocus.
  - Corrected errors in the server edit view.
  - Fixed typo in bookmark description.
  - Adjusted default role settings in `mysql.sql`.
  - Updated local flag in EventTags to be boolean.
  - Corrected filenames in RHEL background worker migration guide.
  - Improved performance by increasing chunk size for sighting sync.

For a complete list of updates, please refer to the [changelog pages](https://www.misp-project.org/Changelog.txt). Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!

