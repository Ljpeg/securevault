from flask import Flask
from config import Config
from extensions import db, jwt, migrate
from app.routes.auth_routes import auth_bp
from app.routes.vault_routes import vault_bp
from app.routes.admin_routes import admin_bp


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  # initialize extensions
  db.init_app(app)
  jwt.init_app(app)
  migrate.init_app(app, db)

  #register blueprints
  app.register_blueprint(auth_bp)
  app.register_blueprint(vault_bp)
  app.register_blueprint(admin_bp)

  return app