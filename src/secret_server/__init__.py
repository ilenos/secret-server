import sys

from loguru import logger

from secret_server.config.base import Settings

settings = Settings.from_env()

logger.remove()
logger.add(sink=sys.stderr, level=settings.secret_server.log_level)
