---
title: Pristimanis
date: 2018-10-25
tags: ["pristimantis", "code", "citellus"]
---

## Introduction

You might be already aware of the other project I am working on [Citellus](https://citellus.org/) the project aim is to perform diagnosis on top a sosreport or any other file system snapshot. This is new project mainly for the automating the manual operations using [Ansible](https://www.ansible.com/).

Since I am working with [OpenStack](https://www.openstack.org) the most, most of the playbooks are made for [OpenStack](https://www.openstack.org) and hence the examples as well.

## Preparing the environment:

```bash
git clone https://gitlab.com/zerodayz/pristimantis.git
cd pristimantis
source ansiblerc
source  ~stack/stackrc
sh scripts/openstack/prepare-etc-hosts.sh | sudo tee -a /etc/hosts
tripleo-ansible-inventory --static-inventory inventory
ansible overcloud -m ping  -u heat-admin
```

## Example of collecting sosreports from Overcloud nodes:

```bash
ansible-playbook -i inventory tasks/collect-sosreport.yaml -e case_id=12345 -e only_plugins=system -e hosts=overcloud
ls ~/overcloud-*
tar -tf ~/overcloud-*
```