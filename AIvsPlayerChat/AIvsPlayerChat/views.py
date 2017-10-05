from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import Currency as c
import random
import re
import requests
import numpy


class SendBack(Page):
    form_model = models.Player
    form_fields = ['sent_back_amount']

    def before_next_page(self):
        self.player.set_payoffs()

    def vars_for_template(self):
        choice = self.session.vars['shuffled_choices_list'][self.round_number - 1]
        option = [self.session.vars['proposals'][choice][choice * 10 + 1],
                  self.session.vars['proposals'][choice][choice * 10 + 2], ]
        self.participant.vars['option_str'] = ['Proposal 1: I receive $' + option[0][0] +
                                               '; the Responder receives $' + option[0][1],
                                               'Proposal 2: I receive $' + option[1][0] +
                                               '; the Responder receives $' + option[1][1]]
        self.participant.vars['proposer_selection'] = numpy.random.choice(self.participant.vars['option_str'],
                                                                          p=self.session.vars['proposals'][choice]['p'])
        if self.round_number == self.session.vars['paying_round']:
            self.participant.vars['PR_proposer_options'] = self.participant.vars['option_str']
            self.participant.vars['PR_proposer_selection'] = self.participant.vars['proposer_selection']
        requests.post('http://127.0.0.1:5000/', json={'round': str(self.round_number),
                                                      'proposals': [option[0][1], option[1][1]],
                                                      'session': self.session.vars['session_code']})
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.participant.vars['proposer_selection'])
        proposer_selection = selection.group(1) + ': He/She receives $' + selection.group(2) +\
                             '; You receive $' + selection.group(3)
        if self.round_number == 1:
            self.participant.vars['proposed'] = [selection.group(3)]
        else:
            self.participant.vars['proposed'].append(selection.group(3))
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.participant.vars['option_str'][0])
        proposer_option1 = selection.group(1) + ': He/She receives $' + selection.group(2) + '; You receive $' +\
                           selection.group(3)
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.participant.vars['option_str'][1])
        proposer_option2 = selection.group(1) + ': He/She receives $' + selection.group(2) + '; You receive $' +\
                           selection.group(3)

        return {
            'proposer_option1': proposer_option1,
            'proposer_option2': proposer_option2,
            'proposer_selection': proposer_selection,
            'round_number': self.round_number,
        }


class Instructions(Page):

    def is_displayed(self):
        return self.round_number == 1


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        for i in self.session.vars['choices_list']:
            if i == 1:
                self.participant.vars['responder_result'] = [[1, c(self.participant.vars['proposed'][0]),
                                                             self.participant.vars['responded'][0],
                                                             self.participant.vars['responder_payoff'][0]]]
            else:
                self.participant.vars['responder_result'].append([i, c(self.participant.vars['proposed'][i-1]),
                                                                 self.participant.vars['responded'][i-1],
                                                                  self.participant.vars['responder_payoff'][i-1]])
        self.participant.vars['PR_responder_payoff'] =\
            self.participant.vars['responder_payoff'][self.session.vars['paying_round'] - 1]
        return {
            'paying_round': self.session.vars['paying_round'],
            'responder_result': self.participant.vars['responder_result'],
            'responder_payoff': self.participant.vars['PR_responder_payoff'],
        }


class Chat(Page):
    timeout_seconds = 120

    def vars_for_template(self):
        return {'player': self.participant.id_in_session,
                'session': self.session.vars['session_code']}

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    # Chat,
    Instructions,
    SendBack,
    Results,
]
