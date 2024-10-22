---
title: MISP ioC retrosearch with misp42 Splunk app.
date: 2024-10-22
layout: post
authors:
- Remi Seguy
tags: ["IOC", "retrosearch", "splunk", "misp42", "integration"]
categories: []
---

## Introduction

Hi, in this blog post I am going to share how I have built a framework on Splunk to retrosearch on [MISP](https://www.misp-project.org/) indicators of compromise.

## Overview

The framework will run a series of scheduled searches to pull the IoC from MISP, search for potential indices, sourcetypes and timestamps in the Splunk TSIDX files (optional) and then searches in every tuple (index,sourcetype) to get the details.  

All results are written to a summary index.

![MISP IoC retrosearch lifecycle](https://github.com/remg427/misp42splunk/blob/master/images/misp42_ioc_retrosearch_lifecycle.png)

## Preparation

### Apps and TAs from [splunkbase](https://splunkbase.splunk.com/)

#### [MISP42]()

First you need to install and configure MISP42 as explained here [Quick Start](./Quick-start)

#### Other apps & TAs

##### [URL Toolbox](https://splunkbase.splunk.com/app/2734)

UTBox is a set of building blocks for Splunk specially created for URL manipulation.

UTBox has been created to be modular, easy to use and easy to deploy in any Splunk environments. It only needs to be deployed on Splunk Search Heads and the bundles will automatically be sent to your Splunk Indexers.

One of the core feature of UTBox is to correctly parse URLs and complicated TLDs (Top Level Domain) using the Mozilla Suffix List. Other functions like shannon entropy, counting, suites, meaning ratio, bayesian analysis, etc, are also available.

### Splunk objects 

The framework uses lookups, macros, a summary index to keep track of findings and some dashboards to review them.

#### Lookups

**LT_100_HUNT_RETRO_STEP_1_MISP_IOC_to_search.csv**  

Create an empty lookup table (CSV)
```
| makeresults
| outputlookup HUNT_LT_100_STEP_1_MISP_IOC_to_search.csv

```
And then create a lookup definition **HUNT_LD_100_MISP_IOC_to_retrosearch** pointing to it.  

**HUNT_KV_201_RETRO_catch_ip**  
Create a KV store with the following fields.
```
field._time = time
field.count = number
field.ctime = time
field.index = string
field.sourcetype = string
```
You could use Splunk App for Lookup File Editing:  

![Create KV store](https://github.com/remg427/misp42splunk/blob/master/images/misp42_ioc_retrosearch_kvstore_creation.png)

and then create a lookup definition **HUNT_LD_201_RETRO_catch_ip** pointing to the KV store HUNT_KV_201_RETRO_catch_ip.  

![Lookup definition](https://github.com/remg427/misp42splunk/blob/master/images/misp42_ioc_retrosearch_lookup_defintion.png)



#### Collecting findings in a dedicated index

The scheduled searches writes the attributes pulled in Step 1 and later used to search for matches in Step 2 and Step 3 to provide a trail for each step. 
Moreover, the findinds on Step 2 and Step 3 are written to allow further processinfg and review via the dashboards.

**Create** an index `misp_hunt_findings` (or any index name of your choice if you adjust the saved searches and dashboards).  

The source strings need to be built in consistent way by step and type of IoCs in order to build dashboards which provides overview and details on the matching IoCs.  

## MISP IoC retrosearch lifecycle
### Step 1 - Pull attributes from MISP

The following scheduled search pulls from the specified MISP instance the attributes of MISP events that have been modified **in the last 25h**. Only attributes created in the last 3d are kept.

**HUNT_101_STEP-1_retrieve_IOC_from_MISP**

```
| mispgetevent misp_instance=misp timestamp=25h limit=1000 warning_list=t not_tags="SOC_DISCARD_EVENT" ```retrieve IOC from sharing misp```
| table * 
| eventstats values(misp_event_uuid) as eventid
| eval misp_instance="misp", limit=1000, page=0, pipesplit="true", expand_object="true", attribute_limit=0, enforceWarninglist="true", includeEventTags="true" 
| eval type=split("domain,domain|ip,hostname,hostname|port,ip-dst,ip-dst|port,ip-src,ip-src|port,uri,url,user-agent,sha256,md5,email-src,email,subject",",") ,
    timestamp="3d" 
| tojson eventid enforceWarninglist includeEventTags, limit, timestamp, type output_field=misp_http_body 
| mispfetch misp_restsearch=attributes not_tags="SOC_DISCARD_EVENT" keep_galaxy=true 
| eval misp_description="https://"+host+"/events/view/"+misp_event_uuid, misp_tag=mvjoin(misp_tag,"▲") ```compute additional fields```
| fields - _raw, host, attribute_limit, eventid, expand_object, getioc, keep_galaxy, last, limit, misp_http_body, misp_org_*, misp_output_mode, misp_restsearch, not_tags, only_to_ids, page, pipesplit, tags, enforceWarninglist
| eventstats values(misp_orgc_name) as misp_orgc_name values(misp_orgc_uuid) as misp_orgc_uuid by misp_orgc_id 
| search misp_domain="*" OR misp_hostname="*" OR misp_ip="*" OR misp_ip_dst="*" OR misp_ip_src="*" OR misp_domain_p_ip="*" 
    OR misp_uri="*" OR misp_url="*" OR misp_user_agent="*" 
    OR misp_md5="*" OR misp_sha256="*" 
    OR misp_email_src="*" OR misp_email="*" OR misp_subject="*" ```remove results with null values``` 
| foreach misp_domain, misp_hostname, misp_ip, misp_ip_dst, misp_ip_src, misp_uri, misp_url, misp_user_agent, misp_md5, misp_sha256, misp_email_src, misp_email, misp_subject 
    [| eval <<FIELD>>=lower('<<FIELD>>')] 
| eval misp_user_agent_length = len(misp_user_agent) ```add time field and user agent length``` 
| eval misp_url=mvappend(misp_url,misp_uri), misp_url=coalesce(misp_url,"null_url_or_uri_value") ```keep only one value in misp_url otherwise store dummy value``` 
| mvexpand misp_url ```Expands the values of a multivalue field into separate events```
| eval misp_url = if(misp_url="null_url_or_uri_value" OR match(misp_url,"\|"), null(), lower(misp_url)) ```lowercase url or store null value if dummy value was present``` 
| eval misp_url=replace(misp_url,"\\\\", "\\\\\\\\") 
| rex mode=sed field=misp_url "s/[\[\]\(\)\{\}\"\']//g" 
| eval misp_domain=mvappend(misp_domain,misp_hostname,additional_URL_domain,additional_URI_domain), misp_domain=coalesce(misp_domain,"null_domain_or_hostname") ```Same kind of processing for domain value``` 
| mvexpand misp_domain ```Expands the values of a multivalue field into separate events``` 
| rex mode=sed field=misp_domain "s/[\[\]\(\)\{\}\"\']//g" ```regex expression to eliminate the following characters ( ) 
    [ ] { } from misp entries ``` 
| eval misp_ip_dst=mvappend(misp_ip,misp_ip_dst,if(`soc_macro_is_ip(misp_domain)`,misp_domain,null())), misp_ip_dst=coalesce(misp_ip_dst,"null_ip") ```ìf misp_domain is an ip will make a multivalue of misp_ip_dst``` 
| mvexpand misp_ip_dst ```Expands the values of a multivalue field into separate events``` 
| rex mode=sed field=misp_ip_dst "s/[\[\]\(\)\{\}\"\']//g" 
| eval misp_ip_dst=case(
    match(misp_ip_dst,"(0\.0\.0\.0|127\.\d+\.\d+\.1)"),null(),
    cidrmatch("10.0.0.0/8", misp_ip_dst) OR cidrmatch("172.16.0.0/12", misp_ip_dst) OR cidrmatch("192.168.0.0/16", misp_ip_dst), null(),
    `soc_macro_is_ip(misp_ip_dst)`, misp_ip_dst,
    1==1,null()) ```clean misp_dst_ip if not an IP or default route or localhost``` 
| eval misp_ip_src=coalesce(misp_ip_src,"null_ip") ```put dummy value for field misp_ip_src if it is null ``` 
| mvexpand misp_ip_src ```Expands the values of a multivalue field into separate events``` 
| rex mode=sed field=misp_ip_src "s/[\[\]\(\)\{\}\"\']//g" 
| eval misp_ip_src=case(
    match(misp_ip_src,"(0\.0\.0\.0|127\.\d+\.\d+\.1)"), null(),
    cidrmatch("10.0.0.0/8", misp_ip_src) OR cidrmatch("172.16.0.0/12", misp_ip_src) OR cidrmatch("192.168.0.0/16", misp_ip_src), null(),
    `soc_macro_is_ip(misp_ip_src)`, misp_ip_src,
    1==1,null()) ```clean misp_src_ip if not an IP or default route or localhost``` 
| eval misp_domain=case(
    misp_domain=="null_domain_or_hostname", null(),
    match(misp_domain,"\.europa\.eu$"), null(),
    `soc_macro_is_ip(misp_domain)`,null(),
    match(misp_domain,"^(DELETE|GET|POST|PUT|HEAD|CONNECT)$"), null(),
    `soc_macro_is_fqdn(misp_domain)`,misp_domain,
    1==1, null() ) ```store lowercase of domain if valid otherwise store null value``` 
| rex mode=sed field=misp_md5 "s/[\[\]\(\)\{\}\"\']//g" 
| rex mode=sed field=misp_sha256 "s/[\[\]\(\)\{\}\"\']//g" 
| rex mode=sed field=misp_email_src "s/[\[\]\(\)\{\}\"\']//g" 
| rex mode=sed field=misp_email "s/[\[\]\(\)\{\}\"\']//g" 
| eval misp_organisation_name = misp_orgc_name 
| rename _time as misp_time 
| eval _time=now() 
| eval misp_value=mvappend(misp_domain, misp_ip_dst, misp_ip_src, misp_url, misp_user_agent, misp_md5, misp_sha256, misp_email_src, misp_email, misp_subject) 
| mvexpand misp_value 
| where isnotnull(misp_value) AND len(misp_value) > 1 
| collect testmode=false index=misp_hunt_findings source="HUNT_101_HUNT_RETRO_LOOKUPGEN_MISP" 
| eval misp_value = if(isnull(already_searched_misp_event_uuid), misp_value, null())
| fillnull value="" misp_domain, misp_ip_dst, misp_ip_src, misp_url, misp_user_agent, misp_md5, misp_sha256 misp_email_src, misp_email, misp_subject 
| eval misp_first_seen = round(if(match(misp_first_seen,"^\d+$"), max(misp_first_seen - 86000*10, relative_time(now(),"-180d")), relative_time(now(),"-180d"))) 
| eval misp_last_seen = round(if(match(misp_last_seen,"^\d+$"), min(misp_last_seen + 86000*10, now()), now())) 
| fields _time, misp_instance, misp_type, misp_value,
    misp_domain, misp_rank, misp_ip_dst, misp_ip_src, 
    misp_url, misp_user_agent, misp_user_agent_length,
    misp_md5, misp_sha256,
    misp_email_src, misp_email, misp_subject,
    misp_description, misp_event_uuid, misp_timestamp, misp_tag, 
    misp_event_info, misp_comment,
    misp_attribute_uuid, misp_first_seen, misp_last_seen
    misp_orgc_id, misp_orgc_name, misp_orgc_uuid 
| stats first(*) as * 
    min(misp_first_seen) as misp_first_seen 
    max(misp_last_seen) as misp_last_seen 
    by misp_value 
| outputlookup override_if_empty=true HUNT_LD_100_MISP_IOC_to_retrosearch
```
### Step 2 - Fast retrosearch on TSIDX files

When the logs are huge, it might be interesting to use a `| tstats` search that is going to inspect only the TSIDX files on Splunk (not checking on the raw logs in the buckets. The splunk command [tstats](https://docs.splunk.com/Documentation/SplunkCloud/latest/SearchReference/Tstats) works only with index-time fields including the metadata index, sourcetype, source, host, _time.  

**TERM()** [TERM](https://docs.splunk.com/Documentation/Splunk/latest/Search/UseCASEandTERMtomatchphrases) is a directive that instructs Splunk SPL to look only on the TSIDX index files. This is very efficient provided you know the format of strings that are indexed into those TSIDX files (you may use `walklex` to have a view on the terms) 

**HUNT_201_STEP-2_CATCH_ALL_MATCHING_IPs**

```
| tstats count 
    min(_time) as et, max(_time) as lt
    where earliest=-180d 
    index=* NOT TERM(nothing_to_search_in_logs) 
    NOT index=notable NOT index="threat_activity" NOT sourcetype="stash" 
    [| makeresults 
    | eval protection_ip="nothing_to_search_in_logs", protection_misp_event_uuid="protection_mechanism" 
    | inputlookup append=t HUNT_LD_100_MISP_IOC_to_retrosearch 
    | search misp_ip_dst="*" OR misp_ip_src="*" OR protection_ip="nothing_to_search_in_logs" 
    | eval ip=mvappend(misp_ip_dst,misp_ip_src,protection_ip), misp_event_uuid=coalesce(misp_event_uuid,protection_misp_event_uuid) 
    | mvexpand ip 
    | where (`soc_macro_is_ip(ip)` OR ip=="nothing_to_search_in_logs") 
    | stats values(*) as * by ip, misp_event_uuid 
    | eval _time=now() 
    | collect testmode=false index=misp_hunt_findings source="HUNT_201_CATCH_ALL_IP_used_as_IOC" 
    | eval search = "TERM(" + ip + ") OR TERM(" + ip + "/32) OR TERM(src=" + ip + ") OR TERM(dst=" + ip + ") OR TERM(" + ip + ":*)" 
    | stats values(search) as search 
    | eval search="(" + mvjoin(search," OR ") + ")"]
    by index, sourcetype, _time span=1d 
| eval time=mvappend(et,lt), time=mvdedup(time) 
| mvexpand time 
| rename time as _time 
| eval ctime=now() 
| outputlookup override_if_empty=true HUNT_LD_201_RETRO_catch_ip 
| eval timestamp = _time 
| eval _time=now() 
| collect testmode=false index=misp_hunt_findings source="HUNT_201_CATCH_ALL_IP_index_sourcetype_time" 
| stats sum(count) as total_match count
```
The key point is on this line (see [Behind the Magnifying Glass: How Search Works](https://conf.splunk.com/files/2016/slides/behind-the-magnifying-glass-how-search-works.pdf)
```
| eval search = "TERM(" + ip + ") OR TERM(" + ip + "/32) OR TERM(src=" + ip + ") OR TERM(dst=" + ip + ") OR TERM(" + ip + ":*)" 
```
- `TERM(1.2.3.4)` works well when an IP address is delimited by **major** breakers (space, quotes) for example for JSON log records.
- `TERM(1.2.3.4/32)` works on some AWS logs having a /32 added.
- `TERM(src=1.2.3.4)` or `TERM(ds=1.2.3.4)`
- `TERM(1.2.3.4:*)` when port is following an IP with : as separator

### Step 3 - Get matching logs

#### Step 3.1 - From Step 2 findings, search for matching logs

In this step, we use a template SPL that is going to be called by a schedule search passing the parameters. This is a technique to write only once the complex SPL and use it as a function.

##### Step 3 - template

**HUNT_301_RETRO_TEMPLATE_hits_on_ip-dst**
```
sourcetype="$alert_sourcetype$"
    [| tstats count where index="$alert_index$" sourcetype="$alert_sourcetype$" by index sourcetype 
    | fields - count 
    | format 
    | fields search] 
    [| makeresults 
    | eval index="main", sourcetype="stash" 
    | fields - _time 
    | inputlookup append=t HUNT_LD_201_RETRO_catch_ip where index="$alert_index$" AND sourcetype="$alert_sourcetype$" 
    | fields index, sourcetype, _time 
    | stats min(_time) as et, max(_time) as lt 
    | eval lt=if(et == lt, lt+1, lt) 
    | eval et = "earliest=" + if(isnull(et), now()-1, et)
    | eval lt = "latest=" + if(isnull(lt), now(), lt)
    | eval search= et + " " + lt 
    | fields search] 
    [| makeresults 
    | eval index="$alert_index$", sourcetype="$alert_sourcetype$" 
    | eval protection_ip="nothing_to_search_in_logs", protection_misp_event_uuid="protection_mechanism" ```store dummy value for safety mechanism in case lookup below failed to be generated``` 
    | inputlookup append=t HUNT_LD_100_MISP_IOC_to_retrosearch ```add content of input lookup to current result``` 
    | eval misp_ip_dst=mvappend(misp_ip,misp_ip_dst,protection_ip), misp_event_uuid=coalesce(misp_event_uuid,protection_misp_event_uuid) 
    | mvexpand misp_ip_dst
    | where `soc_macro_is_ip(misp_ip_dst)` OR misp_ip_dst=="nothing_to_search_in_logs" 
    | stats values(*) as * by misp_ip_dst, misp_event_uuid 
    | eval _time=now() 
    | collect testmode=false index=misp_hunt_findings source="HUNT_301_RETRO_TEMPLATE_hits_on_ip-dst_used_as_IOC" 
    | rename misp_ip_dst as ip 
    | eval search = "TERM(" + ip + ") OR TERM(" + ip + "/32)"  
    | stats values(search) as search 
    | eval search = "(" + mvjoin(search, " OR ") + ")"] 
| fillnull value="not_found" src, src_ip, dest, dest_ip, user, site, status, action 
| fillnull value="not_found" $dest_field$ 
| stats count as total_hit, latest(_raw) as raw_event,
    min(_time) as first_hit , max(_time) as last_hit 
    by index, sourcetype, src, src_ip, dest, dest_ip, user, site, status, action, $dest_field$ 
| eval by_clause_md5=md5(index + sourcetype + src + src_ip + dest + dest_ip + user + site + status + action + $dest_field$) 
| where src!="not_found" OR src_ip!="not_found" OR dest!="not_found" OR dest_ip!="not_found" OR user!="not_found" OR site!="not_found" OR status!="not_found" OR action!="not_found" OR $dest_field$!="not_found" 
| sort 0 - index, sourcetype, src, src_ip, dest, dest_ip, user, site, $dest_field$ last_hit 
| eventstats count as idx_st_hits by index, sourcetype, src, src_ip, dest, dest_ip, user, site, $dest_field$ 
| streamstats count as rc by index, sourcetype, src, src_ip, dest, dest_ip, user, site, $dest_field$ reset_on_change=true 
| where rc <= 50 
| foreach src, src_ip, dest, dest_ip, user, site, status, action, $dest_field$ 
    [ eval <<FIELD>>=if(<<FIELD>>!="not_found",<<FIELD>>,null()) ] 
| lookup HUNT_LD_100_MISP_IOC_to_retrosearch misp_ip_dst as $dest_field$ OUTPUT 
| lookup HUNT_LD_100_MISP_IOC_to_retrosearch misp_ip_dst as dest OUTPUTNEW 
| lookup HUNT_LD_100_MISP_IOC_to_retrosearch misp_ip_dst as dest_ip OUTPUTNEW 
    ```| where isnotnull(misp_event_uuid) ```
| foreach misp_*
    [| eval <<FIELD>>=mvdedup('<<FIELD>>')]
| eval misp_ioc_freshness=last_hit - misp_timestamp 
| eval misp_ioc_freshness=tostring(misp_ioc_freshness, "duration") 
| eval _time=now() 
| collect testmode=false index=misp_hunt_findings source="HUNT_301_TEMPLATE_hits_on_ip-dst_COLLECT_RESULT_IP_DST" ```store results in index```
```

##### Step 3 - Use template for a tuple

Now you have to create saved searches that are going to use the template

**HUNT_339_RETRO_COLLECT_PROXY_SEC_DEST_IP**

```
| savedsearch HUNT_301_RETRO_TEMPLATE_hits_on_ip-dst
    alert_index="global_bluecoat_proxy_sec"
    alert_sourcetype="bluecoat:proxysg:psec:syslog"
    dest_field="r_ip"
```
The timerange needs to be defined on this saved search - not on the template itself. Likewise, scheduling is done on this saved search.

### Step 3.2 - Direct search on maching logs for a specific index based on Step 1

Sometimes the logs are specific enough and interesting like proxy logs. The log format may be also specific and cannot searched well using `tstats` and `TERM()`. An alternative is to build a specific search that will use the IoC from Step 1 to retrieve directly the detailed findings. 

**HUNT_302_HUNT_DIRECT_COLLECT_PROXY_DST_IP**

```
index=proxy AND sourcetype=access earliest=-180d
    [| makeresults 
    | eval index=proxy, sourcetype=access 
    | eval protection_ip="nothing_to_search_in_logs", protection_misp_event_uuid="protection_mechanism" ```store dummy value for safety mechanism in case lookup below failed to be generated``` 
    | inputlookup append=t HUNT_LD_100_MISP_IOC_to_retrosearch ```add content of input lookup to current result``` 
    | eval misp_ip_dst=mvappend(misp_ip_dst,protection_ip), misp_event_uuid=coalesce(misp_event_uuid,protection_misp_event_uuid) 
    | mvexpand misp_ip_dst
    | where `soc_macro_is_ip(misp_ip_dst)` OR misp_ip_dst=="nothing_to_search_in_logs" 
    | stats values(*) as * by misp_ip_dst, misp_event_uuid 
    | eval _time=now() 
    | collect testmode=false index=misp_hunt_findings source="HUNT_301_RETRO_TEMPLATE_hits_on_ip-dst_used_as_IOC" 
    | eval search = "TERM(r_ip=" + misp_ip_dst + ")" 
    | stats values(search) as search 
    | eval search = "(" + mvjoin(search, " OR ") + ")"] 
| fillnull value="not_found" src, src_ip, dest, dest_ip, user, site, status, action 
| stats count as total_hit, latest(_raw) as raw_event,
    min(_time) as first_hit , max(_time) as last_hit 
    by index, sourcetype, src, src_ip, dest, dest_ip, user, site, status, action
| eval by_clause_md5=md5(index +  sourcetype + src + src_ip + dest + dest_ip + user + site + status + action) 
| where src!="not_found" OR src_ip!="not_found" OR dest!="not_found" OR dest_ip!="not_found" OR user!="not_found" OR site!="not_found" OR status!="not_found" OR action!="not_found"
| sort 0 - index, sourcetype, src, src_ip, dest, dest_ip, user, site, last_hit
| eventstats count as idx_st_hits by index, sourcetype, src, src_ip, dest, dest_ip, user, site
| streamstats count as rc by index, sourcetype, src, src_ip, dest, dest_ip, user, site reset_on_change=true 
| where rc <= 50
| foreach src, src_ip, dest, dest_ip, user, site, status, action
    [ eval <<FIELD>>=if(<<FIELD>>!="not_found",<<FIELD>>,null()) ] 
| lookup HUNT_LD_100_MISP_IOC_to_retrosearch misp_ip_dst as dest_ip OUTPUT
| eval misp_first_seen=min(misp_first_seen), misp_last_seen=max(misp_last_seen) 
| where isnotnull(misp_event_uuid) AND ( first_hit >= misp_first_seen OR isnull(misp_first_seen) ) AND ( last_hit <= misp_last_seen OR isnull(misp_last_seen) ) 
| foreach misp_* 
    [| eval <<FIELD>>=mvdedup('<<FIELD>>')] 
| eval misp_ioc_freshness = last_hit - misp_timestamp, misp_ioc_freshness=tostring(misp_ioc_freshness, "duration"), 
    misp_retro_confidence=if( isnotnull(misp_first_seen) AND isnotnull(misp_last_seen), "CATCH:Retrosearch:Confidence:High", "CATCH:Retrosearch:Confidence:Medium") 
| eval _time=now() 
| collect testmode=false index=misp_hunt_findings source="HUNT_301_TEMPLATE_hits_on_ip-dst_COLLECT_RESULT_IP_DST" ```store results in index```
```
