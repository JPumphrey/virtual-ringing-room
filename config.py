import os
import datetime
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 's7WUt93.ir_bFya7'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'filesystem'

    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days = 1)

    FLATPAGES_ROOT = 'blog/'

    FLATPAGES_EXTENSION = '.md'
