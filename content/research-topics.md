---
layout: page
title: MISP, research topics 
permalink: /research-topics/
toc: true
---

# MISP Research topics

Exploring New Horizons in Cyber security and threat intelligence with MISP: Research Opportunities

Welcome to the MISP Research Initiative! [MISP](https://www.misp-project.org/) is an essential open-source project at the forefront of the global cybersecurity landscape. Developed to empower organizations and security professionals in the battle against cyber threats, MISP serves as a distributed platform for sharing, storing, and analyzing threat intelligence data.

We are excited to extend an invitation to researchers, academics, and cybersecurity enthusiasts to embark on a journey of discovery within the realm of MISP. In collaboration with the MISP community, your expertise and innovative thinking can help drive advancements in threat intelligence sharing and enhance the state-of-the art in threat intelligence.

Listed below are a set of potential research topics that touch upon various aspects of MISP, offering a diverse range of opportunities to explore, research, experiment, and contribute to this dynamic field. Whether you are interested in technical challenges, user experience improvements, policy and governance issues, or integration with other cybersecurity tools, there's a topic that aligns with your interests and expertise.

By participating in MISP research, you can:

- Contribute to the development and improvement of MISP features.
- Enhance the effectiveness of threat intelligence sharing.
- Investigate emerging threats and vulnerabilities.
- Shape the future of cybersecurity collaboration and information sharing.

We encourage you to delve into these research topics, collaborate with the MISP community, and make a significant impact on the cybersecurity landscape. Your work has the potential to strengthen the collective defense against cyber threats, safeguard critical infrastructures, and protect the digital world we rely on.

Explore the potential topics below, and let your research journey with MISP begin! We are open to other research topics and the list below is just a way to trigger research ideas.

## MISP correlation analysis and improving algorithm complexity modeling

MISP users frequently experience performance issues when utilizing the correlation feature. This often leads to time-consuming manual debugging of queries, accompanied by adjustments to the existing correlation algorithms. In this research, researcher could aim to conduct an in-depth complexity analysis of the current correlation engines. This analysis will help optimize hardware utilization for more effective correlation. Using this model, system engineers can obtain precise specifications for hardware components like disks, RAM, and CPUs to dimension their hardware accurately.  Additionally, researcher could plan to follow up with enhancements to the existing correlation algorithms. 

## Cryptographic data integrity analysis and improvements

In March 2022, the concept of protected events was introduced to cryptographically sign events, preventing data tampering [^1]. The distribution of cryptographic materials is carried out using Cerberate [^2]. In this research, these mechanisms will be analyzed in-depth, followed by an examination of cryptographic attacks and the proposal of potential solutions or improvements.


# Mis- and dis-information detection and mitigation

The companion tool, Cerebrate [^2], provides an overview of contributors to MISP through cryptographic verification. Nevertheless, the risk of misinformation and disinformation within MISP communities remains ever-present, with malicious users disseminating false information. The objective of this research is to assess the current mechanisms, such as warning lists[^3] and blacklisting [^4] in MISP. Subsequently, researcher could conduct a survey of detailed misinformation and disinformation techniques that could potentially impact MISP communities, followed by the development of appropriate countermeasures.

# Community analysis tools

MISP facilitates the sharing of numerous types of objects [^5] within a sharing community. While some features provide basic statistics on the usage of these objects within a given community, the aim of this research is to comprehensively analyze these statistics, assess their advantages and limitations, and introduce novel automated methods to gain deeper insights into MISP communities, with a particular emphasis on information sharing aspects.

# MISP community rating 

In the rich tapestry of MISP information sharing communities, a wealth of insights and analytical data resides, offering valuable glimpses into the diverse capabilities of organizations engaged in sharing threat intelligence. Our research endeavor seeks to assess algorithms and methodologies that can autonomously evaluate and rate organizations within a MISP community. The outcomes of this research hold the potential for seamless integration into MISP or Cerebrate, enabling the sharing of calculated organizational capabilities and ratings across the community. Such ratings can, in turn, play a pivotal role in the qualification and validation of information generated by these participating organizations. The research results can be then integrated into MISP to qualify the intelligence produced by the rated organisations.

# References
[^1]: https://www.misp-project.org/2022/03/18/MISP.2.4.156.released.html/
[^2]: https://cerebrate-project.org/
[^3]: https://github.com/MISP/misp-warninglists
[^4]: https://www.circl.lu/doc/misp/administration/#blocklists-and-block-rules
[^5]: https://www.misp-project.org/objects.html
