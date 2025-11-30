from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import os

# Importamos las clases de las pantallas (Asegúrate de que existan los archivos en la carpeta screens/)
from screens.home_screen import HomeScreen
from screens.profile_form import ProfileFormScreen
from screens.chat_screen import ChatScreen

# Configuración de tamaño de ventana para pruebas en PC (simula un móvil)
# Esto solo afecta al ejecutar en computadora, en el celular ocupará toda la pantalla.
Window.size = (360, 640)

class KnowMeApp(MDApp):
    def build(self):
        # 1. Configuración del Tema (Material Design)
        self.title = "KnowMe Mobile"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        
        # 2. Configuración del Icono de la Ventana (Para PC/Linux)
        # Se asegura de que la ruta exista para evitar errores si falta el archivo
        if os.path.exists("assets/icons/logo.jpeg"):
            self.icon = "assets/icons/logo.jpeg"
        
        # 3. Cargar los archivos de diseño (.kv)
        # Importante: El orden no altera el producto, pero deben estar todos
        Builder.load_file("ui/home.kv")
        Builder.load_file("ui/profile_form.kv")
        Builder.load_file("ui/chat.kv")
        
        # 4. Gestor de Pantallas (Navigation Controller)
        sm = ScreenManager()
        
        # Añadimos las pantallas al gestor
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProfileFormScreen(name='profile_form'))
        sm.add_widget(ChatScreen(name='chat'))
        
        return sm

if __name__ == "__main__":
    # Imprimimos un mensaje de éxito en consola al arrancar
    print(">>> Iniciando KnowMe Mobile App...")
    KnowMeApp().run()