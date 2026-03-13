---
title: MISP Workbench `v1.0` (beta) Released
authors:
- Luciano Righetti
date: 2026-03-13
banner: /img/blog/misp-workbench/MISP-satellite_workbench-verti-color.jpg
tags: ["integration", "MISP", "Threat Intelligence", "opensearch", "misp-workbench"]
layout: post
---

# MISP Workbench – First Release `v1.0` (beta)
MISP Workbench is a powerful analyst-focused platform designed to tame the challenge of working with large volumes of threat intelligence at scale. It is capable of ingesting data from multiple origins — including MISP instances, external feeds, and other threat intelligence sources — and consolidates them into a unified workspace where analysts can actually get things done.
At its core, MISP Workbench puts the analyst in control: query across your entire data corpus, enrich and process indicators, pivot between related intelligence, and push curated results back to MISP or downstream consumers — all from one place. Whether you're triaging a large batch of incoming indicators, hunting for patterns across feeds, or preparing a finished intelligence product, MISP Workbench is built to cut through the noise and accelerate the workflow from raw data to actionable insight.

This first beta release marks the foundation of that vision — expect rough edges, rapid iteration, and a strong appetite for [feedback](https://github.com/MISP/misp-workbench/discussions/218).

## Use Cases

**Indicator triage at scale** — When a large batch of new indicators arrives from multiple feeds, Workbench lets analysts query, filter, and correlate across the full corpus without jumping between tools or writing one-off scripts.

**Threat hunting** — Define saved searches (hunts) that run on a schedule and alert when matching indicators appear. Useful for persistent monitoring of specific adversary TTPs, infrastructure patterns, or emerging campaigns.

**Feed consolidation and deduplication** — Organisations running several MISP instances or subscribing to multiple commercial and open-source feeds can centralise ingestion, correlate overlapping data, and surface unique intelligence rather than processing the same indicators repeatedly.

**IOC enrichment** — Enrich ingested indicators through misp-modules (passive DNS, WHOIS, sandbox lookups, etc.).

**Intelligence product preparation** — Analysts can pivot between related indicators, build a curated dataset, and export a finished intelligence product without leaving the platform.

## Who Is It For?

| Audience | Why Workbench helps |
|---|---|
| **SOC / IR teams** | Fast triage of incoming indicators against historical data; hunt for related infrastructure during an incident |
| **CTI analysts** | Centralised workspace for multi-source research, enrichment, and finished intelligence production |
| **MISP operators** | Offload heavy correlation and search workloads away from the core MISP instance |
| **Red teams / researchers** | Query large indicator datasets and cross-reference findings across feeds without running ad-hoc scripts |

## Main Features
| Feature | Description |
|---|---|
| [Feed ingestion](https://misp-workbench.readthedocs.io/en/latest/features/feeds/index.md) | Ingest MISP, CSV, JSON, and Freetext feeds on a schedule or on demand |
| [Correlations](https://misp-workbench.readthedocs.io/en/latest/features/correlations.md) | Batch and incremental correlation scans over indexed attributes |
| [Explore](https://misp-workbench.readthedocs.io/en/latest/features/explore.md) | Lucene queries against OpenSearch for fast indicator lookups |
| [Enrichments](https://misp-workbench.readthedocs.io/en/latest/features/enrichments.md) | IOC enrichment powered by [misp-modules](https://github.com/MISP/misp-modules) |
| [Hunt](https://misp-workbench.readthedocs.io/en/latest/features/hunts.md) | Hunts are saved searches that run periodically and trigger alerts. |
| [Notifications](https://misp-workbench.readthedocs.io/en/latest/features/notifications.md) | Event-driven notifications processed by Celery workers |
| **REST API** | FastAPI backend with automatic OpenAPI documentation |
| **Storage** | Garage (S3-compatible) or local filesystem for attachments |

## Get Started

- **Repository:** [MISP/misp-workbench](https://github.com/MISP/misp-workbench)
- **Release:** [beta-1.0](https://github.com/MISP/misp-workbench/releases/tag/beta-1.0)
- **Documentation:** [misp-workbench.readthedocs.io](https://misp-workbench.readthedocs.io/en/latest/)

## Roadmap

Here is a glimpse of what is coming next:

- [MCP Endpoints for LLM-Driven Querying of OpenSearch Data](https://github.com/MISP/misp-workbench/issues/126)
- [AI-assisted Lucene query-builder](https://github.com/MISP/misp-workbench/issues/219)
- [JA4+ correlations](https://github.com/MISP/misp-workbench/issues/132)
- [Flowintel Case Management Integration](https://github.com/MISP/misp-workbench/issues/89)
- [Something else? Let us know](https://github.com/MISP/misp-workbench/issues/new)

Have a feature request, a bug report, or just want to share your experience? Drop some [feedback](https://github.com/MISP/misp-workbench/discussions/218) — it helps shape what gets built next.


## Screenshots
![explore-view](/img/blog/misp-workbench/misp-workbench-1_explore.png)
![hunt-view](/img/blog/misp-workbench/misp-workbench-1_explore.png)
![add-json-feed](/img/blog/misp-workbench/misp-workbench-json-feeds-view.png)

