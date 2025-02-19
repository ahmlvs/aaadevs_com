from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
)

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    # User info
    telegram_user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    # Send a welcome message
    if username:
        text = f"Hello, @{username}! 👋"
    else:
        text = f"Hello, {first_name}! 👋"
    
    await message.answer(text)
