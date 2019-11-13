from datetime import datetime

import pytest

from poll.models import Poll, Choice

class TestPoll(object):
    def test_init(self):
        now = datetime.now()
        p = Poll(id=123, name="Nom", date=now)
        assert p.id == 123
        assert p.name == "Nom"
        assert p.date == now

    def test_string(self):
        now = datetime.now()
        p = Poll(id=123, name="Nom", date=now)
        assert str(p) == "Nom"


class TestChoice(object):
    def test_init(self):
        now = datetime.now()
        p = Poll(id=123, name="Nom", date=now)
        c = Choice(id=123, choice="Choix #1", poll=p)
        assert c.id == 123
        assert c.choice == "Choix #1"
        assert c.poll == p

    def test_string(self):
        now = datetime.now()
        p = Poll(id=123, name="Nom", date=now)
        c = Choice(id=123, choice="Choix #1", poll=p)

        assert str(c) == "Choix #1"
