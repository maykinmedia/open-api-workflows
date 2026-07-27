# Lint OpenAPI specification

Run the [vacuum](https://github.com/daveshanley/vacuum) linter on the
specified OpenAPI specification.

This action deliberately does not use the existing github action, as it appears to not
be maintained.

## Example usage

```yaml
jobs:
  generate:
    runs-on: ubuntu-latest

    outputs:
      schema-path: ${{ steps.generate.outputs.schema-path }}

    steps:
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@f3918649c67da9bc96991ce64cdbb760b9fed28e  # v6.3.3
        id: generate
        with:
          artifact-name: my-project-oas

  lint:
    runs-on: ubuntu-latest
    needs:
      - generate

    steps:
      - name: Download generated OAS
        uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          name: my-project-oas
      - uses: maykinmedia/open-api-workflows/actions/oas-lint@f3918649c67da9bc96991ce64cdbb760b9fed28e  # v6.3.3
        with:
          schema-path: ${{ needs.generate.outputs.schema-path }}
          node-version-file: '.nvmrc'
          vacuum-version: '0.30.0'
```

Note that if you cleverly combine all the actions that you don't even need to check out
the repository.
