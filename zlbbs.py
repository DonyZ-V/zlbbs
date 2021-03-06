from flask import Flask
import config
from exts import db
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp


def creat_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)

    return app


if __name__ == '__main__':
    app = creat_app()
    app.run()
