from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("7873436672:AAHK1j-cu759bzcS_TaVu84QeFc7QgVH_DI")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Бот жұмыс істеп тұр!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Сәлем! Мен жұмыс істеп тұрмын 🧠")
        elif text == "/sayhi":
            send_message(chat_id, "Hi from Flask Telegram Bot!")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
