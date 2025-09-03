# config.py

import os

# Telegram Bot Token (get from @BotFather)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")

# Your Telegram user ID (for admin commands, optional)
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Optional: API keys for music services (e.g., YouTube API key)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_YOUTUBE_API_KEY_HERE")

# Maximum number of songs allowed in the queue
MAX_QUEUE_SIZE = int(os.getenv("MAX_QUEUE_SIZE", "50"))

# Default volume level (0-100)
DEFAULT_VOLUME = int(os.getenv("DEFAULT_VOLUME", "50"))

# Whether to enable logging (True/False)
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() in ("true", "1", "yes")

# Optional: Database URL for storing queues, user data, etc.
DATABASE_URL = os.getenv("DATABASE_URL", "")

# Optional: Lavalink server config (if using Lavalink for music streaming)
LAVALINK_HOST = os.getenv("LAVALINK_HOST", "127.0.0.1")
LAVALINK_PORT = int(os.getenv("LAVALINK_PORT", "2333"))
LAVALINK_PASSWORD = os.getenv("LAVALINK_PASSWORD", "youshallnotpass")

# Other bot settings can be added here as needed
