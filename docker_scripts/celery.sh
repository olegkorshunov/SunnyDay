#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    celery -A src.tasks.celery:celery_app worker -l INFO
elif [[ "${1}" == "flower" ]]; then
    celery -A src.tasks.celery:celery_app flower
fi
