# BASE IMAGE.
FROM python:3.7-alpine

# MAINTAINER.
MAINTAINER Anubhav Sidhu anubhav231989@gmail.com

# ENVIRONMENT VARIABLES.
ENV PYTHONUNBUFFERED 1

# UPDATE THE BASE IMAGE.
RUN apk update

# INSTALL PYTHON PACKAGES REQUIRED DEPENDENCIES.
RUN apk add --virtual build-deps gcc python3-dev jpeg-dev zlib-dev libjpeg musl-dev libressl-dev libffi-dev

# CREATE APPLICATION DIRECTORY.
RUN mkdir -p /application

# SET WORKDIR.
WORKDIR /application

# COPY REQUIREMENTS.TXT
COPY requirements.txt ./requirements.txt

# INSTALL PYTHON DEPENDENCIES.
RUN pip install -r requirements.txt

# REMOVING BUILD DEPENDENCIES.
## RUN apk del build-deps

# COPY APPLICATION CODE.
COPY . ./application

# EXPOSE PORT.
EXPOSE 9000