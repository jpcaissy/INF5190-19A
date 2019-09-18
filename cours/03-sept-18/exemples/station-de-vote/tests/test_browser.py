import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import url_for
import pytest

from poll.models import get_db

@pytest.mark.skipif('BROWSER_TEST' not in os.environ, reason="Browser tests will only run with --driver specified")
@pytest.mark.usefixtures('live_server')
class TestBrowser(object):
    def test_create_new_poll(self, selenium, app):
        wait = WebDriverWait(selenium, 10)

        response = selenium.get(url_for('index', _external=True))
        el = wait.until(EC.element_to_be_clickable((By.ID, 'new-poll')))
        el.click()

        el = wait.until(EC.element_to_be_clickable((By.NAME, 'name')))
        el.send_keys("Mon premier sondage")
        el = selenium.find_elements_by_tag_name("button")[0]
        el.click()

        el = wait.until(EC.element_to_be_clickable((By.NAME, 'choice')))
        el.send_keys("Mon premier choix")
        el = selenium.find_elements_by_id("add-choice")[0]
        el.click()

        wait.until(EC.element_to_be_clickable((By.NAME, 'choice_id')))

        with app.app_context():
            new_poll = get_db().execute("SELECT id, name FROM polls WHERE id = ?", [1]).fetchone()
            assert new_poll[0] == 1
            assert new_poll[1] == "Mon premier sondage"

            new_choice = get_db().execute("SELECT id, choice FROM choices WHERE poll_id = ?", [1]).fetchone()
            assert new_choice[0] == 1
            assert new_choice[1] == "Mon premier choix"
