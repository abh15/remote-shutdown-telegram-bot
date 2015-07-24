#requires python-telegram-bot,install using-
#pip python-telegram-bot
#Run on machine you intend to shut down

__author__ = 'MirSpur'

import telegram
import os


def main():
    #token = "your token here"
    bot = telegram.Bot(token)  # Telegram Bot Authorization Token

    global LAST_UPDATE_ID
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  # Get lastest update

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            text = update.message.text
            username=update.message.from_user.username
            chat_id = update.message.chat.id
            update_id = update.update_id
            if LAST_UPDATE_ID < update_id:
                if text=="shut down" and username=="your user name here":    # your telegram username,so only you can access your pc

                	try:
                        	os.system('shutdown /s /t 5')
                            	LAST_UPDATE_ID = update_id



                   	except:
                        	pass



if __name__ == '__main__':
    main()
print encoded
