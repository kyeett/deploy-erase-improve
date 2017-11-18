FROM python:2.7-alpine

ADD ./requirements.txt ./
ADD ./app /app

RUN pip install -r requirements.txt
