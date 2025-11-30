from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
import threading
from services.api_client import APIClient

class ProfileFormScreen(Screen):
    def submit_data(self):
        # Obtener datos de los text fields definidos en el .kv
        name = self.ids.name_field.text
        bio = self.ids.bio_field.text
        interests = self.ids.interests_field.text
        
        if not name:
            self.show_message("Name is required!")
            return

        # Ejecutar petición en un hilo aparte para no congelar la UI
        threading.Thread(target=self._send_request, args=(name, bio, interests)).start()

    def _send_request(self, name, bio, interests):
        status, response = APIClient.create_profile(name, bio, interests)
        
        if status == 201:
            self.show_message("Profile Created!")
            self._clear_fields()
        else:
            error_msg = response.get('error', 'Unknown Error')
            self.show_message(f"Error: {error_msg}")

    def show_message(self, message):
        toast(message)

    def _clear_fields(self):
        self.ids.name_field.text = ""
        self.ids.bio_field.text = ""
        self.ids.interests_field.text = ""