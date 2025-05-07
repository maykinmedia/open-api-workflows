# OpenAPI comparison

Compare the generated API spec with the version tracked in the repository.

The action fails if differences are found, pointing out oversights of the author. This
requires a job or step to have completed for the generation of the API spec, see the
`oas-generate` action.

## Example usage

```yaml
env:
  DJANGO_SETTINGS_MODULE: myproject.conf.ci

jobs:
  generate-and-compare:
    name: Generate API specification
    runs-on: ubuntu-latest

    steps:
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@main
        id: generate
        with:
          working-directory: backend
          artifact-name: openapi-yaml
          schema-path: src/myproject/api/openapi.yaml

      - uses: maykinmedia/open-api-workflows/actions/oas-compare@main
        with:
          working-directory: backend
          artifact-name: openapi-yaml
          schema-path: src/myproject/api/openapi.yaml
```

All inputs are optional, but recommended to specify explicitly.

