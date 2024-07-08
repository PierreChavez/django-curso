FROM python:3.10-slim as runtime
LABEL authors="PierreChavez"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000