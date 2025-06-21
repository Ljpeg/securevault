from flask import Flask
from config import Config
from extensions import db, jwt, migrate
from app.routes.auth_routes import auth_bp

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  # initialize extensions
  db.init_app(app)
  jwt.init_app(app)
  migrate.init_app(app, db)

  #register blueprints
  app.register_blueprint(auth_bp)

  return app