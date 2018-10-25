---
title: Codename pristimanis
date: 2018-10-25
tags: ["pristimantis", "code", "citellus"]
---

## Introduction

You might be already aware of the other project I am working on [Citellus](https://citellus.org/) the project aim is to perform diagnosis on top a sosreport or any other file system snapshot. This is new project mainly for the automating the manual operations using [Ansible](https://www.ansible.com/).

Since I am working with [OpenStack](https://www.openstack.org) the most, most of the playbooks are made for [OpenStack](https://www.openstack.org) and hence the examples as well.

## Preparing the environment:

```bash
(overcloud) [stack@undercloud-0 ~]$ git clone https://gitlab.com/zerodayz/pristimantis.git
Cloning into 'pristimantis'...
remote: Enumerating objects: 267, done.
remote: Total 267 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (267/267), 53.31 KiB | 0 bytes/s, done.
Resolving deltas: 100% (126/126), done.
(overcloud) [stack@undercloud-0 ~]$ cd pristimantis
(overcloud) [stack@undercloud-0 pristimantis]$ source ansiblerc
(overcloud) [stack@undercloud-0 pristimantis]$ source  ~stack/stackrc
(undercloud) [stack@undercloud-0 pristimantis]$ sh scripts/openstack/prepare-etc-hosts.sh | sudo tee -a /etc/hosts
192.168.24.13 compute-0
192.168.24.14 controller-0
(undercloud) [stack@undercloud-0 pristimantis]$ tripleo-ansible-inventory --static-inventory inventory
No handlers could be found for logger "oslo_config.cfg"
(undercloud) [stack@undercloud-0 pristimantis]$ ansible overcloud -m ping  -u heat-admin
compute-0 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
controller-0 | SUCCESS => {
    "changed": false, 
    "failed": false, 
    "ping": "pong"
}
(undercloud) [stack@undercloud-0 pristimantis]$ 
```

## Example of collecting sosreports from Overcloud nodes:

```bash
(undercloud) [stack@undercloud-0 pristimantis]$ ansible-playbook -i inventory tasks/collect-sosreport.yaml \                                                
> -e case_id=12345 -e only_plugins=system -e hosts=overcloud
 [WARNING]: Found variable using reserved name: host
PLAY [Initializing local sosreport directory] *
---
PLAY RECAP *
compute-0                  : ok=7    changed=4    unreachable=0    failed=0
controller-0               : ok=7    changed=4    unreachable=0    failed=0
undercloud                 : ok=7    changed=3    unreachable=0    failed=0

(undercloud) [stack@undercloud-0 pristimantis]$ ls ~/overcloud-sosreports-12345-20181025T001126.tar 
/home/stack/overcloud-sosreports-12345-20181025T001126.tar
(undercloud) [stack@undercloud-0 pristimantis]$ tar -tf ~/overcloud-sosreports-12345-20181025T001126.tar 
./
./sosreport-compute-0.12345-20181025041140.tar.xz
./sosreport-controller-0.12345-20181025041141.tar.xz
```