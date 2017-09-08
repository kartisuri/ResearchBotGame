from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c,
)

author = 'Karthik'

doc = """
Simple Trust Game with Chat
"""


class Constants(BaseConstants):

    name_in_url = 'my_trust_with_chat'
    players_per_group = None
    num_rounds = 10

    endowment = c(10)
    multiplication_factor = 1

    instructions_template = 'my_trust_with_chat/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    sent_amount = models.PositiveIntegerField(doc="Offer given to Player")
    sent_back_amount = models.CharField(widget=widgets.RadioSelect(),
                                        doc="""Offer Amount Accepted/Rejected by Player""", )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        if self.sent_back_amount == 'Accept':
            p1.payoff = self.session.vars['sent_amount']
        else:
            p1.payoff = 0


class Player(BasePlayer):
    pass

