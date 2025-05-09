# Generate OpenAPI specification

Generate and upload the OpenAPI spefication.

This action takes care of generating the API specification from the code of your
project. Once generated, it is uploaded as an artifact.

## Example usage

```yaml
env:
  DJANGO_SETTINGS_MODULE: myproject.conf.ci

jobs:
  generate:
    name: Generate API specification
    runs-on: ubuntu-latest

    outputs:
      schema-path: ${{ steps.generate.outputs.schema-path }}

    steps:
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@main
        id: generate
        with:
          python-version: '3.12'
          working-directory: backend
          command: bin/generate_api_schema.sh --language en
          artifact-name: openapi-yaml
          schema-path: src/myproject/api/openapi.yaml
```

All inputs are optional, but recommended to specify explicitly.
