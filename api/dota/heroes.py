from flask import Blueprint, jsonify

from models.dota.hero import Hero

heroes_route = Blueprint("heroes", __name__, url_prefix="/heroes")


@heroes_route.route("/")
def get_heroes_list():
    heroes = Hero.query.all()
    return jsonify([hero.as_dict for hero in heroes])


@heroes_route.route("/<int:hero_id>")
def get_hero_items(hero_id: int):
    hero = Hero.query.filter_by(id=hero_id).one_or_none()
    return {
        "name": hero.name,
        "items": [
            {
                "id": item.id,
                "name": item.name
            } for item in hero.items]
    }
