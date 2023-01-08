import telegram
import asyncio
import json

BOT_TOKEN='bot.token'
# {
#    "token" : "token12345678",
#    "chat_id" : 12345678
# }

def main():

    # CHAT BOT TOKEN LOAD
    with open(BOT_TOKEN) as f:
        bot_info = json.load(f)

    token = bot_info['token']
    bot = telegram.Bot(token = token)
    try:
        # Call up the chat ID
        chat_id = int(bot_info['chat_id'])
    except KeyError as e:
        # If you don't have a chat ID, updates it.
        updates = asyncio.run(bot.get_updates())
        chat_id = updates[0].message.chat_id
        bot_info['chat_id'] = chat_id
        with open(BOT_TOKEN, 'w') as f:
            json.dump(bot_info, f, indent=4)

    asyncio.run(bot.sendMessage(chat_id = chat_id, text = '메시지 보내기'))

if __name__ == '__main__':
    main()
