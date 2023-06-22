import asyncio
import telegram
from django.conf import settings

async def send_order(message):
    bot = telegram.Bot(token=settings.TELEGRAM['bot_token'])
    await bot.send_message(text=message, chat_id=settings.TELEGRAM['chat_id'])

def send_order_message_to_telegram(message):
    asyncio.run(send_order(message))