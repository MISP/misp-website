---
title: Information Sharing Maturity Model
layout: post
featured: /assets/images/misp-small.png
---

At MISP project, we are practical. We do software (from MISP core to MISP workbench, data models (from taxonomy, warning-lists, galaxies and practical standards) to solve our problems with information sharing and improve the state of the information shared. If we lack something, we build it.

Various information sharing communities are relying on MISP core to support the sharing of cybersecurity indicators, fraud information, incidents or even threat-actor details. We received interesting feedback of organisations wanting to know the maturity of a specific sharing partner while they are on their sharing community.

So we were wondering whether we could build something that solves the above issue using the information shared within a sharing community relying on MISP. We therefore took our favourite tools and designed a simple maturity model based on real information available in a sharing community.

The sharing model is based on 3 different scoring types, L which stands for minimal access requirement to have an operative access to your MISP sharing community, C which are the different contributions that an organisation can do in the community and EC which are external contributors to the MISP project community providing an independent score.

Community maturity level (if(L)(SUM(C))) which is the score of an organisation based on the contribution within a specific community. This score can be calculated on a each instance/community.

The community maturity level of an organisation can remain private to a community or shared with the community at large depending of the instance configuration.

Global MISP project contribution score (SUM(EC)) which is the score calculated from the MISP project contributions of an organisation. This score is calculated globally by the MISP project.

# Information sharing maturity level (ISML)

The Information Sharing Maturity Level (ISML) is calculated from the sum of values which can be extracted automatically from the MISP instance holding the access to a sharing community. Each value is independent from each others meaning that depending of the information sharing practices of an organisation, a maturity level can be calculated. The maturity level can be represented by a simple vector to show the gap or the current practices and capabilities of an organisation (e.g. an organisation only consuming information via the API has a specific capability which can be rated). As previously stated, this information can be kept privately in a specific sharing community or shared globaly.

- L1 Have access to a MISP instance accessing a community, have at least one user with an encryption key and receive encrypted notification. (M)
- C1 (L1) Contributing via proposals or discussions at least once a year. (M)
- C2 (L1) Actively contributing proposals to recent events. (M)
- C3 (L1) Adding events at least once a year. (M)
- C4 (L1) Adding events at least once a month. (M)
- C5 (L1) Regularly (at least one per week) posting events with adequate classification. (M)
- C6 (L1) Using the API. (M)
- C7 (L1) Complex API usage. (M)
- C8 (L1) Having their own MISP instance. (M)
- C9 (L1) Having own and connected MISP instance. (M)
- C10 (L1) Running their own connected sharing communities.
- C11 (L1) Ensuring best security practices when sharing information.

The aim behind this scores is to help organisations contributing **to know where they are, what they can still do to improve their practices and to fully benefit from information sharing**.

## Global MISP project contribution score


- EC1 Contributing to taxonomies. (M)
- EC2 Contributing to warning-lists. (M)
- EC3 Contributing to galaxy. (M)
- EC4 Contributing to modules. (M)
- EC5 Contributing to MISP core. (M)
