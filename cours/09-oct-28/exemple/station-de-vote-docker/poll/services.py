from poll.models import Poll, Choice, VoteCast

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

        vote = VoteCast.create(
            poll=choice.poll,
            choice=choice
        )

        return vote
