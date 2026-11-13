---
layout: page
title: Guidelines for Building and Federating Cybersecurity Information-Sharing Communities 
permalink: /building-information-sharing-communities/
toc: true
---

## Purpose of this document

This document provides practical guidance for organisations, teams, CSIRTs, CERTs, sectoral groups, professional communities, public-private partnerships, Information Sharing and Analysis Centres (ISACs), Information Sharing and Analysis Organisations (ISAOs), and other communities of interest that want to create or evolve a cybersecurity information-sharing community.

The objective is not to prescribe one organisational model. Information-sharing communities differ in size, mandate, sector, geography, legal environment, technical maturity, and available resources. Instead, this document describes a set of reusable principles, decisions, operational patterns, and maturity steps that can be adapted to the needs of a new or existing community.

It combines two closely related perspectives:

1. **How to create and operate an information-sharing community**: purpose, governance, membership, services, agreements, information-exchange policies, security, compliance, tooling, engagement, and sustainability.
2. **How to federate information-sharing communities and autonomous teams**: interconnecting organisations and communities while preserving their own mandates, data ownership, operational autonomy, and disclosure decisions.

The central principle is that effective information sharing is not primarily a technology problem. Technology can reduce friction and support enforcement, but sustainable sharing depends on **trust, reciprocity, clear purpose, understandable rules, useful contributions, and continuous human interaction**.

MISP is used throughout this document as a reference implementation for structured information exchange because its data model, distribution mechanisms, taxonomies, sharing groups, synchronization features, and decentralised deployment model map naturally to information-sharing communities. The organisational and governance principles, however, are applicable regardless of the platform selected.

## What is an information-sharing community?

An information-sharing community is a group of organisations or individuals that agree to exchange information for a shared purpose. In cybersecurity, this can include information about:

- cyber threats and threat actors;
- incidents and incident-response findings;
- vulnerabilities and coordinated vulnerability disclosure;
- indicators and observables;
- tactics, techniques, and procedures;
- malware and infrastructure analysis;
- defensive measures and detection methods;
- threat hunting and analytical methodologies;
- situational awareness;
- lessons learned and best practices;
- shared data sources and enrichment services;
- operational requests for assistance;
- strategic or sector-specific analysis.

The community can be highly formal, with a legal entity, membership agreements, a steering board, paid services, and dedicated staff. It can also begin as a small circle of trusted practitioners sharing through meetings, chat, email, or a shared platform.

Names such as **ISAC**, **ISAO**, **sharing community**, **community of trust**, **sectoral community**, or **federated team** describe overlapping models. The precise label matters less than having a shared understanding of the community's purpose, participants, rules, and expected value.

### Federation

A **federated information-sharing community** is a collaboration between autonomous organisations or communities that exchange, enrich, and act on information **without relinquishing control over their own operations, infrastructure, data, membership, or disclosure decisions**.

Federation can occur across several dimensions:

- **Cross-organisation:** public, private, academic, non-profit, and operational teams collaborate under an agreed trust framework.
- **Cross-country:** national or regional teams exchange information while respecting jurisdictional and organisational constraints.
- **Cross-sector:** sector-specific communities cooperate to identify threats and cascading effects that do not stop at sector boundaries.
- **Cross-topic:** communities focused on themes such as ransomware, operational technology, vulnerability disclosure, fraud, or supply-chain security exchange selected information.
- **Community-to-community:** established communities connect to one another without merging their governance or membership.

Federation therefore does not require centralisation. A community can remain locally governed while participating in a broader network of trusted peers.

## Core principles

The following principles should guide the design of an information-sharing community from its first meeting through later federation.

### Start with purpose, not tooling

Before choosing a platform, define why the community should exist. Members need a concrete reason to participate. A community that cannot explain its value proposition will struggle to generate sustained contributions regardless of the quality of its technology.

### Trust is the primary infrastructure

Sharing depends on confidence that information will be handled correctly, that mistakes will be treated constructively, and that members will receive value in return for their contributions. Trust usually begins between people before it becomes institutionalised through governance, agreements, processes, and technical controls.

### Lead by example

New communities should not expect members to immediately know what good sharing looks like. Operators and mature members should demonstrate useful contributions, good contextualisation, responsible handling, and constructive feedback.

### Grow participation organically

Overly strict contribution requirements can discourage less mature members or create incentives to share low-value data merely to satisfy quotas. A community should encourage participation, provide examples and training, and progressively raise maturity rather than designing participation around punishment.

### Context is more valuable than volume

A large quantity of indicators without context may be less useful than a smaller set of well-described observations. Members should understand why something is being shared, what confidence exists, how it was observed, what action may be appropriate, and what limitations apply.

### Be lenient on collection and strict on operationalisation

Information that appears irrelevant to one member may be highly valuable to another or may become relevant later. Communities should avoid discarding information solely because it is not immediately actionable. At the same time, information used for blocking, alerting, automated remediation, or other operational actions should pass stricter quality and confidence thresholds.

### Decide on common vocabularies early

Common classification, terminology, taxonomies, and metadata are essential for search, filtering, automation, federation, and interoperability. Agreeing on them early reduces ambiguity and makes later scaling easier.

### Preserve autonomy

Federation should strengthen participants rather than replace their mandates. Each organisation should retain control over its own data, access decisions, local operations, and participation in other communities.

### Keep policy understandable

Rules that cannot be understood by analysts will not be applied consistently. Information-sharing policies should be short enough to be operationally usable, with more detailed legal or procedural material available when necessary.

### Design for evolution

Threats, regulations, technologies, membership, and organisational priorities change. Governance, data models, infrastructure, and processes should therefore be maintainable and adaptable rather than rigid.

## A lifecycle for creating and federating a community

A practical community lifecycle can be organised into the following phases:

1. **Define the purpose and scope.**
2. **Establish governance and membership.**
3. **Define services and the operating model.**
4. **Create information-sharing rules.**
5. **Build trust and engagement mechanisms.**
6. **Select technical mechanisms and architecture.**
7. **Secure the community and address compliance.**
8. **Operate, measure, improve, and federate.**

These phases do not need to be completed sequentially. A small community can start with a lightweight set of decisions and formalise them as participation grows.

