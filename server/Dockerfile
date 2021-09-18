FROM python:3.9 as base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    git \
    && apt-get clean

WORKDIR /server

COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM base as development

FROM base as deployment
COPY ./server /server
