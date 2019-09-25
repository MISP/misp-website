---
title: Benefits of running your own MISP instance
layout: post
featured: /assets/images/misp/blog/community-view.png
---

# Benefits of running your own MISP instance

One topic that regularly pops up during trainings and users that are just getting started with MISP in general is the question of running your own MISP versus using a hosted MISP instance. We have seen a lot of great efforts by ISACs, organisations with national or sectorial responsibilities leading the charge and acting as a central sharing hub for communities.

Whilst their efforts are absolutely pivotal fostering communities and in enabling information sharing, members of such communities should be aware of how to best utilise these resources. In any such community, members have the option to either use the "central sharing instance" as a hosted solution, or run their own MISP instances and interconnect with them to exchange data. In either case, they will have access to the same data and the same export functionalities, so avoiding the need to maintain another server may seem tempting, but do consider the following advantages of opting for your own server instead:

## Ensure that private data remains private

Distribution levels aside, if you create private data for yourself on a hosted instance, you are always have to rely on the hosting organisation to not accidentally view the data with their site admin accounts / directly via the database

## Don't let other snoop on your searches

Inspecting requests against a server you own is trivial, meaning that any search run against a posted MISP instance could be inspected by the system administrators of the hosted instance. What you search for is often more sensitive than the data that you store in your system, your analysts will often take to their knowledge-base such as MISP as a first step to verify whether datapoints are already known, often accidentally including for example victim information

## Avoid being performance limited by overburdened systems

Consider the performance advantages when running heavy filtered lookups against MISP's APIs, the load on sharing instances can be quite heavy depending on the number of organisations participating in the exchange, especially if they too use the hosted instance's APIs for their internal use.

## Take advantage of advanced features

MISP has a wide range of functionalities exclusively available to the host organisation. Be it ZMQ/Kafka/ES connections, local tags for routing 3rd party data, managing private enrichment modules, you're missing out by not running your own system.

## Be the king of your own castle

MISP is a tool that aims to align itself to your workflows, from deciding on vocabularies to use, how to represent certain aspects of the information and setting requirements for how and when information can be shared, MISP site administrators have a host of tools at their disposal to drive how information is encoded and shared. By running your own MISP instance, you can decide for yourself instead of aligning yourself to the visions of your community hosts.


