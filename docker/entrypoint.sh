#!/bin/bash

set -e

if [[ $1 = "webserver" ]]
then
    echo "[ INFO ] Running Python script"
    exec python -u app.py
else
    exec $@
fi
