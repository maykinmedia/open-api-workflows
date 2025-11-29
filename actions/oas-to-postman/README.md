# Generate Postman collection from an OpenAPI specification

Take the provided API specification and verify that a Postman collection can be
generated successfully. The collection is uploaded as artifact so you can download and
test it.

## Example usage

```yaml
jobs:
  generate:
    runs-on: ubuntu-latest

    outputs:
      schema-path: ${{ steps.generate.outputs.schema-path }}

    steps:
      - uses: maykinmedia/open-api-workflows/actions/oas-generate@v6
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
      - uses: maykinmedia/open-api-workflows/actions/oas-to-postman@v6
        with:
          schema-path: ${{ needs.generate.outputs.schema-path }}
          node-version-file: '.nvmrc'
          openapi-to-postman-version: '^5.0.0'
```

Note that if you cleverly combine all the actions that you don't even need to check out
the repository.
