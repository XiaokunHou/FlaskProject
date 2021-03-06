import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bcrypt import Bcrypt
#from flask_babelex import Babel
from flask.ext.babel import Babel

app=Flask(__name__,template_folder='templates')

app.config.from_object('config')
csrf=CsrfProtect(app)
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)
babel=Babel(app)

@babel.localeselector
def get_locale():
    #print request.accept_languages.best_match(LANGUAGES.keys())
    return 'zh_CN'


from iInvest import trustProductView, articleView, assetManagementView, views
from iInvest.manage import views
