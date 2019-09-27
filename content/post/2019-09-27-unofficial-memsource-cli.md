---
title: Unofficial Memsource CLI
date: 2019-09-27
tags: ["memsource", "code", "cli"]
---

You might be already aware of the other project I am working on [Unofficial Memsource CLI](https://github.com/unofficial-memsource/memsource-cli-client).

Memsource CLI is a framework to help with automation of Memsource related tasks. This empowers you to automate repetitive tasks such as project, job creation, analysis runs and others. The framework is cabable to talk to Memsource API using REST client and show you the results of the execution on the screen.

Please if you have any idea on any improvements please do not hesitate to open an [issue](https://github.com/unofficial-memsource/memsource-cli-client/issues).


## Get the code and stay updated:

Following code will create a `git` directory in your `$HOME` directory, fetch the Github project `memsource-cli-client`. After that it will create a virtual environment using `venv`, for anyone out there with `Python 2.7` you will need `python-virtualenv` package. Once the virtual environment is created, it will `pip install` the required packages.

```bash
DIRECTORY="$HOME/git/"

if [[ ! -d ${DIRECTORY} ]]; then
  mkdir ${DIRECTORY}
fi
cd ${DIRECTORY}
if [[ ! -d ${DIRECTORY}/memsource-cli-client ]]; then
  git clone https://github.com/unofficial-memsource/memsource-cli-client.git
  cd memsource-cli-client/
  if [[ -f $(which python3) ]];
  then
    python3 -m venv --system-site-packages .memsource
  else
    if [[ ! -f $(which virtualenv) ]];
    then
      sudo yum -y install python-virtualenv
    fi
    virtualenv --system-site-packages .memsource
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -U pip
  pip install -U setuptools
  pip install -e .
  deactivate
else
  cd memsource-cli-client/
  git checkout master
  git reset --hard
  git pull
  if [[ ! -f $(which python3) ]];
  then
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -e .
  deactivate
fi
source ${DIRECTORY}/memsource-cli-client/.memsource/bin/activate
clear
memsource --help
```

## Preparing the environment:

Once you have the code and your `.memsource` environment is activated.

```bash
export MEMSOURCE_USERNAME=<username>
export MEMSOURCE_PASSWORD=<password>
export MEMSOURCE_TOKEN=$(memsource auth login --user-name $MEMSOURCE_USERNAME --password "${MEMSOURCE_PASSWORD}" -c token -f value)
```

## What's new

This release candidate `0.2rc` contains features such as:

- [Create analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-create)
- [Delete analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-delete)
- [Create analyses by languages](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-language-create)
- [List analyses by project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-project-list)
- [Get Analysis](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Analysis#analyse-show)
- [Login](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Auth#login)
- [Who Am I](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Auth#whoami)
- [Creates job in project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-create)
- [Delete job](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-delete)
- [List jobs in project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-list)
- [Get job](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Jobs#job-show)
- [Create new project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-create)
- [Deletes a project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-delete)
- [List projects](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-list)
- [Get project](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-show)
- [Create new project from template](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-Project#project-template-create)
- [Create user](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-User#user-create)
- [Get user](https://github.com/unofficial-memsource/memsource-cli-client/wiki/Memsource-User#user-get)

For more information please take a look at [wiki](https://github.com/unofficial-memsource/memsource-cli-client/wiki)

## Recommended Tip!

To add autocompletion to your shell so you can type:

`mem[tab]` `pr[tab]` `cr[tab]` which will translate to:

`memsource project create`

```bash
memsource complete | sudo tee /etc/bash_completion.d/memsource > /dev/null
. /etc/bash_completion.d/memsource
```