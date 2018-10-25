---
title: Codename pristimanis
date: 2018-10-25
tags: ["pristimantis", "code", "citellus"]
---

You might be already aware of the other project I am working on [Citellus](https://citellus.org/) the project aim is to perform diagnosis on top a sosreport or any other file system snapshot. This is new project mainly for the automating the manual operations using [Ansible](https://www.ansible.com/).

Since I am working with [OpenStack](https://www.openstack.org) the most, most of the playbooks are made for [OpenStack](https://www.openstack.org).  

Before we start we need to prepare the environment, usually undercloud but it can be any host that has access to your overcloud nodes.

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

## Example of collecting sosreports:

The idea behind this playbook is that it takes the sosreport from `hosts=overcloud` or `hosts=Controller` or `hosts=Compute` depends on the Ansible `inventory`

```bash
ansible-playbook -i inventory tasks/collect-sosreport.yaml -e case_id=12345 -e only_plugins=system -e hosts=overcloud
ls ~/overcloud-*
tar -tf ~/overcloud-*
```