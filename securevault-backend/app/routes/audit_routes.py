from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import create_access_token


audit_bp = Blueprint('aduit', __name__, url_prefix='/audit')

@audit_bp.route('/', methods=['GET'])
def get_log():
  return jsonify({"message": "users log!"})

@audit_bp.route('/', methods=['POST'])
def create_log():
  return jsonify({"message": " new user log!"})