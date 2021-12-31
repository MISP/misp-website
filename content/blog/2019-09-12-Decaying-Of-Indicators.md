---
title: Decaying of Indicators - MISP improved model to expire indicators based on custom models
date: 2019-09-12
layout: post
banner: /img/blog/decay.png
---

# An improved and flexible model to expire indicators

This blog post aims to give a thorough introduction of a new functionality added in MISP 2.4.116, allowing users and organisations to easily expire information depending on their personalised objectives and targets.

MISP, being a distributed system, enables the sharing of data between various users and organisations, often resulting in the parties involved in an exchange not even knowing one another. Whilst having access to a large trove of information is extremely beneficial for all parties involved, however, it can also introduce a whole new set of challenges to deal with.

In this blog post, we will mainly touch on information **quality** and **freshness**, along with other issues such as **trust**, **use-cases** and **interests**. The latter group is partially taken into account, but will not be presented. Nevertheless, these concepts are examined more thoroughly in a [paper](https://arxiv.org/abs/1902.03914) we published that has served as our basis for the implementation, along with a detailed explanation of the solution we have chosen to tackle these issues.

Our main objective is to provide users with a **simple yet customisable system** to automatically (or in some cases manually) mark an *Indicator Of Compromise* (or more generically, an *Attribute*) as **expired**.

Before getting started with showing how the model presented in the paper is implemented in MISP, we first need to have a look at some of the basic concepts required to better understand how the various components are working together.

# The (potentially) annoying bits of the theory

The solution currently supported in MISP is based on two components: The ``base_score`` and the ``score``. The idea is to have an initial fixed value called ``base_score`` taking into account the **quality** of an indicator and a time-dependant ``score``, which decreases with the passage of time.

A simplified version would look something like this:
```
score = base_score * P
```
Where ``P`` is composed of the following ``parameters``:
- ``lifetime``: The lifetime of the IOC or the point in time at which the score of the *Attribute*'s score will reach 0
- ``decay_speed``: The speed at which the decay happens or the speed at which an *Attribute* will lose score

**⚠** **It should be noted that everytime a [*Sightings*](https://www.circl.lu/doc/misp/sightings/) is added to an *Attribute*, the ``score`` is refreshed back to the value of the original ``base_score`` and a new decay is initiated from that point forward.**

# Polynomial Decaying Model built-in in MISP

We still have to see how the ``base_score`` is actually computed. In the current implementation of the *Decaying Model* in MISP, the ``base_score`` is computed from the *Taxonomies* along with the various attached weights. Weights are a means to prioritise extracted ``numerical_values`` from *Taxonomies* over others.

To give the intuition of how the ``base_score`` computation works, let's look at two examples. In these examples, the two *Taxonomies* used are
[*phishing*](https://github.com/MISP/misp-taxonomies/blob/master/phishing/machinetag.json) and [*admiralty-scale*](https://github.com/MISP/misp-taxonomies/blob/master/admiralty-scale/machinetag.json). Both of them contain *Tags* that have a ``numerical_value`` associated to them:
- <img src="/img/blog/decaying/tag-as-A.png" alt="admiraly-scale:source-reliability = Completely reliable" width="300"/>, ``numerical_value = 100``
- <img src="/img/blog/decaying/tag-as-D.png" alt="admiraly-scale:source-reliability = Not usually reliable" width="300"/>, ``numerical_value = 25``
- <img src="/img/blog/decaying/tag-p-H.png" alt="phishing:psychological-acceptability = high" width="250"/>, ``numerical_value = 75``

So, if an *Attribute* only has a single *Tag* attached, for example ``admiralty-scale:source-reliability="Completely reliable"``, the ``base_score`` would be:
```
base_score = 100
```

Weights come into play when multiple *Tags* are attached to an *Attribute*. As a simplification, let's suppose that both *Taxonomies* should have the same importance in regards to the *Attribute*'s score. Thus, the total weight (100) will be shared, assigning both *Taxonomies* a weight of 50.

```
admiralty-scale = 50
phishing        = 50
---------------------
sum              100
```
If an *Attribute* has the *Tags* <img src="/img/blog/decaying/tag-as-A.png" alt="admiraly-scale:source-reliability = Completely reliable" width="300"/> and <img src="/img/blog/decaying/tag-p-H.png" alt="phishing:psychological-acceptability = high" width="250"/> attached, the computation steps would look like this:

![base_score computation steps](/img/blog/decaying/bs-computation-steps.png)

Thus, the ``base_score`` of this *Attribute* will be ``87.50``.


# Short tutorial

Now that we've seen the basic concepts, let's have a look at how MISP implements these components. For these examples, we are using the default [phishing model](https://github.com/MISP/misp-decaying-models/blob/master/models/phishing-model.json) model on a **test** *Event*.

## Integration in MISP

### Endpoint: ``events/view``

At the *Event* level, a new filter button has been added, which attaches the real-time computed ``score`` to all *Attributes* that have been mapped to a *Model*.

<img src="/img/blog/decaying/dm-event.png" alt="Decay Model index" width="700"/>

### Endpoint: ``attribute/restSearch``

The ``attribute/restSearch`` endpoint has been updated and now supports four new parameters to help with filtering out expired *Attributes* or to simply play with the different available models.
- ``includeDecayScore`` **[bool]**: Attach the real-time computed ``score`` of the *Attribute* along with the associated *Model* information
- ``excludeDecayed`` **[bool]**: Filter out all expired IOCs
- ``decayingModel`` **[list]**: List of *Model(s)* that will be attached to the given *Attributes*
- ``modelOverrides`` **[dict]**: JSON that can be used to modify *Model* parameters on-the-fly

Example
```
// attribute/restSearch query that gets every `ip-src` attributes being tagged with tlp or phishing,
// not being expired,
// with a overriden model threshold of 30 for the two models with id 84 and 12.
{
    "type": "ip-src",
    "tags": ["tlp:%","phishing:%"],
    "includeDecayScore": 1,
    "excludeDecayed": 1,
    "modelOverrides": {
        "threshold": 30
    }
    "decayingModel": [84, 12],
}
```

## Default and Custom Models

In MISP, Some *Decaying Models*, called **Default Models**, will be supplied by default. Similarly to *Taxonomies*, *Galaxies* and *misp-objects*, *Decaying Models* will have their [own repository](https://github.com/MISP/misp-decaying-models) along with the possibility to be updated directly from both the API and the UI via a single click. **Default Models** are available to everyone, meaning that they can been viewed and customised by any user having a presence on the MISP instance.

**Custom Models** are user-defined models that are shared with other users. However, if desired, they can be kept private to one's own organisation by turning off the sharing flag, similarly to how the *Tag Collection* feature handles the same concept.

## Decaying Fine Tuning Tool: Setting parameters and mapping model to *Attribute* types

When creating a new *Decaying Model*, modifying its parameters and viewing the outcome of the any changes should be as easy and straight forward as possible. In order to do so, several widgets are included with the latest version of MISP.

### Customising the lifetime and the decay speed parameters

{{<video src="/img/blog/decaying/dm-tool.mp4" title="Decaying Model Fine Tuning Tool - Parameters" >}}

### Setting the ``base_score``: Customising Taxonomies' weights

{{<video src="/img/blog/decaying/dm-bs.mp4" type="video/mp4" title="Decaying Model Fine Tuning Tool - Base score" >}}

### Viewing scores and simulating the model

{{<video src="/img/blog/decaying/dm-simulation.mp4" type="video/mp4" title="Decaying Model Simulation Tool" >}}

# Developer perspective: Creating a model using a different algorithm

The Built-in Polynomial *Decaying Model* implemented in MISP allows users to customise various of its components in order to achieve the desired decay behaviors in a fine-grained manner. Nevertheless, even with the flexibility offered by the system, it is absolutely possible that our model doesn't encompass your specific use-case's needs. Thanks to the implemented architecture, any other formulae or algorithms can be added and used in a straightforward way.

Steps to create a new decay algorithm:
- Create a new file ``$filename`` in ``app/Model/DecayingModelsFormulas/``
- Extend the **Base** class as defined in ``DecayingModelBase``
- Implement the two mandatory functions ``computeScore`` and ``isDecayed`` using your own formula/algorithm
- Create a *Model* and set the ``formula`` field to ``$filename``

```
<?php
include_once 'Base.php';

class Polynomial extends DecayingModelBase
{
    public const DESCRIPTION = 'The description of your new decaying algorithm';

    public function computeScore($model, $attribute, $base_score, $elapsed_time)
    {
       // algorithm returning a numerical score
    }

    public function isDecayed($model, $attribute, $score)
    {
        // algorithm returning a boolean stating
        // if the attribute is expired or not
    }
}
?>
```

# Outcome

Evaluating the **quality** and **freshness** of IOCs is a problem commonly found in Threat Intelligence Platforms. We have tried to solve it using a simple yet customisable system.

Event though the small set of models included in the upcoming MISP release should fit the most common use-cases, we are eagerly awaiting any contributions, fine-tunings or feedback from users. We consider the current implementation to be a foundation, upon which we want to gradually build using both our own findings and the feedback of the community. These would opens us up to plenty of opportunities, including the inclusion of new *Models*, improvements to the precision of existing *Models*', tweaking of the various parameters and even the integration of machine learning algorithms as new *Models*.

Furthermore, we are not done yet! There are already a bunch of improvements cooking at the MISP-Project kitchen,
- Integration of ``False Positive`` and ``Expiration`` *Sightings*
- Tweaks to the formula in order to provide better controls in regards to reseting the ``base_score`` once a *Sighting* has been added
- Per-user overrides for the Taxonomies' ``numerical_values``
- Weights on a *Tag*'s predicate level
