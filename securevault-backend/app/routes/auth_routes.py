from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import create_access_token
from app.models.vault_user import VaultUser

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/ping', methods=['GET'])
def ping():
  return jsonify({"message": "pong from auth!"}), 200

@auth_bp.route('/register', methods=['POST'])
def register_new_user():
  data = request.get_json()
  email = data.get("email")
  password = data.get("password")
  role = data.get("role", "user")

  if not email or not password:
    return jsonify({"error": "Email and password are required"}), 400
  
  if VaultUser.query.filter_by(email=email).first():
    return jsonify({"error": "Email already registered"}), 409
  
  new_user = VaultUser(email=email, role=role)
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
  
  user = VaultUser.query.filter_by(email=email).first()
  if not user or not user.check_password(password):
    return jsonify({"error": "Invalid email or password"}), 401
  
  access_token = create_access_token(identity=user.id)
  return jsonify({"the access_token is": access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
  return jsonify({"message": "user log out!"}), 200

@auth_bp.route('/refresh', methods=['POST'])
def refresh():
  return jsonify({"message": "refresh!"}), 200






