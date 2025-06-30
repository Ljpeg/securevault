from extensions import db
from datetime import datetime, timezone

class VaultItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('vault_user.id'), nullable=False)
  title = db.Column(db.String(120), nullable=False)
  encrypted_data = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
  updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
  is_deleted = db.Column(db.Boolean, default=False)
  vault_logs = db.relationship('VaultLog', backref='vault_item', lazy=True)

  @classmethod
  def get_active_item(cls, item_id, user_id):
    return cls.query.filter_by(id=item_id, user_id=user_id, is_deleted=False).first()