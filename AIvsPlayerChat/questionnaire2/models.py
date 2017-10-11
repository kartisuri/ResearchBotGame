from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)


author = 'Karthik'

doc = """
Questionnaire 2
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    born_year = models.PositiveIntegerField(verbose_name='1. In which year you were born?',
                                            min=1970, max=2010)

    gender = models.CharField(verbose_name='2. What is your gender?',
                              choices=['Male',
                                       'Female'],
                              widget=widgets.RadioSelectHorizontal())

    studies_year = models.CharField(verbose_name='3. What year in your university studies are you now?',
                                    choices=['Year 1',
                                             'Year 2',
                                             'Year 3',
                                             'Year 4',
                                             'Masters',
                                             'Ph. D',
                                             'Others'],
                                    widget=widgets.RadioSelectHorizontal())

    school = models.CharField(verbose_name='4. Which school are you in?')

    major = models.CharField(verbose_name='5. What is your major?')

    nationality = models.CharField(verbose_name='6. What is your nationality?')

    participation = models.CharField(verbose_name='7. Have you participated in economic experiments before?',
                                     choices=['Yes',
                                              'No'],
                                     widget=widgets.RadioSelectHorizontal())

    game_theory = models.CharField(verbose_name='8. Have you studied game theory before?',
                                   choices=['Yes',
                                            'No'],
                                   widget=widgets.RadioSelectHorizontal())

    income = models.CharField(verbose_name='9. What is your monthly family income?',
                              choices=['Less than 2500SGD',
                                       'More than 2500SGD and less than 5000SGD',
                                       'More than 5000SGD and less than 8000SGD',
                                       'More than 8000SGD and less than 15000SGD',
                                       'more than 15000SGD and less than 30000SGD',
                                       'more than 30000SGD'],
                              widget=widgets.RadioSelect())
