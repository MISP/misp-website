---
title: Introducing The New Extended Events Feature in MISP
date: 2018-04-19
layout: post
banner: /img/blog/misp-small.png
---

# Introducing Extended Events

We have just released a new feature for MISP that allows users to build full blown events that extend an existing event, giving way to a combined event view that includes a sum total of the event along with all extending events.

**The success and usefulness of information sharing tools largely hinges on how well it can help you convey your message.**

One of the aspects of this that has been permanently stuck at the top of our internal planning whiteboards has always been the goal to improve the collaborative aspects of information sharing.
For those that have followed MISP's development over the years, we have experimented with various tools that were aiming to improve the way we can all work together as a community, be it by being able to propose changes to the data of 3rd parties, to request additional information or to simply be able to communicate through the platform.

However, one of the more principal challenges that has plagued us for a while was finding a simple solution to wanting to add additional information to someone else's analysis. The proposal system was a great way to partially tackle this, users could add additional attributes or propose modifications to existing ones - after which the original creator of the event could accept and incorporate the changes if they deemed them fit for their event.

What was missing though was the ability to create more complex and often more restricted (when it comes to who gets to see the event) additions to the events of third parties, without having to use administrator privileges to tamper with someone else's event. Whilst definitely frowned upon, the above workaround was used by many for very legitimate reasons. Imagine an ISAC receiving a massive amount of 3rd party data through other MISPs, wanting to pass the information on to their constituents along with their own enrichments and analyses (something that is part of their value proposition). Their choices were limited to tampering with the event or to create duplicates of the information, thereby circumventing the creator organisation restrictions.

The "proper" way to do it was to either link the events via tags or an internal reference attribute type, neither of which were really sufficient. The tag approach still relies on having to group the extension event with the original using the tags that already exist on the original - if they weren't contextualised in a distinct enough way (such as a threat actor, campaign name, etc) this would again require tampering with the original to have common linking tags in place. The internal reference option was very loosely linking events, meaning that analysts still couldn't "get the full picture" when trying to pivot through the linked data.

This is where extended events come into play - they allow users to add the id of a known event to be extended to their extension event. MISP uses this to create the "extended event view" - which takes an Event's data and merges it with all of the extension events' data.

Users can thus add objects, attributes, galaxy clusters or tags to existing events, without having to alter those. They retain full control over the distribution / modifications instead of handing it over to the event's creator. This way the ISAC in the example before could add their analysis / enrichments to a separate event and simply link it to the original report and disseminate it only to their constituents - never having modified the original event in any way.

To create an extension event, simply enter the UUID or ID of the event in the "Extends event" field. If you skip this step, you can always do it at a later point by clicking on "edit event". Create the event as you normally would, replicating any of the data already contained in the event to be extended is not needed.

Users viewing the original report, will now see a new field called "Extended by" as shown below:

![A MISP event extended by another event](/img/blog/extended.png "{class='img-responsive'}")

Clicking on the atomic view / extended view toggle button will allow you to jump from the classical event view to the extended event view. The extended view will add all of the relations, tags, galaxy clusters, attributes and objects of the extender events. The attribute list in extended view also shows the event it originates from along with the creator organisation. Keep in mind that duplicates across several events are not culled.

Extending an event is easy and a nifty lookup interface helps you to select the appropriate event to extend:

![Extending a event when creating a new MISP event](/img/blog/extendadd.png "{class='img-responsive'}")

In the above case, OSINT information contained within an event is extended with additional threat hunting information which are limited to your organisation. The major advantage of such an approach is allowing any organisation to expand information without touching the original event.

At MISP project, we strongly believe that our primary objective should be to create open source tools that serve as a liberating organisations from locked eco-systems and to instead spend their energy and effort on what really matters: information sharing and their own use-cases. With the extend event feature, many new analyst practices can be covered, such as for example:

- Counter analysis of reports and distribution thereof to your trusted partners.
- Extending external information from threat-hunting activities such as those derived from [TheHive](https://thehive-project.org/) and incorporating it back into your knowledgebase within MISP.
- Sharing the qualification of information to your ISAC members along with the original information. The model allows competitive analysis from different ISACs to be shared along with the original report. We all have different viewpoints and sharing those unhindered is a natural evolution of collaborative information sharing.
- Embargoed information can be safely contained in an extension event (e.g. to limit risk of analysts editing incorrect information). This also serves as a potential safeguard for higher classified information that is not to be shared with the broader community.

The design concept of the feature was to be as minimalistic and lightweight as possible to ensure a smooth integration with existing sharing communities. The extended event feature allows us to build new sharing and analysis practices to be used in MISP. We welcome welcome your feedback and look forward to any new use-cases that emerge using this feature.

