import os

CSRF_ENABLED=True
SECRET_KEY='you-will-nerver-guess'
CSRF_SESSION_KEY='csrf key'

basedir=os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') +
                               '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

BABEL_DEFAULT_LOCALE = 'zh_CN'
BABEL_DEFAULT_TIMEZONE = 'UTC+8:00'