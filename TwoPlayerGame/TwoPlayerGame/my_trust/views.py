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
        choice = self.session.vars['shuffled_choices_list'][self.round_number - 1]
        option = [self.session.vars['proposals'][choice][choice * 10 + 1],
                  self.session.vars['proposals'][choice][choice * 10 + 2], ]
        self.participant.vars['option_str'] = ['Proposal 1: I receive $' + option[0][0] +
                                               '; the Responder receives $' + option[0][1],
                                               'Proposal 2: I receive $' + option[1][0] +
                                               '; the Responder receives $' + option[1][1], ]
        if self.round_number == self.session.vars['paying_round']:
            self.participant.vars['PR_proposer_options'] = self.participant.vars['option_str']
        # requests.post('http://127.0.0.1:5000/', json={'round': str(self.round_number),
        #                                               'proposals': [option[0][1], option[1][1]],
        #                                               'session': self.session.vars['session_code']})
        return {
            'proposer_option1': self.participant.vars['option_str'][0],
            'proposer_option2': self.participant.vars['option_str'][1],
            'round_number': self.round_number,
        }

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForP1(WaitPage):
    wait_for_all_groups = True


class WaitForP2(WaitPage):
    wait_for_all_groups = True


class SendBack(Page):
    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        if self.group.sent_amount == 'Proposal 1':
            p1.participant.vars['proposer_selection'] = p1.participant.vars['option_str'][0]
        else:
            p1.participant.vars['proposer_selection'] = p1.participant.vars['option_str'][1]
        if self.round_number == self.session.vars['paying_round']:
            p1.participant.vars['PR_proposer_selection'] = p1.participant.vars['proposer_selection']
        selection = re.search("(.*):.*\$(\d).*\$(\d)", p1.participant.vars['proposer_selection'])
        proposer_selection = selection.group(1) + ': He/She receives $' + selection.group(2) +\
                             '; You receive $' + selection.group(3)
        if self.round_number == 1:
            p1.participant.vars['proposed'] = [selection.group(3)]
        else:
            p1.participant.vars['proposed'].append(selection.group(3))
        selection = re.search("(.*):.*\$(\d).*\$(\d)", p1.participant.vars['option_str'][0])
        proposer_option1 = selection.group(1) + ': He/She receives $' + selection.group(2) + '; You receive $' +\
                           selection.group(3)
        selection = re.search("(.*):.*\$(\d).*\$(\d)", p1.participant.vars['option_str'][1])
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
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        for i in self.session.vars['choices_list']:
            if i == 1:
                p1.participant.vars['proposer_result'] = [[1, c(p1.participant.vars['proposed'][0]),
                                                          p2.participant.vars['responded'][0],
                                                          c(p1.participant.vars['proposer_payoff'][0])]]
                p2.participant.vars['responder_result'] = [[1, c(p1.participant.vars['proposed'][0]),
                                                           p2.participant.vars['responded'][0],
                                                           c(p2.participant.vars['responder_payoff'][0])]]
            else:
                p1.participant.vars['proposer_result'].append([i, c(p1.participant.vars['proposed'][i-1]),
                                                              p2.participant.vars['responded'][i-1],
                                                              c(p1.participant.vars['proposer_payoff'][i-1])])
                p2.participant.vars['responder_result'].append([i, c(p1.participant.vars['proposed'][i-1]),
                                                               p2.participant.vars['responded'][i-1],
                                                               c(p2.participant.vars['responder_payoff'][i-1])])
        p1.participant.vars['PR_proposer_payoff'] =\
            p1.participant.vars['proposer_payoff'][self.session.vars['paying_round']-1]
        p2.participant.vars['PR_responder_payoff'] =\
            p2.participant.vars['responder_payoff'][self.session.vars['paying_round'] - 1]
        return {
            'paying_round': self.session.vars['paying_round'],
            'proposer_result': p1.participant.vars['proposer_result'],
            'responder_result': p2.participant.vars['responder_result'],
            'proposer_payoff': c(p1.participant.vars['PR_proposer_payoff']),
            'responder_payoff': c(p2.participant.vars['PR_responder_payoff']),
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
    Send,
    WaitForP1,
    SendBack,
    WaitForP2,
    ResultsWaitPage,
    Results,
]
