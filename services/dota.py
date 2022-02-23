from decimal import Decimal
from sqlalchemy.exc import IntegrityError

from extentions import db
from settings.config import SERVICES, STEAM
from models.dota.service_price import ServicePrice
from models.dota.item import DotaItem


class DotaService:
    @classmethod
    def update_service_price(cls, item_hash_name: str, price: Decimal, service: str):
        if service in SERVICES:
            if service == STEAM:
                price = round(price / 80, 2)
            item = DotaItem.query.filter_by(name=item_hash_name).one_or_none()
            if not item:
                raise Exception(f"No such item {item_hash_name}")
            service_price = ServicePrice.query.filter_by(service=service, item=item).one_or_none()
            if not service_price:
                item.prices.append(ServicePrice(
                    service=service,
                    price=price
                ))
            else:
                service_price.price = price
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
        else:
            raise Exception(f"No such a service {service}")
