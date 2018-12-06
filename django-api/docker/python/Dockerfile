FROM python:3.7
MAINTAINER: emirdelictbf@gmail.com

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY ./app /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
