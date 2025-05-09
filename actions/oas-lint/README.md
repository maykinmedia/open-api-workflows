# Lint OpenAPI specification

Run the [spectral](https://www.npmjs.com/package/@stoplight/spectral-cli) linter on the
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
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@refactor/reusable-actions
        id: generate
        with:
          artifact-name: my-project-oas

  lint:
    runs-on: ubuntu-latest
    needs:
      - generate

    steps:
      - name: Download generated OAS
        uses: actions/download-artifact@v4
        with:
          name: my-project-oas
      - uses: maykinmedia/open-api-workflows/actions/oas-lint@refactor/reusable-actions
        with:
          schema-path: ${{ needs.generate.outputs.schema-path }}
          node-version-file: '.nvmrc'
          spectral-version: '^6.15.0'
```

Note that if you cleverly combine all the actions that you don't even need to check out
the repository.
