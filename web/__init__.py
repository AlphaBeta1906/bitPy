from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()

@app.errorhandler(400)
def _400(e):
    return jsonify(msg="some data are empty"),400

@app.errorhandler(404)
def _404(e):
    return jsonify(msg="page not found"),404

def run():
    from .config import Config,ConfigProd
    
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    # change to ConfigProd before deploying
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    marshmallow.init_app(app)

    from .routes import bitpy
    from .api import api

    app.register_blueprint(bitpy, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api/v1")
    
    from .model import Link

    return app
    