The diagram groups related decisions and shows how operational experience feeds back into the community's purpose. Activities can overlap; federation can begin with a narrow pilot whenever the relevant rules and capabilities are ready.

[![Community lifecycle: purpose leads to governance and services, sharing rules and trust, architecture and safeguards, then operation and improvement, with lessons feeding back into purpose.](/img/community-guidelines/lifecycle.svg "{.img-responsive}")](/img/community-guidelines/lifecycle.svg)

[Mermaid source](/img/community-guidelines/lifecycle.mmd)

# Part I - Creating the Community

## Define purpose, scope, and value

### Vision, mission, and purpose

The first task is to answer a small number of direct questions:

- What problem are we trying to solve together?
- What should members be able to do through the community that they cannot easily do alone?
- Who is the intended membership?
- What kinds of information are in scope?
- What outcomes should demonstrate that the community is useful?
- Is the community primarily operational, analytical, strategic, capacity-building, or a combination?

A useful mission statement should be specific enough to guide decisions but broad enough to remain valid as the community matures.

For example, a community can be created to improve early warning for a sector, coordinate vulnerability disclosure, share incident findings, exchange malware analysis, mutualise access to datasets, or provide a trusted environment for joint threat analysis.

### Define the community scope

Two common dimensions are:

- **Sectoral scope:** single sector, multiple sectors, or topic-based.
- **Geographical scope:** local, national, regional, cross-border, or international.

Other useful dimensions include organisational type, security clearance or trust level, technical capability, mandate, and operational responsibility.

The scope does not have to remain fixed. Communities often start with a narrow circle of organisations sharing a clear operational problem and later expand.

### Define the value proposition

Members need to understand the practical benefit of participation. Potential benefits include:

- earlier detection of threats observed by peers;
- access to contextualised intelligence rather than isolated indicators;
- mutual support during incidents;
- reduced duplication of analysis;
- access to specialised expertise;
- shared tooling or data sources;
- improved vulnerability-management or disclosure coordination;
- access to training and exercises;
- stronger cross-sector or cross-border situational awareness;
- improved readiness to interact with CSIRTs, regulators, or other communities.

The value proposition should be revisited periodically. A community that no longer solves members' problems will lose participation even if its infrastructure remains operational.


## Establish governance

Governance defines who can make decisions, who performs operational tasks, and how rules are changed.

### Choose an appropriate level of formalisation

A small community may begin with a coordinator and a few documented rules. A larger or more sensitive community may require a legal entity, contractual relationships, formal boards, working groups, dedicated staff, and written escalation procedures.

Possible governance roles include:

- **Coordinating entity or secretariat:** membership, onboarding, community operations, administration, and coordination.
- **Steering or advisory group:** strategic direction and balanced representation of members.
- **Technical operators:** maintenance of sharing platforms and supporting services.
- **Community managers:** engagement, events, communication, and onboarding.
- **Working groups:** specialised topics such as malware, vulnerability disclosure, fraud, threat hunting, or operational technology.
- **Legal/privacy/security contacts:** support for policy, compliance, and sensitive cases.

Avoid creating unnecessary bureaucracy. Governance should make decisions clearer, not slower.

### Policy, standards/guidelines, and procedures

Community documentation can be divided into three useful levels:

- **Policies:** management expectations, principles, and mandatory high-level rules.
- **Standards and guidelines:** common practices, formats, classifications, and recommended or mandatory implementation choices.
- **Procedures:** step-by-step operational instructions for recurring tasks.

This distinction makes it possible to keep high-level policies stable while changing implementation details without renegotiating the entire governance framework.

### Legal structure

A separate legal structure may be useful when the community needs to employ staff, sign contracts, collect membership fees, operate shared infrastructure, procure services, or assume liabilities.

It is not mandatory for every community. Informal or hosted communities can be effective when there is already a trusted coordinating organisation capable of supporting them.

### Types of agreements

The appropriate agreement depends on the community's purpose and legal context. Possible mechanisms include:

| Agreement | Typical use | General level of formality |
|---|---|---|
| Subscriber or membership agreement | Formal membership, paid services, contractual obligations | Legally binding where applicable |
| Confidentiality / NDA | Protection of confidential information | Usually binding |
| Code of conduct | Behaviour, expected practices, community norms | Written; legal effect depends on context |
| Memorandum of Understanding | Cooperation between organisations or communities | Usually a formal statement of cooperation; legal effect varies |
| Operational rules / terms of participation | Practical rules for use of community services | Depends on implementation |
| Informal trust agreement | Small, highly trusted groups | Low formalisation |

Legal enforceability varies by jurisdiction. The community should obtain appropriate legal advice when legal effect matters.

### Non-compliance and dispute handling

Members should know what happens when rules are not respected. The process can be proportional and progressive, for example:

1. clarification and informal discussion;
2. warning and corrective action;
3. temporary restriction of access;
4. review by the governance body;
5. suspension or termination of membership.

A community should distinguish malicious misuse from understandable operational mistakes. Excessively punitive handling of mistakes can reduce willingness to share.

### Exit, organisational change, and mergers

Governance should explain what happens when a member:

- voluntarily leaves;
- loses eligibility;
- changes legal status;
- merges with another organisation;
- is acquired;
- splits into multiple entities;
- ceases operations.

Important questions include the continued handling of previously received information, account revocation, retained local copies, shared credentials, access to sub-communities, and whether permissions transfer to a successor organisation.


## Membership and onboarding

### Membership criteria

Membership criteria should support the community's purpose. Examples include:

- belonging to a defined sector, geography, profession, or constituency;
- having a compatible operational mandate;
- being recommended by an existing trusted member;
- completing a direct meeting or onboarding call;
- agreeing to community policies and information-handling rules;
- identifying operational and administrative points of contact;
- demonstrating an ability to protect shared information.

The criteria should be transparent enough that candidates understand why they are accepted or declined.

### Onboarding process

A practical onboarding process can include:

1. nomination or application;
2. verification of the organisation and contacts;
3. approval according to the community's governance;
4. acceptance of policies or agreements;
5. introduction to the community's purpose and culture;
6. training on information handling and tooling;
7. creation of accounts and technical access;
8. introduction to other members;
9. a first contribution or sharing exercise.

