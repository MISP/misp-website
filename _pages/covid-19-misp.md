---
layout: page
title: COVID-19 MISP
permalink: /covid-19-misp/
toc: true
---

# COVID-19 MISP Information Sharing Community


COVID-19 MISP is a MISP instance retrofitted for a COVID-19 information sharing community, focusing on two areas of sharing:

- Medical information
- Cyber threats related to / abusing COVID-19

The information sharing community has a low barrier of entry, everyone can contribute and use the data. By default, the information is classified as TLP:WHITE for broader distribution and usefulness.

## Who is the target audience for this community ?

- Anyone wanting to gain situational awareness in regards to the current COVID-19 situation
- Security practitioners trying to fend off covid related attacks
- Those wanting to share, collaborate, visualise, automate data
- All data is contextualised as either medical or security related information to make filtering as easy and convenient as possible

## Why use MISP for such a context?

- We are obviously interested on a personal level, as is everyone
- Information sharing is what we do anyway
- The tools that we are building are expanding our capabilities for the future
- Bridging different domains affected in different ways can reveal correlations

## How to get access to the COVID-19 MISP

Access can be requested to CIRCL by sending an email to [CIRCL](mailto:info@circl.lu). A self-registration is also [available](https://covid-19.iglocska.eu/users/register).

## Training

- [MISP COVID-19 replay training session](https://bbb.secin.lu/playback/presentation/2.0/playback.html?meetingId=741e7d15e14e107dbfffe2106a8547abc8460f3e-1585312475228)
- [MISP COVID-19 Training](https://peertube.opencloud.lu/videos/watch/4f7acd4c-a909-4315-87aa-38ba95cceaf2)
- [MISP COVID-19 Slides](https://www.misp-project.org/misp-training/x.5-covid.pdf)

## Public Feeds generated from COVID-19 MISP community

Two public feeds are automatically generated from COVID-19 MISP. A filtered feed with the sources being selected by the MISP project team and another with all IOCs shared in the covid-19 MISP community.

- [covid_misp_filtered_ioc_list.csv](https://covid-19.iglocska.eu/public/covid_misp_filtered_ioc_list.csv)
- [covid_misp_full_ioc_list.csv](https://covid-19.iglocska.eu/public/covid_misp_full_ioc_list.csv)

## How are the public feeds generated

As the MISP API is quite versatile, the script to generate the public feeds is described below:

~~~~shell
curl \
-d '{"returnFormat":"csv","tags":["pandemic:covid-19=\"cyber\""],"enforceWarninglist":1,"requested_attributes":["value","type","event_info"]}' \
-H "Authorization: [API KEY]" \
-H "Accept: application/json" \
-H "Content-type: application/json" \
-X POST https://covid-19.iglocska.eu/events/restSearch \
> /var/www/MISP/app/webroot/public/covid_misp_full_ioc_list.csv

chown www-data:www-data /var/www/MISP/app/webroot/public/covid_misp_full_ioc_list.csv

curl \
-d '{"returnFormat":"csv","org":["CIRCL"], "enforceWarninglist":1,"requested_attributes":["value","type","event_info"], "tags":["pandemic:covid-19=\"cyber\""]
}' \
-H "Authorization: [API KEY]" \
-H "Accept: application/json" \
-H "Content-type: application/json" \
-X POST https://covid-19.iglocska.eu/events/restSearch \
> /var/www/MISP/app/webroot/public/covid_misp_filtered_ioc_list.csv

curl \
-d '{"returnFormat":"csv","eventid":[262, 372, 269],"enforceWarninglist":1,"requested_attributes":["value","type","event_info"],"tags":["pandemic:covid-19=\"c
yber\""], "headerless": 1}' \
-H "Authorization: [API KEY]" \
-H "Accept: application/json" \
-H "Content-type: application/json" \
-X POST https://covid-19.iglocska.eu/events/restSearch \
>> /var/www/MISP/app/webroot/public/covid_misp_filtered_ioc_list.csv

chown www-data:www-data /var/www/MISP/app/webroot/public/covid_misp_filtered_ioc_list.csv
~~~~

## How to access the COVID-19 MISP

- The url of COVID-19 MISP is the following [https://covid-19.iglocska.eu](https://covid-19.iglocska.eu).

## Dashboards available in COVID-19 MISP

![](/assets/images/misp/covid-dash.png){:class="img-responsive"}
