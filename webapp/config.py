import os

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'webapp-secret-key-dev'
    
    # Backend API URL (Running locally on port 5000)
    API_URL = "http://127.0.0.1:5000/api"