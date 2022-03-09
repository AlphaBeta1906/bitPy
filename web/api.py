from flask import Blueprint,request,jsonify,abort,url_for
from . import db
from .model import Link
from .schema import url_schema
from .routes import get_unique_id

api = Blueprint("api", __name__)

@api.get("/")
def api_index():
    return  jsonify(msg="connected")

@api.get("/url/<unique_id>")
def get_url(unique_id):
    link = Link.query.filter_by(short_url = unique_id).first_or_404()
    return jsonify(_url = url_schema.dump(link),short_url=url_for("route.get_url",unique_id=link.short_url))

@api.post("/add_url")
def add_url():
    data = request.get_json(force=True)
    short_url = None
    try:
        url = data["url"]
        unique_id = get_unique_id()
        add = Link(
        original_url = url,
        short_url = unique_id
        )
        db.session.add(add)
        db.session.commit()
    except KeyError:
        abort(400)
    else:
        return jsonify(msg="sucess add url",unique_id=unique_id)
    """
    """