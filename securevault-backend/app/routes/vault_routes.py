from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.vault_item import VaultItem
from app.utils.crypto import encrypt_data, decrypt_data
from app.utils.logging import log_action

vault_bp = Blueprint('vault', __name__, url_prefix='/vault')


@vault_bp.route('/', methods=['GET'])
@jwt_required()
def get_vault_items():
  user_id = get_jwt_identity()
  items = VaultItem.query.filter_by(user_id=user_id).all()

  for item in items:
      log_action(user_id, item.id, "read")
      
  return jsonify([
    {
      "id": item.id, 
      "title": item.title,
      "data": decrypt_data(item.encrypted_data),
      "created_at": item.created_at,
      "updated_at": item.updated_at
      }
      for item in items
      ]), 200

@vault_bp.route('/', methods=['POST'])
@jwt_required()
def new_vault_item():
  user_id = get_jwt_identity()
  data = request.get_json()
  title = data.get("title")
  raw_data = data.get("data")

  if not title or not raw_data:
    return jsonify({"error": "Title and data are required"}), 400
  
  encrypted = encrypt_data(raw_data)
  item = VaultItem(title=title, encrypted_data=encrypted, user_id=user_id)

  db.session.add(item)
  db.session.commit()

  log_action(user_id, item.id, "create")
  return jsonify({"message": "new vault item created!", "id": item.id}), 201

@vault_bp.route('/<item_id>', methods=['GET'])
@jwt_required()
def get_a_vault_item(item_id):
  user_id = get_jwt_identity()
  item = VaultItem.query.filter_by(user_id=user_id, id=item_id).first()
  
  if not item:
    return jsonify({"error": "vault item not found"}), 404
  
  log_action(user_id, item_id, "read")

  return jsonify({
    "id": item.id, 
    "title": item.title,
    "data": decrypt_data(item.encrypted_data), 
    "created_at": item.created_at,
    "updated_at": item.updated_at
    }), 200

@vault_bp.route('/<item_id>', methods=['PUT'])
@jwt_required()
def update_vault_item(item_id):
  user_id = get_jwt_identity()
  item = VaultItem.query.filter_by(user_id=user_id, id=item_id).first()

  if not item:
    return jsonify({"error": "vault item not found"})
  
  data = request.get_json()
  title = data.get("title")
  raw_data = data.get("data")

  if title:
    item.title = title
  if raw_data:
    item.encrypted_data = encrypt_data(raw_data)

  db.session.commit()

  log_action(user_id, item_id, "update")
  return jsonify({"message": "vault item updated!"}), 200

@vault_bp.route('/<item_id>', methods=['DELETE'])
@jwt_required()
def delete_vault_item(item_id):
  user_id = get_jwt_identity()
  item = VaultItem.query.filter_by(user_id=user_id, id=item_id).first()
  
  if not item:
    return jsonify({"error": "vault item not found"})
  
  log_action(user_id, item_id, "delete")
  
  db.session.delete(item)
  db.session.commit()

  return jsonify({"message": "vault item deleted!"}), 200