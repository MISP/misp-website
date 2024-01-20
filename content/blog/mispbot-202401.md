---
title: MISPbot
date: 2024-01-20
layout: post
authors:
- Koen Van Impe
tags: ["bot", "automation", "mastodon", "twitter"]
categories: []
banner: /img/blog/mispbot-img.png
---

# MISPbot

## What is MISPbot?

The MISPbot is a simple tool to allow users to interact with MISP via Mastodon or Twitter.

There are multiple ways to interact with MISP but one approach that was missing is via a *bot*. The [MISPbot](https://github.com/cudeso/mispbot) does just that. It allows users to query MISP, report sightings via a chat bot or request an enrichment. Currently it is implemented for Mastodon (and template code for Twitter is included), but it can easily be extended to Teams, Slack, Mastodon or other platforms.

To avoid confusion, there's no AI or LLM involved. You send basic instructions to the bot (**query** : lookup an indicator in MISP and reply with the events and context details and **sighting** : report a sighting, **help**: return the available commands) and it will reply back.

You can use the *demo* bot or use the MISPbot on your own instance. Do not forget to honour [TLP](https://www.first.org/tlp/) when exposing your data via the bot, something you can achieve with `misp_config["tags"]`.

## Private bot

A private bot can be beneficial in a corporate environment:

- Allow users to **query** an indicator via Teams or Mastodon without having access to MISP;
- **Report** the occurrence of an indicator without forcing users to use a new tool (most users already have access to a corporate chat application);
- Provide ways to do **enrichment** of an indicator via a chat tool, by relying on the MISP infrastructure.

## Demo bot

A demo of the MISPbot is available via [https://infosec.exchange/@mispbot](https://infosec.exchange/@mispbot). This bot uses a MISP server using a large set of [MISP OSINT feeds](https://www.misp-project.org/feeds/). The bot is configured to
- Only reply to the **query** command, the **sightings** command is ignored
- Query the pending notifications every 15 minutes
- A maximum of **50 requests** per 15 minutes (for all accounts)
- A maximum of **20 hits** per reply

Please be gentle with your requests.

![mispbot-conv.png](/img/blog/mispbot-conv.png)

## Twitter

The bot contains template code for Twitter. Unfortunately for Twitter you need a **paid** (Basic) [account](https://help.twitter.com/en/using-x/x-premium-faq) to get the notifications for your account. If you want to sponsor the demo bot account I'm happy to enable the functionality.

# Setup

## Requirements

- A MISP URL and MISP API key with read permissions
- A Python virtual environment with Python libraries
- A Mastodon (or Twitter) account
- The mispbot code

## Install

1. Install the **Python virtual environment** and requirements

```
python -m venv venv
source venv/bin/activate
pip install Mastodon.py tweepy pymisp
```

2. Get the Mastodon access token.

- Go to Account preferences
- **Development** (most often in the left menu, one of the last options)
- Add a **New application**
- Get the **Access Token**

3. Clone the repository and finish the configuration

```
git clone https://github.com/cudeso/mispbot
cp config.template.py config.py
vi config.py
```

Edit `config.py`

```
mastodon_config = {
    "access_token": "",
    "api_base_url": "https://mastodon.social/",
    "username": "",
    "max_mentions": 50,
    "visibility": "public",
    "textcharlimit": 500,
}

misp_config = {
    "url": "",
    "verifycert": False,
    "key": "",
    "to_ids": None,
    "tags": ["tlp:white"],
    "published": True,
    "limit": 20,
    "warninglist": False,
    "info_max_length": 30,
}

log_file = "/var/log/misp/mispbot.log"

bot_command = {
    "query": "query",
    "sighting": "sighting"
}
```

Add the bot to a cron job to query for notifications every 15 minutes.

```
*/15 * * * * /data/mispbot/venv/bin/python mispbot.py >/dev/null 2>&1
```

## Configuration

The configuration is fairly straightforward in `config.py`. Things to consider are

- Mastodon
  - `visibility`: the visibility status of replies
  - `textcharlimit`: the maximum length of a post, depends on your Mastodon server
  - `username`: the full username, including the Mastodon server where your account is hosted
- MISP
  - `to_ids`: Only consider attributes that have to_ids to True
  - `tags`: Required tags for a query
  - `info_max_length`: Trim the event title
