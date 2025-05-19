# Extract version information

Small script/action to extract `version` and `git_sha` outputs from the Git and Github
state that triggered the job/workflow.

Typically you want to collect this information once and then re-use it to tag your
build artifacts like Docker images, or you may need to derive other information from it.

## Example usage

```yaml
jobs:
  setup:
    name: Set up the build variables
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.vars.outputs.version }}
      git_hash: ${{ steps.vars.outputs.git_hash }}
    steps:
      - uses: maykinmedia/open-api-workflows/actions/extract-version@refactor/reusable-actions
        id: vars
```
