# open-api-workflows
[Reusable workflows](/.github/workflows/) for several open-api related projects.
The workflows consists of several jobs which ran similiar across several different
repositories.

## Usage

```yaml
jobs:
  stuff:
    run: ...

  open-api-ci:
    uses: maykinmedia/open-api-workflows/.github/workflows/ci.yml@main
    with:
      main-branch: 'main'
      python-version: '3.11'

  some-other-stuff:
    run: ...
```

Note that for some workflows, a script is expected to be present in the repository:

| Workflow  | Script |  Usage |
| ------------- | ------------- | ------------- |
| ci.yml  | /bin/check_requirements.sh  | Checks for missing requirements |
| code-quality.yml  | /bin/check_schema.sh  | Checks for missing changes in the OAS spec(s) |
| generate-postman-collection.yml  | /bin/generate_postman_collection.sh  | Generates a postman collection from the OAS spec(s) |
| generate-sdks.yml  | /bin/generate_sdks.sh  | Generates sdks from the OAS spec(s) |
| lint-oas.yml  | /bin/lint_oas_files.sh  | Lints the OAS spec(s) |
