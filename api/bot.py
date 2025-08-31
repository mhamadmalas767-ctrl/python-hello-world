import telebot
from flask import Flask, request

TOKEN = "8146126501:AAFvVgU26HQNKSf2TLXISJhBigCLsqpKadI"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# الرد على /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "كيفك؟ 😎")

# Webhook
@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# صفحة فارغة لتأكيد تشغيل السيرفر
@app.route("/")
def index():
    return "بوت شغال على Vercel", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://اسم-مشروعك.vercel.app/{TOKEN}")
    app.run()
