import telebot
from googletrans import Translator

# Set up the Telegram bot
bot = telebot.TeleBot("6271347286:AAF-Y9N-C3YItKZwmxiGSwwqMY0-k0wPcVk")

# Set up the translator
translator = Translator()

# Define a function to handle all messages
@bot.message_handler(func=lambda message: True)
def translate_message(message):
    # Translate the message to Arabic
    translated_text = translator.translate(message.text, dest='ar').text
    # Send the translated message back
    bot.reply_to(message, translated_text)

# Start the bot
bot.polling()
