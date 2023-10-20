from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your bot's API token
API_TOKEN = "6326634215:AAGrjGCch_X59XzDaXj6FgMO3B9S9Bjggew"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your Telegram bot.")

def main():
    updater = Updater(token=API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    # Add more handlers for your bot's functionality here.

    updater.start_polling()
    updater.idle()

print("Bot is running...")
if __name__ == "__main__":
    main()



