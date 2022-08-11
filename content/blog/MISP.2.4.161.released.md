---
title: MISP 2.4.161 released with small improvements and bugs fixed 
date: 2022-08-11
layout: post
banner: /img/blog/workflow.png 
---

We are pleased to announce the immediate availability of [MISP v2.4.161](https://github.com/MISP/MISP/releases/tag/v2.4.161). 

# Small improvements

- A new option added to log the last API request of an API key. (Thanks to Tom King for the contribution)
- Overcorrelation features have some new improvements such as:
  - A new tool to generate occurrence counts (real numbers this time)
  - A hook to truncate over correlating value table on recorrelation
  - We don't longer store the partial counts as occurrences when generating correlations
- Performance improvements in event fetching
- Various performance tuning in the new correlation engine including the full recorrelation

# Bugs fixed

- `tlp:amber+strict` and `tlp:clear` are now valid tags
- [stix2 import] Better `external_references` parsing for attack patterns objects

Thanks to all the contributors and users reporting bugs to make the software better.

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core. 
