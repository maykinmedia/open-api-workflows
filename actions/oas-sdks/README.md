# Generate SDKs from the OpenAPI specification

Given an OpenAPI specification, generate SDKs in a variety of languages/frameworks.

This action helps ensure that the API specification can be used for code generation in
popular frameworks/stacks.

## Example usage

```yaml
jobs:
  generate:
    runs-on: ubuntu-latest

    outputs:
      schema-path: ${{ steps.generate.outputs.schema-path }}

    steps:
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@refactor/reusable-actions
        id: generate
        with:
          artifact-name: my-project-oas

  sdks:
    runs-on: ubuntu-latest
    needs:
      - generate

    steps:
      - name: Download generated OAS
        uses: actions/download-artifact@v4
        with:
          name: my-project-oas
      - uses: maykinmedia/open-api-workflows/actions/oas-sdks@refactor/reusable-actions
        with:
          schema-path: ${{ needs.generate.outputs.schema-path }}
          node-version-file: '.nvmrc'
          spectral-version: '^6.15.0'
```

Note that if you cleverly combine all the actions that you don't even need to check out
the repository.

## Maintenance

The `openapitools.json` file is used for the default configuration. It is not
automatically loaded, but kept as a separate file so there's a least syntax highlighting
and syntax checking in editors. Make sure to copy it into the `action.yml` after making
changes. Be careful to escape dollar signs where needed!

Periodically you can check if there are new generator versions:

```bash
openapi-generator-cli version-manager list
```
