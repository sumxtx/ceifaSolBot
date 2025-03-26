import os
import json
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN=os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN,parse_mode='Markdown') 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "\xF0\x9F\x98\x89 Fala, patraum? /help cualquer coisa.")

@bot.message_handler(commands=['help'])
def help_command(message):
    commands=""" Available Commands:
    /generate - Generate New APIKey, Keypair\n \
            \u26A0 The Bot DON'T store any of your keys \u26A0\n\
            Save them properly before start transactioning.
    
    """
    # TODO: Need to find a way for the bot keep the API_KEY and the PRIVATE_KEY 
    # without enter it all time, but without the bot saving it on himself
    #/balance <wallet_address> <token_address> - Get token balance
    #/buy <amount_sol> <stop_loss> <take_profit> <token_address> - Buy the Token
    bot.reply_to(message, commands)

@bot.message_handler(commands=['generate'])
def generate_command(message):
    response = requests.get(url="https://pumpportal.fun/api/create-wallet")
    dataj = response.json()
    msg_API = f"""*** API KEY ***  
`{dataj['apiKey']}`
  
  
This will be required to send some Transactions.  
\u26A0DO NOT SHARE THIS WITH ANYONE YOU DON'T TRUST  
\u26A0OTHERS MAY OPERATE ON YOUR BEHALF."""
    
    msg_PRIV_KEY = f"""*** PRIVATE KEY ***  
`{dataj['privateKey']}`
  
  
This is used to sign some Transactions.  
And to Keep Control of Your Wallets.  
\u26A0SAVE IT PROPERLY. WE DO NOT SAVE IT!.  
  
\u26A0DO NOT SHARE THIS WITH ANYONE.  
\u26A0SHARING OR NOT SAVING,  
\u26A0MAY IMPLY LOSING ALL YOUR FUNDS."""
    
    msg_PUB_KEY = f"""*** PUBLIC KEY ***  
`{dataj['walletPublicKey']}`
  
  
This is used to to Public Identify Yourself in the Blockchain.  
Others May Send you Funds in this Direction."""

    msg_START_TRAD = f"""*** TO START TRADING ***  
  
  
Fill Up Some Solana to Start Trading.  
First Import your private Key To any Wallet of your choice.  
Then Transfer Solanas To it."""
    bot.reply_to(message, msg_API, parse_mode='Markdown')
    bot.reply_to(message, msg_PRIV_KEY, parse_mode='Markdown')
    bot.reply_to(message, msg_PUB_KEY, parse_mode='Markdown')
    
#@bot.message_handler(commands=['balance'])
#def balance_command(message: Message):
#    try:
#        _, wallet_address, token_address = message.text.split()
#        balance = get_token_balance(wallet_address, token_address)
#        bot.reply(message, f"Token balance: {balance}")
#    except Exception as e:
#        bot.reply_to_(message, f"error: r{e}")
#
#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)
#
def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()
