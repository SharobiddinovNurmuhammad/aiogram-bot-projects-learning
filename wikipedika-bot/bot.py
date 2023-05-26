import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5900425147:AAF7YrwQ-6DIIPytnBfHvp7kiSgRYjXGyAY'

logging.basicConfig(level=logging.INFO)

wikipedia.set_lang('uz')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}./nWikipedia botga xush kelibsiz!")

@dp.message_handler()
async def wiki(message: types.Message):
    try:
        responce = wikipedia.summary(message.text)
        await message.reply(responce)
    except:
        await message.reply("🙃Bunday ma'lumot topilmadi!")

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
