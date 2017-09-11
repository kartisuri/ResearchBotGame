from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
import random
import re

author = 'Karthik'

doc = """
Simple Trust Game for 2 players
"""


class Constants(BaseConstants):

    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 10

    endowment = '$10'
    multiplication_factor = 1

    instructions_template = 'my_trust/Instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):

        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
        # self.group_randomly()


class Group(BaseGroup):

    sent_amount = models.CharField(widget=widgets.RadioSelect(),
                                   doc="""Amount sent by P1""",)
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by P2""",)

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if self.sent_back_amount == 'Accept':
            amount_split = re.search('(.*)\:.*\$(\d).*\$(\d)', self.sent_amount)
            p1.payoff = amount_split.group(2)
            p2.payoff = amount_split.group(3)
        else:
            p1.payoff = 0
            p2.payoff = 0
        if self.round_number == self.session.vars['paying_round']:
            print("Before<<<<<<%s\n<<<<<<<%s\n<<<<<<<<<%s\n<<<<<<<<<<<<%s\n"%(self.sent_amount, self.sent_back_amount,
                                                                        p1.payoff, p2.payoff))
            self.session.vars['PR_proposer_selection'] = self.sent_amount
            self.session.vars['PR_responder_selection'] = self.sent_back_amount
            self.session.vars['PR_proposer_payoff'] = p1.payoff
            self.session.vars['PR_responder_payoff'] = p2.payoff
            print("Session<<<<<<%s\n<<<<<<<%s\n<<<<<<<<<%s\n<<<<<<<<<<<<%s\n" % (self.session.vars[
                                                                                     'PR_proposer_selection'],
                                                                                 self.session.vars[
                                                                                     'PR_responder_selection'],
                                                                                 self.session.vars[
                                                                                     'PR_proposer_payoff'],
                                                                                 self.session.vars[
                                                                                     'PR_responder_payoff']))

class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return 'Proposer'
        else:
            return 'Responder'
