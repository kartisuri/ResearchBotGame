from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random, re


class Send(Page):

    form_model = models.Group
    form_fields = ['sent_amount']

    def sent_amount_choices(self):
        self.session.vars['amount_list'] = [[5, 3], [5, 2], [5, 1], [4, 2], [4, 1],
                                            [3, 1], [3, 2], [2, 1], [2, 2], [1, 1], ]
        if self.round_number == 1:
            self.session.vars['shuffled_amount_list'] = sorted(self.session.vars['amount_list'],
                                                               key=lambda x: random.random())
        self.session.vars['choice'] = self.session.vars['shuffled_amount_list'][self.round_number - 1]
        self.session.vars['options'] = ['A-' + str((10 - self.session.vars['choice'][0])) + 'points, B-' +
                                        str((self.session.vars['choice'][0])) + 'points', 'A-' +
                                        str((10 - self.session.vars['choice'][1])) + 'points, B-' +
                                        str((self.session.vars['choice'][1])) + 'points', ]
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PROptions'] = self.session.vars['options']
        return self.session.vars['options']

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForP1(WaitPage):
    pass


class WaitForP2(WaitPage):
    pass


class SendBack(Page):

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        recvd_amount = re.search('A-\dpoints, B-(\d)points', self.group.sent_amount).group(1)
        return {
            'choice1': self.session.vars['options'][0],
            'choice2': self.session.vars['options'][1],
            'recvd_amount': recvd_amount,
        }

    def sent_back_amount_choices(self):
        return ['Accept', 'Reject',]


class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'choice1': self.session.vars['PROptions'][0],
            'choice2': self.session.vars['PROptions'][1],
            'payoffA': self.session.vars['PRPayoffA'],
            'payoffB': self.session.vars['PRPayoffB'],
            'sent_amount': self.session.vars['PRSentAmount'],
            'sent_back_amount': self.session.vars['PRSentBackAmount'],
        }


page_sequence = [
    Send,
    WaitForP1,
    SendBack,
    WaitForP2,
    ResultsWaitPage,
    Results,
]
