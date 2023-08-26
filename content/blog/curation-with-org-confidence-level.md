---
title: Curate events with an organisation confidence level
date: 2022-11-14
layout: post
authors:
- Koen Van Impe
tags: ["curation"]
categories: []
---

## Quality of threat intelligence

When you receive threat intelligence from different sources you quickly realise there is a big difference in the quality of the received information. Where some organisations go to great length to ensure their events are accurate, complete and contextualised, other organisations use different standards. Some of these differences are caused by particular use cases but can also be caused by human errors or maturity growing pains. Regardless of what's causing these differences, as a consumer, it costs time to wade through events and manually [curate](https://www.first.org/resources/papers/conf2022/FIRST_In-Curation-We-Trust.pdf) them. 

What if I told you that you could save yourself some time by *automatically* classifying events based on the level of trust that you have in contributing organisations? You can then decide that for example indicators from 'trusted' sources are immediately pushed to a detection platform, or synced with your other MISP servers. This trust can be expressed by **your judgement** on the **reliability** and **credibility** of an organisation. And although [MISP Workflows](https://www.misp-project.org/2022/08/08/MISP.2.4.160.released.html/) already get you far in automating a curation process, assigning such a confidence level via the workflow module is currently not immediately possible (see the Notes-section at the end). But there are ways to get around this. 

## Warninglists in support to curate events

In this post I describe how to use warninglists to store a list of trusted organisations and then automatically tag events with a confidence level when events from these organisations are published on the MISP ZeroMQ.

What are the components that we need to build such a solution?

### Warninglist as lookup lists

One of the well-known input filters in MISP are [warninglists](https://github.com/MISP/misp-warninglists). Next to using warninglists as an indication of potential false-positives, you can also use them as lookup lists, verify if a value exists and then have a **follow-up action**. Such an action can for example be the tagging of an event with the [admiralty-scale](https://www.misp-project.org/taxonomies.html#_admiralty_scale). This Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information and is available as a MISP **taxonomy**. 

![Workflow](/img/blog/curation-confidence-level/tags.png)

### ZeroMQ

We also need notifications if new events are received on our MISP server. This can be done by subscribing to [ZeroMQ](https://www.circl.lu/doc/misp/misp-zmq/), a publish-subscribe model that allows real-time integration on MISP activities, such as event manipulations.

### PyMISP

And finally, we need PyMISP to tie everything together.

## Workflow

Now that we know which components are used it's time to look at the workflow. Our script will

1. **Subscribe** to ZeroMQ and pick up queue messages;
2. Do curation if the message concerns an **event from a connected server**, basically it means we received an event via MISP server synchronisation;
3. Get the **warninglists** with the 'trusted' organisations;
4. Query these lists for **matches** with the UUID of the organisation that created the event;
5. - If a match is found, the event is **tagged** with a corresponding Admiralty Scale value;
6. - And depending on the level of trust (typically only for high), the event is **published**.

![Workflow](/img/blog/curation-confidence-level/confidence_level.drawio.png)

## Setup

### Warninglists

First we need to add the warninglists that will hold the UUIDs of the organisations. This can be done under **Input Filters**, **Warninglists** and then **Add Warninglist**.
- Give the warninglist the name `org-confidence-level-high` or `org-confidence-level-medium`;
- Set the type to **string**;
- Set the category to **Known identifier**;
- Add at least one organisation UUID in the **Values** text box and prepend each value with `org_uuid:`;
- Add a comment to describe the organisations'name that correspond with the added UUID. Comment lines have to start with #.

![Workflow](/img/blog/curation-confidence-level/warninglist_1.png)

Once you saved the warninglist, you need to **enable** it by clicking on the "play" button.

![Workflow](/img/blog/curation-confidence-level/warninglist_2.png)

### ZeroMQ

The ZeroMQ configuration is under **Administration**, **Server Settings & Maintenance**, **Plugin** and then **ZeroMQ**. Enable the plugin (`Plugin.ZeroMQ_enable`) and the event notifications (`Plugin.ZeroMQ_event_notifications_enable`). You can enable other queue notifications as well but we will not be using those for the moment.

![Workflow](/img/blog/curation-confidence-level/zeromq_1.png)

### PyMISP

PyMISP is best setup in a Python virtual environment.

```
virtualenv venv
source venv/bin/activate
pip install pymisp
```

PyMISP requires an API key to be functional. If you don't have a key you can create one via **Global Actions**, **My Profile**, **Auth keys**. Then add this key, together with the MISP url, in a `keys.py`.

```
misp_url = "MISP_URL"
misp_key = "API_KEY"
misp_verifycert = False
```

### Curation with org confidence level script

Now that we prepared all components, it's time to introduce the **Python script** that handles the bulk of the work. The script is at the end of this post and can be started from the Python virtual environment.

```
/home/misp/venv/bin/python curation_confidence.py
```

The output of its actions are logged to `/tmp/zmq_output.log` (you can easily change the location).

```
2022-11-10 21:52:21,232 - zmq - DEBUG - Connect to ZMQ
2022-11-10 21:55:38,556 - zmq - DEBUG - Event 7f13bc13-74db-4034-adff-cb7c63f2e998
2022-11-10 21:55:38,810 - zmq - DEBUG - Tag with admiralty-scale:source-reliability="a"
2022-11-10 21:55:39,017 - zmq - DEBUG - Publish
2022-11-10 21:55:45,305 - zmq - DEBUG - Event c3055626-2955-4c73-a0d7-4c3dd053b408
```

To test the well-functioning of the curation you can manually force synchronisation with other servers. As you probably know this can be done with **cake** (the below example does the synchronisation as user id 1, for server id 1).

```
sudo -H -u www-data /var/www/MISP/app/Console/cake Server pull 1 1
```

Once new events are coming in, you should see additional entries in the log file.

### Notes

- MISP can also immediately **block** all events coming from specific organisations. This is done under **Administration**, **Blocklist Organisation**;
- The **order** of the warninglists in the config setting `confidence_mapping` **matters**. First list the 'high' trust and then the 'medium' trust;
- The workflow state is changed from 'incomplete' to 'complete' for 'high' trusted organisations;
- Only events from 'high' trusted organisations (those on the list `org-confidence-level-high`) are published. Events from 'medium' trusted organisations (`org-confidence-level-medium`) are tagged but remain in the unpublished state;
- If there is no match with the warninglists, then no tagging takes place;
- Do not forget to prepend the UUID with the value set in `confidence_mapping_pretext` (default 'org_uuid:');
- - Technically this prefix is not necessary. But it prevents accidental matches when the UUID would be added to other warninglists;
- The warninglists are not cached. There is a minor performance cost but it also means that changes are immediately visible;
- The **workflow** feature of MISP has a logic module to check for a specific creator organisation (module `organisation-if`) but the input data for this module is a fixed list, not a lookup list. Maybe it's worth to create a feature request for this?

### Troubleshooting

The curation will not work if ZeroMQ is not active. You can check on its status via **Administration**, **Server Settings & Maintenance**, **Diagnostics**. Then scroll down to **ZeroMQ** where you can stop and start ZeroMQ.

![Workflow](/img/blog/curation-confidence-level/zeromq_2.png)

If starting fails you can also attempt to kill the underlying Python process. On the Linux console of your MISP server query for the process with `zmq`. This should return one result. You can then kill that process and restart ZeroMQ from the MISP interace.

```
ps -ef | grep -i zmq
www-data  43560  1  0 Nov10 ?  00:00:06 /var/www/MISP/venv/bin/python /var/www/MISP/app/files/scripts/mispzmq/mispzmq.py
kill 43560
```

## Python script

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import zmq
import time
import json
import logging

# Setup MISP object, subscribe to ZMQ and create a logger object
from pymisp import ExpandedPyMISP, MISPObject, MISPEvent, MISPAttribute, MISPOrganisation, MISPServer, MISPTag
sys.path.insert(1, '/home/misp/venv/')
from keys import misp_url, misp_key, misp_verifycert
if misp_verifycert is False:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://%s:%s" % ("127.0.0.1", 50000))
socket.setsockopt(zmq.SUBSCRIBE, b'')
poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)
misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert, debug=False)

logger = logging.getLogger('zmq')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler("/tmp/zmq_output.log", mode='a')
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)

