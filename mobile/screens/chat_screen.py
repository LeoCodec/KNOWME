from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.clock import Clock
import threading
from services.api_client import APIClient

class ChatScreen(Screen):
    def on_enter(self):
        # Cargar historial al entrar
        self.refresh_chat()
        # Auto-refrescar cada 3 segundos
        self.refresh_event = Clock.schedule_interval(self.refresh_chat_callback, 3)

    def on_leave(self):
        # Detener actualización al salir
        if hasattr(self, 'refresh_event'):
            self.refresh_event.cancel()

    def refresh_chat_callback(self, dt):
        self.refresh_chat()

    def refresh_chat(self):
        threading.Thread(target=self._fetch_history).start()

    def _fetch_history(self):
        # AQUÍ ES DONDE DABA EL ERROR ANTES
        # Ahora funcionará porque actualizaste api_client.py
        messages = APIClient.get_chat_history()
        Clock.schedule_once(lambda dt: self._update_ui(messages))

    def _update_ui(self, messages):
        self.ids.chat_list.clear_widgets()
        for msg in messages:
            sender = msg.get('sender', 'bot')
            text = msg.get('text', '')
            
            item = TwoLineAvatarIconListItem(
                text=text,
                secondary_text=sender.upper(),
                bg_color=(0.9, 0.9, 1, 1) if sender == 'user' else (1, 1, 1, 1)
            )
            self.ids.chat_list.add_widget(item)

    def send_message(self):
        msg = self.ids.msg_field.text
        if not msg:
            return

        self.ids.msg_field.text = ""
        threading.Thread(target=self._send_thread, args=(msg,)).start()

    def _send_thread(self, msg):
        success = APIClient.send_chat_message(msg)
        if success:
            self.refresh_chat()