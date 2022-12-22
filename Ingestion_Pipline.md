# Simple bash CSV to Postgres Ingestion Pipeline


## Requirements

 - `psql` 
 - Access to Postgres DB with tables matching csv's in `data` folder
 - `PGPASSWORD`, `PGUSER`, `PGDATABASE` and optionally `PGHOST` environment vars pointed at Postgres DB


## How to copy CSV data to PG
 - Run  `./csvs_to_pg_via_psql.sh copy`


## Hot to only truncate existing data in PG
 - Run  `./csvs_to_pg_via_psql.sh truncate`


## Help Doc available in bash script
```sh
$> ./csvs_to_pg_via_psql.sh -h
Provides tool to copy csvs to DB
      - copy          -> Truncates and Copies all tables
      - truncate      -> Only truncates tables
      
     Requires  PGUSER, PGPASSWORD and PGDATABASE in env
     Optionally uses PGHOST
```