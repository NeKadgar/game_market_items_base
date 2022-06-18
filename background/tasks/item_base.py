from decimal import Decimal
from background.celery_app import app as celery_app
from services.csmoney import DotaDataProcessor
from settings.config import SERVICES, CSMONEY
from models.dota.item import DotaItem
from models.dota.hero import Hero
from models.dota.service_price import ServicePrice
from models.dota.specification import Rarity, Quality, ItemType, Slot
from extentions import db


@celery_app.task(name="update_service_price", queue="items_base_queue")
def update_service_price(
        game_id: int,
        item_hash_name: str,
        price: Decimal,
        service: str,
        hero_name: str = None,
        rarity: str = None,
        item_type: str = None,
        slot: str = None,
        quality: str = None
):
    if service not in SERVICES:
        raise f"No such service {service}"
    if game_id == 570:
        item = DotaItem.query.filter_by(name=item_hash_name).one_or_none()
        if not item and service == CSMONEY:
            item = DotaItem(
                name=item_hash_name,
                quality=Quality(quality).name,
                rarity=Rarity(rarity).name,
                item_type=ItemType(item_type).name,
                slot=Slot(slot).name
            )
            hero = Hero.query.filter_by(name=hero_name).one_or_none()
            if not hero and hero_name:
                hero = Hero(
                    name=hero_name
                )
                hero.items.append(item)
                db.session.add(hero)
            else:
                if hero:
                    item.hero_id = hero.id
            db.session.add(item)

        if not item:
            return {
                "error": "Cant update with not cs money"
            }

        service_price = ServicePrice.query.filter_by(service=service, item=item).one_or_none()
        if not service_price:
            service_price = ServicePrice(
                service=service,
                price=price
            )
            item.prices.append(service_price)
        else:
            service_price.price = price
        if service_price:
            db.session.add(service_price)
        db.session.commit()
    elif game_id == 730:
        pass
    else:
        raise Exception("No such a game")
