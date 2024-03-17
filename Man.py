import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

store_id = 123456  # Replace this with the actual store ID
bot_token = '5893052312:AAEH_T8PKjKb7chsCUfj12wWyMQ-EulTtEc'  # Replace this with your bot's token

def check_id(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id == store_id:
        context.bot.send_message(chat_id=user_id, text='/menu')
    else:
        update.message.reply_text('Sorry, your user ID does not match the store ID.')

def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is the menu:')
    update.message.reply_text('1. Item 1')
    update.message.reply_text('2. Item 2')
    update.message.reply_text('3. Item 3')

def main() -> None:
    updater = Updater(token=bot_token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("check", check_id))
    dispatcher.add_handler(CommandHandler("menu", menu))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
