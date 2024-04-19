---
title: Using your MISP IoCs in Kunai (the open source EDR for Linux) 
date: 2024-04-19
layout: post
tags: ["edr", "kunai"]
#banner: /img/blog/poppy/2.png
---

# Using your MISP IoCs in Kunai

[Kunai](https://github.com/kunai-project/kunai) is an **open-source** security monitoring tool, specifically designed to address the threat-hunting and threat-detection problematic on **Linux**. It has been inspired by [Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon), to provide a Sysmon alike experience to the end user. However, it comes with some more advanced features such as fine grained event filtering, detection rules and IoC matching. In this blog post, we are going to introduce how to implement real time **MISP IoC** matching in a very short amount of time.

## Warm up

The first step to do  is to get familiar with the kind of events **Kunai** is be able to monitor on your system. So please, take a quick read over the [events documentation](https://why.kunai.rocks/docs/category/kunai---events), in order to better understand the following steps. Additionally, the reader may want to get familiar with the documentation explaining how to use the tool for [threat detection purposes](https://why.kunai.rocks/docs/advanced/).

For those not having the time to go through the whole documentation, nothing beats a good example. So below one can find the example of an `execve_script` event generated **for every** script being executed on a system running **Kunai**.

```json
{
  "data": {
    "ancestors": "/usr/lib/systemd/systemd|/usr/bin/login|/usr/bin/zsh|/usr/bin/bash|/usr/bin/xinit|/usr/bin/i3|/usr/bin/bash|/usr/bin/urxvt|/usr/bin/zsh|/usr/bin/bash",
    "parent_exe": "/usr/bin/bash",
    "command_line": "/bin/bash /tmp/tmp.msdKnvj7ax_kunai_test.sh",
    "exe": {
      "file": "/tmp/tmp.msdKnvj7ax_kunai_test.sh",
      "md5": "64b8185d28042ea96feb251e12fe632b",
      "sha1": "31683c67b020d90f02a42e43e7758184ef98c12f",
      "sha256": "cda81b42b75647daf6b70a626380c199fe665d721e63bfe34c96b65da0289627",
      "sha512": "63165b902db5242a01296b39c1d6f2995fde961e29d9470d1862ccde8e2c8a3083659bf5d9c0794bbca620f37c419baec3c1d1941333d37fb9ced795553d2e83",
      "size": 21
    },
    "interpreter": {
      "file": "/usr/bin/bash",
      "md5": "e742da46d05de5afca58a2abcba5343e",
      "sha1": "8d48bdcb10eb85a0bd80c34e13fc01c2f6776043",
      "sha256": "664428e8dd065099a20cb364bdc293dd8f787ef10b9454b64e127a197950a5d6",
      "sha512": "b4e6f555571636f02704271d3a40b8470d04447ca3aaad073818f4041d944533bfbca0d5586dc945a2de8033f8fd4123f4203219e9c7b97ebbc52acd340e598f",
      "size": 1112880
    }
  },
  "info": {
    "host": "...",
    "event": {
      "source": "kunai",
      "id": 2,
      "name": "execve_script",
      "uuid": "520487fc-020c-5569-ed88-38393e49a2d2",
      "batch": 32
    },
    "task": "...",
    "parent_task": "...",
    "utc_time": "2024-02-13T08:34:29.312127521Z"
  }
}
```

As you can see, every **Kunai** event is composed of fields of various types. Some of these types can directly be matched against **IoCs**, following this correspondence table:

|     Kunai data types      | cover IoC type |
| :-----------------------: | :------------: |
|           path            | absolute path  |
| md5, sha1, sha256, sha512 |      hash      |
|       domain / fqdn       | domain / fqdn  |
|        IP address         |  IPv4 / IPv6   |


So any field of a **any Kunai event** having a type in the above table will be checked against the **IoCs** loaded in the tool. Now the only thing we have to do is to feed **Kunai** with data in the expected **IoC** format. The format is pretty basic, yet flexible - the tool simply expects a file containing **JSON** documents. One can find an example file below:

```json
{"uuid": "81050c82-68a5-4130-a56d-a465c8337066", "source":"My MISP Instance", "value":"why.kunai.rocks"}
{"uuid": "dd19ecd1-8237-427a-9b1d-35ff7d17381f", "source":"My MISP Instance", "value":"kunai.rocks"}
```

The format is simple enough to accommodate any **IoC** feed and is easily scriptable. So one could even imagine the creation of such a file from an IP list found on the Internet.

Now, the reader should have a good picture of the topic and we can walk through a small experiment to get a bit more familiar with **Kunai** and its **IoC** matching capabilities.

## A Little Experiment

Let's run **Kunai** without any arguments, merely taking care of redirecting its output:

```bash
sudo kunai | tee /tmp/kunai.log
# if one has jq installed one can pipe kunai output to jq
# in order to get a prettier output
sudo kunai | jq '.' | tee /tmp/kunai.log
```

You should start seeing some events printed on the terminal. You can try generating some more activity by leaving **Kunai** to run in a corner and use your system as you are used to. You can then stop it using `Ctrl + c`. 

If you inspect the logs in `/tmp/kunai.log`, you will most likely find a wealth of useful information, especially if you have security monitoring needs. However, you may also come to the conclusion that there is simply too much useless information for your specific needs. So one can use [filtering / detection rules](https://why.kunai.rocks/docs/advanced/rule_configuration) to be very selective of the events (out of scope for this post) or use **IoC** matching, to only display events matching an **IoC**. So lets do the exact same experiment as previously, but taking a file containing **IoCs** as parameter.

The first thing you need to do is to copy the following content into a file, let's say `/tmp/kunai-iocs.json`:

```json
{"uuid": "81050c82-68a5-4130-a56d-a465c8337066", "source":"My MISP Instance", "value":"why.kunai.rocks"}
{"uuid": "dd19ecd1-8237-427a-9b1d-35ff7d17381f", "source":"My MISP Instance", "value":"kunai.rocks"}
```

Once this is done, start **Kunai**, passing this **IoC file** in the command line:

```bash
sudo kunai -i /tmp/kunai-iocs.json
```

And now the magic happens! You won't see logs any longer, but don't worry it is absolutely normal. Under the hood, **Kunai** is analyzing all the events (as the ones you saw in previous experiments) but it will only display the ones matching **IoCs**. So try to generate some network traffic (use `dig`, `curl` ...) towards domain `why.kunai.rocks` and you should see some events popping up on your terminal. If you visit the website with your browser, make sure it **doesn't use DOH** or any **DNS** protocol different from the one running on port **53.**

If you did the experiment and managed to generate an event matching one of the **IoCs** configured, you may have seen that the generated events contains **additional information** about the **matching IoC** in the `.detection` section of the event.

```json
{
  "data": {
    "ancestors": "/usr/lib/systemd/systemd|/usr/bin/login|/usr/bin/zsh|/usr/bin/bash|/usr/bin/xinit|/usr/bin/i3|/usr/bin/bash|/usr/bin/urxvt|/usr/bin/zsh",
    "command_line": "dig why.kunai.rocks",
    "exe": {
      "file": "/usr/bin/dig"
    },
    "query": "why.kunai.rocks",
    "proto": "udp",
    "response": "kunai-project.github.io",
    "dns_server": {
      "ip": "10.96.0.1",
      "port": 53,
      "public": false,
      "is_v6": false
    }
  },
  "detection": {
    "iocs": [
      "why.kunai.rocks"
    ],
    "severity": 10
  },
  "info": {
    "host": "...",
    "event": {
      "source": "kunai",
      "id": 61,
      "name": "dns_query",
      "uuid": "7cf3a92b-b8fd-9035-4ced-8ca216adbf32",
      "batch": 38
    },
    "task": "...",
    "parent_task": "...",
    "utc_time": "2024-04-18T09:34:31.887637287Z"
  }
}
```

In the above example, we see only one **IoC** under the `detection` section, however if several **IoCs** would match an event, all of them would be in the list. Things should be a bit more concrete for you now, so lets dive into how to automatically ingest **MISP IoCs** into **Kunai**.

## Getting MISP IoCs into Kunai

The only thing which is missing, in order to configure **Kunai** from a **MISP instance**, is a way to  extract **IoCs** and translate them into the expected format. If you have already played with [PyMISP](https://github.com/MISP/PyMISP), this is not something that should be too scary and if you have not, here is the good news: we have a script which does it for you.  You can find the script in question over at the [Kunai tools repository](https://github.com/kunai-project/tools) under the [misp](https://github.com/kunai-project/tools/tree/main/misp) directory. 

Before going further, make sure you have all the modules required (check out [requirements.txt](https://github.com/kunai-project/tools/blob/main/requirements.txt) at repository root) by Python so that this script works. 

The next step is to create a configuration file for the script, simply rename the example configuration into `config.toml` and edit it so that it contains the settings to connect to the desired **MISP** instance.

If you have fulfilled the previous steps, you can simply run the `misp-to-kunai.py` script and you should see your **MISP's attributes**  translated into **Kunai IoC format** flowing in your terminal. This script has some options to be more selective on the **IoC**s to pull, however we will not go through all of them and will let the reader explore them. The only option we will use is the `-o` to write **IoC**s into a file. We encourage you to use the `-o` option to write into a file rather than doing a pure shell redirect as **this option prevents IoC duplication**.

If you take a look at the output generated by `misp-to-kunai.py` you may have noticed that **IoCs** are not exactly in the same format as the one described previously. Indeed, those contain an additional field - it being the `event_uuid` field -, which encodes the **MISP Event UUID** that the **IoC** belongs to. Any additional field to the ones described above, is ignored by **Kunai**, making the **IoC** format fairly flexible. Thanks to this you can add as many fields as you want, for instance to bring contextual information along with the **IoC**. We thought this one would be useful to enrich the **IoC** file with additional context, in case you would wish to correlate back to a **MISP Event**.

It is now time to put everything together:

```bash
# pull IoCs from MISP and store them in Kunai IoC format
./misp-to-kunai.py -o /tmp/kunai-misp-iocs.json

# run Kunai and check all events happening on your
# system against MISP IoCs
sudo kunai -i /tmp/kunai-misp-iocs.json
```

As seen in the previous experiment, you should not see any event coming out of **Kunai** until one actually matches an **IoC** you've just loaded. The easiest way to try and see if everything works as expected is to execute a `dig` command against a domain from the **IoC** list.

Yes, you went though this entire blog post just to end up typing two simple lines into a shell, but now you understand why you typed those and how all this works.

## Final Words

This post aimed at being dense and straightforward, mostly to prevent you from giving up. However, if you would like to go further with the topic, we encourage you to dive into [Kunai's documentation](https://why.kunai.rocks/docs/quickstart). On the Python script side, there are also some interesting options deserving exploration, especially if you are interested in turning it into a service.

All the tools presented here are **open-source**, so feel free to read the code, modify it and contribute to it even in the form of feedback or GitHub issues. This is how we can keep improving our projects and better fit the users' needs.

We hope you learned useful things or at least that you enjoyed reading this article.

## References

[Kunai project on GitHub](https://github.com/kunai-project/)
[Kunai documentation](https://why.kunai.rocks/docs/quickstart)
[Kunai tools](https://github.com/kunai-project/tools)
[PyMISP](https://github.com/MISP/PyMISP)


## Acknowledgement 

The [Kunai open source project](https://github.com/kunai-project/kunai) is developed in the scope of the NGSOTI project and co-funded under Digital Europe Programme by the ECCC (European Cybersecurity Competence Centre and Network).

The NGSOTI project is dedicated to training the next generation of Security Operation Center (SOC) operators, focusing on the human aspect of cybersecurity. It underscores the significance of providing SOC operators with the necessary skills and open-source tools to address challenges such as detection engineering, incident response, and threat intelligence analysis. Involving key partners such as CIRCL, Restena, Tenzir, and the University of Luxembourg, the project aims to establish a real operational infrastructure for practical training. This initiative integrates academic curricula with industry insights, offering hands-on experience in cyber ranges.
