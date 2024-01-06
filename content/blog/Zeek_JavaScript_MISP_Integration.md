---
title: Using Zeek's new JavaScript support for MISP integration
authors:
- Arne Welzel
date: 2024-01-03
banner: /img/blog/zeekjs-misp-overview.png
layout: post
---

# Using Zeek's new JavaScript support for MISP integration

With Zeek 6.0, experimental [JavaScript support](https://docs.zeek.org/en/master/scripting/javascript.html) was added to [Zeek](https://zeek.org/),
making Node.js and its vast ecosystem available to Zeek script developers to more easily integrate with external systems.

## MISP Integration

As a tech-demo, the popular Zeek package [dovehawk](https://github.com/tylabs/dovehawk) has been re-implemented using JavaScript.
The re-implementation is named [zeekjs-misp](https://github.com/awelzel/zeekjs-misp) and has been published on GitHub.

In essence, the new package uses Node's [https module](https://nodejs.org/api/https.html) to communicate with
[MISP's Rest API](https://www.misp-project.org/openapi/), achieving the following:

* Populate Zeek's [Intelligence Framework](https://docs.zeek.org/en/master/frameworks/intel.html) with attributes and event information collected using the [restSearch endpoint](https://www.misp-project.org/openapi/#tag/Attributes/operation/restSearchAttributes).

* Report intelligence matches back to the MISP instance as sightings using the [addSighting endpoint](https://www.misp-project.org/openapi/#tag/Sightings/operation/addSighting).


## Demo

One component for the demo is a [misp-docker](https://github.com/MISP/misp-docker) docker-compose setup.
The misp-docker project makes it very easy to run a local MISP instance for testing.
The default "Tor ALL nodes" feed is enabled in this instance. This feed provides `ip-dst` attributes for all currently known Tor nodes.
zeekjs-misp fetches these and converts the `ip-dst` attributes into Zeek `Intel::ADDR` intelligence items.

The other component of the demo is a Zeek container running in host-network mode with the zeekjs-misp package installed.
Zeek's [official container images](https://hub.docker.com/r/zeek/zeek) have JavaScript support built-in by default.
For demonstration purposes, the individual commands are reproduced below. Usually, the package installation via `zkg`
would be done in a dedicated `Dockerfile`. The MISP options would conventionally be placed into `local.zeek` instead
of directly on the command line.


First, the container is started and the zeekjs-misp package installed:

```
$ docker pull zeek/zeek
$ docker run --net=host --rm -it zeek/zeek
# zeek -N Zeek::JavaScript
Zeek::JavaScript - Experimental JavaScript support for Zeek (built-in)
# echo "yes" | zkg install zeekjs-misp
The following packages will be INSTALLED:
  zeek/awelzel/zeekjs-misp (main)

Proceed? [Y/n] Installing "zeek/awelzel/zeekjs-misp"
Installed "zeek/awelzel/zeekjs-misp" (main)
Loaded "zeek/awelzel/zeekjs-misp"
```

Thereafter, Zeek is invoked as follows. This loads the zeekjs-misp and frameworks/intel/seen
packages and uses the wireless interface of the host (available within the container due to running in host networking mode).
It further configures the zeekjs-misp authentication options for use with the testing MISP instance and enables debug logging:

```
# zeek -C -i  wlp0s20f3 zeekjs-misp frameworks/intel/seen  MISP::url=https://localhost MISP::api_key=6gIV…BAJ MISP::insecure=T MISP::debug=T
<params>, line 1: listening on wlp0s20f3

zeek-misp: Starting up zeekjs-misp
zeek-misp: url https://localhost
zeek-misp: api_key 6gIV...
zeek-misp: refresh_interval 120000
zeek-misp: max_item_sightings 5n
zeek-misp: max_item_sightings_interval 5000
zeek-misp: Schedule for 120000...
zeek-misp: Loading intel data through attributes search
zeek-misp: Attribute search {"tags":[],"to_ids":1,"eventid":[],"type":"!yara,!malware-sample,!ssdeep,!pattern-in-traffic,!btc","from":1695133600}
zeek-misp: searchAttributes done items=8660 requestMs=213.13ms insertMs=108.82661300897598ms
zeek-misp: Summary of attribute types
zeek-misp:   ip-dst = 8660
zeek-misp: Attributes search done
```

The output shows that 8660 `ip-dst` attributes have been fetched from the MISP instance and inserted into Zeek's Intelligence store.
Attributes are fetched every 2 minutes by default. The package provides further configurability to limit the time range,
filter attributes by types, or limit to attributes of specific events only.

There is now a single Zeek process running, monitoring the wireless interface of the host.
Running `nc` on the host system to establish a connection to one of the active Tor node IPs
shows Zeek successfully detecting the connection and producing an `intel.log` entry.

On the host system:
```
$ nc -z -v 97.107.139.108 80
Connection to 97.107.139.108 80 port [tcp/http] succeeded!
```

Within the container where Zeek is running, the `Intel::match` event and sighting
report is logged and the `intel.log` file populated.
```
<params>, line 1: listening on wlp0s20f3
...
zeek-misp: zeek-misp: Intel::match 97.107.139.108
zeek-misp: Sightings reported 97.107.139.108
^Z

# zeek-cut -m ts uid id.resp_h seen.indicator seen.indicator_type sources < intel.log 
ts      uid     id.resp_h       seen.indicator  seen.indicator_type     sources
1702911422.470607       CXNOS517lUT5M5wBuk      97.107.139.108  97.107.139.108  Intel::ADDR     MISP-1
```

Navigating to the event in the MISP UI for the Tor All Nodes feed shows an increased number of sightings:

![MISP sightings reported by zeekjs-misp](/img/blog/zeekjs-misp-sightings.png "{class='img-responsive'}")



## Conclusion

Zeek's new JavaScript support enables easier integration with external systems.
The zeekjs-misp package allows connecting Zeek with a MISP instance using MISP's extensive REST API.
Note that the zeekjs-misp package is currently meant as a tech demo. The author of the package isn't a MISP
user and deploying it in a production environment may come with further requirements.

Feedback and contributions on GitHub are more than welcome.
Also, feel free to reach out in the [Zeek Slack's package channel](https://zeek.org/slack).
