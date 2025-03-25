from flask import Flask, request
import telegram

TOKEN = "8000887434:AAFXUabhZVwN_4aZHLyIJkDHudt4XT_uZMY"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    print("Bot is running...")  # Debugging line
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    print(f"Received message: {message}")  # Debugging line

    bot.send_message(chat_id=chat_id, text=f"Hello! You said: {message}")
    return "OK"

if __name__ == "__main__":
    print("Starting the bot...")  # Debugging line
    app.run(port=5000, debug=True)