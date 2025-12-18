import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import os

BOT_TOKEN = os.getenv("8318888870:AAG_HjP0ucgmq4zDUKsXgEFjj5371LffnZI")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(msg: Message):
    await msg.answer("Bot is running on Render ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
