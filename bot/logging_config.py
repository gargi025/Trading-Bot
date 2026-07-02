from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True
)

logger.add(
    "logs/trading.log",
    level="DEBUG",
    rotation="1 MB",
    retention="10 days",
    enqueue=True
)