from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()

def run():
    from .config import Config
    
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from .routes import bitpy

    app.register_blueprint(bitpy, url_prefix="/")
    
    from .model import Link

    return app
    
