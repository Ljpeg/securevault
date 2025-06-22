from app.models.vault_log import VaultLog
from extensions import db

def log_action(user_id: int, item_id: int, action: str):
  log = VaultLog(user_id=user_id, item=item_id, action=action)
  db.session.add(log)
  db.session.commit()