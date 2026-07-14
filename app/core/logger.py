from loguru import logger
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Remove default logger
logger.remove()

# System log
logger.add(
    "logs/system.log",
    rotation="1 MB",
    level="INFO",
    format="{time} | {level} | {message}"
)

# Error log
logger.add(
    "logs/error.log",
    rotation="1 MB",
    level="ERROR",
    format="{time} | {level} | {message}"
)

# Console output
logger.add(
    lambda msg: print(msg, end=""),
    level="INFO"
)