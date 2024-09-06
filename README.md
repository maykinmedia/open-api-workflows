# open-api-workflows
[Reusable workflows](/.github/workflows/) for several open-api related projects.
The workflows consists of several jobs which ran similiar across several different
repositories.

## Usage

```yaml
# ci.yml
jobs:
  stuff:
    run: ...

  open-api-ci:
    uses: maykinmedia/open-api-workflows/.github/workflows/ci.yml@main
    with:
      main-branch: 'main'
      python-version: '3.11'
      docker-image-name: 'repo-owner/repo-name'
      repository-owner: 'repo-owner'

  some-other-stuff:
    run: ...
```

```yaml
# code-quality.yml
jobs:
  stuff:
    run: ...

  open-api-code-quality:
    uses: maykinmedia/open-api-workflows/.github/workflows/code-quality.yml@main
    with:
      apt-packages: 'libgdal-dev gdal-bin'
      python-version: '3.11'
      node-version: '18'
      postgres-version: '12-2.5'

      isort-src-pattern: 'src'
      black-src-pattern: 'src docs'
      flake8-src-pattern: 'src'

      django-settings-module: 'project.conf.ci'
      django-secret-key: dummy

  some-other-stuff:
    run: ...
```

Note that for some workflows, a script is expected to be present in the repository:

| Workflow  | Script |  Usage |
| ------------- | ------------- | ------------- |
| [ci.yml](/.github/workflows/ci.yml)  | /bin/check_requirements.sh  | Checks for missing requirements |
| [code-quality.yml](/.github/workflows/code-quality.yml)  | /bin/check_schema.sh  | Checks for missing changes in the OAS spec(s) |
| [generate-postman-collection.yml](/.github/workflows/generate-postman-collection.yml)  | /bin/generate_postman_collection.sh  | Generates a postman collection from the OAS spec(s) |
| [generate-sdks.yml](/.github/workflows/generate-sdks.yml)  | /bin/generate_sdks.sh  | Generates sdks from the OAS spec(s) |
| [lint-oas.yml](/.github/workflows/lint-oas.yml)  | /bin/lint_oas_files.sh  | Lints the OAS spec(s) |
