from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from exts import db
from zlbbs import creat_app
from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser

app = creat_app()

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('用户添加成功')


@manager.option('-del', '--delete', dest='delete')
def delete_cms_user(delete):
    user = CMSUser.query.filter_by(email=delete).first()
    db.session.delete(user)
    db.session.commit()
    if not CMSUser.query.filter_by(email=delete).first():
        print('成功删除用户 %s'  % delete)
    else:
        print('没有删除成功！')


if __name__ == '__main__':
    manager.run()
