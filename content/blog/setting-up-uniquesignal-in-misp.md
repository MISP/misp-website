---
title: Setting up UniqueSignal in MISP
date: 2026-03-17
layout: post
authors:
- Koen Van Impe
tags: ["vmray", "automation", "feed", "indicators"]
categories: []
banner: /img/blog/vmray_uniquesignal_banner.png
---

**Note**: This post also appeared on the VMRay website: [Setting up UniqueSignal in MISP](https://www.vmray.com/setting-up-uniquesignal-in-misp/).

# VMRay UniqueSignal

Last year VMRay announced **[UniqueSignal](https://www.vmray.com/introducing-uniquesignal-by-vmray/)**, a threat intelligence feed that includes:

* **Indicators of Compromise** (IOCs) such as IPs, URLs and hashes
* **Tactics, Techniques, and Procedures** (TTPs) mapped to **MITRE ATT&CK®**
* **Malware family context** that helps you track how threats evolve over time

What sets this feed apart is its context and relevancy. Rather than simply dumping raw indicators, VMRay provides background drawn from their malware analysis, phishing detection research, and notably their sandbox solutions. This enables you to move quickly from ingestion to action without needing to validate and enrich indicators yourself.

UniqueSignal is available in **STIX, JSON, and CSV**, and it integrates nicely with [**MISP**](https://www.misp-project.org/).

# MISP

**MISP** is an open source, community-driven platform for threat intelligence sharing.

It supports you through the **intelligence lifecycle**: collect raw indicators and events, review and enrich the data, add context, and turn it into actionable intelligence. Once you've curated what matters, you can operationalise it, whether that's feeding Microsoft Defender and Sentinel or something as simple as updating firewall block lists.

Getting data into MISP is easy. You can synchronise with [MISP communities](https://www.misp-project.org/communities/), create your own events, or consume data **feeds**. VMRay's UniqueSignal is available as one of those feeds, so you can add the intelligence from VMRay into your central intelligence repository and use it alongside other collection sources.

## Adding VMRay UniqueSignal as a MISP feed

The diagram below shows the complete workflow for setting up the VMRay UniqueSignal feed in MISP, from initial configuration through to having an active feed pulling in threat intelligence.

![VMRay-UniqueSignal-MISP_new_misp.png](/img/blog/vmray_VMRay-UniqueSignal-MISP_new_misp.png)

### 1. Adding a new feed

You'll find MISP feeds under **Sync Actions > Feeds**. Click on **Add Feed**. 

### 2. Different feed types

There are two ways to use a feed:
- As a **lookup** feed ("Lookup visible"), where events are created on your MISP instance. This is what you want if you plan to work with the information directly.
- As a **cached** feed ("Caching enabled"), mainly used for correlation and validation. The data is stored in a cache but no local events are created. You'd typically use this for high-volume feeds with a relatively short life span.

You can enable both if needed, but we'll use the lookup option for VMRay. There are a few additional settings worth mentioning, like **disable correlation**. You'd typically use that for a high-volume, high-noise feed where correlation on low-value indicators isn't useful. With VMRay, we want correlation enabled so we can link UniqueSignal information to our other sources and build a fuller picture of the threat landscape.

### 3. Basic configuration

Set these basic configuration options:

* **Name**: "VMRay UniqueSignal"
* **Provider**: "VMRay"
* **Input source**: Network (the feed is hosted externally)
* **Source format**: MISP feed
* **URL**: `https://cti-api.vmray.com/v1/misp/`

![add_misp_feed_1_2_3_small.png](/img/blog/vmray_add_misp_feed_1_2_3_small.png)

### 4. Authentication headers

You'll also need to configure **authentication headers**. These identify your MISP node and organisation, and grant you access to the VMRay feed. There are three headers:

- **x-file-format** specifies the MISP export format. You can choose between `MISPFEEDEXTENDED` and `MISPFEEDBASIC`.
- **x-device-id** is a device ID you choose yourself. Ideally, pick the MISP node name or the node UUID (`MISP.uuid`) to make your requests easily recognisable. 
- **x-api-key** is the authentication key VMRay gives you.

A sample format is below, make sure to replace `VMRAY_API_KEY` and `MISP.UUID` with the real values.

```
x-api-key:VMRAY_API_KEY
x-file-format:mispfeedextended
x-device-id:MISP.UUID
```

### 5. Distribution and tagging

A few additional settings aren't strictly required but worth configuring. 

First, set the **distribution level**. In most cases, you won't want to share VMRay events with external communities, so "Your organisation only" makes sense.

You can also apply default tags to events created by the feed. This makes filtering and curation easier. For instance, you might use a single tag like `curation:source="MISP-FEEDS"`, or be more specific with a tag collection containing `curation:source=MISP-FEEDS`, `curation:community=VMRay`, and `admiralty-scale:source-reliability="a"`. 

For reference, that last tag is from the **Admiralty Scale** (sometimes called the NATO System) taxonomy, which ranks source reliability and information credibility. The "a" rating means the source is completely reliable, reflecting our confidence in VMRay. Tags also give you finer control over sharing. The distribution level sets the baseline, but tags let you add specific rules. For example, in your MISP remote server options, you could block all events tagged with `curation:community=VMRay` from ever leaving your organisation. These custom tags will also come in handy when we set up monitoring.

![add_misp_feed_4_5_6_small.png](/img/blog/vmray_add_misp_feed_4_5_6_small.png)

### 6. Enable and submit

Once you've configured everything, make sure the **Enabled** checkbox (at the top of the form) is ticked so the feed is active on your system. 

Then click **Submit** to save the feed. MISP will assign the feed an ID. Make a note of it, you'll need it later.

### 7. Test connection

Before you go further, click the magnifying glass next to the feed to preview what's available. This also checks whether any network filters or gateway devices are blocking access to VMRay, and confirms that you've entered the API key correctly. If you do hit proxy issues, ask your network team to allowlist HTTPS access to `cti-api.vmray.com`.

![explore_events_small.png](/img/blog/vmray_explore_events_small.png)

### 8. Scheduled task

Now set up a scheduled task to pull in the feed regularly. MISP gives you two options: use its built-in task scheduler, or use the Linux cron daemon with the MISP CLI. Both work well. Cron has a proven track record, but the built-in scheduler is easier and doesn't need console access.

**Using the built-in scheduler:**

Go to **Administration > Scheduled tasks**. 

Set the schedule type to **Feed**, the action to **Fetch**, and select **VMRay UniqueSignal** from the feed dropdown. For the polling frequency, set **Runs every** to 1 and **Period** to "Every day" (VMRay updates the feed once a day). Add a description like "Daily pull of VMRay UniqueSignal feed" and enable the schedule.

![scheduled_task_small.png](/img/blog/vmray_scheduled_task_small.png)

**Using cron:**

Add a crontab entry to the `www-data` user (or `apache` on Red Hat systems) in the format:

```
00 3 * * * /var/www/MISP/app/Console/cake Server fetchFeed <user_id> <feed_id>
```

Make sure to replace `<user_id>` with the user ID you want to run the fetch (typically your system services account), and `<feed_id>` with the ID you noted earlier.

## Finishing tasks

Once you've added the feed, it's just a matter of time before the VMRay events start flowing in.

### VMRay MISP organisation

In MISP, each event has two types of organisations: the organisation that created the threat event ("Creator org") and the organisation that owns the event ("Owner org"). The owner is typically the organisation running the MISP instance, which in this case is your organisation. The creator is VMRay.

Once events start flowing in, you'll notice a new remote organisation appears in your MISP instance: VMRay, with the organisation UUID `73374ca8-55c7-4f6e-ac2f-395d49317fea`. This doesn't mean VMRay can log in to your server. The organisation entry is there to maintain database integrity. You can also use this organisation identifier when setting up monitoring and dashboards later.

### Verifying the logs

If all goes well, events should start appearing in your system. If they don't, here's what to check:

- **Can you browse the feed remotely?** If not, your network route or authentication headers need fixing. Sort this out first.
- **Is the scheduled task enabled?** Double-check it's active.
- **Are there feed jobs in the queue?** Look under **Administration > Jobs** to see if fetch jobs appear.
- **Is task scheduling working?** Verify there's at least one MISP scheduler worker running. Check under **Administration > Server Settings & Maintenance**, then the **Workers** tab.
- **Using cron?** Try running the fetch command directly via the MISP CLI as the `www-data` user: `sudo -u www-data /var/www/MISP/app/Console/cake Server fetchFeed 1 2` (replace 1 with your user ID and 2 with your feed ID) and check the output.

The logs from the task scheduler, as well as the standard MISP error logs (under Logs, Application Logs) can also help you find the root cause of ingestion problems.

![task_schedule_log_small.png](/img/blog/vmray_task_schedule_log_small.png)

### Monitoring dashboard

Beyond checking logs, you can track feed activity through MISP dashboards. Widgets let you monitor trends for specific tags or organisation activity, which is perfect for keeping an eye on the VMRay feed.

Remember those tags we set up earlier? They're useful here too. Go to **Dashboards** and click **Add Widget** in the left menu. 

**Trending Tags widget:**

Select "Trending Tags" and use this configuration to filter for VMRay events:

```json
{
    "alias": "VMRay feed",
    "filter": {
        "filter_event_tags": "curation:community=\"vmray\""
    }
}
```

If you're pulling from multiple communities, you can broaden the filter to `curation:community` to see all your community sources.

**Usage data widget:**

Add the "Usage data" widget with this filter to track VMRay feed usage:

```json
{
    "alias": "VMRay usage data",
    "filter": {
        "uuid": "73374ca8-55c7-4f6e-ac2f-395d49317fea"
    }
}
```

This filters by the VMRay organisation UUID.

**Event stream widget:**

Finally, add an "Event stream" widget to see a live view of incoming VMRay events:

```json
{
    "alias": "VMRay event stream",
    "filter": {
        "orgs": "vmray"
    }
}
```

![misp_dashboard_small.png](/img/blog/vmray_misp_dashboard_small.png)

# What's next?

We've covered how to set up the VMRay UniqueSignal feed in MISP.

Next, we'll look at using UniqueSignal operationally for detection and response. We'll cover integrations with **Microsoft Defender** and Microsoft Sentinel, and build custom **MISP workflows** to push selected indicators with analyst notes into detections and hunting queries.

# New MISP visual identity

Have you noticed the **new MISP logo** in the banner/flowchart diagram?

The new logo reflects MISP's identity as a **mature, reliable, and central platform** in the Threat Intelligence ecosystem. Did you also spot the octopus? It represents MISP's ability to aggregate data from multiple sources and orchestrate multi-directional analysis across diverse intelligence feeds.