KnowMe Web Dashboard 🌐

Panel de administración web ligero. Demuestra cómo consumir la misma API que la app móvil pero desde un entorno de navegador, logrando un ecosistema distribuido completo.

🚀 Características

Dashboard Visual: Vista general de los perfiles registrados.

Chat Web Sincronizado: Permite conversar con el bot y ver el historial sincronizado con el móvil.

Visualización NLP: Muestra gráficamente las etiquetas y el idioma detectado por el backend.

📚 Explicación de Librerías (Requirements)

A diferencia del Backend, este frontend se mantiene ligero:

Flask: Aquí se usa para renderizar las plantillas HTML (render_template) y servir los archivos estáticos (CSS/JS).

requests: Aunque el navegador usa JavaScript fetch para muchas cosas, Python usa requests para validaciones del lado del servidor si fuera necesario.

Jinja2: Motor de plantillas que permite inyectar datos (como la URL de la API) directamente en el HTML.

flask-cors: (Opcional aquí) Útil si quisiéramos exponer recursos estáticos a otros dominios.

🛠️ Instalación y Ejecución

Activar Entorno Virtual (Propio de WebApp):

source venv/bin/activate


Instalar Dependencias:

pip install -r requirements.txt


Iniciar Cliente Web:

python app.py


La web correrá en http://127.0.0.1:5001 (Puerto distinto al Backend para evitar conflictos).

Desarrollado con ❤️ por LeoCodec