The onboarding process is one of the first opportunities to establish trust and behavioural norms.

### Different participation models

Not all members need identical capabilities. A community can support:

- full members;
- observers;
- trusted partners;
- service providers;
- public-sector liaison organisations;
- research or academic partners;
- temporary incident-specific participants;
- sub-community membership.

Differences in access and responsibilities should be explicit.

### External communication and growth

The community should decide how visible it wants to be. Some communities deliberately remain small and invitation-only; others need public communication to attract new participants, explain their role, publish outputs, or build relationships with neighbouring communities.

An external communication approach can define:

- whether the membership list is public;
- who may speak on behalf of the community;
- which outputs may be published publicly;
- how new organisations can express interest;
- how conferences, workshops, and outreach are used for recruitment;
- how public reporting avoids exposing sensitive member activity.

Growth should remain aligned with purpose. More members are useful only if the trust model, governance, and services can scale with them.


## Define services and the operating model

Information sharing is usually the core capability, but communities often become more valuable by offering complementary services.

### Typical services

Potential services include:

- structured cyber-threat information exchange;
- incident and situational-awareness briefings;
- vulnerability information and coordinated disclosure;
- threat analysis and enrichment;
- malware analysis;
- forensic support;
- threat hunting;
- shared detection engineering;
- access to shared datasets or enrichment sources;
- vulnerability-management support;
- joint exercises and training;
- analytical working groups;
- law-enforcement or public-sector liaison;
- case coordination;
- qualification, validation, or scoring of shared information;
- community-developed tools, taxonomies, playbooks, and methodologies.

A new community should begin with a small set of services that can be delivered reliably rather than an ambitious catalogue that cannot be maintained.

### Operating model

Decide who provides each service and under which conditions. Services may be:

- provided centrally by the community operator;
- contributed by members;
- provided by specialised working groups;
- procured from third parties;
- mutually provided through federation.

### Funding and sustainability model

Possible funding models include:

- membership fees;
- subscriptions to specific services;
- public funding or grants;
- support from a coordinating organisation;
- donations or sponsorship;
- mixed funding.

Funding should not unintentionally create incentives that undermine trust, such as using member-contributed information in ways that members did not expect.

### External partnerships

A community may need structured relationships with public authorities, law-enforcement bodies, research organisations, service providers, other ISACs/ISAOs, vulnerability coordinators, or international partners. These relationships should be explicit about:

- the purpose of the partnership;
- whether the external party is a member, observer, service provider, or separate peer community;
- what information can be exchanged;
- whether onward redistribution is permitted;
- escalation and points of contact;
- whether a dedicated MoU, NDA, or other agreement is appropriate.

A partnership does not automatically imply access to all community information. The principle of least necessary access should also apply to trusted external partners.

# Part II - Rules for Information Sharing

## Create an information-exchange policy

An information-exchange policy is one of the most important documents in the community. It should answer four questions for any shared item:

1. **Handling:** how must the recipient protect it?
2. **Action:** what may the recipient do with it?
3. **Sharing:** with whom may it be redistributed?
4. **Licensing:** what terms govern reuse?

These dimensions can be expressed using standards such as the FIRST Information Exchange Policy framework, Traffic Light Protocol markings, community-specific taxonomies, or equivalent mechanisms.

### Handling

Handling rules can address:

- confidentiality;
- access on a need-to-know basis;
- storage requirements;
- encryption;
- retention;
- logging;
- requirements for onward recipients;
- handling of personal or regulated data;
- notification if information is exposed or misused.

### Permitted actions

Recipients need to understand whether information is intended for:

- awareness only;
- internal analysis;
- correlation;
- threat hunting;
- detection;
- blocking;
- automated prevention;
- incident response;
- vulnerability remediation;
- redistribution;
- publication.

This is particularly important when an indicator might lead to an operational action. An indicator useful for investigation is not automatically appropriate for blocking.

### Sharing and redistribution

The policy should define:

- the dissemination marking scheme;
- whether redistribution is permitted;
- whether redistribution requires approval;
- whether sharing is limited to a specific group;
- whether community-to-community federation is allowed;
- how to handle information received from third parties;
- when regulatory or mandatory reporting obligations override normal community rules.

### Licensing

Where relevant, state whether information can be reused, modified, redistributed, integrated into products, or published. Avoid assuming that all data received by the community can be redistributed merely because it is technically accessible.

The following decision flow applies before sending information to another member or community. Review all applicable terms together: a dissemination marking alone does not describe every permitted action or reuse condition. Mandatory reporting obligations should be resolved through the applicable policy and legal process.

[![Before sharing, check permission for the recipient and purpose, clarify missing permission, verify technical controls, and preserve provenance and markings when sending.](/img/community-guidelines/sharing-decisions.svg "{.img-responsive}")](/img/community-guidelines/sharing-decisions.svg)

If the intended recipient or purpose changes, repeat the checks. Passing these checks permits the exchange; operational use still requires a separate assessment of quality, confidence, and suitability.

[Mermaid source](/img/community-guidelines/sharing-decisions.mmd)

### Attribution and anonymity

A community should decide whether members may:

- share under their organisation's name;
- share anonymously to the community;
- ask the operator to publish on their behalf;
- use pseudonymous identities;
- prohibit attribution outside the community.

Anonymous or delegated sharing can lower barriers to contribution, but the operator must still preserve sufficient internal provenance for trust, abuse handling, and quality control.

### Mandatory and voluntary sharing

Regulatory reporting and voluntary peer-to-peer sharing can coexist, but recipients should be able to distinguish them. Context should make clear whether information is shared because of an obligation, as a voluntary contribution, or both.

### Sub-communities

As communities grow, subsets of members often need their own sharing spaces. Examples include:

- a sector-specific subgroup in a national community;
- a temporary incident working group;
- a vulnerability-disclosure group;
- a malware-analysis group;
- a group limited to organisations operating a particular technology.

The operator should decide whether sub-communities are allowed, how they are created, who administers membership, how their lifecycle is maintained, and whether they can federate independently.

