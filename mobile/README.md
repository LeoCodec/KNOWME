KnowMe Mobile App 📱

Aplicación nativa multiplataforma desarrollada en Python. Sirve como la interfaz principal para que los usuarios interactúen con el ecosistema KnowMe desde sus dispositivos móviles.

🚀 Características

Interfaz Moderna: Diseño Material Design implementado con KivyMD.

Sincronización Real: Los datos se guardan en la nube (Backend) y se reflejan en la Web.

Chat Móvil: Interfaz de chat fluida conectada a la base de datos central.

Multiplataforma: Código único que funciona en Android (APK), Linux, Windows y macOS.

📚 Explicación de Librerías (Requirements)

Estas librerías son esenciales para la interfaz gráfica y la compilación con Buildozer:

Interfaz Gráfica (GUI)

Kivy: El motor gráfico OpenGL que permite crear apps táctiles y fluidas.

kivymd: Colección de widgets estilo Material Design (Botones, Barras, Listas) que hacen que la app se vea moderna.

Kivy-Garden: Módulos adicionales para Kivy.

pillow: Manejo y procesamiento de imágenes (iconos, fotos).

Conectividad

requests: Cliente HTTP para enviar los datos del perfil y mensajes al Backend Flask.

urllib3, idna, certifi, charset-normalizer: Dependencias de seguridad y codificación para asegurar conexiones estables a internet.

Utilidades de Compilación

docutils, Pygments: Utilizadas internamente por las herramientas de documentación y Kivy.

🛠️ Ejecución y Compilación

Modo Desarrollo (PC)

Instalar dependencias: pip install -r requirements.txt

Correr App: python main.py

Generar APK (Android)

Este proyecto está listo para Buildozer.

Inicializar: buildozer init

Configurar buildozer.spec (Asegurar permisos de INTERNET).

Compilar: buildozer android debug

Desarrollado con ❤️ por LeoCodec