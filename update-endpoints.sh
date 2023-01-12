#!/bin/bash

upstream_defined=$(git config --local -l | grep -q remote.upstream)

if [[ $upstream_defined -gt 0 ]]; then
  git remote add upstream git@github.com:ibm-cloud-docs/log-analysis.git
else
  echo "Upstream repository already defined, so skipping the setup"
fi

git checkout -b "endpoints-update-$(gdate --utc '+%Y-%m-%d-%H%M%S')" > /dev/null 2>&1

virtualenv venv > /dev/null 2>&1
source ./venv/bin/activate > /dev/null 2>&1
pip install . > /dev/null 2>&1
./venv/bin/generate_endpoints_markdown_document > endpoints.md

export PAGER=cat
number_of_changes=$(git diff -- endpoints.md | wc -l)

if [[ $number_of_changes -gt 0 ]]; then
  echo "Found DNS changes, create a new pull request with changes"

  git add endpoints.md > /dev/null 2>&1
  git commit -m "Log Analysis: Update endpoints

Update the endpoints from current state of DNS.
  " > /dev/null 2>&1
  git push origin > /dev/null 2>&1
  # Make sure gh creates the pull request towards the upstream IBM
  # repository
  git config --local remote.upstream.gh-resolved base > /dev/null 2>&1
  gh pr create --fill
else
  echo "No DNS changes found for Log analysis endpoints"
fi
