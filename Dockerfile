FROM python:3.9.19-slim as runtime
LABEL authors="PierreChavez"

RUN  python3 -m venv envs/test_env
RUN  . envs/test_env/bin/activate

WORKDIR /usr/src/app

COPY . .