#!/bin/bash
#
# Parses the github ref and extracts the version from the git tag if present, otherwise
# falls back to 'latest'.
#
# Writes the `version` and `git_hash` output variables.
#
# Usage:
#
#   ./extract_version.sh <git-ref> [<default-branch>]
#
# Expects the `$GITHUB_SHA` envvar to be present.

set -euo pipefail

# Initialize vars from arguments
ref=$1
default_branch=${2:-main}

# Strip git ref prefix from version
VERSION=$(echo "$ref" | sed -e 's,.*/\(.*\),\1,')

# Strip "v" prefix from tag name (if present at all)
[[ "$ref" == "refs/tags/"* ]] && VERSION=$(echo $VERSION | sed -e 's/^v//')

# Use Docker `latest` tag convention
[ "$VERSION" == "$default_branch" ] && VERSION=latest

# PRs result in version 'merge' -> transform that into 'latest'
[ "$VERSION" == "merge" ] && VERSION=latest

echo "version=${VERSION}" >> $GITHUB_OUTPUT
echo "git_hash=${GITHUB_SHA}" >> $GITHUB_OUTPUT
