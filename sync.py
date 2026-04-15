from telethon import TelegramClient, events

api_id = 37344755
api_hash = "6663930d08ae0eff4b7a2a726b696599"

source_group = -5131820618      # де пише Python-бот
source_bot = "timetrackerbat_bot"  # username бота без @
target_group_id = -5131820618   # група з OpenClaw

client = TelegramClient("forwarder", api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    sender = await event.get_sender()
    if not sender or getattr(sender, "username", None) != source_bot:
        return

    text = event.raw_text
    if not text:
        return

    await client.send_message(target_group_id, text, parse_mode=None)

client.start()
client.run_until_disconnected()