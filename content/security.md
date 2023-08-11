---
layout: page
title: Security Advisories and Reporting Security Vulnerabilities
permalink: /security/
toc: true
---

## Reporting security vulnerabilities for MISP or related MISP project repositories

Reporting security vulnerabilities is of great importance for us, as MISP is used in multiple critical infrastructures. 

In the case of a security vulnerability report, we ask the reporter to send it directly to [CIRCL](https://www.circl.lu/contact/), if possible encrypted with the following GnuPG key: **CA57 2205 C002 4E06 BA70 BE89 EAAD CFFC 22BD 4CD5**. We usually fix reported and confirmed security vulnerabilities in less than 48 hours, followed by a software release containing the fixes within the following days. 

If you report security vulnerabilities, do not forget to **tell us if and how you want to be acknowledged** and if you already requested CVE(s). Otherwise, we will request the CVE(s) directly.

As one of the critical user-bases of MISP consists of the CSIRT community, it is our duty to clearly state which bug could be abused and have a security impact on a MISP instance. CVE assignment is performed even for minor bugs suspected of having a security impact. This allows every user with MISP instances set up in their environments to understand which bugs could impact their security.

We firmly believe that, even though unfortunately it is often not regarded as common practice in our industry, being as transparent as possible about vulnerabilities, no matter how minor, is of crucial importance. At MISP Project, we care about the security of our users and prefer to have a high number of published CVEs rather than sweeping some of them under the rug.


## Advisories

- [CVE-2015-5719](https://cve.circl.lu/cve/CVE-2015-5719) <= MISP 2.3.92 - app/Controller/TemplatesController.php in Malware Information Sharing Platform (MISP) before 2.3.92 does not properly restrict filenames under the tmp/files/ directory, which has unspecified impact and attack vectors.
- [CVE-2015-5720](https://cve.circl.lu/cve/CVE-2015-5720) <= MISP 2.3.89 - Multiple cross-site scripting (XSS) vulnerabilities in the template-creation feature in Malware Information Sharing Platform (MISP) before 2.3.90 allow remote attackers to inject arbitrary web script or HTML via vectors involving (1) add.ctp, (2) edit.ctp, and (3) ajaxification.js.
- [CVE-2015-5721](https://cve.circl.lu/cve/CVE-2015-5721) <= MISP 2.3.89 - Malware Information Sharing Platform (MISP) before 2.3.90 allows remote attackers to conduct PHP object injection attacks via crafted serialized data, related to TemplatesController.php and populate_event_from_template_attributes.ctp.
- [CVE-2017-7215](https://cve.circl.lu/cve/CVE-2017-7215) <=  MISP 2.4.68 - Cross site scripting in some view elements in the index filter tool in app/webroot/js/misp2.4.68.js and the organisation landing page in app/View/Organisations/ajax/landingpage.ctp of MISP before 2.4.69 allows remote attackers to inject arbitrary web script or HTML.
- [CVE-2017-13671](https://cve.circl.lu/cve/CVE-2017-13671) <= MISP 2.4.79 - app/View/Helper/CommandHelper.php in MISP before 2.4.79 has persistent XSS via comments. It only impacts the users of the same instance because the comment field is not part of the MISP synchronisation.
- [CVE-2017-14337](https://cve.circl.lu/cve/CVE-2017-14337) <= MISP 2.4.79 - When MISP before 2.4.80 is configured with X.509 certificate authentication (CertAuth) in conjunction with a non-MISP external user management ReST API, if an external user provides X.509 certificate authentication and this API returns an empty value, the unauthenticated user can be granted access as an arbitrary user.
- [CVE-2017-15216](https://cve.circl.lu/cve/CVE-2017-15216) <= MISP 2.4.81 - MISP before 2.4.81 has a potential reflected XSS in a quickDelete action that is used to delete a sighting, related to app/View/Sightings/ajax/quickDeleteConfirmationForm.ctp and app/webroot/js/misp.js.
- [CVE-2017-16802](https://cve.circl.lu/cve/CVE-2017-16802) <= MISP 2.4.82 - In the sharingGroupPopulateOrganisations function in app/webroot/js/misp.js in MISP 2.4.82, there is XSS via a crafted organisation name that is manually added.
- [CVE-2017-16946](https://cve.circl.lu/cve/CVE-2017-16946) <= MISP 2.4.82 - The admin_edit function in app/Controller/UsersController.php in MISP 2.4.82 mishandles the enable_password field, which allows admins to discover a hashed password by reading the audit log.
- [CVE-2018-6926](https://cve.circl.lu/cve/CVE-2018-6926) <= MISP 2.4.87 - In app/Controller/ServersController.php in MISP 2.4.87, a server setting permitted the override of a path variable on certain Red Hed Enterprise Linux and CentOS systems (where rh_shell_fix was enabled), and consequently allowed site admins to inject arbitrary OS commands. The impact is limited by the setting being only accessible to the site administrator.
- [CVE-2018-8948](https://cve.circl.lu/cve/CVE-2018-8948) <= MISP 2.4.89 - In MISP before 2.4.89, app/View/Events/resolved_attributes.ctp has multiple XSS issues via a malicious MISP module.
- [CVE-2018-8949](https://cve.circl.lu/cve/CVE-2018-8949) <= MISP 2.4.89 - An issue was discovered in app/Model/Attribute.php in MISP before 2.4.89. There is a critical API integrity bug, potentially allowing users to delete attributes of other events. A crafted edit for an event (without attribute UUIDs but attribute IDs set) could overwrite an existing attribute.
- [CVE-2018-11245](https://cve.circl.lu/cve/CVE-2018-11245) <= MISP 2.4.91 - app/webroot/js/misp.js in MISP 2.4.91 has a DOM based XSS with cortex type attributes.
- [CVE-2018-11562](https://cve.circl.lu/cve/CVE-2018-11562) <= MISP 2.4.91 - An issue was discovered in MISP 2.4.91. A vulnerability in app/View/Elements/eventattribute.ctp allows reflected XSS if a user clicks on a malicious link for an event view and then clicks on the deleted attributes quick filter.
- [CVE-2018-12649](https://cve.circl.lu/cve/CVE-2018-12649) <= MISP 2.4.92 - An issue was discovered in app/Controller/UsersController.php in MISP 2.4.92. An adversary can bypass the brute-force protection by using a PUT HTTP method instead of a POST HTTP method in the login part, because this protection was only covering POST requests.
- [CVE-2018-19908](https://cve.circl.lu/cve/CVE-2018-19908) <= MISP 2.4.98 - An issue was discovered in MISP 2.4.9x before 2.4.99. In app/Model/Event.php (the STIX 1 import code), an unescaped filename string is used to construct a shell command. This vulnerability can be abused by a malicious authenticated user to execute arbitrary commands by tweaking the original filename of the STIX import.
- [CVE-2019-9482](https://cve.circl.lu/cve/CVE-2019-9482) <= MISP 2.4.102 - In MISP 2.4.102, an authenticated user can view sightings that they should not be eligible for. Exploiting this requires access to the event that has received the sighting. The issue affects instances with restrictive sighting settings (event only / sighting reported only).
- [CVE-2019-10254](https://cve.circl.lu/cve/CVE-2019-10254) <= MISP 2.4.105 - In MISP before 2.4.105, the app/View/Layouts/default.ctp default layout template has a Reflected XSS vulnerability.
- [CVE-2019-11812](https://cve.circl.lu/cve/CVE-2019-11812) <= MISP 2.4.107 - A persistent XSS issue was discovered in app/View/Helper/CommandHelper.php in MISP before 2.4.107. JavaScript can be included in the discussion interface, and can be triggered by clicking on the link.
- [CVE-2019-11813](https://cve.circl.lu/cve/CVE-2019-11813) <= MISP 2.4.107 - An issue was discovered in app/View/Elements/Events/View/value_field.ctp in MISP before 2.4.107. There is persistent XSS via link type attributes with javascript:// links.
- [CVE-2019-11814](https://cve.circl.lu/cve/CVE-2019-11814) <= MISP 2.4.107 - An issue was discovered in app/webroot/js/misp.js in MISP before 2.4.107. There is persistent XSS via image names in titles, as demonstrated by a screenshot.
- [CVE-2019-12794](https://cve.circl.lu/cve/CVE-2019-12794) <= MISP 2.4.108 - An issue was discovered in MISP 2.4.108. Organization admins could reset credentials for site admins (organization admins have the inherent ability to reset passwords for all of their organization's users).
- [CVE-2019-12868](https://cve.circl.lu/cve/CVE-2019-12868) <= MISP 2.4.109 - app/Model/Server.php in MISP 2.4.109 allows remote command execution by a super administrator because the PHP file_exists function is used with user-controlled entries, and phar:// URLs trigger deserialization.
- [CVE-2019-14286](https://cve.circl.lu/cve/CVE-2019-14286) <= MISP 2.4.111 - In app/webroot/js/event-graph.js in MISP 2.4.111, a stored XSS vulnerability exists in the event-graph view when a user toggles the event graph view. A malicious MISP event must be crafted in order to trigger the vulnerability.
- [CVE-2019-16202](https://cve.circl.lu/cve/CVE-2019-16202) <= MISP 2.4.114 - MISP before 2.4.115 allows privilege escalation in certain situations. After updating to 2.4.115, escalation attempts are blocked by the checkLoggedActions function with a "This could be an indication of an attempted privilege escalation on older vulnerable versions of MISP (<2.4.115)" message.
- [CVE-2019-19379](https://cve.circl.lu/cve/CVE-2019-19379) <= MISP 2.4.118 - MISP before 2.4.119 In app/Controller/TagsController.php in MISP 2.4.118, users can bypass intended restrictions on tagging data.
- [CVE-2020-8890](https://cve.circl.lu/cve/CVE-2020-8890) <= MISP 2.4.120 - An issue was discovered in MISP before 2.4.121. It mishandled time skew (between the machine hosting the web server and the machine hosting the database) when trying to block a brute-force series of invalid requests.
- [CVE-2020-8891](https://cve.circl.lu/cve/CVE-2020-8891) <= MISP 2.4.120 - An issue was discovered in MISP before 2.4.121. It did not canonicalize usernames when trying to block a brute-force series of invalid requests.
- [CVE-2020-8892](https://cve.circl.lu/cve/CVE-2020-8892) <= MISP 2.4.120 - An issue was discovered in MISP before 2.4.121. It did not consider the HTTP PUT method when trying to block a brute-force series of invalid requests.
- [CVE-2020-8893](https://cve.circl.lu/cve/CVE-2020-8893) <= MISP 2.4.120 - An issue was discovered in MISP before 2.4.121. The Galaxy view contained an incorrectly sanitized search string in app/View/Galaxies/view.ctp.
- [CVE-2020-8894](https://cve.circl.lu/cve/CVE-2020-8894) <= MISP 2.4.120 - An issue was discovered in MISP before 2.4.121. ACLs for discussion threads were mishandled in app/Controller/ThreadsController.php and app/Model/Thread.php.
- [CVE-2020-10246](https://cve.circl.lu/cve/CVE-2020-10246) <= MISP 2.4.122 - Reflected XSS via unsanitized URL parameters. This is related to app/View/Users/statistics_orgs.ctp.
- [CVE-2020-10247](https://cve.circl.lu/cve/CVE-2020-10247) <= MISP 2.4.122 - Persistent XSS in the sighting popover tool. This is related to app/View/Elements/Events/View/sighting_field.ctp.
- [CVE-2020-13153](https://cve.circl.lu/cve/CVE-2020-13153) <= MISP 2.4.125 - app/View/Events/resolved_attributes.ctp in MISP before 2.4.126 has XSS in the resolved attributes view.
- [CVE-2020-14969](https://cve.circl.lu/cve/CVE-2020-14969) <= MISP 2.4.128 - app/Model/Attribute.php in MISP 2.4.127 lacks an ACL lookup on attribute correlations. This occurs when querying the attribute restsearch API, revealing metadata about a correlating but unreachable attribute.
- [CVE-2020-15411](https://cve.circl.lu/cve/CVE-2020-15411) <= MISP 2.4.128 - An issue was discovered in MISP 2.4.128. app/Controller/AttributesController.php has insufficient ACL checks in the attachment downloader.
- [CVE-2020-15412](https://cve.circl.lu/cve/CVE-2020-15412) <= MISP 2.4.128 - An issue was discovered in MISP 2.4.128. app/Controller/EventsController.php lacks an event ACL check before proceeding to allow a user to send an event contact form.
- [CVE-2020-25766](https://cve.circl.lu/cve/CVE-2020-25766) <= MISP 2.4.131 - An issue was discovered in MISP before 2.4.132. It can perform an unwanted action because of a POST operation on a form that is not linked to the login page.
- [CVE-2020-28043](https://cve.circl.lu/cve/CVE-2020-28043) <= MISP 2.4.133 - MISP through 2.4.133 allows SSRF in the REST client via the use_full_path parameter with an arbitrary URL.
- [CVE-2020-28947](https://cve.circl.lu/cve/CVE-2020-28947) <= MISP 2.4.134 - In MISP 2.4.134, XSS exists in the template element index view because the id parameter is mishandled. 
- [CVE-2020-29572](https://cve.circl.lu/cve/CVE-2020-29572) =< MISP 2.4.135 - app/View/Elements/genericElements/SingleViews/Fields/genericField.ctp in MISP 2.4.135 has XSS via the authkey comment field.
- [CVE-2021-25324](https://cvepremium.circl.lu/cve/CVE-2021-25324) <= MISP 2.4.136 - Stored XSS in the galaxy cluster view via a cluster name to app/View/GalaxyClusters/view.ctp.
- [CVE-2021-25325](https://cvepremium.circl.lu/cve/CVE-2021-25325) <= MISP 2.4.136 - XSS via galaxy cluster element values to app/View/GalaxyElements/ajax/index.ctp. Reference types could contain javascript: URLs.
- [CVE-2021-25323](https://cvepremium.circl.lu/cve/CVE-2021-25323) <= MISP 2.4.136 - The default setting of MISP 2.4.136 did not enable the requirements (aka require_password_confirmation) to provide the previous password when changing a password.
- [CVE-2021-3184](https://cvepremium.circl.lu/cve/CVE-2021-3184) <= MISP 2.4.136 - XSS via a crafted URL to the app/View/Elements/global_menu.ctp user homepage favourite button.
- [CVE-2021-27904](https://cvepremium.circl.lu/cve/CVE-2021-27904) <= MISP 2.4.139 - An issue was discovered in app/Model/SharingGroupServer.php in MISP 2.4.139. In the implementation of Sharing Groups, the "all org" flag sometimes provided view access to unintended actors.
- [CVE-2021-31780](https://cvepremium.circl.lu/cve/CVE-2021-31780) <= MISP 2.4.141 - an incorrect sharing group association could lead to information disclosure on an event edit. When an object has a sharing group associated with an event edit, the sharing group object is ignored and instead the passed local ID is reused.
- [CVE-2021-35502](https://cvepremium.circl.lu/cve/CVE-2021-35502) <= MISP 2.4.144 - app/View/Elements/genericElements/IndexTable/Fields/generic_field.ctp in MISP 2.4.144 does not sanitize certain data related to generic-template:index.
- [CVE-2021-36212](https://cvepremium.circl.lu/cve/CVE-2021-36212) <= MISP 2.4.145 - app/View/SharingGroups/view.ctp in MISP 2.4.145 does not sanitize the sharing group name.
- [CVE-2021-37534](https://cvepremium.circl.lu/cve/CVE-2021-37534) <= MISP 2.4.146 - app/View/GalaxyClusters/add.ctp in MISP 2.4.146 allows Stored XSS when forking a galaxy cluster.
- [CVE-2021-37742](https://cvepremium.circl.lu/cve/CVE-2021-37742) <= MISP 2.4.147 - app/View/Elements/GalaxyClusters/view_relation_tree.ctp in MISP 2.4.147 allows Stored XSS when viewing galaxy cluster relationships.
- [CVE-2021-37743](https://cvepremium.circl.lu/cve/CVE-2021-37743) <= MISP 2.4.147 - app/View/GalaxyElements/ajax/index.ctp in MISP 2.4.147 allows Stored XSS when viewing galaxy cluster elements in JSON format.
- [CVE-2021-39302](https://cvepremium.circl.lu/cve/CVE-2021-39302) <= MISP 2.4.148 - MISP in certain configurations, when used with PostgreSQL (which is not a default configuration), allows SQL injection via the app/Model/Log.php $conditions['org'] value.
- [CVE-2021-41326](https://cvepremium.circl.lu/cve/CVE-2021-41326) < MISP 2.4.148 - app/Lib/Export/OpendataExport.php mishandles parameter data that is used in a shell_exec call.
- [CVE-2022-27245](https://cvepremium.circl.lu/cve/CVE-2022-27245) <= MISP 2.4.155 - An issue was discovered in MISP before 2.4.156. app/Model/Server.php does not restrict generateServerSettings to the CLI. This could lead to SSRF.  
- [CVE-2022-27243](https://cvepremium.circl.lu/cve/CVE-2022-27243) <= MISP 2.4.155 - An issue was discovered in MISP before 2.4.156. app/View/Users/terms.ctp allows Local File Inclusion via the custom terms file setting. 
- [CVE-2022-27246](https://cvepremium.circl.lu/cve/CVE-2022-27246) <= MISP 2.4.155 - An issue was discovered in MISP before 2.4.156. An SVG org logo (which may contain JavaScript) is not forbidden by default. 
- [CVE-2022-27244](https://cvepremium.circl.lu/cve/CVE-2022-27244) <= MISP 2.4.155 - An issue was discovered in MISP before 2.4.156. A malicious site administrator could store an XSS payload in the custom auth name. This would be executed each time the administrator modifies a user.   
- [CVE-2022-29530](https://cvepremium.circl.lu/cve/CVE-2022-29530) < MISP 2.4.158 - There is stored XSS in the galaxy clusters.
- [CVE-2022-29534](https://cvepremium.circl.lu/cve/CVE-2022-29534) < MISP 2.4.158 - In UsersController.php, password confirmation can be bypassed via vectors involving an "Accept: application/json" header.
- [CVE-2022-29529](https://cvepremium.circl.lu/cve/CVE-2022-29529) < MISP 2.4.158 - There is stored XSS via the LinOTP login field.
- [CVE-2022-29533](https://cvepremium.circl.lu/cve/CVE-2022-29533) < MISP 2.4.158 - There is XSS in app/Controller/OrganisationsController.php in a situation with a "weird single checkbox page."
- [CVE-2022-29528](https://cvepremium.circl.lu/cve/CVE-2022-29528) < MISP 2.4.158 - PHAR deserialization can occur.
- [CVE-2022-29531](https://cvepremium.circl.lu/cve/CVE-2022-29531) < MISP 2.4.158 - There is stored XSS in the event graph via a tag name.
- [CVE-2022-42724](https://cvepremium.circl.lu/cve/CVE-2022-42724) < MISP 2.4.163 - allows attackers to discover role names (this is information that only the site admin should have).
- [CVE-2022-47928](https://cvepremium.circl.lu/cve/CVE-2022-47928) < MISP 2.4.167 - XSS in the template file uploads in app/View/Templates/upload_file.ctp. 
- [CVE-2023-24070](https://cvepremium.circl.lu/cve/CVE-2023-24070) < MISP 2.4.168 - app/View/AuthKeys/authkey_display.ctp in MISP through 2.4.167 has an XSS in authkey add via a Referer field.
- [CVE-2023-24026](https://cvepremium.circl.lu/cve/CVE-2023-24026) < MISP 2.4.168 - In app/webroot/js/event-graph.js has an XSS vulnerability via an event-graph preview payload.
- [CVE-2023-24027](https://cvepremium.circl.lu/cve/CVE-2023-24027) < MISP 2.4.168 - In app/webroot/js/action_table.js allows XSS via a network history name.
- [CVE-2023-24028](https://cvepremium.circl.lu/cve/CVE-2023-24028) < MISP 2.4.168 - In app/Controller/Component/ACLComponent.php has incorrect access control for the decaying import function.
- [CVE-2022-48328](https://cvepremium.circl.lu/cve/CVE-2022-48328) < MISP 2.4.167 - app/Controller/Component/IndexFilterComponent.php in MISP before 2.4.167 mishandles ordered_url_params and additional_delimiters.
- [CVE-2022-48329](https://cvepremium.circl.lu/cve/CVE-2022-48329) < MISP 2.4.166 -  MISP before 2.4.166 unsafely allows users to use the order parameter, related to app/Model/Attribute.php, app/Model/GalaxyCluster.php, app/Model/Workflow.php, and app/Plugin/Assets/models/behaviors/LogableBehavior.php.  
- [CVE-2023-28606](https://cvepremium.circl.lu/cve/CVE-2023-28606) < MISP 2.4.169 - js/event-graph.js in MISP before 2.4.169 allows XSS via event-graph node tooltips. 
- [CVE-2023-28607](https://cvepremium.circl.lu/cve/CVE-2023-28607) < MISP 2.4.169 - js/event-graph.js in MISP before 2.4.169 allows XSS via the event-graph relationship tooltip. 
- [CVE-2023-28884](https://cvepremium.circl.lu/cve/CVE-2023-28884) < MISP 2.4.170 - app/Lib/Tools/CustomPaginationTool.php allows XSS in the community index. 
- [CVE-2023-37306](https://cvepremium.circl.lu/cve/CVE-2023-37306) < MISP 2.4.173 - MISP 2.4.172 mishandles different certificate file extensions in server sync. An attacker can obtain sensitive information because of the nature of the error messages.  
- [CVE-2023-40224](https://cvepremium.circl.lu/cve/CVE-2023-40224) <= MISP 2.4.174 - allows XSS in app/View/Events/index.ctp.

## PGP Key

~~~~
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=fKH+
-----END PGP PUBLIC KEY BLOCK-----
~~~~

