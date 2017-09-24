from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otree.api import Currency as c
import random
import requests
import re


class Send(Page):

    form_model = models.Group
    form_fields = ['sent_amount']

    def vars_for_template(self):
        self.session.vars['proposals'] = {1: {11: ['5', '5'], 12: ['7', '3']},
                                          2: {21: ['5', '5'], 22: ['8', '2']},
                                          3: {31: ['5', '5'], 32: ['9', '1']},
                                          4: {41: ['6', '4'], 42: ['8', '2']},
                                          5: {51: ['6', '4'], 52: ['9', '1']},
                                          6: {61: ['7', '3'], 62: ['9', '1']},
                                          7: {71: ['7', '3'], 72: ['8', '2']},
                                          8: {81: ['8', '2'], 82: ['9', '1']},
                                          9: {91: ['8', '2'], 92: ['8', '2']},
                                          10: {101: ['9', '1'], 102: ['9', '1']}, }
        self.session.vars['choices_list'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.round_number == 1:
            self.session.vars['shuffled_choices_list'] = sorted(self.session.vars['choices_list'],
                                                                key=lambda x: random.random())
            self.session.vars['result_proposals'] = []
            for i in self.session.vars['shuffled_choices_list']:
                responder_proposals = [self.session.vars['proposals'][i][i*10+1][1],
                                       self.session.vars['proposals'][i][i*10+2][1], ]
                self.session.vars['result_proposals'].append(responder_proposals)
        choice = self.session.vars['shuffled_choices_list'][self.round_number - 1]
        option = [self.session.vars['proposals'][choice][choice * 10 + 1],
                  self.session.vars['proposals'][choice][choice * 10 + 2], ]
        self.session.vars['option_str'] = ['Proposal 1: I receive $' + option[0][0] +
                                           '; the Responder receives $' + option[0][1],
                                           'Proposal 2: I receive $' + option[1][0] +
                                           '; the Responder receives $' + option[1][1], ]
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PR_proposer_options'] = self.session.vars['option_str']
        # requests.post('http://172.23.206.99:6000/', json={'round_proposals': {str(self.round_number):
        #                                                                       self.session.vars['option_str']}})
        requests.post('http://192.168.99.1:6000/', json={'round_proposals': {str(self.round_number):
                                                                                 [option[0][1], option[1][1]]}})
        return {
            'proposer_option1': self.session.vars['option_str'][0],
            'proposer_option2': self.session.vars['option_str'][1],
            'round_number': self.round_number,
        }

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
        if self.group.sent_amount == 'Proposal1':
            self.session.vars['proposer_selection'] = self.session.vars['option_str'][0]
        else:
            self.session.vars['proposer_selection'] = self.session.vars['option_str'][1]
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PR_proposer_selection'] = self.session.vars['proposer_selection']
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.session.vars['proposer_selection'])
        proposer_selection = selection.group(1) + ': He/She receives $' + selection.group(2) +\
                             '; You receive $' + selection.group(3)
        if self.round_number == 1:
            self.session.vars['proposed'] = [selection.group(3)]
        else:
            self.session.vars['proposed'].append(selection.group(3))
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.session.vars['option_str'][0])
        proposer_option1 = selection.group(1) + ': He/She receives $' + selection.group(2) + '; You receive $' +\
                           selection.group(3)
        selection = re.search("(.*):.*\$(\d).*\$(\d)", self.session.vars['option_str'][1])
        proposer_option2 = selection.group(1) + ': He/She receives $' + selection.group(2) + '; You receive $' +\
                           selection.group(3)

        return {
            'proposer_option1': proposer_option1,
            'proposer_option2': proposer_option2,
            'proposer_selection': proposer_selection,
            'round_number': self.round_number,
        }


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
        for i in self.session.vars['choices_list']:
            if i == 1:
                self.session.vars['proposer_result'] = [[1, c(self.session.vars['proposed'][0]),
                                                         self.session.vars['responded'][0],
                                                         self.session.vars['proposer_payoff'][0]],]
                self.session.vars['responder_result'] = [[1, c(self.session.vars['proposed'][0]),
                                                         self.session.vars['responded'][0],
                                                         self.session.vars['responder_payoff'][0]],]
            else:
                self.session.vars['proposer_result'].append([i, c(self.session.vars['proposed'][i-1]),
                                                             self.session.vars['responded'][i-1],
                                                             self.session.vars['proposer_payoff'][i-1]])
                self.session.vars['responder_result'].append([i, c(self.session.vars['proposed'][i-1]),
                                                              self.session.vars['responded'][i-1],
                                                              self.session.vars['responder_payoff'][i-1]])
        self.session.vars['PR_proposer_payoff'] =\
            self.session.vars['proposer_payoff'][self.session.vars['paying_round']-1]
        self.session.vars['PR_responder_payoff'] =\
            self.session.vars['responder_payoff'][self.session.vars['paying_round'] - 1]
        return {
            'paying_round': self.session.vars['paying_round'],
            'proposer_result': self.session.vars['proposer_result'],
            'responder_result': self.session.vars['responder_result'],
            'proposer_payoff': self.session.vars['PR_proposer_payoff'],
            'responder_payoff': self.session.vars['PR_responder_payoff'],
        }

class Chat(Page):

    timeout_seconds = 300

    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Chat,
    Instructions,
    Send,
    WaitForP1,
    SendBack,
    WaitForP2,
    ResultsWaitPage,
    Results,
]
