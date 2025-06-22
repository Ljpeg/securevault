from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class VaultUser(db.Model): 
  __tablename__ = 'vault_user'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password_hash = db.Column(db.String(256), nullable=False)
  role = db.Column(db.String(50), default="user", nullable=False)
  vault_items = db.relationship('VaultItem', backref='vault_user', lazy=True)
  vault_logs = db.relationship('VaultLog', backref='vault_user', lazy=True)
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  