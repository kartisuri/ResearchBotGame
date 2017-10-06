from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
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

    interested = models.PositiveIntegerField(verbose_name='1. Interested',
                                             # choices=[1, 2, 3, 4, 5],
                                             choices=[[1, 'Very Slightly or Not at All'],
                                                      [2, 'A Little'], [3, 'Moderately'],
                                                      [4, 'Quite a Bit'], [5, 'Extremely']],
                                             widget=widgets.RadioSelectHorizontal())

    distressed = models.PositiveIntegerField(verbose_name='2. Distressed',
                                             # choices=[1, 2, 3, 4, 5],
                                             choices=[[1, 'Very Slightly or Not at All'],
                                                      [2, 'A Little'], [3, 'Moderately'],
                                                      [4, 'Quite a Bit'], [5, 'Extremely']],
                                             widget=widgets.RadioSelectHorizontal())

    excited = models.PositiveIntegerField(verbose_name='3. Excited',
                                          # choices=[1, 2, 3, 4, 5],
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    upset = models.PositiveIntegerField(verbose_name='4. Upset',
                                        # choices=[1, 2, 3, 4, 5],
                                        choices=[[1, 'Very Slightly or Not at All'],
                                                 [2, 'A Little'], [3, 'Moderately'],
                                                 [4, 'Quite a Bit'], [5, 'Extremely']],
                                        widget=widgets.RadioSelectHorizontal())

    strong = models.PositiveIntegerField(verbose_name='5. Strong',
                                         # choices=[1, 2, 3, 4, 5],
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())

    guilty = models.PositiveIntegerField(verbose_name='6. Guilty',
                                         # choices=[1, 2, 3, 4, 5],
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())

    scared = models.PositiveIntegerField(verbose_name='7. Scared',
                                         # choices=[1, 2, 3, 4, 5],
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())

    hostile = models.PositiveIntegerField(verbose_name='8. Hostile',
                                          # choices=[1, 2, 3, 4, 5],
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    enthusiastic = models.PositiveIntegerField(verbose_name='9. Enthusiastic',
                                               # choices=[1, 2, 3, 4, 5],
                                               choices=[[1, 'Very Slightly or Not at All'],
                                                        [2, 'A Little'], [3, 'Moderately'],
                                                        [4, 'Quite a Bit'], [5, 'Extremely']],
                                               widget=widgets.RadioSelectHorizontal())

    proud = models.PositiveIntegerField(verbose_name='10. Proud',
                                        # choices=[1, 2, 3, 4, 5],
                                        choices=[[1, 'Very Slightly or Not at All'],
                                                 [2, 'A Little'], [3, 'Moderately'],
                                                 [4, 'Quite a Bit'], [5, 'Extremely']],
                                        widget=widgets.RadioSelectHorizontal())

    irritable = models.PositiveIntegerField(verbose_name='11. Irritable',
                                            # choices=[1, 2, 3, 4, 5],
                                            choices=[[1, 'Very Slightly or Not at All'],
                                                     [2, 'A Little'], [3, 'Moderately'],
                                                     [4, 'Quite a Bit'], [5, 'Extremely']],
                                            widget=widgets.RadioSelectHorizontal())

    alert = models.PositiveIntegerField(verbose_name='12. Alert',
                                        # choices=[1, 2, 3, 4, 5],
                                        choices=[[1, 'Very Slightly or Not at All'],
                                                 [2, 'A Little'], [3, 'Moderately'],
                                                 [4, 'Quite a Bit'], [5, 'Extremely']],
                                        widget=widgets.RadioSelectHorizontal())

    ashamed = models.PositiveIntegerField(verbose_name='13. Ashamed',
                                          # choices=[1, 2, 3, 4, 5],
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    inspired = models.PositiveIntegerField(verbose_name='14. Inspired',
                                           # choices=[1, 2, 3, 4, 5],
                                           choices=[[1, 'Very Slightly or Not at All'],
                                                    [2, 'A Little'], [3, 'Moderately'],
                                                    [4, 'Quite a Bit'], [5, 'Extremely']],
                                           widget=widgets.RadioSelectHorizontal())

    nervous = models.PositiveIntegerField(verbose_name='15. Nervous',
                                          # choices=[1, 2, 3, 4, 5],
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    determined = models.PositiveIntegerField(verbose_name='16. Determined',
                                             # choices=[1, 2, 3, 4, 5],
                                             choices=[[1, 'Very Slightly or Not at All'],
                                                      [2, 'A Little'], [3, 'Moderately'],
                                                      [4, 'Quite a Bit'], [5, 'Extremely']],
                                             widget=widgets.RadioSelectHorizontal())

    attentive = models.PositiveIntegerField(verbose_name='17. Attentive',
                                            # choices=[1, 2, 3, 4, 5],
                                            choices=[[1, 'Very Slightly or Not at All'],
                                                     [2, 'A Little'], [3, 'Moderately'],
                                                     [4, 'Quite a Bit'], [5, 'Extremely']],
                                            widget=widgets.RadioSelectHorizontal())

    jittery = models.PositiveIntegerField(verbose_name='18. Jittery',
                                          # choices=[1, 2, 3, 4, 5],
                                          choices=[[1, 'Very Slightly or Not at All'],
                                                   [2, 'A Little'], [3, 'Moderately'],
                                                   [4, 'Quite a Bit'], [5, 'Extremely']],
                                          widget=widgets.RadioSelectHorizontal())

    active = models.PositiveIntegerField(verbose_name='19. Active',
                                         # choices=[1, 2, 3, 4, 5],
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())

    afraid = models.PositiveIntegerField(verbose_name='20. Afraid',
                                         # choices=[1, 2, 3, 4, 5],
                                         choices=[[1, 'Very Slightly or Not at All'],
                                                  [2, 'A Little'], [3, 'Moderately'],
                                                  [4, 'Quite a Bit'], [5, 'Extremely']],
                                         widget=widgets.RadioSelectHorizontal())
