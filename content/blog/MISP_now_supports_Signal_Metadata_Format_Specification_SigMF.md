---
title: MISP now supports Signal Metadata Format Specification SigMF 
date: 2023-08-23 
layout: post
tags: ["SigMF", "SIGINT", "MISP", "Threat Intelligence", "Signal Intelligence"]
banner: /img/blog/sigint.png
---

As one of the outcomes of [GeekWeek8](https://www.cyber.gc.ca/en/geekweek/geekweek-8), MISP now supports a new set of features useful for handling radio frequency information in the [Signal Metadata Format Specification](https://github.com/sigmf/SigMF)) (SigMF), commonly used in Software Defined Radio (SDR), digital signal processing and data analysis applications.

![GeekWeek logo singal waterfall](https://user-images.githubusercontent.com/1659902/262598006-9e1df43f-eed1-4bec-b72f-809240eef238.gif)

### SigMF

[Signal Metadata Format Specification]((https://github.com/sigmf/SigMF)) (SigMF) has emerged as a powerful tool for describing and annotating signals. It provides a standardized way to store and exchange metadata related to various signal types, enabling seamless collaboration and efficient data sharing across diverse domains.

It was designed with the intention of promoting interoperability among signal processing tools, making it easier for researchers, engineers, and data scientists to work with a wide range of signals.

SigMF metadata includes information such as signal frequency, sample rate, time stamps, annotations, and other relevant attributes that aid in comprehending the nature of the signal. 

### SigMF Data Handling on MISP

#### New Object Templates

New object templates based on the [Signal Metadata Format Specification]((https://github.com/sigmf/SigMF)) (SigMF) such as:

* `SigMF Recording` (.sigmf-meta + sigmf-data)
* `SigMF Archive`
* `SigMF Expanded Recording`

Implemented via PR [#398](https://github.com/MISP/misp-objects/pull/398).

#### Enriching Objects

MISP version 2.4.175 now allows enriching objects. `misp-modules` can handle objects and can define which template name or uuid applies to certain objects.

![image](https://github.com/MISP/MISP/assets/1659902/d5dfe9d1-6807-467e-bec0-77c0d41b9fd3)

When defining your `misp-module` you can add an object template name as `input` to the `mispattributes` dictionary, example:

```python
mispattributes = {
    'input': ['sigmf-recording'],
    'output': [
        'MISP objects'
    ],
    'format': 'misp_standard'
}
```

`sigmf-recording` is a object template name, when click on the enrichment icon (![image](https://github.com/MISP/MISP/assets/1659902/d731f0a5-17b1-4ae7-9708-607d26cf9a96)) in the object envelop, MISP will propose a list of possible enrichments that match that object template:
![image](https://github.com/MISP/MISP/assets/1659902/f9a0c85d-89ce-4d10-88bd-f2af85445709)
 
For accessing the full object in the `misp-module`, you can do the following:
```python
def handler(q=False):
    request = json.loads(q)
    object = request.get("object")
    ...
``` 

Implemented via PR [#9187](https://github.com/MISP/MISP/pull/9187)

#### SigMF enrichment MISP Module 

Thanks to this new object enrchment feature, a new MISP module that expands a `SigMF Recording` into a `SigMF Expanded Recording` was added, it turns some of the signals metadata items into MISP attributes so users can use MISP search and other feature and generates a waterfall plot of the signal.

Additionally, if the enrichment module is applied to a `SigMF Archive`, it extracts the archive into several `SigMF Recording` objects.

![SigMF Objects in MISP](https://user-images.githubusercontent.com/1659902/262600327-d0ca4922-4cae-4eea-9c0b-af03dc9d0ad2.png)

![SigMF expansion module waterfall plot](https://user-images.githubusercontent.com/1659902/262599812-c05e8f2c-6f36-4b0b-b62c-cae56eea1e78.png)

Implemented via PR [#628](https://github.com/MISP/misp-modules/pull/628)
