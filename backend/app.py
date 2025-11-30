from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from routes.profile_routes import profile_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # CORS: Critical for Mobile App (Buildozer) and WebApp communication
    # resources={r"/api/*": ...} enables access to all API routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(profile_bp)
    
    # Create tables on startup
    with app.app_context():
        db.create_all()
        print(">>> Database initialized.")
        
    return app

app = create_app()

if __name__ == '__main__':
    # host='0.0.0.0' is MANDATORY for local network access (Mobile/Emulator)
    app.run(host='0.0.0.0', port=5000, debug=True)