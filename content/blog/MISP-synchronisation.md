# MISP Synchronisation

## Introduction

To ensure effective threat intelligence sharing, **MISP** allows data synchronisation between different instances. The administrators of each instance can decide whether they want to send or receive data with the instances they want. In addition, synchronization also allows filtering between the data you want between public and private internal instances. However, this synchronisation mechanism must follow strict rules that define how and to what extent information can be shared.

As there are many issues at stake, it is therefore relevant to set up tests that verify these rules are correctly applied. I will explain here how I deployed multiple MISP instances locally and how I implemetend CI synchronisation tests on the MISP repository.

## What is synchronisation in MISP?

In this section, I will quickly explain the basic behavior of MISP synchronisation.
If you want to explore the concept in more detail, please check the [official MISP documentation](https://www.circl.lu/doc/misp/sharing/).

### Setup

A MISP instance can share data with another one in two ways:

* **PUSH**: The instance sends data to another.
* **PULL**: The instance fetches data from another.

To make it work, specific configurations are required on both instances.

For example, in the figure below, **Instance A** can push and pull data to/from **Instance B**. To achieve this, **Org A** must exist on both instances. Additionally, on **Instance B**, Org A must have a **Sync User** whose API key will be used by **Instance A** for synchronisation.

If you also want **Instance B** to push/pull data with **Instance A**, you need to mirror this configuration.

![MISP Synchronisation](/img/blog/synchronisation/sync.png)

### Data distribution levels

Each data in MISP is associated with a **distribution level**, which determines how it can be shared with other instances.

There are five distribution levels:

* **0 – Your organization only**: The information is only visible to the organization that created it.
* **1 – This community only**: The information is shared only with organizations present locally on the MISP instance.
* **2 – Connected communities**: The information can be shared with servers connected via synchronisation (partner MISP instances).
* **3 – All communities**: The information can be shared with all connected servers, including the servers of connected servers.
* **4 – Sharing group**: The information is shared only with a defined sharing group, which allows precise control over which entities can access the information.

The figure below illustrates how events with different distribution levels are propagated between multiple instances after a **PUSH** action:

![MISP distribution](/img/blog/synchronisation/distribution.png)


## Deploy several instance locally

### Deploy several instance locally
To perform synchronisation tests, both manually and automatically, it is necessary to run several MISP instances on your local machine.

For this purpose, I used the existing subrepository [misp-docker](https://github.com/MISP/misp-docker), which makes it easy to deploy a MISP instance inside a Docker container.

To define how many instances to deploy and how they should be connected, I created a configuration file where each instance and its connections can be specified. I then implemented a script that automatically deploys the required Docker containers and configures the synchronisation setup as described in the [Setup](#setup) section.

The figure below illustrates the deployment of two MISP instances locally, showing the addresses and ports used by the containers to communicate:

![MISP local](/img/blog/synchronisation/setup_local.png)

### Running tests

To ensure that the synchronisation feature remains functional in the MISP pipeline, I developed a set of test scenarios in **Python**, each representing a specific synchronisation case.

For this, I relied on the [PyMISP](https://github.com/MISP/pymisp) library, which provides convenient access to the MISP API.

Currently, the test suite contains **53 scenarios**, but more can easily be added since the possible synchronisation cases are nearly infinite.


## Conclusion
The implementation of synchronisation tests has enabled the detection of several abnormal behaviors. 
It should be noted that these errors mainly concern specific scenarios that are relatively rarely used by most users. However, identifying them highlights the importance of regularly checking all synchronisation mechanisms, including those that are used less frequently.

## Complementary links

* **MISP Synchronisation repository**: [https://github.com/MISP/misp-synchronisation](https://github.com/MISP/misp-synchronisation)
  (Deployment process and test execution are detailed here.)

* **End-of-studies report**: My full report, including details about synchronisation testing during my internship, is available [here](/Internship-report_Lacroix).

---
