import asyncio
import logging
import sys
from os import getenv
import wikipedia
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6990681753:AAGKY2DjwI8hWyRX9s5l3L_8odPsEuA0MwQ"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

wikipedia.set_lang('uz')
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Wikipediaga hush kelibsiz kimni qidirmoqchisiz?')


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.reply(wikipedia.summary(message.text))
    except :
        await message.answer("So'rov topilmadi")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
