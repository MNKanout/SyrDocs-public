FROM ubuntu:latest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

# install dependencies
RUN apt-get update \
    && apt-get -y install python3-pip python3-dev

# install dependencies
RUN pip3 install -r requirements.txt