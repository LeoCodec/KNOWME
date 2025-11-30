KnowMe - Ecosistema Full Stack Python 🐍

KnowMe es un proyecto educativo y tecnológico diseñado para demostrar el poder de Python en todas las capas del desarrollo de software moderno: Backend, Frontend Web y Aplicaciones Móviles Nativas.

Este repositorio contiene un ecosistema distribuido completo donde una sola API alimenta a múltiples plataformas simultáneamente, integrando además capacidades de Inteligencia Artificial (NLP).

📂 Estructura del Proyecto

El repositorio está organizado en tres módulos principales, cada uno funcionando de manera independiente pero conectados entre sí:

1. 🧠 Backend (/backend)

El cerebro del sistema.

Tecnología: Flask, SQLAlchemy, SQLite.

IA: Motor spaCy para Procesamiento de Lenguaje Natural (detección de idioma y extracción de palabras clave).

Función: Expone una API REST (/api/profile, /api/chat) que sirve datos a la web y al móvil.

2. 📱 Mobile App (/mobile)

La experiencia nativa.

Tecnología: Python, Kivy, KivyMD.

Función: Aplicación táctil para Android (compilable vía Buildozer) y Escritorio. Permite crear perfiles y chatear con el bot.

Características: Sincronización en tiempo real y diseño Material Design.

3. 🌐 Web App (/webapp)

El panel de administración.

Tecnología: Flask (Frontend), HTML5, JavaScript (Fetch API).

Función: Dashboard web para visualizar los perfiles creados y monitorear el chat en tiempo real desde un navegador.

🚀 Guía de Inicio Rápido

Para ejecutar todo el ecosistema en tu máquina local (Linux/Mac/Windows), necesitarás abrir 3 terminales simultáneas.

Prerrequisitos Globales

Python 3.10+

Virtualenv (pip install virtualenv)

Paso 1: Encender el Backend (Terminal 1)

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download es_core_news_md  # Solo la primera vez
python app.py
# Running on [http://0.0.0.0:5000](http://0.0.0.0:5000)



Paso 2: Encender la WebApp (Terminal 2)

cd webapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
# Running on [http://127.0.0.1:5001](http://127.0.0.1:5001)



Paso 3: Correr la App Móvil (Terminal 3)

cd mobile
# Asegúrate de tener las dependencias de Kivy instaladas en tu sistema
pip install -r requirements.txt
python main.py



📸 Capturas de Pantalla

| Web Dashboard | Mobile App |
| Gestión de perfiles y chat web | Interfaz Material Design nativa |

(Puedes subir tus capturas de pantalla a una carpeta docs/img y enlazarlas aquí)

🛠️ Tecnologías Utilizadas

Lenguaje: Python

Web Framework: Flask

Mobile Framework: KivyMD

NLP: spaCy

Base de Datos: SQLite (SQLAlchemy ORM)

👤 Autor

Desarrollado con ❤️ por LeoCodec.

Este proyecto es de código abierto y está pensado para fines educativos sobre arquitecturas de software distribuidas en Python.