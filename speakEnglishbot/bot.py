import logging

from aiogram import Bot, Dispatcher, executor, types
from speakEnglishloops import speakenglish
from googletrans import Translator


API_TOKEN = '5900425147:AAF7YrwQ-6DIIPytnBfHvp7kiSgRYjXGyAY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Translate object
translator = Translator()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def get_speakenglish(message: types.Message):
    til = translator.detect(message.text).lang
    msg = message.text
    if len(message.text.split()) >= 2:
        dest = 'en' if til == 'uz' else 'uz'
        await message.reply(f"{translator.translate(text=message.text, dest=dest).text}")
    else:
        if til=='uz':
            msg = translator.translate(text=message.text, dest='en').text

        loops = speakenglish(msg)

        if loops:
            await message.answer(f"Words:\n{loops['definitions']}")
            if loops.get('auido'):
                await message.reply_audio(loops['auido'])
        else:
            await message.reply("Bunday so'z topilmadi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)