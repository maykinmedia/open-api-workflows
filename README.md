# open-api-workflows

[Reusable workflows](/.github/workflows/) and [actions](./actions) for projects that
implement an API.

The re-usable workflows compose a number of jobs that should be kept similar across
a multitude of repositories, while the actions provide lower-level building blocks
that are also useful in projects that aren't purely API-focused.

## Usage (workflows)

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
