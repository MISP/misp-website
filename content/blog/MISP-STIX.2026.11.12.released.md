---
title: "MISP-STIX 2026.11.12 released: MISP Extensions for STIX 2.1"
author:
 - Christian Studer
date: 2026-11-16
tags: ["MISP", "STIX", "Threat Intelligence", "CTI", "release"]
layout: post
banner: /img/blog/misp-stix_conversion_features.png
---

# MISP-STIX 2026.11.12: MISP Extensions replace the custom STIX 2.1 content

## Introduction

[misp-stix](https://github.com/MISP/misp-stix) is the Python library powering bidirectional conversion between MISP and STIX (versions 1.x, 2.0 and 2.1).
It is used by MISP core software, available as `misp-stix` on [PyPI](https://pypi.org/project/misp-stix/), and also available directly as a conversion service on [cti-transmute.org](https://cti-transmute.org).

Version **2026.11.12** is out. The main change is in the **STIX 2.1 export**: it no longer writes the custom objects and properties that STIX 2.1 deprecates. MISP content now goes into STIX 2.1 through **extension definitions of MISP's own, the MISP Extensions**, and the import reads them back.

In short:

- A STIX 2.1 bundle exported by MISP **no longer contains any `x-misp-*` object or `x_misp_*` property**.
- The MISP attributes, objects and galaxy clusters that no STIX object represents become **`misp-attribute`, `misp-object` and `misp-galaxy-cluster`** objects.
- MISP values that a standard STIX object has no property for go into **one property extension** on that object.
- The four extensions come with **policy documentation, JSON schemas and example bundles**, so anyone can validate MISP's STIX 2.1 output and parse it.
- The 2.1 output now **keeps content the custom syntax lost**: `to_ids` set to `false`, `first_seen` and `last_seen`, and a cluster's own description.
- The **import reads both syntaxes**, so bundles written by earlier releases import as before.
- Several conversions that used to **fail the whole document now lose only the faulty element**, or nothing at all. Most of these fixes come from community pull requests.

**Upgrade your readers too.** A reader on `2026.10.12` or earlier loses content from the bundles the new version exports. This includes a MISP instance importing STIX 2.1 files exported by an upgraded instance.

## Why move away from custom objects and properties?

The [STIX 2.1 specification](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) deprecates custom objects and properties (section 11) in favour of extension definitions (section 7.3). An extension definition is a STIX object of its own. It names who created the extension and gives it a version and a JSON schema, so a consumer can learn what the extended content means and check it, instead of guessing from an `x_` prefix.

misp-stix kept using the custom syntax in its 2.1 export until now. This worked, but it had two problems. First, the content was opaque to anyone but misp-stix. Second, a few values were dropped along the way because the custom syntax had no place for them. This release fixes both.

## The four MISP Extensions

The STIX 2.1 export now carries MISP's own content through four extension definitions. They have fixed ids, are at version `1.0.0`, and are created by the MISP Project identity (`identity--55f6ea65-aa10-4c5a-bf01-4f84950d210f`):

| Extension | Extension type | Extension definition id |
|:---|:---|:---|
| MISP Attribute Extension | `new-sdo`, defining `misp-attribute` | `extension-definition--c1f2c0fa-3786-4f27-bf57-cf050ecfc104` |
| MISP Object Extension | `new-sdo`, defining `misp-object` | `extension-definition--a093107b-933f-4d72-a9a6-6d7318adadda` |
| MISP Galaxy Cluster Extension | `new-sdo`, defining `misp-galaxy-cluster` | `extension-definition--573a76d8-f8a0-4f53-bc93-f2777576b7b9` |
| MISP Property Extension | `property-extension`, on standard objects | `extension-definition--5ece67ea-2e8b-4ed0-bb69-26d69053ee0b` |

The three `new-sdo` extensions each define one object type for MISP content that has no STIX equivalent. The property extension is shared by every standard STIX object type MISP extends. This includes SDOs such as `attack-pattern`, `location` or `threat-actor`, SCOs such as `file`, `url` or `windows-registry-key`, and `indicator`, `note` and `opinion`.

## What changes in the STIX 2.1 output

### Custom objects become `misp-*` objects

`x-misp-attribute`, `x-misp-object` and `x-misp-galaxy-cluster` become `misp-attribute`, `misp-object` and `misp-galaxy-cluster`. They keep the same uuid in their id, and their properties lose the `x_misp_` prefix. Each object declares its extension in `extensions`.

Here is a `bank-account` object, which has no STIX equivalent, as exported by `2026.10.12` (trimmed to two attributes, `created_by_ref` and labels left out):

```json
{
    "type": "x-misp-object",
    "spec_version": "2.1",
    "id": "x-misp-object--695e7924-2518-4054-9cea-f82853d37410",
    "created": "2020-10-25T16:22:00.000Z",
    "modified": "2020-10-25T16:22:00.000Z",
    "x_misp_name": "bank-account",
    "x_misp_meta_category": "financial",
    "x_misp_attributes": [
        {
            "type": "iban",
            "object_relation": "iban",
            "value": "LU1234567890ABCDEF1234567890",
            "category": "Financial fraud",
            "uuid": "8acaad62-227a-4988-96e7-4586847421a2",
            "to_ids": true
        },
        {
            "type": "text",
            "object_relation": "institution-name",
            "value": "Central Bank",
            "category": "Other",
            "uuid": "c206e7b4-7333-40a3-bf02-9647d32f9df2"
        }
    ]
}
```

And the same object, as exported by `2026.11.12`:

```json
{
    "type": "misp-object",
    "spec_version": "2.1",
    "id": "misp-object--695e7924-2518-4054-9cea-f82853d37410",
    "created": "2020-10-25T16:22:00.000Z",
    "modified": "2020-10-25T16:22:00.000Z",
    "name": "bank-account",
    "meta_category": "financial",
    "attributes": [
        {
            "type": "iban",
            "object_relation": "iban",
            "value": "LU1234567890ABCDEF1234567890",
            "category": "Financial fraud",
            "uuid": "8acaad62-227a-4988-96e7-4586847421a2",
            "to_ids": true
        },
        {
            "type": "text",
            "object_relation": "institution-name",
            "value": "Central Bank",
            "category": "Other",
            "uuid": "c206e7b4-7333-40a3-bf02-9647d32f9df2",
            "to_ids": false
        }
    ],
    "extensions": {
        "extension-definition--a093107b-933f-4d72-a9a6-6d7318adadda": {
            "extension_type": "new-sdo"
        }
    }
}
```

Note the `"to_ids": false` on the second attribute. The custom syntax left it out, so the import gave the attribute its type's default instead. The `misp-*` types always write `to_ids`, `true` or `false`. They also write `first_seen` and `last_seen` whenever MISP has them, and the attribute `data` in base64 whenever there is a payload.

For galaxy clusters, `x_misp_description` used to join the galaxy's description and the cluster's description into a single string. A `misp-galaxy-cluster` now carries them separately, as `galaxy_description` and `description`.

### Custom properties move into the MISP Property Extension

When a standard STIX object cannot hold every value of a MISP object, the values left over used to go out as `x_misp_<name>` properties. They now go into the object's `extensions`, under the property extension's id, next to any predefined extension such as `windows-pebinary-ext` or `socket-ext`. A `url` object whose leftover values were `x_misp_domain`, `x_misp_host`, `x_misp_ip` and `x_misp_port` now reads:

```json
"extensions": {
    "extension-definition--5ece67ea-2e8b-4ed0-bb69-26d69053ee0b": {
        "extension_type": "property-extension",
        "domain": "example.com",
        "host": "www.example.com",
        "misp_ip": "198.51.100.7",
        "port": "443"
    }
}
```

A property name is the old one without its `x_misp_` prefix. Names the STIX base schema cannot take as they are get escaped. For example, a name shorter than three characters takes a `misp_` prefix, so `ip` becomes `misp_ip`. The [policy documentation](https://github.com/MISP/misp-stix/blob/main/data/misp-extensions/extension-definition-specifications/misp-5ec/README.md) gives the exact rules to read names back.

MISP values of objects nested inside STIX structures (a `pe` object and its sections inside `windows-pebinary-ext`, registry values inside a `windows-registry-key`) had no valid place in STIX 2.1. They now go into **nested rooms** of the property extension: `windows_pebinary_ext`, `windows_pebinary_ext.sections` and `values`.

### Patterns follow the values

Indicators compare MISP values where the observable now holds them, through the property extension's path:

```
[url:x_misp_domain = 'example.com']
```

becomes:

```
[url:extensions.'extension-definition--5ece67ea-2e8b-4ed0-bb69-26d69053ee0b'.domain = 'example.com']
```

### The bundle carries its definitions

A STIX 2.1 bundle using a MISP Extension now includes the extension definitions it uses and the MISP Project identity that creates them, each only once. In an event, they go with the identities, ahead of the Report or Grouping. **`objects[1]` is therefore no longer guaranteed to be the Report.** Consumers should not rely on this order, nor on the definitions being present. The import recognises the extensions by their fixed ids alone.

### What stays the same

- The `misp:type=…`, `misp:category=…`, `misp:name=…` and other **labels** are standard STIX properties and do not change, so a bundle is recognised as MISP's as before.
- **STIX 2.0** has no extension definitions. Its export keeps the `x-misp-*` objects and the `x_misp_*` properties, and changes only where four fixes stop it losing content (see below).

## Importing

- The **Internal import** (STIX produced by MISP) reads both the MISP Extensions and the custom syntax, object by object. STIX 2.1 bundles written up to `2026.10.12` import into the same MISP content as before.
- The import also reads extension paths in **Indicators that have no Observed Data next to them**, so a bundle reduced to its Indicators still imports whole.
- An identity that only creates extension definitions, like the MISP Project identity, converts to nothing in MISP. It does not become an `organization` object.
- A bundle whose MISP content sits only in property extensions now **parses with `stix2.parse` and its default `allow_custom=False`**, which refused the `x_misp_*` properties. A bundle with a `misp-*` object still needs `allow_custom=True`, unless `misp_stix_converter` is imported, which registers the types.

## Specification, schemas and examples

The MISP Extensions are documented in the repository, in the style of the STIX specification:

- The [policy documentation](https://github.com/MISP/misp-stix/blob/main/data/misp-extensions/extension-definition-specifications/misp-5ec/README.md) describes the four extensions, their properties, naming rules and conformance notes.
- The [JSON schemas](https://github.com/MISP/misp-stix/tree/main/data/misp-extensions/extension-definition-specifications/misp-5ec) are the normative definition. The directory can be given directly to `stix2_validator --schemas`.
- **Eight example bundles**, taken from the 2.1 export of test events, are validated against the schemas by the test suite.
- The [packaged definition objects](https://github.com/MISP/misp-stix/tree/main/misp_stix_converter/data/misp_extensions) ship with the library.

The [mapping documentation](https://github.com/MISP/misp-stix/tree/main/documentation) is also regenerated to describe the new 2.1 output.

## More robust conversions

Several conversions used to fail the whole document because of a single faulty element. Now only that element is lost, with an Error, or it is kept.

### Export

- **An event galaxy that fails** no longer loses the whole document, in both STIX versions. The galaxy is lost alone and its tag goes out as a label of the Report or Grouping. A 2.1 region cluster with no ` - ` code, such as `Antarctica`, exports as a Location ([#121](https://github.com/MISP/misp-stix/pull/121)).
- **A 2.1 annotation without text** no longer raises `MissingPropertiesError`. It goes out as a `misp-object` ([#122](https://github.com/MISP/misp-stix/pull/122)).
- **An event creator (`Orgc`) missing its uuid or name** no longer raises a `TypeError`. The event exports without its creator identity, with an Error ([#118](https://github.com/MISP/misp-stix/pull/118)).
- **A network socket with an out-of-enum `socket-type` or `domain-family`** exports as `network-traffic`, instead of falling back to a custom object.
- **STIX 2.0 galaxy clusters** carry `first_seen` and `last_seen` as `x_misp_first_seen` and `x_misp_last_seen`. Before, they went out unprefixed, which failed the document or got dropped on import.

### Import

- **A Sighting naming an organisation the bundle does not carry** no longer loses the whole document. The Sighting is dropped with an Error, and a Sighting with no `where_sighted_refs` is imported with no organisation.
- **An ` AND ` inside a quoted pattern value** no longer splits the pattern. A file named `evil AND you.exe` used to cost its object, and a `filename|md5` attribute could silently get wrong values. Every pattern reader now splits outside quoted values only ([#132](https://github.com/MISP/misp-stix/pull/132)).
- **A hash MISP has no type for**, such as a `CRC32` next to an MD5, no longer costs its object. It is kept as a `text` attribute named after the hash (`crc32`), with a Warning (reported in [#133](https://github.com/MISP/misp-stix/pull/133)).
- **`to_ids` from the pattern**: the values of a `domain-ip` object, and the values read from an artifact (a file's malware sample, an image's url), now take their `to_ids` from the Indicator's pattern, like other observable values, instead of their type's default.

## Upgrading

```bash
pip install --upgrade misp-stix
```

Before upgrading, check the following:

- **Python 3.11 or later is required**, together with **pymisp 3.0**. Python 3.10 is no longer supported, and Python 3.15 now is.
- `pycountry` 26 is required.
- **STIX 2.1 consumers** of MISP output should read the extensions instead of the `x_misp_*` properties. The [release notes](https://github.com/MISP/misp-stix/releases/tag/2026.11.12) list the migration rules, and the schemas are the reference.
- **Readers on `2026.10.12` or earlier lose content** from the new 2.1 bundles: `misp-*` objects, values in property extensions, analyst Opinions, and more. Upgrade them, including MISP instances importing STIX 2.1 from upgraded instances.
- Do not assume `objects[1]` of an event bundle is the Report.

This release has no security advisory. Every change comes with tests, and the suite now stands at **3,043 tests**, run on every Python version from 3.11 to 3.15.

The full list of changes, with commit references, is in the [release notes](https://github.com/MISP/misp-stix/releases/tag/2026.11.12).

## Acknowledgements

Many thanks to **elhoim** for the pull requests [#118](https://github.com/MISP/misp-stix/pull/118), [#121](https://github.com/MISP/misp-stix/pull/121), [#122](https://github.com/MISP/misp-stix/pull/122) and [#132](https://github.com/MISP/misp-stix/pull/132), and for the report in [#133](https://github.com/MISP/misp-stix/pull/133). Five of the fixes in this release come from these contributions.

- Source code: [https://github.com/MISP/misp-stix](https://github.com/MISP/misp-stix)
- Release notes: [https://github.com/MISP/misp-stix/releases/tag/2026.11.12](https://github.com/MISP/misp-stix/releases/tag/2026.11.12)
- MISP Extensions specification: [https://github.com/MISP/misp-stix/tree/main/data/misp-extensions/extension-definition-specifications/misp-5ec](https://github.com/MISP/misp-stix/tree/main/data/misp-extensions/extension-definition-specifications/misp-5ec)
- PyPI: [https://pypi.org/project/misp-stix/](https://pypi.org/project/misp-stix/)
- Online conversion service: [https://cti-transmute.org](https://cti-transmute.org)
