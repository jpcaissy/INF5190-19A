import os

import click
from flask.cli import with_appcontext
from peewee import Model, MySQLDatabase, AutoField, CharField, DateTimeField, ForeignKeyField

def get_db():
    return {
        "user": os.environ.get('DB_USER', 'root'),
        "password": os.environ.get('DB_PASSWORD', 'password'),
        "host": os.environ.get('DB_HOST', 'localhost'),
        "port": int(os.environ.get('DB_PORT', '3306')),
    }

class BaseModel(Model):
    class Meta:
        database = MySQLDatabase('poll', **get_db())

class Poll(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(null=False)
    date = DateTimeField()

    def number_of_votes(self):
        return self.vote_casts.count()

    def __str__(self):
        return self.name

class Choice(BaseModel):
    id = AutoField(primary_key=True)
    choice = CharField(null=False)
    poll = ForeignKeyField(Poll, backref="choices")

    def number_of_votes(self):
        return self.vote_casts.count()

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
