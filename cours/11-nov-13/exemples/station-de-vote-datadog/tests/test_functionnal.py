from datetime import datetime

import pytest

from poll.models import Poll, Choice, VoteCast

class TestPoll(object):
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

            VoteCast.create(
                poll=p,
                choice=c1
            )
            VoteCast.create(
                poll=p,
                choice=c1
            )
            VoteCast.create(
                poll=p,
                choice=c2
            )

            assert p.number_of_votes() == 3


class TestRoutes(object):
    def test_empty_index(self, app, client):
        with app.app_context():
            response = client.get("/")
            assert response.status_code == 200
            assert Poll.select().count() == 0
            assert b"Aucuns sondages actifs" in response.data

    def test_index(self, app, client):
        with app.app_context():
            now = datetime.now()
            p = Poll(id=None, name="Mon premier sondage", date=now)
            p.save()

            response = client.get("/")
            assert Poll.select().count() == 1
            assert response.status_code == 200
            assert b"Aucuns sondages actifs" not in response.data
            assert b"Mon premier sondage" in response.data
