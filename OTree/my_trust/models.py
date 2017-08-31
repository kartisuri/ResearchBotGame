from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c,
)
import random, pickle

author = 'Karthik'

doc = """
Simple Trust and Ultimatum Game
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
        self.session.vars['amount_list'] = [[5, 3], [5, 2], [5, 1], [4, 2], [4, 1],
                                            [3, 1], [3, 2], [2, 1], [2, 2], [1, 1], ]
        if self.round_number == 1:
            random.shuffle(self.session.vars['amount_list'])


class Group(BaseGroup):

    sent_amount = models.CurrencyField(widget=widgets.RadioSelect(),
                                       doc="""Amount sent by P1""",)
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",)

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if self.sent_back_amount == 'Accept':
            p1.payoff = Constants.endowment - self.sent_amount
            p2.payoff = self.sent_amount * Constants.multiplication_factor
        else:
            p1.payoff = 0
            p2.payoff = 0


class Player(BasePlayer):
    pass
