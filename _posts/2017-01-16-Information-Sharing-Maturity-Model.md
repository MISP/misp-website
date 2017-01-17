---
title: Information Sharing Maturity Model
layout: post
featured: /assets/images/misp-small.png
---

At MISP project, we are practical. We do software (from MISP core to MISP workbench, data models (from taxonomy, warning-lists, galaxies and practical standards) to solve our problems with information sharing and improve the state of the information shared. If we lack something, we build it.

Various information sharing communities are relying on MISP core to support the sharing of cybersecurity indicators, fraud information, incidents or even threat-actor details. We received interesting feedback of organisations wanting to know the maturity of a specific sharing partner while they are on their sharing community. Understanding the maturity and information sharing capabilities of an organisation can help to better serve them by knowing which scheme of contribution they usually use. From an open source software perspective, this model supports us to discover where functionallities are lacking or under used.

So we were wondering whether we could build an automatic calculation of a maturity model that solves the above issue using the information shared within a sharing community relying on MISP. We therefore took our favourite tools and designed a simple maturity model based on real information available in a sharing community.

The sharing model is based on 2 different scoring types, C which are the different contributions that an organisation can do in the community and EC which are external contributors to the MISP project community providing an independent score.

Community maturity level (SUM(C)) which is the score of an organisation based on the contribution within a specific community. This score can be calculated on a each instance/community.

The community maturity level of an organisation can remain private to a community or shared with the community at large depending of the instance configuration.

Global MISP project contribution score (SUM(EC)) which is the score calculated from the MISP project contributions of an organisation. This score is calculated globally by the MISP project.

# Information Sharing Maturity Level (ISML)

The Information Sharing Maturity Level (ISML) is calculated from the sum of values which can be extracted automatically from the MISP instance holding the access to a sharing community. Each value is independent from each others meaning that depending of the information sharing practices of an organisation, a maturity level can be calculated. The maturity level can be represented by a simple vector to show the gap or the current practices and capabilities of an organisation (e.g. an organisation only consuming information via the API has a specific capability which can be rated). As previously stated, this information can be kept privately in a specific sharing community or shared globally.

- L1 Have access to a MISP instance accessing a community, have at least one user with an encryption key and receive encrypted notification. This is the minimal requirement to start calculating the ISML. (M)
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
- C11 Ensuring best security practices when sharing information. (e.g. when TLP:AMBER information is shared, encryption of the notification is enabled.)

The aim behind this score is to help organisations contributing **to know where they are, what they can still do to improve their practices and to fully benefit from information sharing**.

MISP events are composed of one or more attributes which describe the intent of the event package from indicators, vulnerabilities or any relevant information. The scoring is based on the events contributed or the proposal made as described at each level. A value is usually derived from an automatic analysis within the MISP instance (where M is mentioned). Some values parameter are still under investigation on how the value is properly derived from an instance (where M is lacking).

## Global MISP Project Contribution Score

Global MISP project contribution score is independent of the Information Sharing Maturity Level. This score is for scoring the level of contribution within the open source project MISP. it's an additional score to see how far an organisation is contributing to the MISP project.

- EC1 Contributing to taxonomies. (M)
- EC2 Contributing to warning-lists. (M)
- EC3 Contributing to galaxy. (M)
- EC4 Contributing to modules. (M)
- EC5 Contributing to MISP core. (M)
- EC6 Reporting bugs or issues or ideas. (M)

Contributing stands for at least one pull-request at least every year on the corresponding public git repository. Reporting means to open at least one issue per year.

# Next Steps

The current maturity model is a first proposal based on the current practices within information sharing communities relying on MISP. **We seek additional feedback to expand the maturity level or make it more accurate**. An issue on GitHub is available where you can provide feedback or updates. Then, in the next few weeks, a first version of the Information Sharing Maturity Level will be implemented in MISP core. This project is to fit within the overall goal to provide a sharing platform where contributors have incentive to contribute more (aka ***the gamification project***).
