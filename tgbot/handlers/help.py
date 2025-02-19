from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler responds to the `/help` command.
    """

    help_text = (
        "🤖 *Bot Commands Guide:*\n"
        "/start -- Start the bot\n"
        "/help -- Show this help message\n"
        "💬 Just send me a text message, and I'll echo it back!"
    )
    await message.answer(help_text, parse_mode="Markdown")
