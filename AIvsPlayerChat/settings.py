import os
from os import environ
import dj_database_url
import otree.settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # PRODUCTION SERVER CONFIG
# DEBUG = False
# ADMIN_USERNAME = 'admin'
# ADMIN_PASSWORD = 'hello'
# AUTH_LEVEL = 'STUDY'
# DATABASES = {
#     'default': dj_database_url.config(
#         default=r'postgres://postgres@localhost/django_db'
#     )
# }

# DEVELOPMENT and TESTING SERVER CONFIG
DEBUG = True
ADMIN_USERNAME = environ.get('OTREE_USER')
ADMIN_PASSWORD = environ.get('OTREE_PASSWORD')
AUTH_LEVEL = environ.get('OTREE_AUTH')
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

ROOMS = [
    {
        'name': 'ntu_hss_lab_six',
        'display_name': 'HSS Lab 6',
        'participant_label_file': 'participant_label.txt',
    },
]

# don't share this with anybody.
SECRET_KEY = 'r$y$#=fkhiebyt6wk1%bf9$w7anylwt$l1%xb6^5j%u*&hv8#('

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'SGD'
USE_POINTS = False

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [],
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 5.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'AIvsPlayerChat',
        'display_name': "Computer vs Human",
        'num_demo_participants': 2,
        'app_sequence': ['questionnaire1', 'AIvsPlayerChat', 'questionnaire2', 'payment'],
    },
    {
        'name': 'beauty',
        'display_name': "Beauty Game Player vs Player",
        'num_demo_participants': 2,
        'app_sequence': ['beauty', 'payment'],
    },
    {
        'name': 'BeautyAI',
        'display_name': "Beauty Game Bot vs Player",
        'num_demo_participants': 1,
        'app_sequence': ['BeautyAI', 'payment'],
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
