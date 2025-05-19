==============
Change history
==============

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
