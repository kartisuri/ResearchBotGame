from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)


author = 'Karthik'

doc = """
Questionnaire 1
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    distressed = models.PositiveIntegerField(verbose_name='1. Distressed',
                                             choices=[[1, 'Very Slightly or Not at All'],
                                                      [2, 'A Little'], [3, 'Moderately'],
                                                      [4, 'Quite a Bit'], [5, 'Extremely']],
                                             widget=widgets.RadioSelectHorizontal())

    excited = models.PositiveIntegerField(verbose_name='2. Excited',
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    upset = models.PositiveIntegerField(verbose_name='3. Upset',
                                        choices=[[1, 'Very Slightly or Not at All'],
                                                 [2, 'A Little'], [3, 'Moderately'],
                                                 [4, 'Quite a Bit'], [5, 'Extremely']],
                                        widget=widgets.RadioSelectHorizontal())

    scared = models.PositiveIntegerField(verbose_name='4. Scared',
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())

    enthusiastic = models.PositiveIntegerField(verbose_name='5. Enthusiastic',
                                               choices=[[1, 'Very Slightly or Not at All'],
                                                        [2, 'A Little'], [3, 'Moderately'],
                                                        [4, 'Quite a Bit'], [5, 'Extremely']],
                                               widget=widgets.RadioSelectHorizontal())

    alert = models.PositiveIntegerField(verbose_name='6. Alert',
                                        choices=[[1, 'Very Slightly or Not at All'],
                                                 [2, 'A Little'], [3, 'Moderately'],
                                                 [4, 'Quite a Bit'], [5, 'Extremely']],
                                        widget=widgets.RadioSelectHorizontal())

    inspired = models.PositiveIntegerField(verbose_name='7. Inspired',
                                           choices=[[1, 'Very Slightly or Not at All'],
                                                    [2, 'A Little'], [3, 'Moderately'],
                                                    [4, 'Quite a Bit'], [5, 'Extremely']],
                                           widget=widgets.RadioSelectHorizontal())

    nervous = models.PositiveIntegerField(verbose_name='8. Nervous',
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    determined = models.PositiveIntegerField(verbose_name='9. Determined',
                                             choices=[[1, 'Very Slightly or Not at All'],
                                                      [2, 'A Little'], [3, 'Moderately'],
                                                      [4, 'Quite a Bit'], [5, 'Extremely']],
                                             widget=widgets.RadioSelectHorizontal())

    afraid = models.PositiveIntegerField(verbose_name='10. Afraid',
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())
