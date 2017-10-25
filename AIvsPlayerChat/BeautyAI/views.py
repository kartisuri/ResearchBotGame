from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c
import random


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Guess(Page):
    form_model = models.Player
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True


class Results(Page):

    def vars_for_template(self):
        self.participant.vars['guess'] = random.randint(11,20)
        self.player.set_payoffs()
        return {
            'player1_guess': c(self.player.guess),
            'player2_guess': c(self.participant.vars['guess'])
        }


page_sequence = [Instructions,
                 Guess,
                 ResultsWaitPage,
                 Results]
