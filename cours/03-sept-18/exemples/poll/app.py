import os
from datetime import datetime

from flask import Flask, request, redirect, url_for, abort

from models import init_app, Poll, Choice
from services import PollServices
import views

app = Flask("poll", instance_relative_config=True)
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, "db.sqlite"),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass
init_app(app)

@app.route('/')
def index():
    polls = Poll.get_polls()
    if polls:
        return views.index(polls)
    else:
        return views.index_empty()

@app.route('/polls/new', methods=['GET'])
def polls_new():
    poll = Poll(None, '', None)
    return views.new_poll(poll)

@app.route('/polls/new', methods=['POST'])
def polls_create():
    poll = PollServices.create_new_poll_from_post_data(request.form, datetime.now())

    return redirect(url_for('poll', poll_id=poll.id))


@app.route('/polls/<int:poll_id>', methods=['GET'])
def poll(poll_id):
    poll = Poll.get_poll_by_id(poll_id)
    if not poll:
        return abort(404)

    choices = Choice.get_choices_for_poll(poll)
    return views.view_poll(poll, choices)

@app.route('/polls/<int:poll_id>/choices/new', methods=['POST'])
def choice_create(poll_id):
    poll = Poll.get_poll_by_id(poll_id)
    if not poll:
        return abort(404)

    choice = PollServices.create_new_choice_for_poll_from_post_data(poll, request.form)
    return redirect(url_for('poll', poll_id=poll.id))

@app.route('/polls/<int:poll_id>/vote', methods=['POST'])
def poll_vote(poll_id):
    poll = Poll.get_poll_by_id(poll_id)
    if not poll:
        return abort(404)

    choice_id = request.form['choice_id']
    choice = Choice.get_by_id_for_poll(poll, choice_id)
    if not choice:
        return abort(404)

    choice.cast_vote()

    return redirect(url_for('poll', poll_id=poll.id))
