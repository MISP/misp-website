---
title: SACTI - Secure aggregation of cyber threat intelligence 
date: 2022-10-27
layout: post
banner: /img/blog/sacti/SACTI_logo_small.jpg
---

# **SACTI: Secure aggregation of cyber threat intelligence**

# Overview

Communities can share cyber threat intelligence on platforms, such as MISP. In the H2020 project Prometheus TNO has developed a way to securely aggregate cyber threat intelligence and publish the result on MISP.

# Problem

Cyber Threat Intelligence (CTI) consists of structured information on malware, actors, campaigns et cetera. It uses the following two core types of information. Indicators of Compromise (IoC) provide information on the threat itself. And sightings give information on the detection of threats in the IT system. Communities are formed to share this type of information, typically with a source for IoCs.

Sharing information on cyber threats has many benefits to all organization. Jointly, it is easier to recognize the current threats and develop adequate responses. And this requires information from the participating organizations. They have to report how often they have sighted a certain Indicator of Compromise (IoC). However, organizations are often hesitant to share this. Additionally, also the financial damage incurred by the IoC may be aggregated and reported with the same techniques. However, here we will concentrate on the number of sightings.

# Our solution

There are a couple of reasons why organizations may choose not to publish information about the observed cyber threats. Information about the observed cyber threats may provide hackers with suggestions about attacks that an organization does not detect or is particularly susceptible to. For this reason we should focus on the aggregated observations over all participating organizations. If the response group is sufficiently large, the aggregated number of sightings will provide attackers with little information about the vulnerability of any single organization. Yet, the aggregate number of sightings of an IoC provides very useful group information to decide which cyber threats to focus on.

Nonetheless, it may still happen that only a single member of the response group has observed a certain attack. If everyone is aware of this, as regularly happens with prominent ransomware cases, then the aggregate may still reveal this sensitive information. To prevent this from happening, the aggregate should only be published, if sufficiently many non-zero sightings have been submitted.

This is implemented using a multi-party computation protocol, based on Shamir secret sharing. This prevents that a small group of colluding parties is able to extract any information from a protocol run. In this way the security demands can be met in a scalable way, so that this approach is also viable for large groups with long lists of IoCs. If the protocol has run successfully, the aggregated result is uploaded automatically to MISP.

![Picture4](/img/blog/sacti/Picture4.png)

![Picture5](/img/blog/sacti/Picture5.png)

# In more detail

To limit the amount of communication, all communication runs via a central party, called the aggregator. In this way, it is possible to group messages, so that as few message as possible are sent. The role of the aggregator could be performed by an information sharing and analysis center (ISAC). The aggregator may be considered a trusted party, which could simplify the solution. However, to provide as much certainty as possible to the participants, this is not done. 

Each participant uses the binary encoding of the (integer) number of sightings. For performance reasons integer consisting of 7 bits are used. Each bit in this encoding is secret shared with one share for each party. Afterwards, it must be check that all bits are indeed bits. This means that the numbers $`b`$ the shares reconstruct to must satisfy $`b(1-b)=0`$.

The next check counts the number of zero-sightings. Only if all 7 bits of a number are equal to zero, we have a zero-sighting. This means that we would like to compute $`\prod_{i=1}^{7}(1-b_{i})`$, which is equal to 1 if and only if the submitted integer is equal to zero. Summing this over all participants yields the number of submitted zeros. Comparing this with the pre-set threshold of the maximum number of tolerable zero-sightings is the second check. If both check yield positive results, it is time to perform the final aggregation and reveal the result.

Secure multiplication of secret shares must be designed carefully to provide both security and correctness. For that reason, some extra information on the submitted bits is provided and used. This also means that additional consistency check must be performed. The above sketch of the protocol does not yet contain all details.

# Security model

A lattice-based PKI is in place to ensure confidentiality and integrity of the sent messages. Signatures are necessary to prevent the injection of messages by outsiders.  

The aim of this software is to aggregate the reported sightings in a way that prevents a colluding minority of participants to learn the number of sightings of any single party. It is not possible to defend against participants that submit a false number of sightings as input.

The solution is secure in the semi-honest model; this means that participants are expected to obey the protocol, but may try to extract as much information as possible. A number of checks are executed during the protocol to detect deviations from the instructions, but the system is currently not fully secure against malicious attackers, which may even attempt to deviate from the protocol to obtain secret information.

# Implementation

The demonstrator is built in Python using the Shamir secret-sharing library from mpc.tno.nl. The, code, installation instructions and usage instructions can be found [here](https://github.com/COSSAS/sacti). Further backgrounds (including a demonstration video) can be found [here](https://cossas-project.org/portfolio/sacti/).

Since the software was developed within the EU's [Prometheus](h2020.prometheus.eu) project, the PKI in the demonstrator is self-made and based on lattice-based standardization candidates from NIST's PQC standardization competition.  However, it is not suitable for operational applications.  It is only suitable for simulation on one machine and for research purposes. Organizations using this protocol should replace it with a properly implemented and tested PKI.

Nonetheless, presented software can be used to get acquainted with the ideas behind SACTI. The performance of SACTi does not rely significantly on the used cryptography. Furthermore, we have attempted to write the software in such a way that a transition to a distributed run is relatively straightforward.

If you would like to get in touch with us about SACTI, we can be reached via our [Slack channel](cossas.slack.com).

# Performance

Efficiency seems very promising, but demands for large CTI communities are very high. We are optimistic that these can be met with this solution, but we have no conclusive result​s. In particular, it has not been possible to properly simulated hundreds of parties.

The figures below were generated with a simulation of the entire community, consisting of the aggregator and all the participants, on a single machine. For the runtime dependence on the number of IoC we expect a linear behaviour, which is indeed clearly observed.

![Picture2](/img/blog/sacti/Picture2.png)

For the dependence on the number of parties the situation is not as clear. If $`n`$ parties join the protocol run, every submitted value will be split in $`n`$ shares. The amount of information a party must process increases linearly with the number of participants. Since we are simulating all $`n`$ parties on a single machine, we expect a quadratically increasing runtime. However, the (small-scale) simulations indicate a faster expansion. This may be due to deficiencies in the code or clogging in the machine's processing unit.

![Picture3](/img/blog/sacti/Picture3.png)

It should be mentioned that the simulation on a single machine does not suffer from communication delays that will occur in distributed simulations. 
Exploratory tests have indicated that the choice of cryptographic algorithms in the PKI have a negligible effect on the protocol's performance.

# Conclusion

Cyber threat intelligence can be aggregated securely with the help of secret sharing. To demonstrate this TNO has developed a protocol with a robust security and realistic run-times for communities of 100 participants and 10,000 of IoC's. Although a full extension to the malicious security model has not (yet) been achieved and some improvement on the protocols improvement is desirable, we are confident that this is within reach. In this way we hope that communities can increase their awareness of cyber risks and improve their resilience.
