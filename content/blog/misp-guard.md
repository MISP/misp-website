---
title: MISP Guard
banner: /img/blog/misp-guard-architecture.png
date: 2022-09-13
layout: post
---

Let's say that by no means should an attribute of type `passport-number` leave your MISP instance. Aside from the analyst following best practices when encoding the data, MISP does not have a built-in mechanism to prevent these leaks to happen, but now you can achieve this by using a third-party tool called [misp-guard](https://github.com/MISP/misp-guard/).

[misp-guard](https://github.com/MISP/misp-guard/) is a [mitmproxy](https://mitmproxy.org/) addon that inspects and blocks outgoing events to external MISP instances via sync mechanisms (PULL/PUSH) based on a set of customizable block rules.

For the example above, the block rules would look like this:
```json
{
    "block_rules": [
        {
            "id": "no-passports",
            "description": "Block passport numbers",
            "blocked_attribute_types": [
                "passport-number"
            ]
        }
    ]
}
```

## How it works
### External PULL
From the point of view an External MISP that tries to pull from your instance, MISP Guard acts as a reverse proxy that inspects the external requests and allows only the ones strictly required for server syncronization, it then forwards the requests to your MISP instance and inspects the content of the outgoing events. If any of the block rules matches, the event is droped and never leaves your premises.
External MISP servers will create the connections to MISP Guard host, not your Internal MISP instance.

### Internal PUSH
From the point of view of your Internal MISP instance, you must configure MISP to use MISP Guard as a proxy (`Proxy.host` and `Proxy.port` settings).
When the Internal MISP instance tries to push an event, MISP Guard inspects the content and if any of the block rules matches, the event is droped.

> NOTE: By default this addon will block all outgoing HTTP requests that are not required during a MISP server sync. All rejected/blocked requests are logged.

For a more detailed explanation check [misp-guard README](https://github.com/righel/misp-guard/blob/main/README.md)

## Block Rules

* `blocked_tags`: Blocks if the event/attributes contains certain tags.
* `blocked_distribution_levels`: Blocks if the event/objects/attributes matches one of the blocked distribution levels.
  * `"0"`: Organisation Only
  * `"1"`: Community Only
  * `"2"`: Connected Communities
  * `"3"`: All Communities
  * `"4"`: Sharing Group
  * `"5"`: Inherit Event
* `blocked_sharing_groups_uuids`: Blocks if the event/objects/attributes matches one of the blocked sharing groups uuids.
* `blocked_attribute_types`: Blocks if the event contains an attribute matching one of this types.
* `blocked_attribute_categories`: Blocks if the event contains an attribute matching one of this categories.
* `blocked_object_types`: Blocks if the event contains an object matching one of this types.

See sample config [here](https://github.com/MISP/misp-guard/blob/main/src/test/test_config.json).

## Installation
```console
$ git clone https://github.com/MISP/misp-guard.git
$ cd src/
$ pip install -r requirements.txt
```

### Setup
1. Define your block rules in the `config.json` file.
2. Start mitmproxy with the `mispguard` addon:
    ```console
    $ mitmdump -s mispguard.py -p 8888 --set config=config.json
    Loading script mispguard.py
    MispGuard initialized
    running block rules: no-tlp-red-events
    Proxy server listening at *:8888
    ``` 
    * _Add **`-k`** to accept self-signed certificates._
    * _Add **`--certs *=your-cert.pem`** to specify a leaf certificate_

3. Configure the proxy in your MISP instance, set the following MISP  `Proxy.host` and `Proxy.port` settings accordingly.

Done, outgoing MISP sync requests will be inspected and dropped according to the specified block rules.

> NOTE: add **`-v`** to increase verbosity and display debug logs.

#### Running `mitmdump` as a Service
Ideally you want to run `mitmdump` as reliably as posible, you can use [Supervisor](http://supervisord.org/) to configure it as a service.

Sample `supervisord` program configuration:
```
[program:misp-guard]
directory=/home/user/misp-guard/src
user=your-user
command=python3 /home/user/.local/bin/mitmdump -s mispguard.py -p 8888 --certs *=your-cert.pem --set config=config.json
autostart=true
autorestart=true
redirect_stderr=false
stderr_logfile=/var/log/misp-guard-error.log
stdout_logfile=/var/log/misp-guard.log
```