Compartmentalisation should solve a real trust or operational need. Too many isolated groups can fragment information and weaken the wider community.

## What should be shared?

### Sources

Community information can originate from:

- incident-response investigations;
- internal SOC or CSIRT observations;
- malware analysis;
- honeypots, spam traps, sensors, or sandboxing;
- open-source intelligence;
- vulnerability research and disclosure;
- commercial or partner intelligence where redistribution is permitted;
- shared datasets;
- threat hunting;
- member reports and requests;
- public reports that have been enriched by members.

### Types of contributions

Useful contributions include more than new indicators:

- incident reports;
- observations and sightings;
- corrections;
- false-positive feedback;
- confidence or relevance assessments;
- relationships between existing items;
- attribution hypotheses and counter-analysis;
- mitigation guidance;
- detection rules;
- vulnerabilities and remediation information;
- analytical reports;
- methods and workflows;
- requests for assistance;
- lessons learned.

A healthy community allows members to improve information shared by others rather than treating each contribution as immutable.

### Add context

Whenever possible, shared information should explain:

- what was observed;
- when and where it was observed;
- why it may matter;
- the source or provenance;
- the level of confidence;
- the intended use;
- known limitations;
- relationships with other information;
- whether the information has already been validated or operationalised.

### False positives and uncertainty

Uncertainty should be represented rather than hidden. Analysts need ways to express confidence, disagreement, false positives, expiry, sightings, and alternate interpretations.

A useful operational rule is:

> Keep potentially useful analytical information when storage and policy allow it, but apply stricter selection before using information for automated defensive actions.

## Common vocabularies and data models

### Why vocabulary matters

A shared vocabulary allows members and connected communities to interpret information consistently. It supports:

- search;
- filtering;
- prioritisation;
- automation;
- access control;
- cross-community synchronization;
- statistics and measurement.

A community should agree early on the minimum vocabularies required for its most common use cases.

### MISP taxonomies

MISP taxonomies provide machine-readable vocabularies for classification and marking. Communities can select and enforce a subset of vocabularies appropriate for their use case and can create their own when required.

Possible uses include describing:

- confidence;
- information sensitivity;
- priority;
- intended use;
- threat level;
- sector;
- workflow status;
- source reliability;
- information-exchange policy.

### MISP galaxies

MISP galaxies provide richer contextual structures for concepts such as:

- threat actors;
- campaigns;
- malware families;
- ransomware;
- tools;
- attack techniques;
- mitigation or methodology frameworks.

Communities can maintain local knowledge while also reusing common open vocabularies. Alternate perspectives should be representable rather than forcing one community's analysis to become globally authoritative.

### Interoperability

The goal of standardisation is not to eliminate local differences. It is to make the meaning of those differences explicit enough that information can move safely between systems and communities.

# Part III - Building the Human Community

## Trust, reciprocity, and engagement

### Human relationships

Trust often begins through personal interaction before being reinforced through written agreements and technical controls. Useful mechanisms include:

- face-to-face workshops;
- working sessions;
- bilateral discussions;
- joint incident handling;
- training;
- tabletop exercises;
- staff exchanges;
- informal community events;
- regular virtual meetings.

The community operator should create opportunities for members to know whom they are sharing with.

### Lead by example

Operators and mature members should demonstrate:

- how to structure useful information;
- how much context to provide;
- how to mark sensitivity;
- how to communicate uncertainty;
- how to give feedback;
- how information can be operationalised safely.

This is usually more effective than imposing complex contribution rules at the beginning.

### Feedback loops

Feedback makes sharing valuable. Useful mechanisms include:

- sightings;
- comments;
- corrections;
- proposals for changes;
- enrichment;
- acknowledgement of usefulness;
- follow-up on how information helped an investigation;
- recognition of contributors.

A community that only distributes information from a central source is a feed, not a collaborative sharing community.

The feedback loop connects contribution to operational value. Information can remain useful for analysis even when it does not meet the threshold for a particular defensive action. Feedback and updates follow the same handling and redistribution rules as the original contribution.

[![Peers enrich and validate observations, assess suitability for operational use, and return findings and corrections to improve the shared information.](/img/community-guidelines/feedback-loop.svg "{.img-responsive}")](/img/community-guidelines/feedback-loop.svg)

[Mermaid source](/img/community-guidelines/feedback-loop.mmd)

### Recognition and credit

Contributors should receive credit when policy permits. Recognition can be simple: acknowledgement in a report, visibility in community statistics, invitations to present work, or explicit thanks from other members.

Do not appropriate members' analysis or present community contributions as the operator's own work.

### Cultural and linguistic differences

Cross-border communities need to account for different terminology, communication styles, legal assumptions, and analytical conventions. Common taxonomies and structured metadata help, but they do not replace direct human interaction.

## Communication and collaboration channels

No single tool supports every form of collaboration. A community usually needs several channels.

### Human-to-human communication

Typical mechanisms include:

- chat platforms;
- secure email;
- mailing lists;
- voice and video conferencing;
- forums;
- collaborative notes or wikis;
- in-person meetings.

Chat platforms such as Mattermost or comparable alternatives can support channels, role-based access, threaded discussion, notifications, integrations, and auditability. The exact product is less important than matching the community's confidentiality and operational requirements.

### Case management

Structured intelligence exchange and operational coordination are different problems. When members jointly handle investigations, incidents, vulnerability disclosures, or analysis tasks, a case-management layer can provide:

- shared task coordination;
- distributed ownership;
- references to intelligence objects;
- progress tracking;
- role-based access;
- audit trails;
- workflow templates;
- controlled sharing of selected case metadata.

A federated case-management model should allow each organisation to keep internal details private while selectively exposing enough information for coordination.

Open-source tools such as FlowIntel can be considered where integration with MISP and shared analytical workflows is useful, but communities should select tools based on their actual requirements and avoid unnecessary lock-in.

### Shared analytical workflows

Documenting repeatable analytical workflows can improve reproducibility and knowledge transfer. A workflow can describe:

- enrichment steps;
- validation routines;
- decision points;
- required data sources;
- tools used;
- expected outputs;
- escalation or response procedures.

