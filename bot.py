import telebot
import os
from dotenv import load_dotenv
from gpt_engine import ask_gpt

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_query = message.text
    response = ask_gpt(user_query)
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.infinity_polling()