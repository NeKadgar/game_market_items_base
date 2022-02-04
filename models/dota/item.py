from extentions import db
from models.dota.specification import ItemType, Slot, Quality, Rarity


class DotaItem(db.Model):
    __tablename__ = "dota_item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False, index=True)
    quality = db.Column(db.Enum(Quality), nullable=False)
    rarity = db.Column(db.Enum(Rarity), nullable=False)
    item_type = db.Column(db.Enum(ItemType), nullable=False)
    slot = db.Column(db.Enum(Slot), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('dota_hero.id'), nullable=True)
    prices = db.relationship("ServicePrice", back_populates="item", lazy="dynamic")
