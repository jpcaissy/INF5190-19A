import os
import tempfile

os.environ['DATABASE'] = ":memory:"

import pytest
from peewee import SqliteDatabase

from poll import create_app
from poll.models import get_db_path, Poll, Choice, VoteCast


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    database = SqliteDatabase(get_db_path())
    database.create_tables([Poll, Choice, VoteCast])

    yield app

    database.drop_tables([Poll, Choice, VoteCast])


@pytest.fixture
def client(app):
    return app.test_client()
