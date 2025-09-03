import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream, InputAudioStream

# Replace these with your actual values or environment variables
API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
ASSISTANT_SESSION = "assistant"  # String session or leave as string for bot account

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client(ASSISTANT_SESSION, api_id=API_ID, api_hash=API_HASH)

pytgcalls = PyTgCalls(assistant)

# This example assumes you have a local audio file named "sample.mp3"
AUDIO_FILE = "sample.mp3"

# Command to start playing music in a voice chat
@app.on_message(filters.command("play") & filters.private)
async def play(_, message: Message):
    chat_id = message.chat.id

    # Join voice chat
    try:
        await pytgcalls.join_group_call(
            chat_id,
            InputStream(
                InputAudioStream(
                    AUDIO_FILE,
                )
            ),
            stream_type=1,  # Audio stream
        )
        await message.reply_text("🎵 Started playing music!")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

# Command to leave voice chat
@app.on_message(filters.command("stop") & filters.private)
async def stop(_, message: Message):
    chat_id = message.chat.id
    try:
        await pytgcalls.leave_group_call(chat_id)
        await message.reply_text("🛑 Stopped playing music and left the voice chat.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

async def main():
    await assistant.start()
    await app.start()
    await pytgcalls.start()
    print("Bot is running...")
    await idle()

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(main())
