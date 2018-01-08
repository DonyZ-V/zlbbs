from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from exts import db
from zlbbs import creat_app
from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission

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
        print('成功删除用户 %s' % delete)
    else:
        print('没有删除成功！')


@manager.command
def create_role():
    # 1. 访问者(可以修改个人信息)
    visitor = CMSRole(name='访问者', desc='只能修改相关数据，不能修改。')
    visitor.permissions = CMSPermission.VISITOR

    # 2. 运营角色 (修改个人信息，管理帖子，管理评论，管理前台用户。)
    operator = CMSRole(name='运营', desc='管理帖子，管理评论，管理前台用户。')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER

    # 3. 管理员 (拥有绝大部分权限)
    admin = CMSRole(name='管理员', desc='拥有本系统所有的权限！')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 4. 开发者
    developer = CMSRole(name='开发者',desc='开发人员专用角色。')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor,operator,admin,developer])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
