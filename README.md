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

      django-settings-module: 'project.conf.ci'
      django-secret-key: dummy

  some-other-stuff:
    run: ...
```
