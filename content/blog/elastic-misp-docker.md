---
title: MISP - Elastic Stack - Docker Lab 
date: 2024-04-05
layout: post
banner: /img/blog/elastic-lab/elastic-misp-architecture.png
tags: ["MISP", "Threat Intelligence", "Elastic", "Elasticsearch", "Filebeat", "Alerts", "Integration", "Docker"]
categories: []
authors:
- Luciano Righetti
---

# MISP - Elastic Stack - Docker

This lab explains how to connect MISP to the Elastic Stack in order to leverage IOCs from MISP and trigger alerts based on user defined rules.

![Elastic-MISP Overview Diagram](/img/blog/elastic-lab/architecture.png "{class='img-responsive'}")


MISP is used to gather IOCs from different sources such as open source Threat Intelligence feeds. 

Filebeat pulls IOCs from MISP and pushed them to the Elasticsearch instance via the Threat Intel module [^1].

To simplify this guide Elastic Agent [^2] in installed standalone mode is installed on the hosts we want to monitor, but Fleet [^3] could be used instead. 

Kibana [^4] is used for exploring the IOCs, creating rules and visualizing the alerts.  

Everything in this lab is run on Docker [^5].

[^1]: https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-threatintel.html
[^2]: https://www.elastic.co/guide/en/fleet/current/install-standalone-elastic-agent.html
[^3]: https://www.elastic.co/guide/en/fleet/current/fleet-overview.html
[^4]: https://www.elastic.co/kibana
[^5]: https://github.com/righel/elastic-misp-docker-lab

## Installation
1. Clone the lab repository.
    ```bash
    $ git clone https://github.com/righel/elastic-misp-docker-lab.git & cd elastic-misp-docker-lab
    ```

### MISP

2. Create the .env file:
    ```
    $ cp template.env .env
    ```

3. Start the MISP containers.
    ```
    $ docker compose up -d
    ```

4. When MISP containers finish starting, create a sync user for Elastic on MISP.


    Using MISP CLI:
    ```
    $ docker-compose exec misp-core app/Console/cake User create elastic@admin.test 5 1
    $ docker-compose exec misp-core app/Console/cake User change_authkey elastic2@admin.test
    Old authentication keys disabled and new key created: 06sDmKQK3E6MSJwsOhYT3N4NzfTpe53ruV0Bydf0
    ```
    
    Using MISP UI:
    
    Default MISP credentials

    > User: admin@admin.test
    > 
    > Password: admin
    

### Elastic Stack

> The yaml configuration files for Elasticsearch, Kibana and Filebeat are located in `elastic/config/` directory. You can review and change these settings before deploying Elastic Stack.

For adjusting the Filebeat MISP Threat Intel module, check `elastic/config/filebeat.yml`:
```yaml
filebeat.modules:
  - module: threatintel
    misp:
      enabled: true
      var.input: httpjson
      var.url: "https://${MISP_HOST}/events/restSearch"
      var.api_token: "${MISP_ELASTIC_API_KEY}"
      var.first_interval: 24h
      var.interval: 10m
      var.ssl.verification_mode: none
      var.filters:
        type: ["md5", "sha256", "sha512", "url", "uri", "ip-src", "ip-dst", "hostname", "domain"]
        tags: ['workflow:state="complete"']
```

For more details refer to the official docs: 
* https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-threatintel.html#misp


5. Modify some environment variables before firing up Elastic Stack.

    * `KIBANA_ENCRYPTION_KEY`: Has to be 32 chars string to set up `xpack.encryptedSavedObjects.encryptionKey` on Kibana. 
    * `MISP_ELASTIC_API_KEY`: The MISP API key generated in step 4 for the sync user `elastic@admin.test`.

6. Start the Elastic Stack containers.
    ```
    $ docker-compose -f docker-compose.elastic.yml -d
    ```
    
Now you can use MISP and the Elastic Stack.


## Creating Kibana detection rules

1. Go to _Kibana_ > _Security_ > _Rules_ and click on _Detection rules (SIEM)_

    ![Kibana Security Rules page](/img/blog/elastic-lab/kibana_detection_rules.png "{class='img-responsive'}")

2. Click on ![Kibana Add Elastic Rules](/img/blog/elastic-lab/kibana_add_rules_button.png "{class='img-responsive'}") and search for _Threat Intel_, and select the rules you are interested on.

    ![Kibana Install Threat Intel rules](/img/blog/elastic-lab/kibana_add_elastic_rules.png "{class='img-responsive'}")

3. Click on ![Kibana Install rules](/img/blog/elastic-lab/kibana_install_rules_button.png "{class='img-responsive'}")

4. Go back to _Kibana_ > _Security_ > _Rules_ and click on _Detection rules (SIEM)_, click on the _Disabled rules_ filter to show the recently installed rules (by default they are disabled), and enable them.

    ![Kibana Enabled rules](/img/blog/elastic-lab/kibana_installed_rules.png "{class='img-responsive'}")

Now Elastic will generate alerts if it detects any hash, url or domain matching with MISP IOCs.

## Demo

### Install Elastic Agent (standalone)

1. Go to _Kibana_ > _Management_ > _Fleet_ and switch to the _Agent policies_ tab and click on the _Create agent policy_ button.

![Kibana Fleet Create Agent Policy](/img/blog/elastic-lab/kibana_create_agent_policy.png "{class='img-responsive'}")

