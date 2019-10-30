FROM python:3.7-alpine

COPY poll /poll
RUN pip install peewee flask

VOLUME /data
EXPOSE 5000
ENV DATABASE /data/db.sqlite
CMD FLASK_DEBUG=1 FLASK_APP=poll flask run --host=0.0.0.0
