from . import models
from ._builtin import Page


class Questionnaire(Page):
    form_model = models.Player
    form_fields = ['born_year',
                   'gender',
                   'studies_year',
                   'school',
                   'major',
                   'nationality',
                   'participation',
                   'game_theory',
                   'income'
                   ]


page_sequence = [
    Questionnaire
]
