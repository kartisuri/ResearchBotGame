from . import models
from ._builtin import Page, WaitPage

import random


class Chat(Page):

    timeout_seconds = 60

    # def is_displayed(self):
    #     return self.round_number == 1


class SendBack(Page):

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        self.session.vars['amount_list'] = [[5, 3], [5, 2], [5, 1], [4, 2], [4, 1],
                                            [3, 1], [3, 2], [2, 1], [2, 2], [1, 1], ]
        if self.round_number == 1:
            self.session.vars['shuffled_amount_list'] = sorted(self.session.vars['amount_list'],
                                                               key=lambda x: random.random())
        self.session.vars['choice'] = self.session.vars['shuffled_amount_list'][self.round_number-1]
        self.session.vars['sent_amount'] = random.choice(self.session.vars['choice'])
        return {
            'sent_amount': self.session.vars['sent_amount']
        }

    def sent_back_amount_choices(self):
        return ['Accept', 'Reject',]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        return {
            'sent_amount': self.session.vars['sent_amount']
        }


page_sequence = [
    Chat,
    SendBack,
    ResultsWaitPage,
    Results,
]
