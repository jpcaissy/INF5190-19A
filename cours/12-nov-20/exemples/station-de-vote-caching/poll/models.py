import os

import click
from flask.cli import with_appcontext
from peewee import Model, MySQLDatabase, AutoField, CharField, DateTimeField, ForeignKeyField
import redis

redis_cache = redis.Redis(host='127.0.0.1', port=6379, db=0)

def get_db():
    return {
        "user": os.environ.get('DB_USER', 'root'),
        "password": os.environ.get('DB_PASSWORD', 'password'),
        "host": os.environ.get('DB_HOST', 'localhost'),
        "port": int(os.environ.get('DB_PORT', '3316')),
    }

class BaseModel(Model):
    class Meta:
        database = MySQLDatabase('poll', **get_db())

class Poll(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(null=False)
    date = DateTimeField()

    def number_of_votes(self):
        cache_key = "poll-total-votes-{0}".format(self.id)
        votes = redis_cache.get(cache_key)

        if votes is not None:
            votes = votes.decode('utf-8')
        else:
            votes = self.vote_casts.count()
            redis_cache.set(cache_key, votes)

        return votes

    def __str__(self):
        return self.name

class Choice(BaseModel):
    id = AutoField(primary_key=True)
    choice = CharField(null=False)
    poll = ForeignKeyField(Poll, backref="choices")

    def number_of_votes(self):
        cache_key = "choice-total-votes-{0}".format(self.id)
        votes = redis_cache.get(cache_key)

        if votes is not None:
            votes = votes.decode('utf-8')
        else:
            votes = self.vote_casts.count()
            redis_cache.set(cache_key, votes)

        return votes

    def __str__(self):
        return self.choice

class VoteCast(BaseModel):
    id = AutoField(primary_key=True)
    poll = ForeignKeyField(Poll, backref="vote_casts")
    choice = ForeignKeyField(Choice, backref="vote_casts")


@click.command("init-db")
@with_appcontext
def init_db_command():
    database = MySQLDatabase('poll', **get_db())
    database.create_tables([Poll, Choice, VoteCast])
    click.echo("Initialized the database.")


def init_app(app):
    app.cli.add_command(init_db_command)
