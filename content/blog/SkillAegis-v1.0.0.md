---
title: SkillAegis
banner: /img/blog/SkillAegis/skillaegis-banner.png
author:
 - Sami Mokaddem
date: 2024-08-14
layout: post
---

# Design and Execute Cyber Threat Intelligence Scenarios with SkillAegis

Practical experience is essential for skill development, and effective training must be both engaging and capable of identifying gaps in understanding. That's why we're pleased to launch version 1.0.0 of SkillAegis, your new training companion.

SkillAegis was developed with these principles in mind, providing trainers with a platform to design, execute, and monitor scenario-based exercises that simulate real-world situations that you may encounter as an outcome of cyber threats. Based from our past experience in delivering MISP trainings to various user groups, we realized that we needed a tool to help us improve the hands-on part we usually give. As a result, we drove the development on primarily integrating tools such as MISP.

Practically speaking, SkillAegis offers a structured environment for honing one's skills in working with threat intelligence and information management.


## Core Features of SkillAegis

### Scenario Creation
SkillAegis enables trainers to design custom training exercises tailored to specific objectives. These scenarios can be configured to simulate a wide range of cyber incidents, offering a controlled environment where users can practice and sharpen their skills.

![SkillAegis Scenario Creation](/img/blog/SkillAegis/SkillAegis-Editor_index_cut.png)

### Exercise Execution & Real-Time Monitoring
After the scenarios are designed, SkillAegis facilitates their deployment and execution, allowing participants to actively engage with the exercises. The platform's live dashboard offers real-time tracking of participant progress and exercise outcomes, giving trainers and trainees immediate feedback on performance.

![SkillAegis Realtime Monitoring](/img/blog/SkillAegis/SkillAegis-Dashboard_exercise.png)

## The SkillAegis Platform

The SkillAegis platform consists of 3 applications:
- **[SkillAegis](https://github.com/MISP/SkillAegis) Main Application**
- **[SkillAegis Editor](https://github.com/MISP/SkillAegis-Editor)**
- **[SkillAegis Dashboard](https://github.com/MISP/SkillAegis-Dashboard)**

Let's have a quick look at what these applications do.

### [SkillAegis](https://github.com/MISP/SkillAegis) (Main Application) 
The **Main Application** configures and initiates the other two components of the system. It also includes several production-ready scenarios that trainers can use as inspiration or adapt for their own exercises. While each applications can be run individually, it's highly recommended to use it to streamline the experience.

![SkillAegis Main Platform](/img/blog/SkillAegis/skillaegis_main_app.png)

### [SkillAegis Editor](https://github.com/MISP/SkillAegis-Editor)

The SkillAegis Editor is the tool for designing and creating new training exercises. It allows you to configure metadata such as difficulty level and tags, as well as develop tasks (also called injects), specify their execution order, outline requirements and triggers for each task, and set criteria for evaluation and completion.

![SkillAegis Scenario Creation](/img/blog/SkillAegis/SkillAegis-Editor_designer.png)

Writing evaluations for injects can be challenging, even for experienced users, and poorly configured evaluation conditions can hinder trainees from completing the exercises, leading to frustration. The built-in Inject Tester provides the tooling to configure, test, debug, and optimize individual injects, ensuring they work as expected.

![SkillAegis Scenario Creation](/img/blog/SkillAegis/SkillAegis-Editor_inject-tester.png)

### [SkillAegis Dashboard](https://github.com/MISP/SkillAegis-Dashboard)

The SkillAegis Dashboard application enables the execution of training sessions and provides real-time visualization of participant progress.

Upon selecting a scenario to run, the application begins tracking and monitoring the progress of all participants. The interface displays the completion status for each inject, whilst also showing participant activity via a heatmap. It also provides live logs of user actions within the training environment.

{{<video src="/img/blog/SkillAegis/SkillAegis-Dashboard-recording.mp4" title="SkillAegis Dashboard demo" >}}

Additionally, the selected exercise can be displayed in fullscreen mode, making it suitable for presentations on a classroom screen.

![SkillAegis Dashboard Fullscreen exercise](/img/blog/SkillAegis/SkillAegis-Dashboard_fullscreen.png)

### Scenario Format

The scenarios in SkillAegis are described using the [Common Exercise Format (CEXF)](https://misp.github.io/cexf/)
The [format description](https://github.com/MISP/cexf/blob/main/format-description.md) provides details on the JSON structure and the semantics for each key. Although scenarios can be manually written, we recommend using the [SkillAegis Editor](https://github.com/MISP/SkillAegis-Editor) to streamline and simplify the process.


### Current Integration with MISP

Initially designed to enhance MISP training quality delivered by the MISP core team, SkillAegis features advanced integration with MISP. Most injects are designed to interact with the data created or stored in MISP. Additionally, SkillAegis can query MISP directly to search for data or monitor user activity, and it supports replaying trainees' actions within MISP. To enable this functionality, provide SkillAegis with access to a training MISP instance using a valid site-admin API Key. SkillAegis will then be able to configure the MISP instance to support all scenario features and advanced evaluation strategies for injects.


## Availability and Pricing

SkillAegis is free and open-source under the AGPLv3 license! Download it and start enhancing your cyber threat-intelligence training at no cost. Enjoy full access with no strings attached!

## Join the Development

SkillAegis is still in its early stages. Get started now and help us enhance and expand its features. Join us on GitHub to contribute to its development and explore new integrations.




