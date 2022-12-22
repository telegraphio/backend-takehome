#!/bin/bash

help() {
    echo "Provides tool to copy csvs to DB"
    echo "      - copy          -> Truncates and Copies all tables"
    echo "      - truncate      -> Only truncates tables"
    echo "      "
    echo "     Requires  PGUSER, PGPASSWORD and PGDATABASE in env"
    echo "     Optionally uses PGHOST"
    
}

if [[ $# -eq 0 ]] ; then
    help
    exit 0
fi

if [[ ! -v PGUSER ]]; then
    echo "PGUSER is not set"
    exit 1
elif [[ ! -v PGPASSWORD ]]; then
    echo "PGPASSWORD is not set"
    exit 1
elif [[ ! -v PGDATABASE ]]; then
    echo "PGDATABASE is not set"
    exit 1
elif [[ ! -v PGHOST ]]; then
    PGHOST='localhost'
fi


connectionString="postgresql://$PGUSER:$PGPASSWORD@$PGHOST/$PGDATABASE"

truncate() {
    echo "Truncating current data in PG tables"
    psql "${connectionString}" -c "TRUNCATE equipment CASCADE"
    psql "${connectionString}" -c "TRUNCATE locations CASCADE"
    psql "${connectionString}" -c "TRUNCATE events CASCADE"
    psql "${connectionString}" -c "TRUNCATE waybills CASCADE"
}

copydata(){
    echo "Uploading data from client to PG"
    psql "${connectionString}" -c "\copy equipment FROM 'data/equipment.csv' delimiter ',' csv header"
    psql "${connectionString}" -c "\copy locations FROM 'data/locations.csv' delimiter ',' csv header"
    psql "${connectionString}" -c "\copy waybills FROM 'data/waybills.csv' delimiter ',' csv header"
    psql "${connectionString}" -c "\copy events FROM 'data/events.csv' delimiter ',' csv header"
}

for arg in "$@"; do
    if [ "$arg" == "--help" ] || [ "$arg" == "-h" ];  then
        help
        exit 0
    elif [ "$arg" == "truncate" ]; then
        truncate
    elif [ "$arg" == "copy" ]; then
        truncate
        copydata
    else
        echo "Unknown CMD"
        exit 1
    fi
done