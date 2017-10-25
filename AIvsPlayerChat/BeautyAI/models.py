from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Currency as c
)


doc = """
You are randomly matched to play a game against one of the students in this room.
In the game, each of you requests an amount of money (an integer) between 11 and 20 dollars.
Each participant will receive the amount he requests.
A participant will receive an additional 20 dollars if:
(i) he asks for exactly one dollar less than the other player, or
(ii) he asks for 20 dollars and the other player asks for 11 dollars.
You will receive your payment in the next lesson, without knowing against whom you played.
What amount of money do you request?
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'beauty_game_ai'
    bonus = c(20)


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.PositiveIntegerField(max=20, min=11)
    is_bonus = models.PositiveIntegerField(min=0, max=2)

    def set_payoffs(self):
        if self.guess - self.participant.vars['guess'] == -1:
            self.payoff = c(self.guess) + Constants.bonus
            self.is_bonus = 1
        elif self.guess - self.participant.vars['guess'] == 1:
            self.payoff = c(self.guess)
            self.is_bonus = 0
        elif self.guess == 20 and self.participant.vars['guess'] == 11:
            self.payoff = c(self.guess) + Constants.bonus
            self.is_bonus = 2
        elif self.guess == 11 and self.participant.vars['guess'] == 20:
            self.payoff = c(self.guess)
            self.is_bonus = 0
        else:
            self.payoff = c(self.guess)
            self.is_bonus = 0


