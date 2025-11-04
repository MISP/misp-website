---
title: MISP v2.5.24 - Security & Stability Update 
banner: /img/blog/graph-cn.png
author:
 - MISP Project team
date: 2025-11-04
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

This release focuses on security enhancements, bug fixes, and minor improvements to stability and functionality.

- [GCVE-1-2025-0010](https://vulnerability.circl.lu/vuln/gcve-1-2025-0010) < MISP 2.5.24 - Arbitrary file-hash inclusion via templates in the template engine in MispAttribute allows a web user to obtain the MD5 hash of any file accessible to them via inclusion of tmp_name in templates.
- [GCVE-1-2025-0011](https://vulnerability.circl.lu/vuln/gcve-1-2025-0011) < MISP 2.5.24 - Invalid check for uploaded file validity in EventsController can lead to arbitrary file inclusion / deletion via import modules by spoofing the tmp_name of the request.
- [GCVE-1-2025-0012](https://vulnerability.circl.lu/vuln/gcve-1-2025-0012) < MISP 2.5.24 - Potential vulnerability in file check upload but this vulnerability is non-exploitable as the code is never executed. This vulnerability information is kept for archiving.
- [GCVE-1-2025-0013](https://vulnerability.circl.lu/vuln/gcve-1-2025-0013) < MISP 2.5.24 - Authorization bypass / improper access control in app/Controller/SharingGroupBlueprintsController.php in MISP on web application /or API allows an authenticated low-privilege user to inject arbitrary organizations into existing sharing groups (including groups that should not be extendable), thereby granting those organizations access to shared resources and escalating access via crafted sharing-group blueprints or API requests that bypass validation.
- [GCVE-1-2025-0014](https://vulnerability.circl.lu/vuln/gcve-1-2025-0014) < MISP 2.5.24 - Cross-site scripting in Mermaid chart rendering component in MISP event report allows a remote attacker part of a MISP community to execute arbitrary JavaScript in the victim’s browser via injection of HTML tags in raw Mermaid charts synchronized through event reports.
- [GCVE-1-2025-0015](https://vulnerability.circl.lu/vuln/gcve-1-2025-0015) < MISP 2.5.24 - Cross-site scripting in decaying tool simulation UI/component in MISP on web application allows an attacker/org who can set an organization's display name to execute arbitrary JavaScript in other users' browsers when they view or run simulations via a crafted organization name containing a script payload that is rendered unsanitized when a specific attribute is chosen for the simulation.
- [GCVE-1-2025-0016](https://vulnerability.circl.lu/vuln/gcve-1-2025-0016) < MISP 2.5.24 - Local file inclusion in [ImportFromUrl() URL handling component in MISP event report (with pandoc support) on server-side document import feature / web application allows an attacker who can supply a URL to read local filesystem documents and disclose sensitive information (limited to document file types) via providing file:// URLs to ImportFromUrl() that are fetched without proper scheme/host validation.

Thanks to Raphael Lob and Jeroen Pinoy from NATO Cyber Security Center for the security evaluation and report.

## Fixes

### Security

*   **jQuery UI Upgrade:** Upgraded `jquery-ui` used by `gridstack` to address a security vulnerability (fixes #10531).
*   **Local File Inclusion:** Fixed a local file inclusion vulnerability for document files via `importFromUrl()`, reported by Jeroes Pinoy.
*   **Decaying Model Tool:** Implemented a speculative fix for an edge case with an unescaped OR name in the decaying model tool, reported by Jeroen Pinoy.
*   **Mermaid Sanitisation:** Improved mermaid sanitisation, maintaining the ability to render mermaid arrows while fixing a security issue, reported by Jeroen Pinoy.
*   **File Validity Check:** Corrected a logic error in file validity checks (non-exploitable), reported by Raphael Lob from NATO Cyber Security Center.
*   **Object File Uploads:** Enhanced sanitisation of the `tmp_file` name in object file uploads, thanks to Jeroen Pinoy from NATO Cyber Security Center.
*   **Sharing Group Blueprint Access Control:** Tightened access control for sharing group blueprints, thanks to Jeroen Pinoy from NATO Cyber Security Center.
*   **Uploaded File Validity:** Fixed an invalid check for uploaded file validity, thanks to Raphael Lob from NATO Cyber Security Center.

### Other Fixes

*   **Publish Process:** Tentative flipping of the publish flag at the start of the publish process to avoid timing issues due to slow server responses.
*   **Publishing:** Moved publishing to separate background processes to prevent congestions caused by unreachable servers in in-line execution.
*   **Users Periodic Summary:** Improved handling of tag filtering and usage of defined variables.
*   **Galaxy Cluster Fetcher:** Corrected association when fetching target clusters from relations.
*   **Workflow Tag After Save:** Ensured correct execution start when an event is tagged (fixes #10478).
*   **Logs Index:** Ignored `search_token` and empty filters in the logs index.
*   **Cerebrate Pull Sharing Group:** Correctly re-used the `extend` state set on Cerebrate.
*   **On-Demand Correlation:** Fixed integrity constraint violation when correlating an event with multiple correlating equal value2 attributes (correlations will now show up on a single attribute in these cases, as discussed in #10521).
*   **Logs Index:** Ignored `search_token` and empty filters in the logs index.

