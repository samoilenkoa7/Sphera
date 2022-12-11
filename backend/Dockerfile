FROM ubuntu

MAINTAINER Artur Kryshka "samoilenkoa7@gmail.com"
RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3.10-dev

COPY . ./app
WORKDIR /app
RUN pip3 install -r requirements.txt