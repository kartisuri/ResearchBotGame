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

    name_in_url = 'my_trust_ai'
    players_per_group = None
    num_rounds = 10

    endowment = '10'

    instructions_template = 'AIvsPlayer/Instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):

        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
        # self.group_randomly()


class Group(BaseGroup):

    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",
                                        choices=['Accept', 'Reject'])

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        if self.sent_back_amount == 'Accept':
            amount_split = re.search('(.*)\:.*\$(\d).*\$(\d)', self.session.vars['proposer_selection'])
            p1.payoff = amount_split.group(3)
        else:
            p1.payoff = 0
        if self.round_number == self.session.vars['paying_round']:
            self.session.vars['PR_proposer_selection'] = self.session.vars['proposer_selection']
            self.session.vars['PR_responder_selection'] = self.sent_back_amount
            self.session.vars['PR_responder_payoff'] = p1.payoff


class Player(BasePlayer):
    pass