Reusable workflows can be shared between autonomous teams even when the underlying case data remains local.

# Part IV - Technical Architecture and Federation

## Choosing an information-sharing architecture

There is no single correct architecture. The choice depends on trust, scale, resources, sovereignty requirements, latency, and operational maturity.

### Central or hub-and-spoke

A coordinating organisation operates a central sharing platform used by members.

**Advantages:**

- easy onboarding;
- simpler administration;
- consistent configuration;
- lower infrastructure burden for members;
- useful for bootstrapping a new community.

**Trade-offs:**

- dependency on the central operator;
- central availability and capacity become important;
- the hub has greater visibility into community activity;
- governance of the central service becomes critical.

### Peer-to-peer or mesh

Multiple organisations operate their own platforms and synchronize directly with selected partners.

**Advantages:**

- strong local autonomy;
- no single repository is required;
- resilience against loss of a central service;
- selective bilateral or topical relationships.

**Trade-offs:**

- greater operational complexity;
- policy consistency is harder;
- members require more technical capability;
- synchronization filters and trust relationships require careful maintenance.

### Hierarchical

Local or sectoral communities connect to coordinating nodes, which may in turn connect to other national, regional, or international communities.

This can reflect organisational mandates and allow each layer to filter, validate, enrich, or redistribute information according to its role.

The main risk is that hierarchy becomes confused with authority over the underlying data. The originating organisation's distribution decisions and provenance should remain explicit.

### Hybrid

Most mature environments are hybrid. Some members use a centrally hosted platform, others run their own instances, and selected organisations maintain direct relationships for particular topics.

Hybrid architectures are often the most practical because they allow technical maturity and trust relationships to vary between members.

### Architecture selection table

| Question | Hub-and-spoke | Peer-to-peer | Hierarchical | Hybrid |
|---|---:|---:|---:|---:|
| Easy for new members | High | Low | Medium | High |
| Local autonomy | Medium | High | Medium/High | High |
| Operator complexity | Medium | High/distributed | High | High |
| Resilience | Medium | High | Medium | High |
| Fine-grained bilateral sharing | Medium | High | Medium | High |
| Suitable for mixed maturity | High | Low/Medium | Medium | High |

The table is indicative rather than prescriptive.

## MISP as a federated information-sharing platform

MISP can support the collection, production, and dissemination of structured cybersecurity information while preserving provenance and distribution choices.

### Deployment models

A community can use MISP in several ways:

- a shared MISP instance hosted by the community operator;
- a shared instance hosted by an existing trusted organisation;
- individual member instances synchronized with the community;
- a mixed model in which some members use the shared instance and others operate their own;
- multiple connected communities exchanging selected information.

The deployment model should follow governance and trust requirements rather than forcing governance to match the technology.

### Collection

MISP can ingest and normalise information from sources such as feeds, incident reports, vulnerability information, malware analyses, automated collection systems, and member contributions.

### Production and enrichment

Analysts can add relationships, context, taxonomies, galaxies, sightings, comments, and other enrichment. This enables the community to co-produce intelligence rather than merely aggregate feeds.

### Dissemination and access control

Important mechanisms include:

- **distribution levels** to describe intended reach;
- **sharing groups** for explicit sets of organisations;
- **tag-based access-control and filtering**;
- **synchronization filters**;
- **feeds** for controlled import or export;
- **audit logging** for traceability;
- **cryptographic mechanisms** where stronger authenticity or integrity controls are required;
- **additional policy-enforcement layers**, such as MISP Guard, where a community needs safeguards beyond normal configuration.

These mechanisms can implement policy, but they cannot define the policy. The community must first agree what sharing is allowed.

### Federation between communities

Federation is not limited to synchronizing every item between every server. Communities should define:

- which categories of information can cross community boundaries;
- whether original distribution markings are preserved;
- whether recipients may redistribute further;
- how provenance is retained;
- whether corrections and sightings flow back to the source;
- how revocation or updates are handled;
- which taxonomies are understood on both sides;
- how incidents involving misuse are escalated.

The objective is controlled interoperability, not maximum replication.

This example shows one selected exchange between two autonomous communities. Each retains its own governance, membership, and private case data. Only approved findings cross the boundary, and feedback returns when permitted by policy.

[![Two locally governed communities exchange selected information through agreed policy and synchronization filters; private case data stays local and permitted feedback can return.](/img/community-guidelines/federation.svg "{.img-responsive}")](/img/community-guidelines/federation.svg)

The same checks apply in either direction and at every onward sharing boundary. A connection to a third community grants no automatic right to forward information received from the first.

[Mermaid source](/img/community-guidelines/federation.mmd)


## Shared data sources

Information-sharing communities often become more useful when they can provide controlled access to evidence and enrichment sources in addition to finished intelligence.

Possible shared sources include:

- passive DNS;
- malware repositories;
- sandbox results;
- passive TLS/certificate datasets;
- network telemetry;
- sinkhole or honeypot data;
- vulnerability datasets;
- scanning results;
- abuse information;
- reputation datasets;
- historical threat-intelligence collections.

Shared datasets can reduce duplicated work and allow members to validate findings independently.

### Access models

Not every dataset should be copied to every member. Possible models include:

- query-only access;
- API access;
- limited export of derived indicators;
- full synchronization;
- case-specific access;
- access restricted to a working group;
- local analysis with only derived results shared.

### Provenance and reproducibility

Where possible, analytical results should record which datasets or enrichment services were used. This improves reproducibility, helps other analysts validate conclusions, and strengthens operational trust without necessarily exposing the underlying sensitive data.

# Part V - Security, Privacy, and Compliance

## Security requirements

Communities routinely handle sensitive information. Security requirements should cover both the central services and member responsibilities.

### Data in transit and at rest

Consider requirements for:

- transport encryption;
- encryption at rest where appropriate;
- secure authentication;
- multi-factor authentication;
- account lifecycle management;
- privileged access;
- backups;
- logging and monitoring;
- secure administrative access;
- patch and vulnerability management;
- incident response for the community infrastructure.

### Least privilege and compartmentalisation

Access should match need. Sub-communities, sharing groups, roles, and dedicated instances can be used to reduce unnecessary exposure.

