import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import (
    BotCommand,
    MenuButtonCommands
)
from config import BOT_TOKEN
from handlers import (
    start,
    help,
    echo,
)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # All handlers should be attached to the Router (or Dispatcher)
    dp = Dispatcher()

    # Registering handlers
    dp.include_routers(
        start.router,
        help.router,
        echo.router,
    )

    # Setup menu
    await bot.set_my_commands([
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/help", description="Help"),
    ])
    await bot.set_chat_menu_button(
        menu_button=MenuButtonCommands(
            type="commands"
        )
    )

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
