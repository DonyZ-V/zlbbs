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


CMS_USER_ID = 'QWERASDF'


# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
# 邮箱
MAIL_USERNAME = ""
# 授权码
MAIL_PASSWORD = ""
# 默认和mail_username一样
MAIL_DEFAULT_SENDER = ""
