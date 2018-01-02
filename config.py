import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_DATABASE = 'zlbbs'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_PORT,DB_DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
