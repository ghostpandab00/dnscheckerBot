from telegram.ext import *
import telegram
import os
import dnscheck as d

global bot
TOKEN = os.environ['token']
bot = telegram.Bot(TOKEN)

PORT = int(os.environ.get('PORT', 9999))

def start(update, context):
    username = update.message.from_user
    update.message.reply_text('Hey! {} Thank you for choosing me!\n\n\n $whoami: DNS RECORDS BOT \n\n $purpose: To fetch the DNS records of domain\n\n Use /help to see the input syntax'.format(username['username']))

def help(update, context):
    update.message.reply_text('Send the domain name.\n Eg: example.com')

def recordcheck(update, context):
    userinput = str(update.message.text)
    response = d.dnscheck(userinput)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, recordcheck))

    updater.start_webhook(listen="127.0.0.1",
                        port=int(PORT),
                        url_path=TOKEN,
                        webhook_url='https://46124f86548d.ngrok.io/' + TOKEN)

    updater.idle()

main()
