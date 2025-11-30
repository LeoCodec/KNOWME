import os

class Config:
    # Database configuration (SQLite)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'knowme.db')
    
    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key for sessions (critical for production)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-dev-key'
    
    # Allow ASCII characters in JSON responses (for accents, ñ, etc.)
    JSON_AS_ASCII = False