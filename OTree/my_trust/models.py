from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c,
)
import random, re

author = 'Karthik'

doc = """
Simple Trust Game for two players
"""


class Constants(BaseConstants):

    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 10

    endowment = c(10)
    multiplication_factor = 1

    instructions_template = 'my_trust/Instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Group(BaseGroup):

    sent_amount = models.CharField(widget=widgets.RadioSelect(),
                                   doc="""Amount sent by P1""",)
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",)

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        amount_split = re.search('A-(\d)points, B-(\d)points', self.sent_amount)
        if self.sent_back_amount == 'Accept':
            p1.payoff = amount_split.group(1)
            p2.payoff = amount_split.group(2)
        else:
            p1.payoff = 0
            p2.payoff = 0
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PRSentAmount'] = self.sent_amount
            self.session.vars['PRSentBackAmount'] = self.sent_back_amount
            self.session.vars['PRPayoffA'] = p1.payoff
            self.session.vars['PRPayoffB'] = p2.payoff


class Player(BasePlayer):
    pass
