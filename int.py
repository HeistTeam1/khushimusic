# int.py

# Messages and text constants for Telegram Music Bot

WELCOME = """
🎵 Welcome to MusicBot! 🎵

Use these commands to control music playback:

/play <song name or URL> - Play or queue a song
/pause - Pause current song
/resume - Resume paused song
/skip - Skip current song
/queue - Show song queue
/stop - Stop playback and clear queue

Enjoy your music! 🎶
"""

PLAYING = "▶️ Now playing: {}"
PAUSED = "⏸️ Music paused."
RESUMED = "▶️ Music resumed."
SKIPPED = "⏭️ Skipped to next song."
STOPPED = "⏹️ Music stopped and queue cleared."
QUEUE_EMPTY = "The queue is empty."
ADDED_TO_QUEUE = "➕ Added to queue: {}"
ERROR = "❌ Error: {}"
NOT_PLAYING = "No music is playing right now."
NO_PERMISSION = "❌ You don't have permission to do that."
USAGE = "Usage: {}"

HELP = """
Commands:
/play <song name or URL> - Play or add song to queue
/pause - Pause music
/resume - Resume music
/skip - Skip current song
/queue - Show queue
/stop - Stop music
/help - Show this help message
"""

BOT_USERNAME = "MusicBot"

