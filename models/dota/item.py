from extentions import db
from models.dota.specification import ItemType, Slot, Quality, Rarity


class DotaItem(db.Model):
    __tablename__ = "dota_item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, index=True)
    quality = db.Column(db.Enum(Quality), nullable=False)
    rarity = db.Column(db.Enum(Rarity), nullable=False)
    item_type = db.Column(db.Enum(ItemType), nullable=False)
    slot = db.Column(db.Enum(Slot), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('dota_hero.id'), nullable=True)
    prices = db.relationship("ServicePrice", back_populates="item", lazy="dynamic")

    @classmethod
    def process_csmoney(cls, item_data):
        name = item_data.get("steamName")
        instance = cls.query.filter_by(name=name).one_or_none()

        if not instance:
            instance = cls(name=name)
            # price_instance = instance.prices.filter_by(service=CSMONEY).one_or_none()
            # if price_instance:
            #     price_instance.price = item_data.get("defaultPrice")
            # else:
            #     price_instance = ServicePrice()