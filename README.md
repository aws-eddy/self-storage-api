## Self Storage API

Activate the virtual environment `mypy` by running:
`source mypy/bin/activate`

To start running the development server run
`fastapi dev`

### Database setup
We don't talk to database directly, instead we talk to a database management system to talk to the database directly.

DBMS: Postgresql is going to be used in this project

psycopg3: postgres driver

Starting database