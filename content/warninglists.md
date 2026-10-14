---
layout: page
title: MISP Warning Lists
permalink: /warninglists/
description: Search all MISP warning lists by name, match type and matching attribute to help identify potential false positives.
---

# Put your indicators in context

Explore all the warning lists in [misp-warninglists](https://github.com/MISP/misp-warninglists). These lists identify indicators that may be known, benign, or potential false positives, such as public DNS resolvers, private networks, popular domains, and internet scanners.

Search by name or description and filter by match type or MISP attribute type. Each card includes the list version, entry count, matching attributes, examples, and links to the complete source and JSON definition. `ALL` means a list applies to every attribute type.

A match provides context for analysis; it does not establish that an indicator is harmless. This catalogue describes upstream lists. The lists enabled in your own MISP instance depend on its configuration.

{{< warninglist-catalog >}}

## Use warning lists with MISP

In MISP, open **Warninglists** under **Input Filters**, update the lists, and enable those relevant to your organisation. Review matches alongside the event's context before deciding how to use an indicator.

[Download catalogue metadata](/data/warninglists.json) · [Read the warning-list documentation](https://github.com/MISP/misp-warninglists#readme) · [Contribute a warning list](https://github.com/MISP/misp-warninglists#format-of-a-warning-list)
