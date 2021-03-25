import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # slack tokens
    SLACK_VERIFICATION_TOKEN = ''
    SLACK_OAUTH_TOKEN = ''
    SLACK_BOT_TOKEN = ''
