from . import marshmallow
from .model import Link

class LinkSchema(marshmallow.Schema):
    class Meta:
        fields = ("original_url","date")

url_schema = LinkSchema()