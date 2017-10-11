from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
import random
import re
import string

author = 'Karthik'

doc = """
Simple Game for 2 players
"""


class Constants(BaseConstants):

    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 10
    endowment = '10'


class Subsession(BaseSubsession):

    def creating_session(self):
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
                responder_proposals = [self.session.vars['proposals'][i][i * 10 + 1][1],
                                       self.session.vars['proposals'][i][i * 10 + 2][1], ]
                self.session.vars['result_proposals'].append(responder_proposals)
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
            # random_session_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            self.session.vars['session_code'] = self.session.code
            self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    sent_amount = models.CharField(widget=widgets.RadioSelect(),
                                   doc="""Amount sent by P1""",
                                   choices=['Proposal 1', 'Proposal 2'])
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",
                                        choices=['Accept', 'Reject'])

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        amount_split = re.search('(.*):.*\$(\d).*\$(\d)', p1.participant.vars['proposer_selection'])
        p1_pay = amount_split.group(2)
        p2_pay = amount_split.group(3)
        if self.sent_back_amount == 'Accept':
            if self.round_number == self.session.vars['paying_round']:
                p1.payoff = p1_pay
                p2.payoff = p2_pay
            else:
                p1.payoff = 0
                p2.payoff = 0
        else:
            p1_pay = 0
            p2_pay = 0
            p1.payoff = p1_pay
            p2.payoff = p2_pay
        if self.round_number == 1:
            p2.participant.vars['responded'] = [self.sent_back_amount]
            p1.participant.vars['proposer_payoff'] = [p1_pay]
            p2.participant.vars['responder_payoff'] = [p2_pay]
        else:
            p2.participant.vars['responded'].append(self.sent_back_amount)
            p1.participant.vars['proposer_payoff'].append(p1_pay)
            p2.participant.vars['responder_payoff'].append(p2_pay)


class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'Proposer'
        else:
            return 'Responder'
