from app.models.vault_log import VaultLog
from app.utils.permissions import admin_required
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# Get all logs
@admin_bp.route('/logs', methods=['GET'])
@jwt_required()
@admin_required
def get_all_logs():
  logs = VaultLog.query.all()
  if logs:
    return jsonify([{
      "user_id": log.user_id, 
      "item_id": log.item_id,
      "action": log.action, 
      "timestamp": log.timestamp.isoformat()
    } 
    for log in logs
    ])
  else:
    return jsonify({"error": "No logs found"})

# Get logs by user id

# Get logs by item id