Compartmentalisation should be deliberate. Excessive fragmentation can make the community harder to operate and can prevent useful correlation.

### Auditability

Members should have confidence that important actions can be reviewed. Depending on the system, relevant audit events may include:

- access changes;
- membership changes;
- publication and modification;
- synchronization activity;
- administrative actions;
- changes to sharing groups or distribution policies.

Auditability reinforces accountability but should itself respect privacy and proportionality.

### Security responsibilities of members

The community should define whether members need to satisfy baseline controls before receiving sensitive information. Requirements can be proportional to the sensitivity of the shared data rather than identical for every membership level.

## Privacy, data protection, and legal constraints

Legal and regulatory requirements differ between jurisdictions and sectors. Communities should obtain appropriate advice and avoid treating this document as a substitute for legal analysis.

### Data minimisation and proportionality

The community should determine what personal or regulated data is actually necessary for its purpose and avoid collecting information without an operational reason.

### Pseudonymisation and anonymisation

Pseudonymisation may reduce privacy risk but can also reduce analytical value. If information is transformed, recipients should understand enough about the transformation to interpret its limitations.

Where possible, represent the transformation or anonymisation technique as metadata so that analysts can understand how the data differs from the original observation.

### Data-protection clauses and transparency

Membership agreements, terms of use, or information-sharing policies can define responsibilities for processing personal data. Public-facing services should provide appropriate privacy information and a contact point for data-protection requests.

### Mandatory disclosure and legal requests

The community should define how members and the operator handle legal or regulatory obligations that may require disclosure outside the normal sharing policy. The process should be clear before a crisis occurs.

### Cross-border federation

When information crosses jurisdictions, the federation should understand whether differences in law, contractual obligations, or organisational mandate affect onward sharing or processing.

# Part VI - Maturity and Federation

## Maturity model for information-sharing communities

Community maturity is not simply a measure of technical automation. It reflects trust, governance, participation, data quality, integration into operational processes, and the ability to cooperate with other communities.

A useful maturity progression is:

### Stage 1 - Ad-hoc sharing

- bilateral email, chat, or meetings;
- personal trust;
- limited documentation;
- case-by-case sharing decisions.

**Goal:** establish value and trusted relationships.

### Stage 2 - Structured community

- defined membership;
- common rules and basic governance;
- shared vocabulary;
- common platform or structured exchange format;
- recurring meetings and activities.

**Goal:** make collaboration repeatable.

### Stage 3 - Automated and federated exchange

- synchronization or APIs;
- explicit distribution policies;
- institutional rather than purely personal trust;
- sub-communities and controlled interconnection;
- documented security and compliance practices.

**Goal:** scale without losing control.

### Stage 4 - Collaborative analysis and co-production

- joint enrichment and correlation;
- shared analytical workflows;
- working groups;
- shared datasets;
- feedback loops and sightings;
- coordinated incident or vulnerability work.

**Goal:** move from exchange to joint knowledge production.

### Stage 5 - Integrated intelligence lifecycle

- sharing is embedded in detection, response, vulnerability management, and decision-making;
- information flows back from operational systems to the community;
- communities federate with other communities through defined policies;
- automation supports analysts without hiding provenance or policy decisions;
- governance, tooling, and membership evolve continuously.

**Goal:** create a sustainable distributed intelligence ecosystem.

### Maturity is not uniform

Members will have different capabilities. A federation does not need every organisation to reach the same stage. Mature members can provide infrastructure, examples, training, and services that help less mature members participate without forcing them into an unrealistic operating model.

### Maturity does not mean centralisation

A mature community can be highly decentralised. The relevant question is whether information can move reliably and safely according to agreed rules, not whether all data is stored in one place.

## When and how to federate with other communities

A community is ready to federate when it can explain its own rules well enough for another community to rely on them.

### Federation readiness questions

Before establishing synchronization or recurring exchange, ask:

- Do both communities understand each other's membership model?
- Are information-handling and redistribution rules compatible?
- Can both sides preserve provenance and distribution markings?
- Are common vocabularies available?
- Is there an escalation path if information is mishandled?
- Are technical contacts identified?
- Can data be filtered according to topic, sensitivity, or origin?
- Can members opt out of wider dissemination when required?
- Is there a process for corrections, updates, or revocation?
- Are cross-border or sector-specific legal constraints understood?

### Start with a narrow federation

A practical approach is to begin with:

- one well-defined topic;
- a small sharing group;
- a limited set of taxonomies;
- a manually reviewed synchronization policy;
- named operational contacts;
- a review after a defined trial period.

Broader automation can follow after both sides understand the information flow.

### Community bridges

An organisation can belong to multiple communities and act as a bridge, but this does not mean it may automatically forward information between them. Bridge organisations must respect the distribution policy of each source community.

Technical connectivity never implies redistribution authority.


# Part VII - Operations and Sustainability

## Running the community

### Regular activities

A sustainable operating rhythm can include:

- periodic member meetings;
- threat or incident briefings;
- working-group sessions;
- technical sharing exercises;
- tabletop exercises;
- training;
- platform maintenance reviews;
- governance reviews;
- onboarding sessions;
- cross-community exchanges.

Regular interaction matters even when there is no major incident.

### Community management

Active participation must be nurtured. Useful practices include:

- welcoming new members visibly;
- connecting members with common interests;
- asking for feedback on community services;
- helping members make their first contribution;
- reducing unnecessary noise;
- recognising useful analysis;
- creating opportunities for members to present their work;
- following up when a member becomes inactive.

### Incident-specific collaboration

Existing trust and common tooling allow temporary working groups to form quickly during major incidents, vulnerabilities, or campaigns. The community should define how such groups are created, who can join, what information remains after the group closes, and how findings are fed back into the broader community.


## Measure community health

Metrics are useful only when they support the community's purpose. Pure volume can be misleading.

### Quantitative indicators

Possible metrics include:

- number of active organisations;
- number of active individual participants;
- frequency of contributions;
- number of members contributing, not only consuming;
- sightings and feedback;
- response time to requests;
- number of joint activities;
- number of collaborative investigations;
- amount of information enriched by members;
- use of community information in detection or response;
- participation in training and workshops;
- cross-community exchanges.

