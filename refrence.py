import time

from telegram.ext import *
import requests

# Bot 1
API_KEY = "5306827159:AAElZBG2_x8JGVfDhehimKNLqiNYXOXSPo0"


def start_command(update, context):
    if (update.message.chat.id == 785696317):
        update.message.reply_text("Welcome to the bot")
    else:
        update.message.reply_text("You are Not allowed")

def help_command(update, context):
    if (update.message.chat.id == 785696317):
        update.message.reply_text(" /message Enter Message You Want To broadCast \n /view To view the message  \n /send To broadCast The Message \n /viewGroups Get list of the groups")


accounts = ["@AKTestGroupOne","@AKTestGroupTwo","@AKTestGroupThree"]
msg = []


# Message area adding and sending
def handel_msg(update, context):

    msg.append(update.message.text)
    print("this is msg- ",msg[0])


def message(update, context):
    if (update.message.chat.id == 785696317):
        update.message.reply_text("Enter message you want to send")
        msg.clear()
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handel_msg))
        updater.start_polling()

# Displaying the message going to broadcast
def view_msg(update, context):
    if (update.message.chat.id == 785696317):
        update.message.reply_text("this is your msg")
        update.message.reply_text(msg[0])


def handel_user(update, context):

    data = update.message.text
    accounts.append(f'@{data}')
    update.message.reply_text(f'Group:- {data} added to list')


def add_user(update, context):
    update.message.reply_text("Enter groups you want to add")

    updater.dispatcher.add_handler(MessageHandler(Filters.text, handel_user))
    updater.start_polling()



def delete_user(update, context):
    accounts.clear()
    update.message.reply_text("All users deleted Sucessfully from the list")

# To display the groups that message is going to broadcast
def view_groups(update, context):
    if (update.message.chat.id == 785696317):
        update.message.reply_text("Displaying the groups")
        update.message.reply_text(accounts)
        print(accounts)


def send_command(update, context):
    if(update.message.chat.id == 785696317):
        sendMsg(msg[0])
        update.message.reply_text("msg send successfully !")
    else:
        update.message.reply_text("You are not allowed to send the message in the Group!")

def sendMsg(text):

    apiURL = f'https://api.telegram.org/bot{API_KEY}/sendMessage'
    try:
        for i in accounts:
            time.sleep(1)
            response = requests.post(apiURL, json={'chat_id': i, 'text': text})
            print(response.text)
    except Exception as e:
        print(e)


updater = Updater(API_KEY , use_context=True)
dp = updater.dispatcher

def handle_message(update, context):
    update.message.reply_text("not a valid command!")


def error(update, context):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    updater.dispatcher.add_handler(CommandHandler("message", message))
    updater.dispatcher.add_handler(CommandHandler("send", send_command))
    updater.dispatcher.add_handler(CommandHandler("view", view_msg))

    updater.dispatcher.add_handler(CommandHandler("viewGroups", view_groups))
    updater.dispatcher.add_handler(CommandHandler("deleteGroups", delete_user))
    updater.dispatcher.add_handler(CommandHandler("addUser", add_user))

    dp.add_error_handler(error)
    # dp.add_handler(MessageHandler(Filters.command, handle_message))
    # dp.add_handler(MessageHandler(Filters.photo, image_handler))

    updater.start_polling()
    updater.idle()
