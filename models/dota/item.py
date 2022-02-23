from extentions import db
from models.dota.specification import ItemType, Slot, Quality, Rarity
from models.dota.service_price import ServicePrice


class DotaItem(db.Model):
    __tablename__ = "dota_item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False, index=True)
    quality = db.Column(db.Enum(Quality), nullable=False)
    rarity = db.Column(db.Enum(Rarity), nullable=False)
    item_type = db.Column(db.Enum(ItemType), nullable=False)
    slot = db.Column(db.Enum(Slot), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('dota_hero.id'), nullable=True)
    prices = db.relationship("ServicePrice", back_populates="item", lazy='select')

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quality": self.quality.value,
            "rarity": self.rarity.value,
            "item_type": self.item_type.value,
            "slot": self.slot.value,
            "hero": self.hero.name if self.hero else None,
            "prices": [service_price.as_dict for service_price in self.prices]
        }
