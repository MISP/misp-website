---
title: MISP 2.4.156 released including a new synchronisation event signing mechanism and many new features
date: 2022-03-18
layout: post
banner: /img/signed-sync.png
---

We are pleased to announce the immediate availability of MISP v2.4.156 - a release bringing several new features and fixes two critical vulnerabilities. **We highly encourage everyone to update to this version as soon as possible**.

# Protected mode - cryptographic signing of synchronisation

With the current tensions, information assurance in many ways is becoming more and more important across the different MISP communities. Whilst foul play is often quickly discovered and leads to the ejection from a sharing community, leading to an inherent self-healing mechanism of the different networks, in some cases due to information's criticality, more active measures are needed.

By design, MISP's sharing mechanisms rely on trust relationships between the different interconnected nodes in the various MISP networks. This means that in a mesh network of MISP nodes, information can travel via trusted synchronisation users, the information's veracity being ensured by the various site administrators of the different instances. 

In some cases this is not enough, especially when exchanging data that is meant to be adhered to blindly in a highly automated fashion. Vetted block lists for example affecting large constituencies and the automatic blocking of traffic for service providers for example.

To support this use-case, MISP as of v2.4.156 has a new mechanism that allows event creators to attach a set of PGP instance signing keys to an event, which are used to sign the events on each hop of the synchronisation. This allows recipient MISPs to discard any updates coming from nodes that cannot produce a valid signature with one of the initial signing keys.

## An example

Alice and Bob each have their own MISP instances, with Alice feeding Bob with critical information. Bob trusts this information immediately and blindly. Eвa, wanting to remove data points or diluting the information from Alice's stream, is also part of their broader network. 

Traditionally, Alice sharing an event to the network would propagate to both Bob's and Eвa's instance. Eвa could in this case abuse her administrative privileges to modify the event, perhaps injecting disinformation and removing valid data. By synchronising this back to Bob, Bob's instance would see an incoming synchronised edit, which in a mesh network could be legitimate and as such it would accept the change. Propagating it further back to Alice would be blocked by MISP's protection against remote modifications to data at origin.

![unprotected_sync_mode](https://user-images.githubusercontent.com/3668672/159035794-918f9c33-74dc-44e2-84db-34fdb1ba726a.png)

With protected mode enabled, this situation changes drastically. Alice could add her own signing key as well as Bob's to the event, ensuring that the only parties able to relay modifications to the event would be Alice and Bob. When leaving Alice's instance, the event would get signed with Alice's signing key. Since the event contains both Alice's and Bob's key, any subsequent modifications from Alice would be accepted by Bob's instance. Incoming edits would be signed by Alice's key, meaning that Bob would validate the package with its locally stored public key of from the initial exchange.

This means that Eвa modifying the event and attempting to share it with Bob would get rejected, as Eвa, lacking the private keys of Alice and Bob, can only sign it with her own key, which Bob's instance would immediately flag as suspicious and ultimately reject it.

![protected_sync_mode](https://user-images.githubusercontent.com/3668672/159036489-f2d457aa-cb23-42a8-b10b-6d9e9a02e7f9.png)

## Usage

To get started with the feature, simply use the new protected mode field in the event view, you can convert any event into protected mode:

![protected1](https://user-images.githubusercontent.com/3668672/159038886-d82a516b-1281-4649-ac2d-ea456f7468ed.png)

At which point you can start adding individual keys:

![protected2](https://user-images.githubusercontent.com/3668672/159039506-e896ca51-7a96-4f3f-a46b-718df9e0072c.png)

Keep in mind that you can add multiple instance signing keys if you wish for your trusted partners (or your own instances, for example if you have an internal and a sharing MISP in the DMZ).

![protected3](https://user-images.githubusercontent.com/3668672/159039670-eb1e3b3d-8089-45c0-9511-aaf0ffc80b89.png)

As a caveat, keep in mind that this mechanism limits the distribution of data inadvertently. Even if the distribution level would allow it, the synchronisation will be limited by who can sign the event for further propagation, so use this new functionality when the use-case really calls for it. 

A massive thank you to our good friend [Trey Darley](https://twitter.com/treyka) (@treyka) of Cert.be for the brainstorming session that lead to the implementation of this feature!

# Context summary export

A new export format was added that generates an HTML representation of a summary of all context information from a set of filtered data. One could for example use restsearch to generate all context from any event that is attributed to a threat actor. The resulting HTML will include the Mitre ATT&CK matrix of all leveraged techniques in the selected events as well as any other labelling and context.

# Event warning system

The new warning system warns users about potential improvements to an event they could be making, such as resolving tagging issues, improving the quality of the event, etc. The system comes with a plugable module system, easily build and deploy your own warning system.

![warning_system](https://user-images.githubusercontent.com/3668672/159040894-99d951e3-a076-40c7-9bbd-9ff619df2e5c.png)

# Internal reworks

@JakubOnderka continues his massive crusade against ugly spaghetti code, with a continuous stream of refactorings, this time massively improving the code-base of the synchronisation mechanism.

# Pentest - Several security issues resolved

We would like to thank Ianis BERNARD of NATO Cyber Security Centre. Based on the findings of their pentest we were able to resolve several security vulnerabilities and as such we highly encourage everyone to update to v2.4.156 ASAP.

## Security fixes resolved

Two critical security vulnerabilities were fixed in this release. We strongly recommend everyone to install this version as soon as possible.

- [Potential SSRF attacks fixed](https://github.com/MISP/MISP/commit/8dcf414340c5ddedfebbc972601646d38e1d0717) on generateServerSettings(), the interface is now restricted to the cli interface only.
- [Potential LFI attack fixed](https://github.com/MISP/MISP/commit/8cc93687dcd68e1774b55a5c4e8125c0c8ddc288) via custom file setting.
- [Restrict SVG logo](https://github.com/MISP/MISP/commit/08a07a38ae81f3b55d81cfcd4501ac1eb1c9c4dc) upload for organisation by default and make it optional to limit potential risk of SVG with active payload.

# LinOTP auth improvements

Thanks to the lovely work submitted by @andurin, the LinOTP authentication subsystem now includes several improvements, amongst others the ability to conveniently manage and disable the subsystem directly via the system settings.

Originally, the only way to disable the LinOTP authentication was to purge the related settings from the configuration files. In order not to break the expected functionality for users that already have LinOTP configured, the default behaviour for the new "LinOTP.enable" setting behaves a bit different from other similar settings: When no value was assigned by an administrator, the module is enabled by default if the LinOTP configuration keys exist in the configuration file. That means, if you've had it configured from before, by default it will be enabled. Other than that it will be disabled. 

Confirming the setting as either enabled or disabled by an administrator will override this behaviour with the selected setting.

 
# A long list of other improvements

We have received a massive list of pull requests for enhancements and fixes. Make sure you check out the [changelog](https://www.misp-project.org/Changelog.txt) for further details.

# Acknowledgement

We would like to thank all the [contributors](https://www.misp-project.org/contributors), reporters and users who have helped us in the past months to improve MISP and information sharing at large. This release includes multiple updates in [misp-objects](https://www.misp-project.org/objects.html), [misp-taxonomies](https://www.misp-project.org/taxonomies.html) and [misp-galaxy](https://www.misp-project.org/galaxy.html).

As always, a detailed and [complete changelog is available](https://www.misp-project.org/Changelog.txt) with all the fixes, changes and improvements in MISP core.

