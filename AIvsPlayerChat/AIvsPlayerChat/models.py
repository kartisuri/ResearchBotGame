from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
import random
import re

author = 'Karthik'

doc = """
Computer vs Player
"""


class Constants(BaseConstants):
    name_in_url = 'AIvsPlayerChat'
    players_per_group = None
    num_rounds = 10
    endowment = '10'


class Subsession(BaseSubsession):

    def creating_session(self):
        self.session.vars['proposals'] = {1: {11: ['5', '5'], 12: ['7', '3'], 'p': [0.5, 0.5]},
                                          2: {21: ['5', '5'], 22: ['8', '2'], 'p': [0.5, 0.5]},
                                          3: {31: ['5', '5'], 32: ['9', '1'], 'p': [0.5, 0.5]},
                                          4: {41: ['6', '4'], 42: ['8', '2'], 'p': [0.5, 0.5]},
                                          5: {51: ['6', '4'], 52: ['9', '1'], 'p': [0.5, 0.5]},
                                          6: {61: ['7', '3'], 62: ['9', '1'], 'p': [0.5, 0.5]},
                                          7: {71: ['7', '3'], 72: ['8', '2'], 'p': [0.5, 0.5]},
                                          8: {81: ['8', '2'], 82: ['9', '1'], 'p': [0.5, 0.5]},
                                          9: {91: ['8', '2'], 92: ['8', '2'], 'p': [0.5, 0.5]},
                                          10: {101: ['9', '1'], 102: ['9', '1'], 'p': [0.5, 0.5]}}
        self.session.vars['choices_list'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.round_number == 1:
            self.session.vars['shuffled_choices_list'] = sorted(self.session.vars['choices_list'],
                                                                key=lambda x: random.random())
            self.session.vars['result_proposals'] = []
            for i in self.session.vars['shuffled_choices_list']:
                responder_proposals = [self.session.vars['proposals'][i][i * 10 + 1][1],
                                       self.session.vars['proposals'][i][i * 10 + 2][1]]
                self.session.vars['result_proposals'].append(responder_proposals)
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
            self.session.vars['session_code'] = self.session.code


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",
                                        choices=['Accept', 'Reject'])
    competent = models.PositiveIntegerField(choices=[[1, 'Very Incompetent'],
                                                     [2, 'Incompetent'], [3, 'Slightly Incompetent'],
                                                     [4, 'Neutral'], [5, 'Slightly Competent'],
                                                     [6, 'Competent'], [7, 'Very Competent']],
                                            widget=widgets.RadioSelectHorizontal())
    ignorant = models.PositiveIntegerField(choices=[[1, 'Very Ignorant'],
                                                    [2, 'Ignorant'], [3, 'Slightly Ignorant'],
                                                    [4, 'Neutral'], [5, 'Slightly Knowledgeable'],
                                                    [6, 'Knowledgeable'], [7, 'Very Knowledgeable']],
                                           widget=widgets.RadioSelectHorizontal())
    responsible = models.PositiveIntegerField(choices=[[1, 'Very Irresponsible'],
                                                       [2, 'Irresponsible'], [3, 'Slightly Irresponsible'],
                                                       [4, 'Neutral'], [5, 'Slightly Responsible'],
                                                       [6, 'Responsible'], [7, 'Very Responsible']],
                                              widget=widgets.RadioSelectHorizontal())
    intelligent = models.PositiveIntegerField(choices=[[1, 'Very Unintelligent'],
                                                       [2, 'Unintelligent'], [3, 'Slightly Unintelligent'],
                                                       [4, 'Neutral'], [5, 'Slightly Intelligent'],
                                                       [6, 'Intelligent'], [7, 'Very Intelligent']],
                                              widget=widgets.RadioSelectHorizontal())
    sensible = models.PositiveIntegerField(choices=[[1, 'Very Foolish'],
                                                    [2, 'Foolish'], [3, 'Slightly Foolish'],
                                                    [4, 'Neutral'], [5, 'Slightly Sensible'],
                                                    [6, 'Sensible'], [7, 'Very Sensible']],
                                           widget=widgets.RadioSelectHorizontal())

    def set_payoffs(self):
        amount_split = re.search('(.*):.*\$(\d).*\$(\d)', self.participant.vars['proposer_selection'])
        payoff = amount_split.group(2)
        if self.sent_back_amount == 'Accept':
            if self.round_number == self.session.vars['paying_round']:
                self.payoff = payoff
            else:
                self.payoff = 0
        else:
            payoff = 0
            self.payoff = payoff
        if self.round_number == 1:
            self.participant.vars['responded'] = [self.sent_back_amount]
            self.participant.vars['responder_payoff'] = [payoff]
        else:
            self.participant.vars['responded'].append(self.sent_back_amount)
            self.participant.vars['responder_payoff'].append(payoff)
