import time
from decouple import config
from gpt import *

from data import *
from telegram.ext import *
import requests

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler


TG_API_KEY = config('TG_API_TOKEN')



def start_command(update, context):
    # p = get_gemini_response("Good morning")
    update.message.reply_text(f"Welcome to the Capx AirHunter bot \n Let's begin Hunt for airdrops with /Hunt")

def help_command(update, context):
    update.message.reply_text(" /Hunt to start with Capx AirHunter")


def test(update: Update, context: CallbackContext) -> None:
    # Define the keyboard options
    keyboard = [['Option 1', 'Option 2', 'Option 3']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Send a welcome message with the options
    update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    if user_message == 'Option 1':
        update.message.reply_text('You selected Option 1.')
    elif user_message == 'Option 2':
        update.message.reply_text('You selected Option 2.')
    elif user_message == 'Option 3':
        update.message.reply_text('You selected Option 3.')
    else:
        update.message.reply_text('Please choose a valid option.')


def select_blockchain(update: Update, context: CallbackContext) -> None:
    keyboard = [['Ethereum', 'Polkadot', 'Solana']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Please choose a Blockchain:', reply_markup=reply_markup)

def handle_message_solana_select(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    print("herer are we")
    m = SOLANA
    if user_message !="":
        for i in m:
            if i['name'] == user_message:
                print("here")
                update.message.reply_text(f"Details for {m['name']}:\n{m['description']}")
                break

def handle_message_select(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    if user_message == 'Ethereum':
        
        new_keyboard = [['Live Airdrop', 'Upcomming Airdrop'], ['Past Airdrops']]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please choose from the Ethereum options:', reply_markup=reply_markup2)        

    elif user_message == 'Polkadot':
        new_keyboard = [['Live Airdrop.', 'Upcomming Airdrop'], ['Past Airdrops']]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please choose from the Polkadot options:', reply_markup=reply_markup2)

    elif user_message == 'Solana':
        new_keyboard = [['Live Airdrop..', 'Upcomming Airdrop'], ['Past Airdrops']]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please choose from the Solana options:', reply_markup=reply_markup2)
    

    elif user_message == 'Live Airdrop':
        m = ETHREUM
        
        update.message.reply_text('Live Airdrops On Ethereum..')
        list_ = []
        for j, i in enumerate(m):
            update.message.reply_text(f"{j + 1}. {i['name']}")
            list_.append(i["name"])

        new_keyboard = [list_]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please Select for detail description:', reply_markup=reply_markup2)
    
    
    elif user_message == 'Live Airdrop.':
        m = POLKADOT
        POLKADOT_DETAILS = True
        update.message.reply_text('Live Airdrops On Polkadot..')
        list_ = []
        for j, i in enumerate(m):
            update.message.reply_text(f"{j + 1}. {i['name']}")
            list_.append(i["name"])

        new_keyboard = [list_]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please Select for detail description:', reply_markup=reply_markup2)
    

    elif user_message == 'Live Airdrop..':
        update.message.reply_text('Live Airdrops On Solana..')
        SOLANA_DETAILS = True
        m = SOLANA
        list_ = []
        for j, i in enumerate(m):
            update.message.reply_text(f"{j + 1}. {i['name']}")
            list_.append(i["name"])

        new_keyboard = [list_]
        reply_markup2 = ReplyKeyboardMarkup(new_keyboard, resize_keyboard=True)
        update.message.reply_text('Please Select for detail description:', reply_markup=reply_markup2)
    
    
    elif user_message !="":
        n1 = SOLANA
        n2 = ETHREUM
        n3 = POLKADOT

        for i in n1:
            if i['name'] == user_message:
                update.message.reply_text("Loading information....")
                reply = ""
                prompt = f'''Task:

**Summarize the Text:**
Please summarize the following text, ensuring the summary is concise and captures the key details of the project and the airdrop mentioned. The summary should include essential information about the project, the nature of the airdrop, and any notable features or benefits.

**Step-by-Step Guide:**
After summarizing, provide a detailed and in-depth step-by-step guide on how to claim the airdrop mentioned in the text.

Incorporate the claimable URL provided in the description into your guide where appropriate.

**Text for Summary and Guide:**

{ i['description'] }
total_value: { i['total_Value'] }

**Example Claimable URL:**

If the description includes a URL like https://example.com/airdrop, ensure this is included in the guide.

**Instructions:**

Please keep in mind that this message will be broadcasted on Telegram, so adhere to the formatting appropriate for Telegram text, such as using bold and italics for headings and key details.

**Claim URL:** { i['claimurl'] }
                    '''
                ai_agent = get_gemini_response(prompt)
                update.message.reply_text(ai_agent)
                break
        for i in n2:
            if i['name'] == user_message:
                update.message.reply_text("Loading information....")
                reply = ""
                prompt = f'''Task:

**Summarize the Text:**
Please summarize the following text, ensuring the summary is concise and captures the key details of the project and the airdrop mentioned. The summary should include essential information about the project, the nature of the airdrop, and any notable features or benefits.

**Step-by-Step Guide:**
After summarizing, provide a detailed and in-depth step-by-step guide on how to claim the airdrop mentioned in the text.

Incorporate the claimable URL provided in the description into your guide where appropriate.

**Text for Summary and Guide:**

{ i['description'] }
total_value: { i['total_Value'] }

**Example Claimable URL:**

If the description includes a URL like https://example.com/airdrop, ensure this is included in the guide.

**Instructions:**

Please keep in mind that this message will be broadcasted on Telegram, so adhere to the formatting appropriate for Telegram text, such as using bold and italics for headings and key details.

**Claim URL:** { i['claimurl'] }
                    '''
                ai_agent = get_gemini_response(prompt)
                update.message.reply_text(ai_agent)
                break
        for i in n3:
            if i['name'] == user_message:
                update.message.reply_text("Loading information....")
                reply = ""
                prompt = f'''Task:

**Summarize the Text:**
Please summarize the following text, ensuring the summary is concise and captures the key details of the project and the airdrop mentioned. The summary should include essential information about the project, the nature of the airdrop, and any notable features or benefits.

**Step-by-Step Guide:**
After summarizing, provide a detailed and in-depth step-by-step guide on how to claim the airdrop mentioned in the text.

Incorporate the claimable URL provided in the description into your guide where appropriate.

**Text for Summary and Guide:**

{ i['description'] }
total_value: { i['total_Value'] }

**Example Claimable URL:**

If the description includes a URL like https://example.com/airdrop, ensure this is included in the guide.

**Instructions:**

Please keep in mind that this message will be broadcasted on Telegram, so adhere to the formatting appropriate for Telegram text, such as using bold and italics for headings and key details.

**Claim URL:** { i['claimurl'] }
                    '''
                ai_agent = get_gemini_response(prompt)
                update.message.reply_text(ai_agent)
                break
    
    
    # elif user_message !="" and POLKADOT_DETAILS:
    #     n = POLKADOT
    #     for i in n:
    #         update.message.reply_text("At the polka....")
    #         if i['name'] == user_message:
    #             print("At the polka....")
    #             update.message.reply_text("Loading information....")
    #             reply = ""
    #             prompt = f'''Please summarize the following text, and then provide a clear, step-by-step guide on how to claim the airdrop mentioned:

    #                 {i['description']}

    #                 The summary should be concise and highlight the key details of the Drift Protocol project and the airdrop. The step-by-step guide should be user-friendly, outlining eligibility criteria, how to check eligibility, and any additional steps required to claim the airdrop. Also, include the URL where users can check their eligibility.
    #                 claimUrl: {i['claimurl']}
    #                 '''
    #             ai_agent = get_gemini_response(prompt)
    #             update.message.reply_text(ai_agent)
    #             # break

    
    elif user_message == 'Upcomming Airdrop':
        update.message.reply_text('More Details comming soon..')

    elif user_message == 'Upcomming Airdrop.':
        update.message.reply_text('More Details comming soon..')
    
    elif user_message == 'Past Airdrops':
        update.message.reply_text('More Details comming soon..')
    
    else:
        update.message.reply_text('Please choose a valid option.')


def get_latest_on_comming(update: Update, context: CallbackContext) -> None:
    keyboard = [['Latest Airdrop', 'Upcomming Airdrop']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Please choose the forllowing:', reply_markup=reply_markup)


def get_more_details_Solana(_name, description,):
    # prompt = _name
    # ai_agent = get_gemini_response(prompt)
    # return ai_agent
    update.message.reply_text(f'Details: \n {res}')

def get_more_details_Solana(_name):
    prompt = _name
    ai_agent = get_gemini_response(prompt)
    return ai_agent

updater = Updater(TG_API_KEY , use_context=True)
dp = updater.dispatcher

def error(update, context):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    # Commands
    print("Starting Telegram Bot...")
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    
    # Select Blockchain.
    updater.dispatcher.add_handler(CommandHandler("Hunt", select_blockchain))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message_select))
    
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message_solana_select))
    
    # updater.dispatcher.add_handler(CommandHandler("test", test))
    # updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


    dp.add_error_handler(error)
    # dp.add_handler(MessageHandler(Filters.command, handle_message))
    # dp.add_handler(MessageHandler(Filters.photo, image_handler))

    updater.start_polling()
    updater.idle()
