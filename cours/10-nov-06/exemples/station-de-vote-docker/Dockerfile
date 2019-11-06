FROM python:3.7-alpine

COPY poll /poll
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install peewee flask pymysql cryptography

EXPOSE 5000
ENV DB_USER root
ENV DB_PASSWORD password
ENV DB_HOST db
CMD FLASK_DEBUG=1 FLASK_APP=poll flask run --host=0.0.0.0
