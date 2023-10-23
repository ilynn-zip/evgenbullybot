import configure
import logic
from back import keep_alive
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = configure.config['token']
BOT_NAME = configure.config['name']


#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(logic.start_counting())

async def show_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(logic.get_print_str(True))

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(logic.start_counting(True))

async def manual_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(logic.manual(update.message.text))
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(logic.help_message())


#responses
def handle_response(text : str) -> str:
    return logic.start_counting(True)

async def handle_messages(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    #print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        #if BOT_NAME in text:
        #    new_text = text.replace(BOT_NAME,'').strip()
        #    response = handle_response(new_text)
        if text.find("жен") != -1:
            response = handle_response('')
        else:
            return
    else:
        response = handle_response(text)
    
    #response = handle_response(text)

    #print(response)
    await update.message.reply_text(response)


async def error (update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} \n*caused error {context.error}')

#keep_alive()
if __name__ == '__main__':

    print('Starting...')

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('jenya', show_command))
    app.add_handler(CommandHandler('zero', reset_command))
    app.add_handler(CommandHandler('set', manual_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_messages))

    app.add_error_handler(error)

    print('Polling...\n')
    app.run_polling(poll_interval=1.0)
