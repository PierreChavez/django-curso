FROM python:3.9.19-slim as runtime
LABEL authors="PierreChavez"

WORKDIR /usr/src/envs

RUN python3 -m venv env1 && . /usr/src/envs/env1/bin/activate && pip install django

WORKDIR /usr/src/app

COPY . .