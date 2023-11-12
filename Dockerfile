FROM python:3.8-alpine

WORKDIR /app

RUN apk add make automake gcc g++ subversion python3-dev

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

RUN python server.py
