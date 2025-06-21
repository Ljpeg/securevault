from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import create_access_token
from app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/ping', methods=['GET'])
def ping():
  return jsonify({"message": "pong from auth!"}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  email = data.get("email")
  password = data.get("password")

  if not email or not password:
    return jsonify({"error": "Email and password are required"}), 400
  
  if User.query.filter_by(email=email).first():
    return jsonify({"error": "Email already registered"}), 409
  
  new_user = User(email=email)
  new_user.set_password(password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = data.get("email")
  password = data.get("password")

  if not email or not password:
    return jsonify({"error": "Email and password are required"}), 400
  
  user = User.query.filter_by(email=email).first()
  if not user or not user.check_password(password):
    return jsonify({"error": "Invalid email or password"}), 401
  
  access_token = create_access_token(identity=user.id)
  return jsonify({"access_token": access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
  return jsonify({"message": "user log out!"}), 200

@auth_bp.route('/refresh', methods=['POST'])
def refresh():
  return jsonify({"message": "refresh!"}), 200



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

audit_bp = Blueprint('aduit', __name__, url_prefix='/audit')

@audit_bp.route('/', methods=['GET'])
def get_log():
  return jsonify({"message": "users log!"})

@audit_bp.route('/', methods=['POST'])
def create_log():
  return jsonify({"message": " new user log!"})

