from . import models
from ._builtin import Page
import socket


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


class Chat(Page):
    timeout_seconds = 120

    def vars_for_template(self):
        player_label = self.participant.code
        if self.participant.label:
            player_label = self.participant.label
        return {
            'player': player_label,
            'session': self.session.code,
            'ip': [(s.connect(('8.8.8.8', 53)),
                   s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
            }

    def is_displayed(self):
        return self.round_number == 1


class ChatQuestionnaire(Page):
    form_model = models.Player
    form_fields = ['competent',
                   'ignorant',
                   'responsible',
                   'intelligent',
                   'sensible'
                   ]

    def is_displayed(self):
        return self.round_number == 1


class Welcome(Page):
    pass


page_sequence = [
    Welcome,
    Chat,
    ChatQuestionnaire,
    Questionnaire
]
