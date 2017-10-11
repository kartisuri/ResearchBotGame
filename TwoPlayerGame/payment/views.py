from ._builtin import Page


class Payment(Page):

    def vars_for_template(self):
        return {
            'label': self.participant.label,
            'payoff': self.participant.payoff,
            'fee': self.session.config.get('participation_fee'),
            'total': self.participant.payoff + self.session.config.get('participation_fee'),
            'code': self.participant.code
        }


page_sequence = [
    Payment
]
