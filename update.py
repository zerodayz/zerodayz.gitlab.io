#!/usr/bin/env python3
# coding: utf-8

'''
Check Hugo new releases from Hugo GitHub repo and update image automaticaly

Usage: update.py API_token project_uri
'''

import base64
import requests
import re
import sys
from urllib.parse import quote

GITLAB_URL = "https://gitlab.com/api/v4"
COMMIT_MESSAGE = "Update Hugo to version %s"

def compare_versions(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
    return normalize(version1) >= normalize(version2)

if len(sys.argv) != 3:
    print('Usage: update.py API_token project_uri')
    exit(1)

# Get vars from script arguments
GITLAB_TOKEN = sys.argv[1]
GITLAB_PROJECT = quote(sys.argv[2], safe='')

# Get latest release
rrelease = requests.get('https://api.github.com/repos/gohugoio/hugo/releases/latest')
if rrelease.status_code != 200:
    print('Failed to get Hugo latest release from GitHub')
    exit(1)

release = rrelease.json()
print('Last Hugo version is %s'%release['name'])

# Get repository tags
rtags = requests.get('%s/projects/%s/repository/tags'%(GITLAB_URL, GITLAB_PROJECT))
if rtags.status_code != 200:
    print('Failed to get tags from GitLab project')
    exit(1)

# If a higher version is present in the GitLab repository, do nothing
for tag in rtags.json():
    if tag['release'] is None:
        continue
    if compare_versions(tag['release']['tag_name'], release['name'][1:]):
        print('Already up to date, nothing to do')
        exit(0)
print('No tag is higher or equal to Hugo version.\nUpdating...')

# Find release archive checksum from GitHub
for asset in release['assets']:
    if re.search('checksums.txt', asset['name']):
        rchecksums = requests.get(asset['browser_download_url'])
        if rchecksums.status_code != 200:
            print('Failed to get checksums file from GitHub')
            exit(1)
        for line in rchecksums.text.split("\n"):
            if 'hugo_%s_Linux-64bit.tar.gz'%(release['name'][1:]) in line:
                checksum = line[:64]
                break

# Get Dockerfile from repository
rdockerfile = requests.get('%s/projects/%s/repository/files/Dockerfile/raw?ref=registry'%(GITLAB_URL, GITLAB_PROJECT))
if rdockerfile.status_code != 200:
    print('Failed to get Dockerfile from %s:'%sys.argv[1])
    print(rdockerfile.json())
    exit(1)
dockerfile = rdockerfile.text.split("\n")

# Replace env variables
for index, line in enumerate(dockerfile):
    if "ENV HUGO_VERSION" in line:
        dockerfile[index] = "ENV HUGO_VERSION %s"%release['name'][1:]
    if "ENV HUGO_SHA" in line:
        dockerfile[index] = "ENV HUGO_SHA %s"%checksum

# Update Dockerfile on repository
rupdate = requests.put('%s/projects/%s/repository/files/Dockerfile?branch=registry&author_name=Update%%20script&content=%s&commit_message=%s&encoding=base64'%(
    GITLAB_URL,
    GITLAB_PROJECT,
    quote(base64.b64encode("\n".join(dockerfile).encode()), safe=''),
    quote(COMMIT_MESSAGE%(release['name'][1:]), safe='')
), headers={'Private-Token': GITLAB_TOKEN})
if rupdate.status_code != 200:
    print("Failed to update Dockerfile:")
    print(rupdate.json())
    exit(1)
print('Dockerfile was updated to version %s'%release['name'][1:])

# Create new tag
rtag = requests.post('%s/projects/%s/repository/tags?tag_name=%s&ref=registry&message=%s&release_description=%s'%(
    GITLAB_URL,
    GITLAB_PROJECT,
    release['name'][1:],
    quote(COMMIT_MESSAGE%(release['name'][1:]), safe=''),
    quote(release['body'], safe='')
), headers={'Private-Token': GITLAB_TOKEN})
if rtag.status_code != 201:
    print('Failed to create tag:')
    print(rtag.json())
    exit(0)
print('Tag %s created'%release['name'][1:])
print('Done !')
