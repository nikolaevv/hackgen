# hackgen

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/nikolaevv/hackgen/blob/main/LICENSE)

Api for fast generating backend & frontend source code for project.
Frontend: https://github.com/nikolaevv/hackgen-web

Now app supports Python / Fast API for backend and React JS for frontend. It can be good instrument for programmer competitions (hackatons, cups, etc) and pet projects.
It uses [own API](https://github.com/nikolaevv/hackgen) for generating code.
It is planned to add support of Django, Flask, Vue and other modern frameworks.

Why it is required service:
- You don't have to waste time for writing thousands lines of similar code
- Using modern light & fast frameworks
- Generated code contains all needful instruments
- It's interface is fast & beautiful

## Install
- Clone repository using `git clone https://github.com/nikolaevv/hackgen`
- Move to this respository: `cd hackgen`
- Run `docker-compose up` for starting docker image

## What does it generate
- Backend
  - `models.py`
  - `schemas.py` (serialization for requests based on models)
  - `crud.py` (Create, read, update & delete operations for models)
  - `main.py` (API controllers based on CRUD operations)
  - `requirements.txt` (auto built dependencies)
- Frontend
  - components (arrow-functional components from list)
  - selectors (special functions for getting objects from redux store)
  - actions (actions of getting one or many objects of all models)
  - query-config (config with all requests, created in API)
