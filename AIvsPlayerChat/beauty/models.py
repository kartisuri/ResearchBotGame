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
    players_per_group = 2
    num_rounds = 1
    name_in_url = 'beauty_game'
    bonus = c(20)


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p1.guess - p2.guess == -1:
            p1.payoff = c(p1.guess) + Constants.bonus
            p1.is_bonus = 1
            p2.payoff = c(p2.guess)
            p2.is_bonus = 0
        elif p1.guess - p2.guess == 1:
            p1.payoff = c(p1.guess)
            p1.is_bonus = 0
            p2.payoff = c(p2.guess) + Constants.bonus
            p2.is_bonus = 1
        elif p1.guess == 20 and p2.guess == 11:
            p1.payoff = c(p1.guess) + Constants.bonus
            p1.is_bonus = 2
            p2.payoff = c(p2.guess)
            p2.is_bonus = 0
        elif p1.guess == 11 and p2.guess == 20:
            p1.payoff = c(p1.guess)
            p1.is_bonus = 0
            p2.payoff = c(p2.guess) + Constants.bonus
            p2.is_bonus = 2
        else:
            p1.payoff = c(p1.guess)
            p1.is_bonus = 0
            p2.payoff = c(p2.guess)
            p2.is_bonus = 0


class Player(BasePlayer):
    guess = models.PositiveIntegerField(max=20, min=11)
    is_bonus = models.PositiveIntegerField(min=0, max=2)
