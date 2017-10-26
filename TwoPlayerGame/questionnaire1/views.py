from . import models
from ._builtin import Page


class Questionnaire(Page):
    form_model = models.Player
    form_fields = ['distressed',
                   'excited',
                   'upset',
                   'scared',
                   'enthusiastic',
                   'alert',
                   'inspired',
                   'nervous',
                   'determined',
                   'afraid',
                   ]


class Welcome(Page):
    pass


page_sequence = [
    Welcome,
    Questionnaire
]
