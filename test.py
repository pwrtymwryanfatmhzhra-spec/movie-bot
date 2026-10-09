import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "سلام! یه فیلم بفرست تا file_id رو بگیری.")

@bot.message_handler(content_types=['video', 'document'])
def get_file_id(message):
    if message.video:
        file_id = message.video.file_id
        file_name = message.video.file_name or "ویدیو"
    elif message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name or "فایل"
    else:
        return
    
    bot.reply_to(
        message,
        f"🎬 نام: {file_name}\n\n🔑 کد (file_id):\n`{file_id}`",
        parse_mode='Markdown'
    )

print("ربات تست روشن شد...")
bot.polling()
