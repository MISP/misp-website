---
title: MISP v2.5.3 and v2.4.201 released with numerous enhancements, bug fixes, and security improvements to strengthen threat information sharing capabilities. 
banner: /img/blog/galaxy-link.png
author:
 - MISP Project team
date: 2024-12-22
tags: ["MISP", "Threat Intelligence", "release" ]
layout: post
---

We are excited to announce the latest updates to [MISP](https://github.com/misp/misp) with versions **v2.5.3** and **v2.4.201**, which bring numerous enhancements, bug fixes, and security improvements to strengthen threat information sharing capabilities. As with any security release, we highly recommend that you update ASAP and inform your partners to do the same. 

## 🚀 **New Features**  

### **Improved Editor and Report Management**  
- **CodeMirror Editor Plugin**: Added a new `placeholder` plugin to display placeholders in the editor interface.  
- **Instance-Wide Report Variables**: Introduced instance-wide template variables for reports.  
  - Only site administrators can create, edit, or delete these variables.  
  - All users can now utilize and view these variables.  
### **Protected event improvements**
  - Exchanging of protected events via feeds is now supported
  - Uploading protected events via the import MISP JSON functionality is now supported
  - Added new endpoint to let the instance sign arbitrary data on demand (with a new role permission and ACL setting to go along with this powerful functionality)

## 🔧 **Changes and Enhancements**  

### **Statistics and Database Improvements**  
- **Statistics Update**: Added the count of objects on the MISP instance.  
- **Database Schema**: Updated schema for enhanced performance and compatibility.  
- **CLI-Only Settings**: Server settings have been further restricted to CLI-only for improved security.

### **Performance Optimizations**  
- Faster methods for attribute validation, internal MySQL cache, and virtual field fetching.  
- Optimized `simdjson` for faster UTF-8 validation.  

### **UI Enhancements**  
- **Event Row Objects**: Truncate long text in highlighted attributes for better readability.  
- Improved UI messages for file alias management, error handling, and general clarity in the Event report's "Imported Picture" page.  
- Notices about unknown clusters are now less alarming.  

### **Sync and Server Improvements**  
- Added UI and API export to display bound synchronization users in `/users` and `/servers` views.  
- Updated Redis serializer to default to JSON.  

## 🛠 **Fixes**  

### **Security Fixes**  
- **Stored XSS**: Fixed stored XSS vulnerabilities in:  
  - Custom cluster exports to MISP Galaxy format.  
  - Editor interfaces for ad-hoc workflows.  
- **Analysis File Upload**: Enhanced sanitization and error handling to mitigate filename tampering risks.  
- **Protected Events**:  
  - Tightened requirements for modifying protected events.  
  - Added validation for MISP JSON file uploads and signed feeds.  

### **Other Bug Fixes**  
- Fixed internal server errors for non-site admins when viewing collections.  
- Addressed issues with file uploads, ACL enforcement, and UI redirects.  
- Fixed typos, incorrect notices, and messages in various UI components.  
- Restored functionality for bookmark deletions and organization-level bookmark management.  
- Improved STIX1 import handling for packages without titles.  
- Enhanced LDAPAuth to support configurable email fields and TLS/LDAPS connections.

## 🧩 **Other Updates**  
- **Performance**: Multiple optimizations to improve speed and database efficiency.  
- **Documentation**:  
  - Updated OpenAPI documentation for `analystData/indexMinimal`.  
  - Minor fixes to README installation instructions.  
- **Merges**: Codebase consolidation from multiple branches to ensure stability across versions.  

### **Contributors and Acknowledgments**  
We extend our gratitude to the contributors and security researchers who reported issues and provided fixes:  
- **Jeroen Pinoy**  
- **Ianis Bernard (Acylia)**  
- **Fukusuket (Fukusuke Takahashi)**  
- **Wachizungu**  
- **Christian Studer**  
- **Luciano Righetti**  
- **Jakub Onderka**  
- **Vincenzo Caputo**  

### **Upgrade Notes**  
- Existing installations should run the upgrade scripts and verify Redis serializer settings.  
- Ensure TLS configurations are properly set if using LDAPAuth.  

---

We highly recommend all users to upgrade to these latest versions for improved stability, performance, and security.

**Thank you for supporting MISP!**  
