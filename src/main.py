import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from translations import Translations
from keyboard_layout import correct_layout, NotSupportedLayoutException

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(Translations.get_translation("start"))


@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    await message.answer(Translations.get_translation("help"))


@dp.message()
async def fix_layout_handler(message: types.Message) -> None:
    """
    Handler will correct text written using a wrong keyboard layout and send it back.
    """
    try:
        text_to_correct = ""
        if message.text:
            text_to_correct = message.text
        elif message.caption:
            text_to_correct = message.caption
        else:
            return await message.answer(
                Translations.get_translation("nothing_to_correct")
            )
        corrected_text = correct_layout(text_to_correct)
        return await message.answer(corrected_text)
    except NotSupportedLayoutException:
        return await message.answer(
            Translations.get_translation("not_supported_layout")
        )
    except:
        return await message.answer(
            Translations.get_translation("something_went_wrong")
        )


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
