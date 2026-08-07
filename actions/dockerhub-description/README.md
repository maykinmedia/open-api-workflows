# Generate Dockerhub Description

This composite action generates a Docker Hub repository description from a JSON configuration file, rendered through a Jinja2 template.

## Example usage

```yaml
- uses: actions/checkout@<ref>

- name: Generate README
  uses: maykinmedia/open-api-workflows/actions/dockerhub-description@<ref>
  with:
    config-file: './docker/ci/config.json'
    output-file: './docker/ci/README.md'
```

- `config-file`: Path in your project to the JSON file with project configurations. Default: `./docker/ci/config.json`.
- `output-file`: Path in your project where the rendered README will be written. Default: `./docker/ci/README.md`.

Both paths are resolved relative to your project's repository, not to `open-api-workflows`, make sure `actions/checkout` runs before this step and that `config-file` exists at that path.
