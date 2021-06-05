FROM python:3.9.5-alpine3.13
MAINTAINER Roddy <roddy.gonzalez.89@gmail.com>

# OS libs
RUN apk add zlib-dev jpeg-dev gcc alpine-sdk
RUN mkdir -p /src/app/
WORKDIR /src/app/

# pip/python libs
COPY requirements.txt ./
RUN pip install -r requirements.txt

# app
ADD app/ ./
EXPOSE 5000
CMD flask run --host 0.0.0.0
