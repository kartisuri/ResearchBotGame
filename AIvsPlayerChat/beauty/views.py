from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Guess(Page):
    form_model = models.Player
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        return {
            'player1_guess': c(self.group.get_player_by_id(1).guess),
            'player2_guess': c(self.group.get_player_by_id(2).guess)
        }


page_sequence = [Instructions,
                 Guess,
                 ResultsWaitPage,
                 Results]
