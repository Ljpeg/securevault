from extensions import db
from datetime import datetime, timezone

class VaultLog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('vault_user.id'), nullable=False)
  item_id = db.Column(db.Integer, db.ForeignKey('vault_item.id'), nullable=False)
  action = db.Column(db.String(50), nullable=False)
  timestamp = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)