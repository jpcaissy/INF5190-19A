from poll.models import Poll, Choice, get_db

class PollServices(object):
    @classmethod
    def create_new_poll_from_post_data(cls, post_data, date):
        poll = Poll(
            id=None,
            name=post_data['name'],
            date=date
        )
        poll.save()

        return poll

    @classmethod
    def create_new_choice_for_poll_from_post_data(cls, poll, post_data):
        choice = Choice(
            id=None,
            choice=post_data['choice'],
            poll=poll
        )
        choice.save()

        return choice
