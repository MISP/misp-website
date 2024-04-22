---
title: MISP 2.4.190 (and 2.4.191) released with new feed improvement, workflows and a new benchmarking suite. 
date: 2024-04-22
layout: post
tags: ["MISP", "Threat Intelligence", "release" ]
banner: /img/blog/opinion-view.png
---

We are excited to announce the release of MISP v2.4.190. This latest version introduces a slew of new features, improvements, and fixes designed to streamline operations and enhance security measures for our users. 

### What’s New in MISP v2.4.190?

#### Enhanced Tagging and Event Management

- **Advanced Tag Collection for Events**: Users can now specify collections of tags to apply to events automatically when using the [feed:pullEvents] feature. This allows for more precise and organized tagging, leading to better event categorization and retrieval.

- **Conditional Execution Stopping in Workflows**: The new [workflowModules:stop-execution] feature lets users provide a specific reason for stopping a workflow. This is crucial for auditing and maintaining records of why certain processes were halted.

#### Robust Data Handling and Performance

- **Unpublished Event Settings**: The [feed] functionality now includes an option to keep all pulled events in an unpublished state, helping maintain privacy and control over event visibility until ready for disclosure.

- **Benchmarking Suite**: A comprehensive new benchmarking suite has been added to continuously collect and analyze performance metrics such as memory usage and query counts for individual users, endpoints and user-agents. This data is crucial for optimising MISP's performance and reliability as well as identifying misbehaving tools/users/integrations.

### Key Changes and Updates

- **Updated Components**: Major components such as PyMISP, misp-galaxy, and various taxonomy lists have been updated to their latest versions to ensure users have access to the most current data and features.

- **Improved System Logging and Handling**: Several changes have been made to improve how MISP logs and handles data. These include modifications to syslog outputs to avoid line breaks and ensure consistent field counts, enhancing the overall stability and readability of logs.

### Fixes and Optimizations

- **Bug Fixes**: This update addresses several bugs, including issues with tag collection permissions, HTML rendering in analyst data threads, and event report imports from URLs.

- **Performance Enhancements**: Numerous tweaks have been made to reduce memory usage and improve performance across various functions, particularly those involving synchronization and event handling.

### Other Noteworthy Changes

- **Accessibility Improvements**: The update includes enhancements to the user interface's accessibility, such as enabling keyboard focus on certain elements to aid users who rely on keyboard navigation.

- **API Extensions**: New OpenAPI functionalities have been exposed (it was present but not documented), such as allowing data encapsulation in requests and extending STIX export capabilities to attribute levels.

This version of MISP not only introduces new capabilities but also builds on the existing features to provide a more robust, efficient, and user-friendly platform for handling cybersecurity data and events. We encourage all users to upgrade to take full advantage of these improvements.

# MISP 2.4.191

We have released 2.4.191 in rapid succession after 2.4.190 to resolve an issue introduced to the event index filtering

### What’s Fixed in MISP v2.4.191?

- **Event index filtering**: A new feature introducing ANDed tags on the event index has introduced a regression with the way we handle multiple tags in the filters. This issue is now resolved and the new feature has been postponed to 2.4.192 to ensure that it is up to snuff with the expectations.

- **Set OIDC issuer**: It is now possible to set the issuer in the OIDC authentication subsystem.

### A long list of bug fixes

Please refer to the full [changelog](https://www.misp-project.org/Changelog.txt) for a full list of fixes and improvements. Many thanks to all the diligent contributors that ensure that MISP keeps improving rapidly!
