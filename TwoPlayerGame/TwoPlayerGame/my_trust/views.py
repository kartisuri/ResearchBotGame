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
        self.session.vars['options'] = ['Proposal 1: I receive $' + str((10 - self.session.vars['choice'][0])) +
                                        '; the Responder receives $' + str((self.session.vars['choice'][0])),
                                        'Proposal 2: I receive $' + str((10 - self.session.vars['choice'][1])) +
                                        '; the Responder receives $' + str((self.session.vars['choice'][1]))]
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PR_proposer_options'] = self.session.vars['options']
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
        proposer_selection_grouping = re.search('(.*)\:.*\$(\d).*\$(\d)', self.group.sent_amount)
        proposer_selection = proposer_selection_grouping.group(1) + ': He/She receives ' +\
                             proposer_selection_grouping.group(2) + '; You receive ' +\
                             proposer_selection_grouping.group(3)
        proposer_option1_grouping = re.search('(.*)\:.*\$(\d).*\$(\d)', self.session.vars['options'][0])
        proposer_option1 = proposer_option1_grouping.group(1) + ': He/She receives ' + \
                             proposer_option1_grouping.group(2) + '; You receive ' + \
                             proposer_option1_grouping.group(3)
        proposer_option2_grouping = re.search('(.*)\:.*\$(\d).*\$(\d)', self.session.vars['options'][1])
        proposer_option2 = proposer_option2_grouping.group(1) + ': He/She receives ' + \
                           proposer_option2_grouping.group(2) + '; You receive ' + \
                           proposer_option2_grouping.group(3)
        return {
            'proposer_option1': proposer_option1,
            'proposer_option2': proposer_option2,
            'proposer_selection': proposer_selection,
        }

    def sent_back_amount_choices(self):
        return ['Accept', 'Reject',]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'proposer_option1': self.session.vars['PR_proposer_options'][0],
            'proposer_option2': self.session.vars['PR_proposer_options'][1],
            'proposer_payoff': self.session.vars['PR_proposer_payoff'],
            'responder_payoff': self.session.vars['PR_responder_payoff'],
            'proposer_selection': self.session.vars['PR_proposer_selection'],
            'responder_selection': self.session.vars['PR_responder_selection'],
        }


page_sequence = [
    # Instructions,
    Send,
    WaitForP1,
    SendBack,
    WaitForP2,
    ResultsWaitPage,
    Results,
]
