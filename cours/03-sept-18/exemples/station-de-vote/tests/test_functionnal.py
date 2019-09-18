from datetime import datetime

import pytest

from poll.models import get_db, Poll, Choice

class TestPoll(object):
    def test_save_inserts_row(self, app):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Nom", date=now)
            p.save()

            new_poll = get_db().execute("SELECT id, name, date FROM polls WHERE id = ?", [1]).fetchone()
            assert new_poll[0] == 1
            assert new_poll[1] == "Nom"
            assert new_poll[2] == str(now)

    def test_save_updates(self, app):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Nom", date=now)
            p.save()

            new_poll = get_db().execute("SELECT id, name, date FROM polls WHERE id = ?", [1]).fetchone()
            assert new_poll[0] == 1
            assert new_poll[1] == "Nom"
            assert new_poll[2] == str(now)

            p.name = "Nouveau nom"
            p.save()

            new_poll = get_db().execute("SELECT name FROM polls WHERE id = ?", [1]).fetchone()
            assert new_poll[0] == "Nouveau nom"

    def test_get_poll_by_id(self, app):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Nom", date=now)
            p.save()

            new_poll = Poll.get_poll_by_id(1)
            assert new_poll.id == 1
            assert new_poll.name == "Nom"
            assert new_poll.date == str(now)

    def test_get_polls(self, app):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Nom", date=now)
            p.save()

            p = Poll(id=None, name="Nom #2", date=now)
            p.save()

            new_poll = Poll.get_polls()

            assert new_poll[0].id == 1
            assert new_poll[0].name == "Nom"
            assert new_poll[0].date == str(now)

            assert new_poll[1].id == 2
            assert new_poll[1].name == "Nom #2"
            assert new_poll[1].date == str(now)

    def test_get_number_of_votes(self, app):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Nom", date=now)
            p.save()

            assert p.number_of_votes() == 0

            c1 = Choice(id=None, choice="Premier choix", poll=p)
            c1.save()

            c2 = Choice(id=None, choice="Deuxième choix", poll=p)
            c2.save()

            assert p.number_of_votes() == 0

            c1.cast_vote()
            c1.cast_vote()
            c2.cast_vote()

            assert p.number_of_votes() == 3


class TestRoutes(object):
    def test_empty_index(self, app, client):
        with app.app_context():
            response = client.get("/")
            assert response.status_code == 200
            assert b"Aucuns sondages actifs" in response.data

    def test_index(self, app, client):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Mon premier sondage", date=now)
            p.save()

            response = client.get("/")
            assert response.status_code == 200
            assert b"Aucuns sondages actifs" not in response.data
            assert b"Mon premier sondage" in response.data
