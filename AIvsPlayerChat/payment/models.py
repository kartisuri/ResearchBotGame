from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'Karthik'

doc = """
Payment Info
"""


class Constants(BaseConstants):
    name_in_url = 'payment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
