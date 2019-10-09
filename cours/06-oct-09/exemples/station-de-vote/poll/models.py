import sqlite3

import click
from flask import g
from flask import current_app
from flask.cli import with_appcontext

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])

    return g.db

def close_db(_):
    db = g.get("pop", None)
    if db:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

class Poll(object):
    @classmethod
    def get_poll_by_id(cls, id):
        db = get_db()
        raw_poll = get_db().execute("SELECT id, name, date FROM polls WHERE id = ?", [id]).fetchone()

        if raw_poll:
            return cls(
                id=raw_poll[0],
                name=raw_poll[1],
                date=raw_poll[2],
            )

        return None

    @classmethod
    def get_polls(cls, query=None):
        db = get_db()
        if query:
            sql = "SELECT id, name, date FROM polls WHERE name LIKE '%{0}%' ORDER BY id ASC".format(query)
            raw_polls = get_db().execute(sql).fetchall()
            print("Executing query `{0}`".format(sql))
        else:
            raw_polls = get_db().execute("SELECT id, name, date FROM polls ORDER BY id ASC").fetchall()
        polls = []
        for raw_poll in raw_polls:
            polls.append(cls(
                id=raw_poll[0],
                name=raw_poll[1],
                date=raw_poll[2]
            ))

        return polls

    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

    def save(self):
        db = get_db()
        if self.id == None:
            db.execute("INSERT INTO polls VALUES (null, ?, ?)", [self.name, self.date])
            self.id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        else:
            db.execute("UPDATE polls SET name = ?, date = ? WHERE id = ?", [self.name, self.date, self.id])

        db.commit()

    def number_of_votes(self):
        return get_db().execute("SELECT count(*) FROM vote_casts WHERE poll_id = ?", [self.id]).fetchone()[0]

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<id={id}> {name}".format(id=self.id, name=self.name)


class Choice(object):
    @classmethod
    def get_choices_for_poll(cls, poll):
        db = get_db()
        raw_choices = get_db().execute("SELECT id, choice FROM choices WHERE poll_id = ?", [poll.id]).fetchall()

        choices = []
        for raw_choice in raw_choices:
            choices.append(cls(
                id=raw_choice[0],
                choice=raw_choice[1],
                poll=poll,
            ))

        return choices

    @classmethod
    def get_by_id_for_poll(cls, poll, choice_id):
        db = get_db()
        raw_poll = get_db().execute("SELECT id, choice FROM choices WHERE id = ? and poll_id= ? ", [choice_id, poll.id]).fetchone()

        if raw_poll:
            return cls(
                id=raw_poll[0],
                choice=raw_poll[1],
                poll=poll,
            )

        return None

    def __init__(self, id, choice, poll):
        self.id = id
        self.choice = choice
        self.poll = poll

    def save(self):
        db = get_db()
        if self.id == None:
            db.execute("INSERT INTO choices VALUES (null, ?, ?)", [self.choice, self.poll.id])
            self.id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        else:
            db.execute("UPDATE choices SET choice = ? WHERE id = ?", [self.choice, self.id])

        db.commit()

    def cast_vote(self):
        db = get_db()
        db.execute("INSERT INTO vote_casts VALUES (null, ?, ?)", [self.poll.id, self.id])
        db.commit()

    def number_of_votes(self):
        return get_db().execute("SELECT count(*) FROM vote_casts WHERE choice_id = ?", [self.id]).fetchone()[0]

    def __str__(self):
        return self.choice

    def __repr__(self):
        return "<id={id}> {choice}".format(id=self.id, choice=self.choice)



@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
