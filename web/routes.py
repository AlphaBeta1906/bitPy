from flask import Blueprint,render_template,request,redirect,url_for
from .model import Link
from . import db

bitpy = Blueprint("route", __name__, template_folder="templates")


def get_unique_id():
    import random
    import string

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=4))

@bitpy.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        unique_id = get_unique_id()
        
        add = Link(
        original_url = url,
        short_url = unique_id
        )
        db.session.add(add)
        db.session.commit()
        short_url = unique_id
        return redirect(url_for("route.url",short_url = short_url))
    return render_template("index.jinja")

@bitpy.route("/url/<short_url>")
def url(short_url):
    return render_template("url.jinja",short_url = short_url)


@bitpy.route("/<unique_id>")
def get_url(unique_id):
    link = Link.query.filter_by(short_url = unique_id).first_or_404()
    return redirect(link.original_url)    
