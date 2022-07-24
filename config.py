import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

# Gives access to the project in any OS we find ourselves in
# Allows outside files/folders to be added to the project
# from the base directory

class Config():
    """
    Set config variables for the flask app.
    Using enviroment variables where available otherwise
    creat the config variable if not done already.
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOU ARE NOT ALLOWED'
    DEPLOY_DATABASE_URL =  os.environ.get('postgresqlhttps://dashboard.heroku.com/apps/tank-inventory')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turns off update messages from sqlalchemy