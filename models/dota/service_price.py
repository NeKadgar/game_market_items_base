from sqlalchemy.sql import func
import datetime
from extentions import db


class ServicePrice(db.Model):
    __tablename__ = "dota_service_price"
    __table_args__ = (
        db.UniqueConstraint("service", "item_id", name="_dota_service_item_uc"),
    )

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(10))
    item_id = db.Column(db.Integer, db.ForeignKey("dota_item.id"))
    item = db.relationship("DotaItem", back_populates="prices")
    price = db.Column(db.Numeric(precision=6, scale=2), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, server_default=func.now(),
                           onupdate=func.current_timestamp())

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "service": self.service,
            "price": self.price,
            "updated_at": self.updated_at.strftime("%d.%m.%Y %H:%M")
        }
