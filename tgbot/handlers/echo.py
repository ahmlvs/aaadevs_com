from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message) -> None:
    """
    This handler echoes back any received text message.
    If the message doesn't contain text, it sends a fallback response.
    """
    if message.text:
        await message.answer(message.text)
    else:
        await message.answer("❌ I can only process text messages!")
