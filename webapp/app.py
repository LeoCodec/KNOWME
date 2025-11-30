from flask import Flask, render_template
from config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config)

# Inject API_URL into all templates context
@app.context_processor
def inject_api_url():
    return dict(api_url=app.config['API_URL'])

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    # RUNNING ON PORT 5001 to avoid conflict with Backend (5000)
    print(">>> WebApp running on http://127.0.0.1:5001")
    app.run(debug=True, port=5001)