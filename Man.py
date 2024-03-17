import logging
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

store_id = 123456  # Replace this with the actual store ID
bot_token = '5893052312:AAEH_T8PKjKb7chsCUfj12wWyMQ-EulTtEc'  # Replace this with your bot's token

def check_id(update, context):
    user_id = update.message.from_user.id
    if user_id == store_id:
        context.bot.send_message(chat_id=user_id, text='/menu')
    else:
        update.message.reply_text('Sorry, your user ID does not match the store ID.')

def menu(update, context):
    update.message.reply_text('Here is the menu:')
    update.message.reply_text('1. Item 1')
    update.message.reply_text('2. Item 2')
    update.message.reply_text('3. Item 3')

def error_handler(update, context):
    """Log any errors that occur."""
    logger.error(f'Update {update} caused error {context.error}')

def main():
 #   updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("check", check_id))
    dispatcher.add_handler(CommandHandler("menu", menu))

    # Log errors
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
   main()
