import telebot

# Set up the Telegram bot
bot = telebot.TeleBot("6271347286:AAF-Y9N-C3YItKZwmxiGSwwqMY0-k0wPcVk")

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # Send a "hi" message back
    bot.send_message(message.chat.id, "Hi!")

# Start the bot
bot.polling()
