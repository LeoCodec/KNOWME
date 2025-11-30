from flask import Blueprint, request, jsonify
from database import db
from models.chat import ChatMessage
from utils.language import detect_language
import random

chat_bp = Blueprint('chat_bp', __name__)

@chat_bp.route('/api/chat', methods=['GET'])
def get_history():
    # Devolver los últimos 50 mensajes para mantener el historial
    messages = ChatMessage.query.order_by(ChatMessage.timestamp.asc()).limit(50).all()
    return jsonify([m.to_dict() for m in messages]), 200

@chat_bp.route('/api/chat', methods=['POST'])
def send_message():
    data = request.json
    user_text = data.get('text', '')
    
    if not user_text:
        return jsonify({"error": "Empty message"}), 400

    # 1. Detectar idioma
    lang = detect_language(user_text)

    # 2. Guardar mensaje del usuario
    user_msg = ChatMessage(sender='user', text=user_text, language=lang)
    db.session.add(user_msg)
    
    # 3. Generar respuesta del BOT (Lógica simple pero efectiva)
    bot_reply = ""
    
    if lang == 'es':
        respuestas = [
            f"Entendido: '{user_text}'. ¿En qué más puedo ayudarte?",
            "Interesante. Cuéntame más sobre eso.",
            "He procesado tu mensaje en español.",
            "¡Hola! Soy KnowMe. Todo sistemas operativos."
        ]
        if "hola" in user_text.lower():
            bot_reply = "¡Hola! ¿Cómo estás hoy?"
        else:
            bot_reply = random.choice(respuestas)
    else:
        # Default to English
        answers = [
            f"Understood: '{user_text}'. How else can I help?",
            "Interesting. Tell me more.",
            "I processed your message in English.",
            "Hello! I am KnowMe. Systems online."
        ]
        if "hello" in user_text.lower() or "hi" in user_text.lower():
            bot_reply = "Hello there! How are you?"
        else:
            bot_reply = random.choice(answers)

    # 4. Guardar respuesta del BOT
    bot_msg = ChatMessage(sender='bot', text=bot_reply, language=lang)
    db.session.add(bot_msg)
    
    db.session.commit()

    return jsonify({
        "user_msg": user_msg.to_dict(),
        "bot_msg": bot_msg.to_dict()
    }), 201