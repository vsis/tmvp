FROM python:3.9.5-alpine3.13
MAINTAINER Roddy <roddy.gonzalez.89@gmail.com>

# OS libs
RUN apk add zlib-dev jpeg-dev gcc alpine-sdk tesseract-ocr tesseract-ocr-data-spa
RUN mkdir -p /src/app/
WORKDIR /src/app/

# pip/python libs
COPY requirements.txt ./
RUN pip install -r requirements.txt

# app
ADD app/ ./
EXPOSE 80
CMD gunicorn -w 4 -b 0.0.0.0:80 app:app
