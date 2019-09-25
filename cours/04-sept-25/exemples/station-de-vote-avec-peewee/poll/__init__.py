import os
from datetime import datetime

from peewee import DoesNotExist
from flask import Flask, request, redirect, url_for, abort

from poll.models import init_app, Poll, Choice
from poll.services import PollServices
from poll import views

def create_app(initial_config=None):
    app = Flask("poll")
    init_app(app)

    @app.route('/')
    def index():
        polls = Poll.select()
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
        poll = Poll.get_or_none(Poll.id == poll_id)
        if not poll:
            return abort(404)

        return views.view_poll(poll)

    @app.route('/polls/<int:poll_id>/choices/new', methods=['POST'])
    def choice_create(poll_id):
        poll = Poll.get_or_none(Poll.id == poll_id)
        if not poll:
            return abort(404)

        choice = PollServices.create_new_choice_for_poll_from_post_data(poll, request.form)
        return redirect(url_for('poll', poll_id=poll.id))

    @app.route('/polls/<int:poll_id>/vote', methods=['POST'])
    def poll_vote(poll_id):
        try:
            vote = PollServices.cast_vote_from_post_data(poll_id, request.form)
        except DoesNotExist:
            return abort(404)

        return redirect(url_for('poll', poll_id=vote.poll.id))

    return app
