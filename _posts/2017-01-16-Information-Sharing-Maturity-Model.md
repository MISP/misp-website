---
title: Information Sharing Maturity Model
layout: post
featured: /assets/images/misp-small.png
---

Here at the *MISP project*, we are practical oriented people. We create software (from *MISP core* to *MISP workbench*), develop data models (such as taxonomies, warning-lists and galaxies) and build practical standards to solve information sharing challenges and improve the general state of information sharing. That's what we strive for. If we lack something, we build it. If we see a requirement, we fullfil it. Unbureaucratically, result-orientedly and professionally.

These days, various information sharing communities build their Information Sharing infrastructure on *MISP core* to support the sharing of cybersecurity indicators, fraud information, incidents or even threat-actor details. We received interesting feedback from organisations wanting to know the maturity of other sharing partners [TODO: not clear enough] residing within their sharing community. Understanding the maturity and information sharing capabilities of an organisation can help in order to be able to better serve them by knowing which schemes of contribution they usually use. From an open source software perspective, this model supports us in our pursuit to discover where functionallities are lacking or are under used.

One day we asked ourselves the question whether we could build an automated calculation of maturity using a model that solves the above issue, namely the use of information shared within a sharing community in MISP. We therefore took our favourite tools and designed a simple maturity model based on real information available in a sharing community.

The maturity model is based on 2 different scoring types: *C* which describes the different types of contributions that an organisation can partake in within the community and *EC* describing the organisations' maturity within the scope of external contributions [TODO: should it not be 'contributions'?] to the MISP project community itself, facilitating an independent score. The different types of contributions are defined further down.

Community maturity level *(SUM(C))*, which is the score of an organisation based on the contribution within a specific community. This score can be calculated on each instance/community. 

The community maturity level of an organisation can remain private to a community or be shared with the community at large, depending on the configuration of the instance.

The global MISP project contribution score *(SUM(EC))* is the score derived from the MISP project contributions by an organisation. This score is calculated globally by the MISP project.

# Information Sharing Maturity Level (ISML)

The Information Sharing Maturity Level (ISML) is calculated from the sum of values which can be extracted automatically from the MISP instance provisioning access to a sharing community. Each value is independent from one another, meaning that depending on the information sharing practices of an organisation, a maturity level can be calculated [TODO: not clear for me]. The maturity level can be represented by a simple vector to show the gap of the current practices and capabilities of an organisation (e.g. an organisation only consuming information via the API has a specific capability which can be rated). As previously stated, this information can be kept privately in a specific sharing community or shared globally.

- L1 Have access to a MISP instance accessing a community, have at least one user with an encryption key and receive encrypted notifications. This is the minimal requirement to start calculating the ISML. (M)
- C1 Contributing via proposals or discussions at least once a year. (M)
- C2 Actively contributing proposals to recent events. (M)
- C3 Adding events at least once a year. (M)
- C4 Adding events at least once a month. (M)
- C5 Regularly (at least one per week) posting events with adequate classification. (M)
- C6 Using the API. (M)
- C7 Complex API usage. (M)
- C8 Having their own MISP instance. (M)
- C9 Having own and connected MISP instance. (M)
- C10 Running their own connected sharing communities.
- C11 Ensuring best security practices when sharing information (e.g. when TLP:AMBER information is shared, encryption of the notification is enabled).

The aim behind this score is to help organisations contributing **to know where they stand, what they can still do to improve their practices and to fully benefit from information sharing**.

MISP events are composed of one or more attributes which describe the intent of the event package from indicators, vulnerabilities or any other relevant information. The scoring is based on contributed events or the proposals made as described at each level. A value is usually derived from an automatic analysis within the MISP instance (where M is mentioned). Some parameter are still under investigation on how the value is properly derived from an instance (where M is lacking).
[TODO: Previous paragraph is about automatically fetching data. Suggestion to replace M with A. (M) naturally feels like 'manual' and (A) like automatic, so the (M) is confusing]

## Global MISP Project Contribution Score

Global MISP project contribution score is independent from the Information Sharing Maturity Level. This score is for calculating the level of contribution to the open source project MISP. It is an additional score to see to which extent an organisation is contributing to the MISP project.

- EC1 Contributing to taxonomies. (M)
- EC2 Contributing to warning-lists. (M)
- EC3 Contributing to galaxy. (M)
- EC4 Contributing to modules. (M)
- EC5 Contributing to MISP core. (M)
- EC6 Reporting bugs or issues or ideas. (M)

Contributing stands for at least one pull-request, at least once a year on the corresponding public git repository. Reporting means to open at least one issue per year. [TODO: more points for more?]

# Next Steps

The current maturity model is a first proposal based on the current practices within information sharing communities relying on MISP. **We seek additional feedback to expand the maturity level or make it more accurate**. An issue on GitHub is available where you can provide feedback or updates. In the next few weeks, a first version of the Information Sharing Maturity Level will be implemented in the MISP core. This project is to fit within the overall goal to provide a sharing platform where contributors have incentives to contribute more (aka ***the gamification project***).
