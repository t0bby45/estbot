from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Бұл жерде орнатылған болуы керек
if not BOT_TOKEN:
    raise Exception("BOT_TOKEN деген айнымалы анықталмаған!")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Бот жұмыс істеп тұр!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Келген хабар:", data)  # Лог үшін

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Сәлем! Мен жұмыс істеп тұрмын 🧠")
        elif text == "/sayhi":
            send_message(chat_id, "Hi from Flask Telegram Bot!")
        else:
            send_message(chat_id, "Мен тек /start пен /sayhi-ге жауап беремін 😎")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    resp = requests.post(url, json=payload)
    print("Жіберу статусы:", resp.status_code)

if __name__ == "__main__":
    # local-да жұмыс үшін, production-да gunicorn керек
    app.run(host="0.0.0.0", port=5000)
