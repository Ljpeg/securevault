from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import create_access_token

vault_bp = Blueprint('vault', __name__, url_prefix='/vault')

@vault_bp.route('/ping', methods=['GET'])
def ping():
  return jsonify({"message": "pong from vault!"}), 200

@vault_bp.route('/', methods=['GET'])
def get_vault():
  return jsonify({"message": "items from!"}), 200

@vault_bp.route('/', methods=['POST'])
def new_item():
  return jsonify({"message": "new vault item!"}), 200

@vault_bp.route('<item_id>', methods=['GET'])
def get_item():
  return jsonify({"message": "a vault item!"}), 200

@vault_bp.route('/<item_id>', methods=['PUT'])
def update_item():
  return jsonify({"message": "updated vault item!"}), 200

@vault_bp.route('/<item_id>', methods=['DELETE'])
def delete_item():
  return jsonify({"message": "deleted vault item!"}), 200