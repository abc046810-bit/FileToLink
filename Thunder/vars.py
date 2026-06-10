# Thunder/vars.py

import os

from dotenv import load_dotenv
from typing import Set, Optional
from Thunder.utils.logger import logger

load_dotenv("config.env")

def str_to_bool(val: str) -> bool:
    return val.lower() in ("true", "1", "t", "y", "yes")

def str_to_int_set(val: str) -> Set[int]:
    if not val:
        return set()
    result: Set[int] = set()
    for x in val.split():
        try:
            result.add(int(x))
        except (TypeError, ValueError):
            continue
    return result



class Var:
    API_ID: int = int(os.getenv("API_ID", "34981849"))
    API_HASH: str = os.getenv("API_HASH", "30cb2f87a2777d6df2b0f7af95c0e721")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

    if not all([API_ID, API_HASH, BOT_TOKEN]):
        logger.critical("Missing required Telegram API configuration")
        raise ValueError("Missing required Telegram API configuration")

    NAME: str = os.getenv("NAME", "TheSK")
    SLEEP_THRESHOLD: int = int(os.getenv("SLEEP_THRESHOLD", "600"))
    WORKERS: int = int(os.getenv("WORKERS", "8"))

    BIN_CHANNEL: int = int(os.getenv("BIN_CHANNEL", "-1003881108469"))

    if not BIN_CHANNEL:
        logger.critical("BIN_CHANNEL is required")
        raise ValueError("BIN_CHANNEL is required")

    PORT: int = int(os.getenv("PORT", "8080"))
    BIND_ADDRESS: str = os.getenv("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL: int = int(os.getenv("PING_INTERVAL", "840"))
    NO_PORT: bool = str_to_bool(os.getenv("NO_PORT", "True"))

    OWNER_ID: int = int(os.getenv("OWNER_ID", "8723278238"))

    if not OWNER_ID:
        logger.warning("WARNING: OWNER_ID is not set. No user will be granted owner access.")

    FQDN: str = os.getenv("FQDN", "") or BIND_ADDRESS
    HAS_SSL: bool = str_to_bool(os.getenv("HAS_SSL", "True"))
    PROTOCOL: str = "https" if HAS_SSL else "http"
    PORT_SEGMENT: str = "" if NO_PORT else f":{PORT}"
    URL: str = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

    SET_COMMANDS: bool = str_to_bool(os.getenv("SET_COMMANDS", "True"))

    DATABASE_URL: str = os.getenv("DATABASE_URL", "mongodb+srv://developerbro723_db_user:9axC7c7iQm0G3ESO@cluster0.dr8m75m.mongodb.net/?appName=Cluster0")

    if not DATABASE_URL:
        logger.critical("DATABASE_URL is required")
        raise ValueError("DATABASE_URL is required")

    MAX_BATCH_FILES: int = int(os.getenv("MAX_BATCH_FILES", "50"))

    CHANNEL: bool = str_to_bool(os.getenv("CHANNEL", "True"))

    BANNED_CHANNELS: Set[int] = str_to_int_set(os.getenv("BANNED_CHANNELS", ""))

    MULTI_CLIENT: bool = False

    FORCE_CHANNEL_ID: Optional[int] = None
    
    force_channel_env = os.getenv("FORCE_CHANNEL_ID", "-1003874499055").strip()

    if force_channel_env:
        try:
            FORCE_CHANNEL_ID = int(force_channel_env)
        except ValueError:
            logger.warning(f"Invalid FORCE_CHANNEL_ID '{force_channel_env}' in environment; must be an integer.")

    TOKEN_ENABLED: bool = str_to_bool(os.getenv("TOKEN_ENABLED", "True"))
    TOKEN_TTL_HOURS: int = int(os.getenv("TOKEN_TTL_HOURS", "12"))

    SHORTEN_ENABLED: bool = str_to_bool(os.getenv("SHORTEN_ENABLED", "True"))
    SHORTEN_MEDIA_LINKS: bool = str_to_bool(os.getenv("SHORTEN_MEDIA_LINKS", "False"))
    URL_SHORTENER_API_KEY: str = os.getenv("URL_SHORTENER_API_KEY", "7e48f2827e6d8301f946d92780ce9c5ceb1bcb1c")
    URL_SHORTENER_SITE: str = os.getenv("URL_SHORTENER_SITE", "https://vplink.in")

    GLOBAL_RATE_LIMIT: bool = str_to_bool(os.getenv("GLOBAL_RATE_LIMIT", "False"))
    MAX_GLOBAL_REQUESTS_PER_MINUTE: int = int(os.getenv("MAX_GLOBAL_REQUESTS_PER_MINUTE", "4"))

    RATE_LIMIT_ENABLED: bool = str_to_bool(os.getenv("RATE_LIMIT_ENABLED", "False"))
    MAX_FILES_PER_PERIOD: int = int(os.getenv("MAX_FILES_PER_PERIOD", "2"))
    RATE_LIMIT_PERIOD_MINUTES: int = int(os.getenv("RATE_LIMIT_PERIOD_MINUTES", "1"))
    MAX_QUEUE_SIZE: int = int(os.getenv("MAX_QUEUE_SIZE", "100"))
