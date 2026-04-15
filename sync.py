import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Змінні середовища
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

source_group = int(os.getenv("SOURCE_GROUP_ID"))
target_group_id = int(os.getenv("TARGET_GROUP_ID"))
source_bot = os.getenv("SOURCE_BOT_USERNAME")

# Ініціалізація клієнта
client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    sender = await event.get_sender()
    if not sender or getattr(sender, "username", None) != source_bot:
        return

    text = event.raw_text
    if not text:
        return

    await client.send_message(target_group_id, text)

print("✅ Forwarder is running...")
client.start()
client.run_until_disconnected()
