import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).resolve().parent
load_dotenv(dotenv_path=basedir / '.env')

class Config:
  SECRET_KEY = os.getenv("SECRET_KEY")
  JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
  ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  DEBUG = False 
  JWT_VERIFY_SUB = False

class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  DEBUG = False