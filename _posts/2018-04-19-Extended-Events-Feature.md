---
title: Introducing The New Extended Events Feature in MISP
layout: post
featured: /assets/images/misp-small.png
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

![A MISP event extended by another event](/assets/images/misp/blog/extended.png){:class="img-responsive"}

Clicking on the atomic view / extended view toggle button will allow you to jump from the classical event view to the extended event view rapidly. The extended view will add all of the relations, tags, galaxy clusters, attributes and objects of the extender events. The attribute list in extended view also shows the event it originates from along with the creator organisation. Keep in mind that duplicates across several events are not culled.

Extending an event is easy and a nifty lookup interface helps you to select the appropriate event to extend:

![Extending a event when creating a new MISP event](/assets/images/misp/blog/extendadd.png){:class="img-responsive"}

In the above case, OSINT information contained within an event is extended with additional threat hunting information which are limited to your organisation. The major advantage of such approach is allowing any organisation to expand information without touching the original event.

In MISP, we strongly believe that we should create open source tool that give freedom to organisations and people to use the information sharing tools for any use-cases. With the extend event feature, many new analysis practices can be covered:

- Counter analysis of reports and distributing the counter analysis to your trusted partners.
- Extending external information from threat-hunting such as [TheHive](https://thehive-project.org/) and storing it back in your knowledge-database in MISP.
- Sharing qualification information to your ISAC members along with the original information. The model allows competitive analysis from different ISACs to be shared from the original report.
- Embargo information can be safely contained in an external event (e.g. to limit risk of analysts editing incorrect information).

The design of the feature was minimal and light to ensure a smooth integration with existing sharing communities. The extended event feature allows to build new sharing and analysis practices to be used in MISP. We welcome welcome your feedback and are interested in all new use-cases using this feature.

