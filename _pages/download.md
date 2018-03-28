---
layout: page
title: Download
permalink: /download/
toc: true
---

## Download and Install MISP

[MISP source code is available on GitHub](https://github.com/MISP/MISP) including documentation and scripts for installation.

[ChangeLog](/Changelog.txt) contains a detailed list of updates for each software release in the core of the MISP software.

### Requirements

MISP can be easily installed on any standard GNU/Linux distribution. Installation guides for various distributions are included in the [INSTALL directory](https://github.com/MISP/MISP/tree/2.4/INSTALL). If you did a git clone of MISP for the installation, an [UPDATE procedure is available](https://github.com/MISP/MISP/blob/2.4/INSTALL/UPDATE.txt) to keep your MISP up-to-date.

### Virtual images

If you would like to test MISP and don't want to do an installation, CIRCL generates automatically VMware images and VirtualBox at each MISP core commit. Available at the [following location](https://www.circl.lu/misp-images/latest/). The image can be used for production but we highly recommend to change the default credentials and salt pre-configured with such images.

The default credentials for the automatically generated virtual machines are the following:

~~~~
For the MISP web interface -> admin@admin.test:admin
For the system -> misp:Password1234
Please add the following forwards on your VM Host:

VBoxManage controlvm MISP_VM_NAME natpf1 www,tcp,,8080,,80
VBoxManage controlvm MISP_VM_NAME natpf1 ssh,tcp,,2222,,22
VBoxManage controlvm MISP_VM_NAME natpf1 dashboard,tcp,,8001,,8001
~~~~

### Vagrant

[misp-vagrant](https://github.com/MISP/misp-vagrant) deploys MISP project software with Vagrant.

### Docker containers

- A [docker container for MISP](https://github.com/xme/misp-docker) is maintained by Xavier Mertens.
- Another [MISP docker container](https://github.com/harvard-itsecurity/docker-misp) is maintained by Ventz Petkov.

### Puppet

- [puppet-misp](https://github.com/voxpupuli/puppet-misp) This module installs and configures MISP (Malware Information Sharing Platform) on CentOS 7.

### Ansible

- [MISP ansible](https://github.com/juju4/ansible-MISP) An ansible role to setup a MISP instance.

## License

The MISP software is an open source and free software released under the [AGPL](https://github.com/MISP/MISP/blob/2.4/LICENSE) (Affero General Public License). We are committed to ensure that MISP will remain a free and open source project on the long-run.

The MISP taxonomies are licensed under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) (CC0 1.0) - Public Domain Dedication. This allows interoperability with any product. (open source or proprietary) 
