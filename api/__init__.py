from flask import Blueprint
from api import dota

dota_routes = Blueprint("dota", __name__, url_prefix="/570/")

dota_routes.register_blueprint(dota.items.items_route)
dota_routes.register_blueprint(dota.heroes.heroes_route)
