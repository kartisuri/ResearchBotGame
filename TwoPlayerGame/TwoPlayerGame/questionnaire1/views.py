from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Instructions(Page):
    pass


class Questionnaire(Page):
    form_model = models.Player
    form_fields = ['interested',
                   'distressed',
                   'excited',
                   'upset',
                   'strong',
                   'guilty',
                   'scared',
                   'hostile',
                   'enthusiastic',
                   'proud',
                   'irritable',
                   'alert',
                   'ashamed',
                   'inspired',
                   'nervous',
                   'determined',
                   'attentive',
                   'jittery',
                   'active',
                   'afraid',
                   ]


page_sequence = [
    # Instructions,
    Questionnaire
]
