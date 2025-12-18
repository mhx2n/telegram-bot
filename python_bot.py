import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "8318888870:AAG_HjP0ucgmq4zDUKsXgEFjj5371LffnZI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# start command
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.reply(
        "📁 File Rename Bot\n\n"
        "👉 যেকোনো ফাইল পাঠাও\n"
        "👉 তারপর নতুন নাম পাঠাও (extension সহ)\n\n"
        "Example:\nmy_file.pdf"
    )

# store last file
user_files = {}

@dp.message(F.document | F.video | F.audio)
async def get_file(message: Message):
    file = message.document or message.video or message.audio
    user_files[message.from_user.id] = file
    await message.reply("✏️ নতুন ফাইল নাম পাঠাও (extension সহ)")

@dp.message(F.text)
async def rename_file(message: Message):
    user_id = message.from_user.id

    if user_id not in user_files:
        return

    new_name = message.text.strip()
    file = user_files[user_id]

    await bot.send_chat_action(message.chat.id, "upload_document")

    await bot.send_document(
        chat_id=message.chat.id,
        document=file.file_id,
        caption="✅ Renamed Successfully",
        filename=new_name
    )

    del user_files[user_id]

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
