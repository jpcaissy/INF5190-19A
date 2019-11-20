import redis

from poll.models import Poll, Choice, VoteCast

redis_cache = redis.Redis(host='127.0.0.1', port=6379, db=0)

class PollServices(object):
    @classmethod
    def create_new_poll_from_post_data(cls, post_data, date):
        poll = Poll.create(
            name=post_data['name'],
            date=date
        )

        return poll

    @classmethod
    def create_new_choice_for_poll_from_post_data(cls, poll, post_data):
        choice = Choice.create(
            choice=post_data['choice'],
            poll=poll
        )

        return choice

    @classmethod
    def cast_vote_from_post_data(cls, poll_id, post_data):
        choice = Choice.get(Choice.poll_id == poll_id, Choice.id == post_data['choice_id'])
        redis_cache.delete("poll-total-votes-{0}".format(poll_id))
        redis_cache.delete("choice-total-votes-{0}".format(choice.id))

        vote = VoteCast.create(
            poll=choice.poll,
            choice=choice
        )

        return vote
