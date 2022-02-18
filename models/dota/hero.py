from extentions import db


class Hero(db.Model):
    __tablename__ = "dota_hero"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    items = db.relationship("DotaItem", backref='hero', lazy=False)

    @property
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
