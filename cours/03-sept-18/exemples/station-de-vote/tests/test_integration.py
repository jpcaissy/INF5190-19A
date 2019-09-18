import pytest

class TestPoll(object):
    def test_create_new_poll(self, app, client):
        with app.app_context():
            response = client.get("/")
            assert response.status_code == 200
            assert b"Aucuns sondages actifs" in response.data

            response = client.get("/polls/new")
            assert response.status_code == 200

            response = client.post("/polls/new", data={"name": "Mon premier sondage"})
            assert response.status_code == 302
            assert response.location == "http://localhost/polls/1"

            response = client.get("/polls/1")
            assert response.status_code == 200
            assert b'Mon premier sondage' in response.data
