---
title: How to push to a TAXII server from MISP 
date: 2023-04-29
layout: post
banner: /img/blog/taxii-1.png
---

If you want to push data from your MISP instance to a TAXII server, there are a few steps you need to follow. Firstly, you'll need to ensure that your MISP instance is configured to export data in a format that the TAXII server can accept. This typically involves converting the data to STIX 2.x format by using the builtin [misp-stix converter](https://github.com/MISP/misp-stix). Next, you'll need to establish a connection between your MISP instance and the TAXII server by configuring the appropriate API and collection endpoints in the MISP sync action. Once this is done, you can initiate the data transfer from your MISP instance to the TAXII server by pushing the searched data to the designated API and collection.

MISP has an automatic feature to support the automatic export from MISP to a TAXII 2.1 server. This article includes all the steps including the installation of TAXII 2.1 server for testing.

# TAXII 2.1 server configuration example

### Install medallion

- From git

```bash
git clone https://github.com/oasis-open/cti-taxii-server.git
cd cti-taxii-server

# optional but appreciated
virtualenv -p python3 venv
source ./venv/bin/activate

pip3 install -r requirements.txt
pip3 install .
```

- From pypi
```bash
pip3 install medallion
```

### Run medallion

Some important points:
- medallion runs on http only
- the default port is 5000
- look at the configuration file and check the options
- **set the host address with the `-h` option**

```bash
medallion -h <HOST> -c <config_file.json>
```

### Push data to TAXII

MISP has an integration for TAXII servers, which includes:

- TAXII servers configuration listing
- discovery end point on each TAXII server to list and choose:
    - the API root
    - the collections
- Filtering on the content to push

The list of TAXII servers is available via the `Sync Actions` tab -> `List Taxii Servers`

![](/img/blog/taxii-1.png)

#

#### Make your running TAXII server reachable from MISP

In order to add a new connection to a TAXII server, you need to provide:
- the server url
- an API key being the base64 encoded string of `<username>:<password>`
- the API root
- the collection name

![](static/img/blog/taxi-2.png)

#

#### Filter on the data to push

In the TAXII server connection config, you can define filter rules.

Those rules are basically the ones you would use as `HTTP body` of a `restSearch` request. [restSearch filters options are documented in our OpenAPI](https://www.misp-project.org/openapi/).


This means you can filter on a lot of different things, for example:

- data that is owned by your own organisation
  ```json
  {
    "org": "<YOUR_ORG>"
  }
  ```
- content marked with certain tags
  ```json
  {
    "tags": [
      "tlp:white",
      "stix_push"
    ]
  }
  ```
- a more specific example
  ```json
  {
    "org": "CIRCL",
    "tags": "tlp:white",
    "type": [
      "ip-src",
      "ip-dst"
    ]
  }
  ```

    
#

The feature is converting your content to STIX 2.x format then it can be automatically exported and pushed to the designated API and collection on the TAXII server.

