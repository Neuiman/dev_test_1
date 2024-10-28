#!/bin/bash

alembic stamp head
alembic revision --autogenerate -m "last"

alembic upgrade head

cd src

uvicorn api:app --reload --host 0.0.0.0 --port 8000