2. Click on the policy to access it and click on _Add integration_ and search for _Network Packet Capture_, click on it and click on _Add Network Packet Capture_

    ![Add Network Packet Capture](/img/blog/elastic-lab/kibana_network_packet_capture_integration.png "{class='img-responsive'}")

3. Configure the Network Packet Capture integration if needed.
    ![Network Packet Capture configuration](/img/blog/elastic-lab/kibana_add_network_packet_capture_integration.png "{class='img-responsive'}")

    Click on _Save and continue_.

    > If prompted to add a Elastic Agent, click on _Add Elastic Agent later_.

    ![Kibana Elastic Agent Policy](/img/blog/elastic-lab/kibana_agent_policy_view.png "{class='img-responsive'}")


4. Click on _Actions_ > _Add agent_, switch to the _Run standalone_ tab.

    ![Configure standanlone Elastic Agent](/img/blog/elastic-lab/kibana_add_elastic_agent.png "{class='img-responsive'}")
    
    Click on _Download Policy_.
    
5. Create an API key for the Elastic Agent communication to Elasticsearch [^6]. Navigate to _Kibana_ > _Stack Management_ > _API keys_ and click Create API key.


    ![Kibana Create Elastic Agent API key](/img/blog/elastic-lab/kibana_add_api_key.png "{class='img-responsive'}")

    1. Enable the _Restrict privileges_ toggle and copy the following configuration.
    
        ```json
        {
          "standalone_agent": {
            "cluster": [
              "monitor"
            ],
            "indices": [
              {
                "names": [
                  "logs-*-*", "metrics-*-*", "traces-*-*", "synthetics-*-*" 
                ],
                "privileges": [
                  "auto_configure", "create_doc"
                ]
              }
            ]
          }
        }

        ```

    2. Click on _Create API key_.

    3. Select _Beats_ and copy the API key.

        ![Elastic Agent API key](/img/blog/elastic-lab/kibana_api_key_view.png "{class='img-responsive'}")

    
7. Open the `elastic-agent.yml` configuration downloaded on step 5 and modify the `outputs` section it to use API authentication and change the Elasticsearch host from `localhost` to `elasticsearch`.

    ```yaml
    outputs:
      default:
        type: elasticsearch
        hosts:
          - 'http://elasticsearch:9200'
        api_key: 'RZAxqY4BZZJcsxX19zAw:d9AabeoqRkKwm27K_KEgKA'
        preset: balanced
    ``` 

8. Install Elastic Agent in the host we want to monitor. Start an Ubuntu container and plug it to the MISP-Elastic Stack lab network.
    ```
    $ docker run -it --network=elastic-misp-docker-lab_default --name=my_monitored_host ubuntu
    ```


9. Follow the steps to install the standalone Elastic Agent [^7].
    ```bash
    $ curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.13.1-linux-x86_64.tar.gz
    root@be44a9a86e24:/# apt update
    ...
    root@be44a9a86e24:/# apt install curl -y
    ...
    root@be44a9a86e24:/# cd /tmp
    root@be44a9a86e24:/# curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.13.1-linux-x86_64.tar.gz
    root@be44a9a86e24:/# tar xzvf elastic-agent-8.13.1-linux-x86_64.tar.gz
    ...
    
    # from a different terminal, copy the elastic-agent.yml config file into the container
    docker cp elastic-agent.yml my_monitored_host:/tmp/elastic-agent-8.13.1-linux-x86_64/elastic-agent.yml
    
    # back on the docker terminal, install the agent
    root@be44a9a86e24:/# cd elastic-agent-8.13.1-linux-x86_64/
    root@be44a9a86e24:/# ./elastic-agent install
        Elastic Agent will be installed at /opt/Elastic/Agent and will run as a service. Do you want to continue? [Y/n]:Y
        Do you want to enroll this Agent into Fleet? [Y/n]:n
        [=   ] Service Started  [32s] Elastic Agent successfully installed, starting enrollment.
        [=   ] Done  [32s]                       
        Elastic Agent has been successfully installed.
    ```
    
    Done. Now the docker container is being monitored by the Elastic Agent and the metrics are being pushed to Elasticsearch.
    
### Testing

1. Go to MISP, create a new Event an add a _ip-dst_ type attribute.
    2. ![Add MISP Attribute](/img/blog/elastic-lab/misp_add_attribute.png "{class='img-responsive'}")

2. Add the _workflow:state="complete"_ tag to the event to it is picked up by Elasticsearch.

    ![MISP Add Tag](/img/blog/elastic-lab/misp_add_workflow_tag.png "{class='img-responsive'}")

3. Publish the Event.

> Depending on the `vars.interval` set on the Threat Intel module in the `filebeat.yml` configuration file, it may take some time for the IOC to get into Elasticsearch.

4. From your monitored docker host, generate traffic to one of the MISP IOCs.
    ```
    root@be44a9a86e24:/# curl -I https://circl.lu
    ...
    ```

5. Navigate to _Kibana_ > _Security_ > _Alerts_, you should now see some alerts triggered by the _Threat Intel IP Address Indicator Match_.
    ![Kibana Security Alerts](/img/blog/elastic-lab/kibana_security_alerts.png "{class='img-responsive'}")

> By default Elastic runs these detection rules every 4 hours, you can configure the internal reduce 


Done! Now you will get alerts on Kibana when an event in one of your monitored hosts matches a MISP IOC. 

[^6]: https://www.elastic.co/guide/en/fleet/current/grant-access-to-elasticsearch.html
[^7]: https://www.elastic.co/guide/en/fleet/current/install-standalone-elastic-agent.html
