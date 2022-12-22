# Docs to bring up Take-Home

Clone project and start Postgres
```sh
git clone git@github.com:be-ez/backend-takehome.git 
cd backend-takehome
cp .env.sample .env
echo "starting Postgres"
docker-compose up -d postgres
```

Create Tables via Alembic
```sh
cd api
virtualenv -p `which python3` env
source env/bin/activate
pip install -r requirements.txt
echo "Adding DB URI to env"
export SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://candidate:password123@localhost:5432/takehome"
echo "Adding tables to DB via alembic"
alembic upgrade head
cd ..
```

Populate DB via `csvs_to_pg_via_psql.sh` see [Ingestion Pipeline](./Ingestion_Pipline.md)
```sh
export PGUSER=candidate
export PGPASSWORD=password123
export PGDATABASE=takehome
./csvs_to_pg_via_psql.sh copy
```
Start API via Docker-Compose
```
docker-compose up -d api
```

Start API via Python
```sh
cd api
gunicorn --reload api.wsgi:app
```

# Telegraph Backend Take-home

This repo has all the information you need to complete the take-home assignment. Know that we are excited about you as a candidate, and can't wait to see what you build!

## Requirements

- Complete user stories [1](#1-ingestion-pipeline) & [2](#2-rest-api) using the language and database of your choice
  - **NOTE**: For the database, Postgres running as a docker container is *preferred*. You can use the provided [docker-compose.yml](./docker-compose.yml) file as a starting point. To use it, simply 
    1. Copy [`.env.sample`](./.env.sample) to `.env` and set the values appropriately
    2. Run the database with the command `docker-compose up -d`
- Provide clear documentation
- Any code you write is clear and well organized
- You spend at least 3-4 hours total on the project (but no more than 6-8 hours)

**BONUS** you provide tests

## User Stories

### 1. Ingestion pipeline

Implement a data ingestion pipeline that allows you to ingest the 4 CSV files into your database for use with your REST API (see user story number 2). Provide clear documentation on how to invoke your pipeline (i.e., run this script, invoke this Makefile target, etc.). Assume that the pipeline can be run on demand and it should drop any existing data and reload it from the files.

### 2. REST API

Create an API server that features the following enpoints

* `/equipment` - data from equipment.csv
* `/events` - data from events.csv
* `/locations` - data from locations.csv
* `/waybills` - data from waybills.csv.
* `/waybills/{waybill id}` - should return information about a specific waybill
* `/waybills/{waybill id}/equipment` - should return the equipment associated with a specific waybill
* `/waybills/{waybill id}/events` - should return the events associated with a specific waybill
* `/waybills/{waybill id}/locations` - should return the locations associated with a specific waybill

All the routes should return JSON.

Any event route should allow for filtering by the `posting_date` field

### 3. **BONUS**: Route endpoint

**Note**: This user story is optional, and on an "if-you-have-time" basis.

Provide a * `/waybills/{waybill id}/route` - should return information about the route associated with a specific waybill

### 4. **BONUS**: Parties endpoint

**Note**: This user story is optional, and on an "if-you-have-time" basis.

Provide a * `/waybills/{waybill id}/parties` - should return information about the parties associated with a specific waybill

## Data description

In the [`data/`](./data) are 4 files.

- [`locations.csv`](./data/locations.csv) - a list of locations. The `id` field is the internal, autogenerated ID for each location. 
- [`equipment.csv`](./data/equipment.csv) - a list of equipment (i.e., rail cars). The `id` field is the internal, autogenerated ID for each piece of equipment. The `equipment_id` field should be considered the primary key for creating relations to other files.
- [`events.csv`](./data/events.csv) - a list of tracking events. The `id` field is the internal, autogenerated ID for each tracking event. The field `waybill_id` is a foreign key to the waybills file. The field `location_id` is a foreign key to the locations file. The field `equipment_id` is a foreign key to the equipment file.
- [`waybills.csv`](./data/waybills.csv) - a list of waybills. A waybill is a list of goods being cariied on a rail car. The `origin_id` and `destination_id` are foreign keys to the locations file. The field `equipment_id` is a foreign key to the equipment file. The `id` field is the internal, autogenerated ID for each waybill. The `route` and `parties` fields contain JSON arrays of objects. The `route` field details the rail stations (AKA "scacs") the train will pass through. The `parties` field defines that various companies involved in shipping the item from its origin to its destination (e.g., shippers, etc.).

**NOTE**: All dates are in UTC.

## Scaffold Project

We have provided a sample REST API that you can finish implementing. Please note that using this sample project **IS NOT REQUIRED**. The sample features:

- Python 3.4+
- [Postgres](https://www.postgresql.org) **OR** you can run the database via [Docker](https://www.docker.com) and [Docker-Compose](https://docs.docker.com/compose/) using the provided [`docker-compose.yml`](./docker-compose.yml) file
- [Falcon](https://falcon.readthedocs.io/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org) - database toolkit for Pythion
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - database migrations

The Falcon project scaffold is inspired by [falcon-sqlalchemy-template](https://github.com/tomlaszczuk/falcon-sqlalchemy-template)

### Scaffold Project - Getting Started

#### Installation and setup

1. Fork and clone this repo onto your own computer
2. Start the database server
    **OR**
    1. Copy [`.env.sample`](./.env.sample) to `.env` and set the values appropriately
    2. Run the database with the command `docker-compose up -d`
3. Depending on the values you used in your `.env` file, set the `SQLALCHEMY_DATABASE_URI` environment variable to point to your database. For example,
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql://candidate:password123@localhost:5432/takehome
  ``` 
4. Change directory to the `webapp` directory and run `pip install -r requirements.txt` to install required dependencies
5. In the same directory, run `gunicorn --reload api.wsgi:app` to run the web application

*The API will be exposed locally at http://127.0.0.1:8000*

Run `curl http://127.0.0.1:8000/health/ping` to test your server. It should return the following JSON:

```json
{"ping": "true"}
```

*It is recommended you create a Python virtual environment for running your project*

### Migrations

Again using Alembic is **NOT** required - it is just provided in case you want to use it to work with the database.
#### Alembic example usage 
Add new migrations with

```
alembic revision --autogenerate -m "migration name"
```

Upgrade your database with

```
alembic upgrade head
```