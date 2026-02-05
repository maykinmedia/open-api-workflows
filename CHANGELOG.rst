==============
Change history
==============

v6.2.4 (2026-02-05)
-------------------

**Bugfixes**

* Ensure the latest versions of all Git tags are fetched before pushing the latest version in ``publish.yml``

v6.2.3 (2026-01-23)
-------------------

**Bugfixes**

* Ensure all Git tags are fetched before pushing the latest version in ``publish.yml``

v6.2.2 (2025-12-15)
-------------------

**Bugfixes**

* Re-enable pushing stable tag for latest versions in ``publish.yml``

v6.2.1 (2025-12-02)
-------------------

**Bugfixes**

* Fix duplicated env key in docs build job

v6.2.0 (2025-12-01)
-------------------

**New features**

* Force colored output for docs build

**Maintenance**

* Use composite action for version info extraction
* Move shell script to extract version into its own file
* Disable pushing of ``stable`` tag in ``publish`` workflow (because in its current form, backports would also be pushed as stable)

**Documentation**

* Fix action usage examples tag reference
* Publish ``stable`` docker tag for semver releases

v6.1.0 (2025-11-27)
-------------------

**New features**

* Publish ``stable`` docker tag for semver releases

v6.0.0 (2025-11-17)
-------------------

💥 **Breaking changes**

* Remove obsoleted workflows

  * ``generate-postman-collection.yml``
  * ``generate-sdks.yml``
  * ``lint-oas.yml``
  * ``oas-check.yml``

**Maintenance**

* [#31] Upgrade codeql-action to v4
* [#15] Remove action that creates a OAF PR
* [maykinmedia/open-api-framework#132] Run docs tests via make instead of pytest

v5.3.0 (2025-05-20)
-------------------

* [maykinmedia/open-api-framework#133] Replace ``black`` / ``isort`` / ``flake8`` with ``ruff`` in ``code-quality.yml`` workflow

v5.2.0 (2025-05-19)
-------------------

* Modularize the OAS actions/workflows into a single workflow ``oas.yml``

v5.1.0 (2025-04-17)
-------------------

* Use uv instead of pip for docs build to speed up the job

v5.0.1 (2025-03-17)
-------------------

Bugfixes
* Replace changed-files action with a basic script (changed-files had a security issue recently)

v5.0.0 (2025-03-06)
-------------------

Breaking changes:
* Pass entire generate OAS command as input, this requires the script to be passed via ``schema-command``
  and the options to be passed via ``schema-options``

New features:
* Compile translations before generating OAS to allow generating OAS in Dutch
* Use ``git diff`` to check OAS changes

v4.2.2 (2025-02-27)
-------------------

* Allow passing of different service name to quickstart job

v4.2.1 (2025-02-25)
-------------------

* Wait for uWSGI to be started in quickstart job

v4.2.0 (2025-02-14)
-------------------

* Add quick start job

v4.1.0 (2025-02-10)
-------------------

* Add apt-packages input to docs build

v4 (2025-01-03)
---------------

* add job to create pull requests to update open-api-framework

v3.0.2 (2024-12-20)
-------------------

* Allow passing of settings module to docs job

v3.0.1 (2024-12-20)
-------------------

* Push repo main branch to Docker latest

v3 (2024-11-01)
---------------

* Add trivy image scan

v2 (2024-10-30)
---------------

* Add check OAF version script

v1 (2024-10-04)
---------------

* Initial release
