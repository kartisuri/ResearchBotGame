from ._builtin import Page


class Payment(Page):

    def vars_for_template(self):
        player_label = self.participant.code
        if self.participant.label:
            player_label = self.participant.label
        return {
            'label': player_label,
            'payoff': self.participant.payoff,
            'fee': self.session.config.get('participation_fee'),
            'total': self.participant.payoff + self.session.config.get('participation_fee'),
            'code': self.participant.code
        }


page_sequence = [
    Payment
]

