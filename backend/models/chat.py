from database import db
from datetime import datetime

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(10), nullable=False) # 'user' o 'bot'
    text = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(5), nullable=True) # 'es' o 'en'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "sender": self.sender,
            "text": self.text,
            "timestamp": self.timestamp.strftime("%H:%M")
        }