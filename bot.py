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
    update.message.reply_text('Hey! {} Thank you for choosing me!\n\n $whoami: DNS RECORDS BOT \n\n $purpose: To fetch the DNS records of domain\n\n Check /help to see more info and input syntax'.format(username['username']))

def help(update, context):
    update.message.reply_text("To check a domain's record send the domain name followed by the record type. \n\n Example: example.com A \n\n Only the below record types are supported \n\n A, AAAA, CNAME MX, NS, SOA, TXT")

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

    updater.start_webhook(listen="0.0.0.0",
                        port=int(PORT),
                        url_path=TOKEN,
                        webhook_url='https://dnscheckerbot.herokuapp.com/' + TOKEN)

    updater.idle()

main()
