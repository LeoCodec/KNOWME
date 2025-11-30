import requests
import json

# IMPORTANTE:
# Usa 10.0.2.2 si estás en Emulador Android.
# Usa 127.0.0.1 si estás probando en tu PC (Linux/Windows) como en el video.
BASE_URL = "http://127.0.0.1:5000/api" 

class APIClient:
    # --- PERFILES ---
    @staticmethod
    def create_profile(name, bio, interests):
        url = f"{BASE_URL}/profile"
        headers = {"Content-Type": "application/json"}
        payload = {
            "name": name,
            "bio": bio,
            "interests": interests
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=5)
            return response.status_code, response.json()
        except requests.exceptions.ConnectionError:
            return 0, {"error": "Error de conexión. Revisa el Backend."}
        except Exception as e:
            return 0, {"error": str(e)}

    # --- CHAT (ESTAS SON LAS FUNCIONES QUE TE FALTAN) ---
    @staticmethod
    def get_chat_history():
        """Obtiene el historial de mensajes del backend"""
        url = f"{BASE_URL}/chat"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                return response.json()
            return []
        except:
            return []

    @staticmethod
    def send_chat_message(text):
        """Envía un nuevo mensaje al backend"""
        url = f"{BASE_URL}/chat"
        payload = {"text": text}
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=5)
            return response.status_code == 201
        except:
            return False