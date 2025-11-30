from database import db
from datetime import datetime

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    interests = db.Column(db.String(255), nullable=True)
    
    # Fields for NLP analysis results
    detected_lang = db.Column(db.String(10), nullable=True)
    keywords = db.Column(db.Text, nullable=True)  # Stored as comma-separated string
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Converts object to dictionary for JSON response"""
        return {
            "id": self.id,
            "name": self.name,
            "bio": self.bio,
            "interests": self.interests,
            "analysis": {
                "language": self.detected_lang,
                "keywords": self.keywords.split(',') if self.keywords else []
            },
            "created_at": self.created_at.isoformat()
        }
        