### Qualitative indicators

Useful qualitative questions include:

- Do members trust the handling of sensitive information?
- Does the shared information solve real problems?
- Are members able to explain the sharing rules?
- Are less mature members improving?
- Is there useful feedback after contributions?
- Are members willing to ask each other for help?
- Does federation create additional value rather than extra noise?

### Avoid vanity metrics

A high number of events, indicators, users, or connected servers does not automatically imply a healthy community. Quality, relevance, trust, and operational use are more important than raw quantity.

## Continuous improvement

The community should periodically review changes in:

- adversary techniques;
- member needs;
- regulation and legal context;
- membership structure;
- technology;
- data sources;
- interoperability requirements;
- external communities and partnerships.

Changes should be reflected in services, vocabularies, procedures, access rules, and architecture.

Flexible data models and modular tooling are useful because new forms of information can be represented without redesigning the entire community.

## Long-term sustainability

Sustainability has technical, organisational, financial, and human dimensions.

### Technical sustainability

- use maintainable technologies;
- document configuration and architecture;
- automate routine maintenance where appropriate;
- avoid unnecessary vendor or platform lock-in;
- maintain backups and recovery plans;
- plan upgrades and security maintenance;
- ensure more than one person understands critical services.

### Organisational sustainability

- maintain explicit ownership of community functions;
- secure recurring resources;
- integrate activities into participating organisations' normal operations;
- maintain governance documents;
- review membership and points of contact;
- avoid dependency on one highly motivated individual.

### Knowledge transfer and succession

Document:

- operational procedures;
- technical architecture;
- community history and decisions;
- onboarding material;
- policy interpretations;
- recurring workflows.

Mentorship, training, and staff exchanges can reduce the loss of trust and knowledge when people change roles.

### 23.4 Motivational sustainability

Members remain active when they perceive real value. Continue demonstrating outcomes such as faster detection, better context, reduced duplication, successful joint investigations, improved defensive actions, or access to expertise that would otherwise be unavailable.

# Part VIII - Practical Templates and Checklists

## Minimum viable community

A new community does not need every mechanism described in this document on day one. A minimum viable community can begin with the following:

- [ ] A short mission and scope statement.
- [ ] A coordinating person or organisation.
- [ ] A defined initial member list.
- [ ] Basic membership criteria.
- [ ] A simple code of conduct or participation agreement.
- [ ] A clear information-handling and redistribution policy.
- [ ] A common sensitivity/dissemination marking scheme.
- [ ] One secure human communication channel.
- [ ] One structured information-sharing mechanism.
- [ ] Named operational and technical contacts.
- [ ] A recurring meeting or working session.
- [ ] An onboarding process.
- [ ] A first sharing exercise or concrete operational use case.

Everything else can evolve from this foundation.

## Recommended document set

A mature community will usually benefit from maintaining the following documents.

### Foundation

1. **Mission, scope, and value proposition**
2. **Governance charter**
3. **Membership and onboarding policy**
4. **Code of conduct / terms of participation**

### Information sharing

5. **Information-exchange policy**
6. **Classification, vocabulary, and taxonomy guidelines**
7. **Data-retention and handling policy**
8. **Federation / inter-community sharing policy**

### Operations

9. **Technical architecture and security baseline**
10. **Incident and misuse escalation procedure**
11. **Account lifecycle procedure**
12. **Community operations handbook**
13. **Business continuity and service recovery procedure**

### Compliance and transparency

14. **Privacy notice and data-protection documentation**
15. **Applicable legal and regulatory requirements register**
16. **Third-party and data-source terms register**

### Improvement

17. **Metrics and community-health review**
18. **Training and exercise plan**
19. **Succession and knowledge-transfer plan**

The list is deliberately modular. Small communities can combine several items into a single concise document.

## Community launch checklist

### Purpose and scope

- [ ] The mission can be explained in one paragraph.
- [ ] The initial use cases are concrete.
- [ ] The intended member population is understood.
- [ ] Members can explain what value they expect.

### Governance

- [ ] Decision-making responsibilities are defined.
- [ ] Membership approval is defined.
- [ ] Non-compliance and exit are addressed.
- [ ] Points of contact are maintained.

### Sharing policy

- [ ] Handling rules are defined.
- [ ] Permitted actions are defined.
- [ ] Redistribution rules are defined.
- [ ] Licensing or reuse terms are understood.
- [ ] Attribution and anonymity rules are defined.

### Tooling

- [ ] Human communication channels are selected.
- [ ] Structured information exchange is available.
- [ ] Access controls match the policy.
- [ ] Logging and account lifecycle are operational.
- [ ] Backups and maintenance responsibilities are assigned.

### Community building

- [ ] An onboarding session exists.
- [ ] A recurring meeting is scheduled.
- [ ] Operators or mature members have prepared example contributions.
- [ ] Feedback mechanisms are available.

### Security and compliance

- [ ] Security requirements are documented.
- [ ] Sensitive information can be compartmentalised.
- [ ] Privacy and data-protection responsibilities are understood.
- [ ] Misuse or accidental disclosure has an escalation path.

## Federation readiness checklist

Before connecting two existing communities, confirm:

- [ ] Both communities have identified operational and technical contacts.
- [ ] Both sides understand the other's membership model.
- [ ] Sharing and redistribution rules are compatible.
- [ ] Provenance can be preserved.
- [ ] Distribution markings can be mapped without weakening them.
- [ ] Common taxonomies or translation rules are available.
- [ ] Synchronization filters are documented.
- [ ] Corrections, sightings, and updates can flow back where appropriate.
- [ ] Revocation or restriction changes can be handled.
- [ ] Cross-border and legal constraints have been reviewed.
- [ ] Incident and misuse escalation paths exist.
- [ ] The federation can start with a limited pilot before broader automation.

## Questions for periodic governance review

At least periodically, the community should ask:

