from sqlalchemy.exc import IntegrityError
from extentions import db
from settings.config import CSMONEY
from models.dota import DotaItem, Hero, ServicePrice, Slot, ItemType, Quality, Rarity


class DotaDataProcessor:
    _expected_fields = ("steamName", "defaultPrice", "quality", "rarity", "slot", "type")

    @classmethod
    def update(cls, data: dict):
        cls._validate(data)
        name = data.get("steamName")
        item = DotaItem.query.filter_by(name=name).one_or_none()
        if not item:
            item = DotaItem(
                name=name,
                quality=Quality(data.get("quality")),
                rarity=Rarity(data.get("rarity")),
                item_type=ItemType(data.get("type")),
                slot=Slot(data.get("slot"))
            )
            heroes = data.get("heroes", None)
            if heroes and len(heroes) > 0:
                hero_name = heroes[0]
                hero = Hero.query.filter_by(name=hero_name).one_or_none()
                if not hero:
                    hero = Hero(name=hero_name)
                    db.session.add(hero)
                item.hero = hero
            db.session.add(item)

        price = ServicePrice.query.filter_by(service=CSMONEY, item=item).one_or_none()
        if not price:
            item.prices.append(ServicePrice(
                service=CSMONEY,
                price=data.get("defaultPrice")
            ))
        else:
            price.price = data.get("defaultPrice")
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    @classmethod
    def _validate(cls, data: dict):
        _error_fields = []
        for field in cls._expected_fields:
            if not data.get(field, None):
                _error_fields.append(field)
        if _error_fields:
            raise Exception(f"Provided not valid data, fields {_error_fields} not exists")
