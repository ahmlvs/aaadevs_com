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
        text = f"Hello, @{username}! 👋\n\n"
    else:
        text = f"Hello, {first_name}! 👋\n\n"
    
    text += "Welcome to aaadevs_com bot.\n\n"
    text += "aaadevs_com: open-source project built with FastAPI, showcasing server-side HTML rendering with Jinja2Templates, and CI/CD deployment using Docker and GitLab.\n\n"
    text += "Source code: [GitHub](https://github.com/ahmlvs/aaadevs_com)\n"
    text += "Website: [aaadevs.com](https://aaadevs.com)\n"
    
    await message.answer(text)