1. Does our original purpose still match member needs?
2. Which services are actually used?
3. Are members contributing as well as consuming?
4. Are the sharing rules understood in practice?
5. Are sub-communities still necessary and correctly governed?
6. Are our taxonomies and vocabularies still appropriate?
7. Are our technical controls enforcing current policy?
8. Have legal or regulatory constraints changed?
9. Are there communities we should federate with, or federation links we should reconsider?
10. Are members receiving useful feedback?
11. Can the community continue operating if key individuals leave?
12. What should we stop doing?

# Part IX - Example Target Operating Model

## Example progression for a new community

A realistic implementation path can look like this.

### Phase A - Trusted nucleus

Start with a small number of organisations that already have a shared operational problem. Establish a secure chat channel, regular meetings, basic handling rules, and a shared MISP environment or sharing group.

Focus on producing a few useful contributions and learning what information members actually need.

### Phase B - Structured community

Document membership, onboarding, a code of conduct, information-exchange policy, vocabularies, and recurring activities. Introduce feedback through sightings, comments, corrections, or joint analysis.

### Phase C - Operational integration

Help members connect community information to their internal processes: SIEM, SOC, detection engineering, vulnerability management, incident response, case management, or threat hunting.

Do not automate blocking or remediation merely because data is structured. Define operational quality thresholds.

### Phase D - Distributed participation

Allow technically mature members to operate their own MISP instances or other interoperable systems. Introduce controlled synchronization and more granular sharing groups.

### Phase E - Federation

Connect to selected external communities using explicit filters, mapped vocabularies, preserved provenance, and compatible redistribution rules. Start narrowly and expand based on experience. This phase can start early in the process.

### Phase F - Collaborative ecosystem

Develop joint analytical workflows, shared datasets, community-developed tooling, cross-community working groups, and continuous feedback between intelligence and operational response.

The progression should remain reversible. A community may simplify an architecture or reduce federation when complexity no longer produces value.

## Common failure modes

### Starting with technology instead of a use case

A technically successful platform can still become an empty community. Begin with problems members already need to solve together.

### Over-formalising too early

Extensive governance before members have demonstrated value can prevent the community from forming. Start with the minimum rules needed for trust and safety, then formalise based on real operational needs.

### Treating members as feed consumers

One-directional distribution does not create a collaborative community. Provide ways for members to contribute observations, questions, corrections, and context.

### Enforcing contribution quotas

Rigid quotas can create junk contributions and exclude organisations that need time to mature. Measure engagement more broadly and invest in capacity building.

### Confusing visibility with permission

The fact that an organisation can technically access information does not imply permission to redistribute it to another community.

### Automating before agreeing on semantics

Synchronization without common understanding of distribution, confidence, taxonomy, and intended use increases risk. Agree on semantics first.

### Excessive compartmentalisation

Sub-groups are useful when they represent real trust boundaries. Too many groups create silos, policy complexity, and lost correlation opportunities.

### Measuring volume instead of value

More indicators, events, users, or synchronization links do not necessarily mean better security. Measure useful outcomes and member confidence.

### Neglecting succession

Communities often depend on a few personal relationships. Document processes and create multiple trusted contacts so that organisational changes do not destroy the community.

# Conclusion

Information-sharing communities succeed when they create **shared value under conditions of trust**. The strongest communities combine clear purpose, pragmatic governance, understandable handling rules, useful technical mechanisms, continuous human interaction, and the ability to evolve.

Federation extends these principles beyond the boundaries of a single community. It allows autonomous organisations and communities to cooperate without requiring a common central authority or a single repository. Each participant can retain control over its own operations and data while contributing to a wider situational picture.

The most sustainable path is incremental:

- establish trust before demanding automation;
- demonstrate useful sharing before imposing contribution requirements;
- establish common vocabularies before scaling synchronization;
- preserve provenance and distribution decisions when federating;
- support both human-to-human and machine-to-machine collaboration;
- measure value rather than volume;
- keep governance and technology adaptable.

MISP provides a practical technical foundation for many of these patterns, but the decisive elements remain social and organisational. Technology can enforce agreed decisions; it cannot replace the trust, reciprocity, and shared purpose from which those decisions originate.

A successful information-sharing community is therefore best understood not as a platform or a database, but as a **living network of trusted organisations that can progressively move from ad-hoc exchange to structured collaboration, joint analysis, operational integration, and federation while preserving autonomy**.

# References and source material

This consolidated guideline was prepared by **CIRCL - Computer Incident Response Center Luxembourg and the MISP Project** and builds primarily on the following source material:

1. **CIRCL / MISP Project**, *Guidelines to setting up an information sharing community such as an ISAC or ISAO*, MISP Compliance repository: <https://github.com/MISP/misp-compliance/blob/master/setting-up-ISACs/guidelines_to_set-up_an_ISAC.md>
2. **CIRCL / MISP Project**, *Model of the Federated Team*, source document used for this consolidation.
3. **MISP Project**, *Introduction into Information Sharing using MISP for CSIRTs / MISP Best Practices*: <https://www.misp-project.org/misp-training/a.4-best-practices.pdf>
4. **MISP Project**, Compliance documentation: <https://github.com/MISP/misp-compliance/>
5. **FIRST**, Information Exchange Policy framework: <https://www.first.org/iep/>
6. **FIRST**, CSIRT Services Framework: <https://www.first.org/standards/frameworks/csirts/>
7. **CTI Capability Maturity Model**: <https://cti-cmm.org/>
8. **MISP Project**, Taxonomies: <https://github.com/MISP/misp-taxonomies>
9. **MISP Project**, Galaxies: <https://github.com/MISP/misp-galaxy>

## Funding

[![Co-funded by the European Union](/img/eu-co-funded-en.jpg "{.img-responsive width='440'}")](https://european-union.europa.eu/)

This document was developed as part of the [FETTA (Federated European Team for Threat Analysis) project](https://www.circl.lu/pub/press/20240131/), co-funded by the European Union through the European Cybersecurity Competence Centre (ECCC) under the Digital Europe Programme (DEP).

### Disclaimer

Co-funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Cybersecurity Competence Centre. Neither the European Union nor the granting authority can be held responsible for them.

## Contact and contributions

This document is intended to be reusable and improved through operational experience. Suggestions, corrections, and contributions can be proposed through the MISP Project and CIRCL community channels.
