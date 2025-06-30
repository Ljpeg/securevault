from app.models.vault_log import VaultLog
from extensions import db

def log_action(user_id: int, item_id: int, action: str, item_deleted: bool = False):
  log = VaultLog(user_id=user_id, item_id=item_id, action=action, item_deleted=item_deleted)
  db.session.add(log)
  db.session.commit()