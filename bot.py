import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

movies = {
    "اینتراستلار": {"type": "فیلم", "year": "2014", "link": "https://example.com/1"},
    "برکینگ بد": {"type": "سریال", "year": "2008", "link": "https://example.com/2"},
    "فرینج": {"type": "سریال", "year": "2008", "link": "https://example.com/3"},
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎬 لیست فیلم‌ها")
    bot.send_message(message.chat.id, "سلام! اسم فیلم یا سریال رو بفرست:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🎬 لیست فیلم‌ها")
def show_list(message):
    text = "📽 لیست:\n\n"
    for name, info in movies.items():
        text += f"• {name} ({info['year']})\n"
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: True)
def search(message):
    query = message.text.strip()
    found = False
    for name, info in movies.items():
        if query in name:
            bot.send_message(message.chat.id, f"🎬 {name}\n📅 {info['year']}\n🎭 {info['type']}\n\n🔗 {info['link']}")
            found = True
    if not found:
        bot.send_message(message.chat.id, "❌ پیدا نشد.")

print("ربات روشن شد...")
bot.infinity_polling()
