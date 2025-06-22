from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from app.models.vault_user import VaultUser

def admin_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    user = VaultUser.query.get(get_jwt_identity())
    if user.role != "admin":
      return jsonify({"error": "Admin access required"}), 403
    return fn(*args, **kwargs)
  return wrapper