from flask import Blueprint, request, abort

from models.dota.item import DotaItem
from api.dota.validators import all_items_schema

items_route = Blueprint("items", __name__, url_prefix="/items")


@items_route.route("/<int:item_id>")
def get_item_by_id(item_id: int):
    item = DotaItem.query.filter_by(id=item_id).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict


@items_route.route("/<item_hash_name>")
def get_item_by_name(item_hash_name: str):
    item = DotaItem.query.filter_by(name=item_hash_name).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict


@items_route.route("/all/")
def get_all_items():
    all_items_schema.validate(request.args)
    offset = request.args.get("offset", 0)
    limit = request.args.get("limit", 1000)
    items = DotaItem.query
    return {
        "total_count": items.count(),
        "limit": limit,
        "offset": offset,
        "items": [{
            "name": item.name,
            "id": item.id,
        } for item in items.offset(offset).limit(limit)]
    }
