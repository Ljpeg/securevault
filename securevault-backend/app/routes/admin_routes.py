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
@admin_bp.route('user/<user_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_user_logs(user_id):
  logs = VaultLog.query.filter_by(user_id=user_id).all()
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

# Get logs by item id
@admin_bp.route('item/<item_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_item_logs(item_id):
  logs = VaultLog.query.filter_by(item_id=item_id).all()
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

# Get all deleted items
@admin_bp.route('/deleted', methods=['GET'])
@jwt_required()
@admin_required
def get_all_deleted():
  deleted_logs = VaultLog.query.filter_by(item_deleted=True).all()
  if deleted_logs:
    return jsonify([{
      "item_id": log.item_id,
      "user_id": log.user_id, 
      "action": log.action, 
      "timestamp": log.timestamp.isoformat()
    } for log in deleted_logs])
  else:
    return jsonify({"error": "No logs found"})