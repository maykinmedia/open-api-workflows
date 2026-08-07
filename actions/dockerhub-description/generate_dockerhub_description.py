#!/usr/bin/env python
#
# The configuration for the README generation lives in ./config.json
#
# /// script
# dependencies = [
#   "jinja2~=3.1.6",
#   "msgspec~=0.19.0",
#   "requests~=2.32.4",
#   "typer~=0.27.0",
# ]
# ///
#
# Usage from the root of the repository:
#
# .. code-block:: bash
#
#     uv run ./docker/ci/generate_dockerhub_description.py --config-file=<config-file> --output-file=<output-file>
#
import re
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

import msgspec
import requests
import typer
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = typer.Typer()

STABLE_PREFIX = "stable/"
RE_SEMVER_TAG = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
README_TEMPLATE = "dockerhub_readme.md.j2"


class TagConfiguration(msgspec.Struct):
    gitRef: str
    tag: str | None = None


class ProjectConfig(msgspec.Struct):
    supportedTags: list[TagConfiguration]
    dockerOrg: str
    dockerRepo: str
    githubOrg: str
    githubRepo: str
    projectName: str
    projectDocumentation: str
    projectDescription: str
    projectDockerUsageUrl: str = ""


@dataclass
class SupportedTag:
    tag: str
    git_ref: str
    git_org: str
    git_repo: str

    @property
    def dockerfile_url(self) -> str:
        return f"https://github.com/{self.git_org}/{self.git_repo}/blob/{self.git_ref}/Dockerfile"


class DockerReadmeGenerator:
    def __init__(self, config_file: ProjectConfig):
        self.config = self._load_config(config_file)

    def _load_config(self, config_file: Path) -> ProjectConfig:
        raw = config_file.read_bytes()
        try:
            return msgspec.json.decode(raw, type=ProjectConfig)
        except msgspec.ValidationError as exc:
            raise ValueError(f"Invalid configuration in {config_file}: {exc}") from exc
        except msgspec.DecodeError as exc:
            raise ValueError(f"Malformed JSON in {config_file}: {exc}") from exc

    def get_tag_names_on_dockerhub(self) -> list[str]:
        tag_names = []

        def _handle_response(response) -> dict:
            response.raise_for_status()
            response_data = response.json()
            tag_names.extend(tag["name"] for tag in response_data["results"])
            return response_data

        with requests.Session() as session:
            response = session.get(
                f"https://hub.docker.com/v2/namespaces/{self.config.dockerOrg}/repositories/{self.config.dockerRepo}/tags",
                params={"page_size": 10},
            )
            response_data = _handle_response(response)
            while next_page := response_data["next"]:
                response = session.get(next_page)
                response_data = _handle_response(response)

        # filter down to semver tags
        return [name for name in tag_names if RE_SEMVER_TAG.match(name)]

    def get_supported_tags(self) -> Iterator[SupportedTag]:
        tag_configurations = self.config.supportedTags
        existing_tags = self.get_tag_names_on_dockerhub()

        for cfg in tag_configurations:
            git_ref = cfg.gitRef
            is_stable = git_ref.startswith(STABLE_PREFIX)
            inferred_tag = (
                git_ref.replace(STABLE_PREFIX, "", 1) if is_stable else git_ref
            )
            tag = cfg.tag or inferred_tag
            explicit_supported_tag = SupportedTag(
                tag=tag,
                git_ref=git_ref,
                git_org=self.config.githubOrg,
                git_repo=self.config.githubRepo,
            )

            if not is_stable:
                yield explicit_supported_tag
                continue

            # find the most recent concrete tag for the stable version
            major, minor, _ = inferred_tag.split(".")
            matching_tags = [
                t for t in existing_tags if t.startswith(f"{major}.{minor}.")
            ]
            if not matching_tags:
                continue

            most_recent = max(matching_tags, key=lambda t: int(t.rsplit(".", 1)[-1]))

            yield SupportedTag(
                tag=most_recent,
                git_ref=most_recent,
                git_org=self.config.githubOrg,
                git_repo=self.config.githubRepo,
            )
            yield explicit_supported_tag

    def render(self) -> str:
        context = {
            "project_name": self.config.projectName,
            "project_documentation": self.config.projectDocumentation,
            "project_description": self.config.projectDescription,
            "project_docker_usage_url": self.config.projectDockerUsageUrl,
            "github_org": self.config.githubOrg,
            "github_repo": self.config.githubRepo,
            "supported_tags": list(self.get_supported_tags()),
        }
        template_dir = Path(__file__).parent
        env = Environment(
            loader=FileSystemLoader(template_dir), autoescape=select_autoescape()
        )
        template = env.get_template(README_TEMPLATE)
        return template.render(context)

    def write(self, output_file: Path) -> None:
        content = self.render()
        with output_file.open("w") as outfile:
            outfile.write(content)

        typer.echo(f"README file generated at: '{output_file}'")


@app.command()
def main(
    config_file: Annotated[
        Path,
        typer.Option(
            help="Path to the JSON configuration file containing project constants."
        ),
    ] = Path("./docker/ci/config.json"),
    output_file: Annotated[
        Path,
        typer.Option(
            help="Path to the output file where the generated description will be written."
        ),
    ] = Path("./docker/ci/README.md"),
):
    generator = DockerReadmeGenerator(config_file=config_file)
    generator.write(output_file)


if __name__ == "__main__":
    app()
