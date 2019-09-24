import os

import click
from flask.cli import with_appcontext
from peewee import Model, SqliteDatabase, AutoField, CharField, DateTimeField, ForeignKeyField

def get_db_path():
    return os.environ.get('DATABASE', './db.sqlite')

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(get_db_path())

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
    database = SqliteDatabase(get_db_path())
    database.create_tables([Poll, Choice, VoteCast])
    click.echo("Initialized the database.")


def init_app(app):
    app.cli.add_command(init_db_command)
