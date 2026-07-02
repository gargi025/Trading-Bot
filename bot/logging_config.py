from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    "logs/trading.log",
    rotation="1 MB",
    retention="10 days",
    level="DEBUG"
)