config = {
    "confidence_mapping": {
            "org-confidence-level-high": "admiralty-scale:source-reliability=\"a\"",
            "org-confidence-level-medium": "admiralty-scale:source-reliability=\"c\""
        },
    "confidence_mapping_pretext": "org_uuid:",
    "auto_publish": ["admiralty-scale:source-reliability=\"a\""]
}

logger.debug("Connect to ZMQ")
while True:
    socks = dict(poller.poll(timeout=None))
    if socket in socks and socks[socket] == zmq.POLLIN:
        message = socket.recv()
        topic, s, m = message.decode('utf-8').partition(" ")        
        
        if topic == 'misp_json_event':
            payload = json.loads(message[len(topic)+1:])
            if payload["action"] == "add_from_connected_server" or payload["action"] == "edit_from_connected_server":
                misp_event = MISPEvent()
                uuid = payload["Event"]                    
                misp_event = misp.get_event(uuid, pythonify=True)
                logger.debug("Event {}".format(uuid))

                # Curation: Add a confidence level for the source organisation
                verify_uuid = "{}{}".format(config["confidence_mapping_pretext"], misp_event.orgc.uuid)
                uuid_in_warninglist = misp.values_in_warninglist(verify_uuid)
                if len(uuid_in_warninglist) > 0:
                    first_match = uuid_in_warninglist[verify_uuid][0]["name"].strip()
                    for el in config["confidence_mapping"]:
                        if first_match == el:
                            misp.tag(uuid, config["confidence_mapping"][el], True)
                            logger.debug("Tag with {}".format(config["confidence_mapping"][el]))
                            # Curation: Auto publish events coming from high confidence sources
                            # Otherwise we just stick to the confidence tag, without publishing
                            if config["confidence_mapping"][el] in config["auto_publish"]:
                                misp.untag(uuid, "workflow:state=\"incomplete\"")
                                misp.tag(uuid, "workflow:state=\"complete\"", True)
                                misp.publish(uuid)
                                logger.debug("Publish")
                            break
        time.sleep(2)
```
