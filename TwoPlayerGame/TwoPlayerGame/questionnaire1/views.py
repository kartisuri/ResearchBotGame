from . import models
from ._builtin import Page


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
    Questionnaire
]
