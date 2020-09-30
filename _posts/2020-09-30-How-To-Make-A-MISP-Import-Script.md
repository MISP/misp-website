---
title: Create an import script for MISP , step-by-step tutorial
layout: post
authors:
- Paul Bourmeau
date: 2020-09-30
tags: ["MISP", "Import Script", "MISP", "Threat Intelligence"]
categories: []
---

# Create an import script for MISP , step-by-step tutorial

## Script description
### Example add_github_user.py

Here the goal is to push to MISP information gathered on Github. The script [add_git_user.py](https://github.com/MISP/PyMISP/blob/main/examples/add_github_user.py) will be used as an example.

An **import script**, it's different from a MISP module.

An import script is run from a terminal to push data into a MISP, but a MISP module runs into a MISP instance. For more information about MISP modules, see [here](https://misp.github.io/misp-modules/)

This script will add data from GitHub as object to an existing MISP event.

**Tips:** in early phase or for testing purpose, it's better to start with an import module to test the code and results. If it's conclusive you can code a MISP module.


### PyMISP install

PyMISP is a Python library to access MISP with REST API. Install the [PyMISP](https://github.com/MISP/PyMISP) library on your machine.

To do so, clone the [repository](https://github.com/MISP/PyMISP) and install the library:

~~~bash
git clone https://github.com/MISP/PyMISP
cd PyMISP
pip3 install .
~~~

### Fork

If you wish to contribute and push your code to the MISP community, you'll need to fork the PyMISP library.

### Meaningful naming

Where to put the files and what are their names?

The script will be in **[PyMISP/examples](https://github.com/MISP/PyMISP/tree/main/examples)** and has the name of the imported service. A short key word is a good practice to describe the script action:

~~~
PyMISP/examples/add_github_user.py
~~~

**tips:** before naming your script, consult the list of available scripts into the PyMISP/examples folder, in order to describe accurately what your import module does.

### Keys management

For all scripts , you need to have a single key file **keys.py**. The file is not to be committed and contains the credentials for connecting to the MISP instance: API key, URL, SSH validations.

- You create a file keys.py into the dir PyMISP/examples.

References to this file will be later set in the script:

~~~python
from keys import misp_url, misp_key, misp_verifycert
~~~


### Required libraries

- PyMISP
- request
- sys
- argparse

### Usage block

We will go through the Python code and explain step-by-step each part.

It will be used by pyDoc, starts with """ and ends with """. You will here describe the usage for the script.

~~~~python
"""
usage: add_github_user.py [-h] -e EVENT [-f] -u USERNAME
Fetch GitHub user details and add it in object in MISP
optional arguments:
-h, --help            show this help message and exit
-e EVENT, --event EVENT
		      Event ID to update
-f, --force-template-update
-u USERNAME, --username USERNAME
		      GitHub username to add
"""
~~~~

### Argument parser

The script needs to grab the event-id (-e), a force to update the template from the repository (-f), and here a user account (-u).

~~~~python
parser = argparse.ArgumentParser(description='Fetch GitHub user details and add it in object in MISP')
parser.add_argument("-e", "--event", required=True, help="Event ID to update")
parser.add_argument("-f", "--force-template-update", required=False, action="store_true")
parser.add_argument("-u", "--username", required=True, help="GitHub username to add")
args = parser.parse_args()
~~~~

### Request

NOTE: If the user doesn't exist, the script is interrupted.

~~~~python
r = requests.get("https://api.github.com/users/{}".format(args.username))
if r.status_code != 200:
		sys.exit("HTTP return is {} and not 200 as expected".format(r.status_code))
if args.force_template_update:
		print("Updating MISP Object templates...")
		update_objects()
pymisp = PyMISP(misp_url, misp_key, misp_verifycert)
~~~~

The PyMISP connection is instantiated with following parameters coming from the file keys.py : *misp_url, misp_keys and misp_verifycert*.

### Object creation

We create a MISP object, the name is object template name:

~~~~python
misp_object = MISPObject(name="github-user")
~~~~

### User data

User data from the GitHub API are transformed into a JSON in order to be parsed by the following commands:

~~~~python
github_user = r.json()
~~~~

Following HTTP GET requests to obtain the following and followers sections of the GitHub user.

~~~~python
rfollowers = requests.get(github_user['followers_url'])
followers = rfollowers.json()
rfollowing = requests.get("https://api.github.com/users/{}/following".format(args.username))
followings = rfollowing.json()
~~~~

Same things for the SSH public keys attached to the GitHub user:

~~~~python
rkeys = requests.get("https://api.github.com/users/{}/keys".format(args.username))
keys = rkeys.json()
~~~~

Then, filling of the object from the github_user json object:

~~~~python
misp_object.add_attributes("follower", *[follower['login'] for follower in followers])
misp_object.add_attributes("following", *[following['login'] for following in followings])
misp_object.add_attributes("ssh-public-key", *[sshkey['key'] for sshkey in keys])
misp_object.add_attribute('bio', github_user['bio'])
misp_object.add_attribute('link', github_user['html_url'])
misp_object.add_attribute('user-fullname', github_user['name'])
misp_object.add_attribute('username', github_user['login'])
misp_object.add_attribute('twitter_username', github_user['twitter_username'])
misp_object.add_attribute('location', github_user['location'])
misp_object.add_attribute('company', github_user['company'])
misp_object.add_attribute('public_gists', github_user['public_gists'])
misp_object.add_attribute('public_repos', github_user['public_repos'])
misp_object.add_attribute('blog', github_user['blog'])
misp_object.add_attribute('node_id', github_user['node_id'])
~~~~

Finaly, you add the new object created, then pushed to the specified event id, on your MISP instance:

~~~~python
retcode = pymisp.add_object(args.event, misp_object)
~~~~

Now it's your turn, to do a MISP import script.
