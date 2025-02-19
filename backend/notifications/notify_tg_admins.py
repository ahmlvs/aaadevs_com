import aiohttp
from config import BOT_TOKEN, ADMINS_LIST


async def send_telegram_notification(contact_data):
    """Send a notification to the admin Telegram list."""
    
    if not BOT_TOKEN or not ADMINS_LIST:
        print("Telegram bot token or admin list is missing!")
        return

    message = (
        f"📩 *New Contact Form Submission*\n"
        f"👤 *Name:* {contact_data['name']}\n"
        f"✉️ *Email:* {contact_data['email']}\n"
        f"🕒 *Time:* {contact_data['created_at']}"
    )

    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    async with aiohttp.ClientSession() as session:
        for admin_id in ADMINS_LIST.split(","):  # Send to each admin
            payload = {
                "chat_id": admin_id.strip(),
                "text": message,
                "parse_mode": "Markdown",
            }
            async with session.post(api_url, json=payload) as response:
                if response.status != 200:
                    print(f"Failed to send message to {admin_id}: {await response.text()}")
