#!/bin/bash

upstream_defined=$(git config --local -l | grep -q remote.upstream)

if [[ $upstream_defined -gt 0 ]]; then
  git remote add upstream git@github.com:ibm-cloud-docs/log-analysis.git
else
  echo "Upstream repository already define, so skipping the setup"
fi

#virtualenv venv
#source ./venv/bin/activate
#pip install .
#./venv/bin/generate_endpoints_markdown_document > endpoints.md
git checkout -b endpoints-update-$(date -I)
git add endpoints.md
git commit -m "Log Analysis: Update endpoints

Update the endpoints from current state of DNS.
"
git push origin

git config --local remote.upstream.gh-resolved base
gh pr create --fill
